from __future__ import annotations

import io
import struct
import sys
from typing import Literal, Union

import numpy as np

PCM = 0x0001
IEEE_FLOAT = 0x0003
EXTENSIBLE = 0xFFFE

AudioData = Union[np.memmap, np.ndarray]
Endian = Literal[">", "<"]  # Big Endian, Little Endian
ByteOrd = Literal["big", "little"]


def _read_fmt_chunk(
    fid: io.BufferedReader, bytes_order: ByteOrd
) -> tuple[int, int, int, int, int]:
    size = int.from_bytes(fid.read(4), bytes_order)

    if size < 16:
        raise ValueError("Binary structure of wave file is not compliant")

    format_tag = int.from_bytes(fid.read(2), bytes_order)
    channels = int.from_bytes(fid.read(2), bytes_order)
    sr = int.from_bytes(fid.read(4), bytes_order)
    fid.read(4)  # This is bitrate but we don't need it
    block_align = int.from_bytes(fid.read(2), bytes_order)
    bit_depth = int.from_bytes(fid.read(2), bytes_order)
    bytes_read = 16

    if format_tag == EXTENSIBLE and size >= 18:
        ext_chunk_size = int.from_bytes(fid.read(2), bytes_order)
        bytes_read += 2
        if ext_chunk_size >= 22:
            extensible_chunk_data = fid.read(22)
            bytes_read += 22
            raw_guid = extensible_chunk_data[6:22]

            if bytes_order == "big":
                tail = b"\x00\x00\x00\x10\x80\x00\x00\xAA\x00\x38\x9B\x71"
            else:
                tail = b"\x00\x00\x10\x00\x80\x00\x00\xAA\x00\x38\x9B\x71"
            if raw_guid.endswith(tail):
                format_tag = int.from_bytes(raw_guid[:4], bytes_order)
        else:
            raise ValueError("Binary structure of wave file is not compliant")

    if format_tag not in {PCM, IEEE_FLOAT}:
        raise ValueError(
            f"Encountered unknown format tag: {format_tag:#06x}, while reading fmt chunk."
        )

    # move file pointer to next chunk
    if size > bytes_read:
        fid.read(size - bytes_read)

    # fmt should always be 16, 18 or 40, but handle it just in case
    _handle_pad_byte(fid, size)

    return format_tag, channels, sr, block_align, bit_depth


def _read_data_chunk(
    fid: io.BufferedReader,
    format_tag: int,
    channels: int,
    bit_depth: int,
    en: Endian,
    block_align: int,
    data_size: int | None,
) -> AudioData:
    bytes_order: ByteOrd = "big" if en == ">" else "little"
    size = int.from_bytes(fid.read(4), bytes_order)

    if data_size is not None:
        # size is only 32-bits here, so get real size from header.
        size = data_size

    bytes_per_sample = block_align // channels

    if bytes_per_sample in (3, 5, 6, 7):
        raise ValueError(f"Unsupported bytes per sample: {bytes_per_sample}")

    if format_tag == PCM:
        if 1 <= bit_depth <= 8:
            dtype = "u1"  # WAVs of 8-bit integer or less are unsigned
        elif bit_depth <= 64:
            dtype = f"{en}i{bytes_per_sample}"
        else:
            raise ValueError(
                f"Unsupported bit depth: the WAV file has {bit_depth}-bit integer data."
            )
    elif format_tag == IEEE_FLOAT:
        if bit_depth in (32, 64):
            dtype = f"{en}f{bytes_per_sample}"
        else:
            raise ValueError(
                f"Unsupported bit depth: the WAV file has {bit_depth}-bit floating-point data."
            )
    else:
        raise ValueError(
            f"Unknown wave file format: {format_tag:#06x}. Supported formats: PCM, IEEE_FLOAT"
        )

    if size % 2 == 0:
        n_samples = size // block_align
    else:
        n_samples = (size - 1) // block_align

    data = np.memmap(
        fid, dtype=dtype, mode="c", offset=fid.tell(), shape=(n_samples, channels)
    )
    fid.seek(size, 1)
    _handle_pad_byte(fid, size)

    return data


def _skip_unknown_chunk(fid: io.BufferedReader, en: Endian) -> None:
    if data := fid.read(4):
        size = struct.unpack(f"{en}I", data)[0]
        fid.seek(size, 1)
        _handle_pad_byte(fid, size)


def _read_rf64_chunk(fid: io.BufferedReader) -> tuple[int, int, Endian]:
    # https://tech.ebu.ch/docs/tech/tech3306v1_0.pdf
    # https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.2088-1-201910-I!!PDF-E.pdf

    heading = fid.read(12)
    if heading != b"\xff\xff\xff\xffWAVEds64":
        raise ValueError(f"Invalid heading for rf64 chunk: {heading!r}")

    chunk_size = fid.read(4)

    bw_size_low = fid.read(4)
    bw_size_high = fid.read(4)

    en: Endian = ">" if (bw_size_high > bw_size_low) else "<"
    bytes_order: ByteOrd = "big" if en == ">" else "little"

    data_size_low = fid.read(4)
    data_size_high = fid.read(4)

    file_size = int.from_bytes(bw_size_low + bw_size_high, "little")
    data_size = int.from_bytes(data_size_low + data_size_high, "little")

    int_chunk_size = int.from_bytes(chunk_size, bytes_order)
    fid.read(40 - int_chunk_size)

    return data_size, file_size, en


def _read_riff_chunk(sig: bytes, fid: io.BufferedReader) -> tuple[None, int, Endian]:
    en: Endian = "<" if sig == b"RIFF" else ">"
    bytes_order: ByteOrd = "big" if en == ">" else "little"

    file_size = int.from_bytes(fid.read(4), bytes_order) + 8

    form = fid.read(4)
    if form != b"WAVE":
        raise ValueError(f"Not a WAV file. RIFF form type is {form!r}.")

    return None, file_size, en


def _handle_pad_byte(fid: io.BufferedReader, size: int) -> None:
    if size % 2 == 1:
        fid.seek(1, 1)


def read(filename: str) -> tuple[int, AudioData]:
    fid = open(filename, "rb")

    try:
        file_sig = fid.read(4)
        if file_sig in (b"RIFF", b"RIFX"):
            data_size, file_size, en = _read_riff_chunk(file_sig, fid)
        elif file_sig == b"RF64":
            data_size, file_size, en = _read_rf64_chunk(fid)
        else:
            raise ValueError(f"File format {file_sig!r} not supported.")

        fmt_chunk_received = False
        data_chunk_received = False
        while fid.tell() < file_size:
            chunk_id = fid.read(4)

            if not chunk_id:
                if data_chunk_received:
                    break  # EOF but data successfully read
                raise ValueError("Unexpected end of file.")

            elif len(chunk_id) < 4 and not (fmt_chunk_received and data_chunk_received):
                raise ValueError(f"Incomplete chunk ID: {chunk_id!r}")

            if chunk_id == b"fmt ":
                fmt_chunk_received = True
                bytes_order: ByteOrd = "big" if en == ">" else "little"
                format_tag, channels, sr, block_align, bit_depth = _read_fmt_chunk(
                    fid, bytes_order
                )
            elif chunk_id == b"data":
                data_chunk_received = True
                if not fmt_chunk_received:
                    raise ValueError("No fmt chunk before data")

                data = _read_data_chunk(
                    fid,
                    format_tag,
                    channels,
                    bit_depth,
                    en,
                    block_align,
                    data_size,
                )
            else:
                _skip_unknown_chunk(fid, en)

    finally:
        fid.seek(0)

    return sr, data


def write(fid: io.BufferedWriter, sr: int, arr: AudioData) -> None:
    # Write RIFF WAV Header
    fid.write(b"RIFF\x00\x00\x00\x00WAVE")

    # Write RF64 WAV Header
    # fid.write(b"RF64\xff\xff\xff\xffWAVEds64")

    # #  - chunk_size
    # fid.write(b'\x1c\x00\x00\x00')  # Value based on bit-depth + '# of samples'

    # # - bw_size, Declaring Little Endian
    # fid.write(b'j@|\x00')
    # fid.write(b'\x00\x00\x00\x00')

    # Write 'fmt' Header
    dkind = arr.dtype.kind

    header_data = b"fmt "

    format_tag = IEEE_FLOAT if dkind == "f" else PCM
    channels = 1 if arr.ndim == 1 else arr.shape[1]
    bit_depth = arr.dtype.itemsize * 8
    bit_rate = sr * (bit_depth // 8) * channels
    block_align = channels * (bit_depth // 8)

    fmt_chunk_data = struct.pack(
        "<HHIIHH", format_tag, channels, sr, bit_rate, block_align, bit_depth
    )

    if not (dkind == "i" or dkind == "u"):
        # add cbSize field for non-PCM files
        fmt_chunk_data += b"\x00\x00"

    header_data += struct.pack("<I", len(fmt_chunk_data))
    header_data += fmt_chunk_data

    # fact chunk (non-PCM files)
    if not (dkind == "i" or dkind == "u"):
        header_data += b"fact"
        header_data += struct.pack("<II", 4, arr.shape[0])

    if len(header_data) + arr.nbytes > 0xFFFFFFFF:
        raise ValueError("Data exceeds wave file size limit")

    fid.write(header_data)

    # Write Data Chunk
    fid.write(b"data")
    fid.write(struct.pack("<I", arr.nbytes))
    if arr.dtype.byteorder == ">" or (
        arr.dtype.byteorder == "=" and sys.byteorder == "big"
    ):
        arr = arr.byteswap()

    # Write the actual data
    fid.write(arr.ravel().view("b").data)

    # Write size info
    size = fid.tell()
    fid.seek(4)
    fid.write(struct.pack("<I", size - 8))
