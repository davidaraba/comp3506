"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

Compression Utilities for Task 4.
"""

from pathlib import Path
from typing import Any, Tuple
import sys
import hashlib
import heapq
from structures.huffman_node import HuffmanNode
from structures.bit_vector import BitVector


def file_to_bytes(path: str) -> bytes:
    """
    Read a file into a byte array
    """
    with open(path, 'rb') as f:
        data = f.read()
    return data


def bytes_to_file(path: str, data: bytes) -> None:
    """
    Write a sequence of bytes to a file
    """
    with open(path, 'wb') as f:
        f.write(data)


def build_frequency_table(data: bytes) -> dict:
    frequency = {}
    for byte in data:
        if byte in frequency:
            frequency[byte] += 1
        else:
            frequency[byte] = 1
    return frequency


def build_huffman_tree(frequency):
    priority_queue = [HuffmanNode(symbol=char, frequency=freq)
                      for char, freq in frequency.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_frequency = left_child._frequency + right_child._frequency
        merged_node = HuffmanNode(symbol=None, frequency=merged_frequency)
        merged_node._left = left_child
        merged_node._right = right_child
        heapq.heappush(priority_queue, merged_node)
    return priority_queue[0]


def generate_huffman_codes(node, path="", codebook={}):
    if node is not None:
        if node._symbol is not None:
            codebook[node._symbol] = path
        else:
            generate_huffman_codes(node._left, path + "0", codebook)
            generate_huffman_codes(node._right, path + "1", codebook)
    return codebook


def huffman_encode(data: bytes, codebook: dict) -> BitVector:
    encoded_data = BitVector()
    for byte in data:
        code = codebook[byte]
        for bit in code:
            encoded_data.append(int(bit))
    return encoded_data


def serialize_codebook(codebook: dict, total_bits: int) -> bytes:
    serialised = bytearray()
    # Write the number of entries in the codebook
    num_entries = len(codebook)
    # 2 bytes for number of entries
    serialised.extend(num_entries.to_bytes(2, byteorder='big'))

    for char, code in codebook.items():
        serialised.extend(char.to_bytes(1, byteorder='big')
                          )  # 1 byte for the character
        code_length = len(code)
        serialised.extend(code_length.to_bytes(
            2, byteorder='big'))  # 2 bytes for code length
        code_int = int(code, 2)
        num_code_bytes = (code_length + 7) // 8
        serialised.extend(code_int.to_bytes(num_code_bytes, byteorder='big'))
    # Include the total number of bits in the encoded data (4 bytes)
    serialised.extend(total_bits.to_bytes(4, byteorder='big'))
    return bytes(serialised)


def deserialise_codebook(data: bytes) -> Tuple[dict, int, int]:
    offset = 0
    codebook = {}
    num_entries = int.from_bytes(data[offset:offset+2], byteorder='big')
    offset += 2
    for _ in range(num_entries):
        char = data[offset]
        offset += 1
        code_length = int.from_bytes(data[offset:offset+2], byteorder='big')
        offset += 2
        num_code_bytes = (code_length + 7) // 8
        code_bytes = data[offset:offset+num_code_bytes]
        offset += num_code_bytes
        code_int = int.from_bytes(code_bytes, byteorder='big')
        code = bin(code_int)[2:].zfill(code_length)
        codebook[code] = char
    # Read the total number of bits (4 bytes)
    total_bits = int.from_bytes(data[offset:offset+4], byteorder='big')
    offset += 4
    return codebook, total_bits, offset


def my_compressor(in_bytes: bytes) -> bytes:
    """
    Your compressor takes a bytes object and returns a compressed
    version of the bytes object.
    """
    frequency_table = build_frequency_table(in_bytes)
    huffman_tree = build_huffman_tree(frequency_table)
    codebook = generate_huffman_codes(huffman_tree)
    encoded_data = huffman_encode(in_bytes, codebook)
    total_bits = encoded_data.get_size()
    serialized_codebook = serialize_codebook(codebook, total_bits)
    return serialized_codebook + encoded_data.to_byte_arr()


def my_decompressor(compressed_bytes: bytes) -> bytes:
    """
    Your decompressor is given a compressed bytes object (from your own
    compressor) and must recover and return the original bytes.
    """
    # Deserialise the codebook and total_bits
    codebook, total_bits, offset = deserialise_codebook(compressed_bytes)
    # Extract the encoded data bytes
    encoded_data_bytes = compressed_bytes[offset:]
    # Reconstruct the bits from the encoded data bytes
    bits_read = 0
    decoded_bytes = bytearray()
    code = ''
    codebook_inverse = codebook

    # Iterate over the bytes and extract bits
    for byte in encoded_data_bytes:
        for i in range(8):
            if bits_read >= total_bits:
                break
            bit = (byte >> (7 - i)) & 1
            bits_read += 1
            code += str(bit)
            if code in codebook_inverse:
                decoded_bytes.append(codebook_inverse[code])
                code = ''
        if bits_read >= total_bits:
            break
    return bytes(decoded_bytes)


def compress_file(in_path: str, out_path: str) -> None:
    """
    Consume a file from in_path, compress it, and write it to out_path.
    """
    in_size = Path(in_path).stat().st_size
    in_data = file_to_bytes(in_path)

    compressed = my_compressor(in_data)

    bytes_to_file(out_path, compressed)
    out_size = Path(out_path).stat().st_size

    print("Compression Benchmark...")
    print("Input File:", in_path)
    print("Input Size:", in_size)
    print("Output File:", out_path)
    print("Output Size:", out_size)
    print("Ratio:", out_size / in_size)


def decompress_file(compressed_path: str, out_path: str) -> None:
    """
    Consume a compressed file from compressed_path, decompress it, and
    write it to out_path.
    """
    compressed_data = file_to_bytes(compressed_path)

    decompressed = my_decompressor(compressed_data)

    bytes_to_file(out_path, decompressed)


def recovery_check(in_path: str, compressed_path: str) -> bool:
    original = file_to_bytes(in_path)
    expected_checksum = hashlib.md5(original).hexdigest()

    decompress_file(compressed_path, "tmp")
    recovered = file_to_bytes("tmp")
    recovered_checksum = hashlib.md5(recovered).hexdigest()

    assert expected_checksum == recovered_checksum, "Uh oh!"


if __name__ == "__main__":
    compress_file(sys.argv[1], sys.argv[2])
    recovery_check(sys.argv[1], sys.argv[2])
