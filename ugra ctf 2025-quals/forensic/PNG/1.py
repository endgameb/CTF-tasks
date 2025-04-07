import struct
import itertools
import zlib

data = open("flag.png", "rb").read()
iend_i = data.rfind(b"IEND")
idat_i = data.find(b"IDAT")

recovered_idat = []

while idat_i < iend_i:
    next_i = data.find(b"IDAT", idat_i + 4)
    if next_i == -1:
        next_i = iend_i
    chunk = data[idat_i - 4:next_i - 4]
    idat_i = next_i

    print("IDAT chunk of stored length (with header)", len(chunk))

    stored_length = len(chunk) - 12
    expected_length, = struct.unpack(">L", chunk[:4])

    print("IDAT chunk with", expected_length - stored_length, "CRs missing,", chunk.count(b'\n'), "LFs present")

    stored_body = chunk[8:-4]
    expected_crc, = struct.unpack(">L", chunk[-4:])

    lf_positions = [i for i, c in enumerate(stored_body) if c == b"\n"[0]]

    # Попытка восстановления с отладочной информацией
    for attempt, insert_cr_at in enumerate(itertools.combinations(lf_positions, expected_length - stored_length), 1):
        fixed_body = stored_body
        for i in insert_cr_at[::-1]:
            fixed_body = fixed_body[:i] + b"\r" + fixed_body[i:]

        current_crc = zlib.crc32(b"IDAT" + fixed_body)
        if current_crc == expected_crc:
            print(f"Chunk recovered (attempt {attempt})")
            recovered_idat.append(fixed_body)
            break
    else:
        print(f"Failed to recover chunk after {attempt} attempts")
        print(f"Expected CRC: {expected_crc:08x}")
        print(f"Last attempted CRC: {current_crc:08x}")
        continue

    ihdr_i = data.find(b"IHDR")
    ihdr_length, = struct.unpack(">L", data[ihdr_i - 4:ihdr_i])
    ihdr = data[ihdr_i - 4:ihdr_i + 8 + ihdr_length]

def write_chunk(type: bytes, content: bytes):
    f.write(struct.pack(">L", len(content)) + type + content + struct.pack(">L", zlib.crc32(type + content)))

with open("recovered.png", "wb") as f:
    f.write(b"\x89PNG\r\n\x1a\n")
    f.write(ihdr)
    for idat in recovered_idat:
        write_chunk(b"IDAT", idat)
    write_chunk(b"IEND", b"")
