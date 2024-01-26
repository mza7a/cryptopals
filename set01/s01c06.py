import base64
from s01c01 import get_chunk
from s01c03 import xor_data
import itertools
import re

def calculate_hamming_distance(str1, str2):
    total = 0
    for i, j in zip(str1, str2):
        xored = bin(i ^ j)[2:]
        for bits in xored:
            if bits == "1":
                total += 1
    return(total)

def find_key_size(byte_data):

    hamming_distance = []

    for i in range(2):
        for key_size in range(2, 40):
            hamming_distance.append(calculate_hamming_distance(byte_data[key_size*i:key_size*(i+1)], byte_data[key_size*(i+1):key_size*(i+2)]) / key_size)
    

    sorted_distance = sorted(hamming_distance)
    return(hamming_distance.index(sorted_distance[0])+2,hamming_distance.index(sorted_distance[1])+2,hamming_distance.index(sorted_distance[2])+2,hamming_distance.index(sorted_distance[3])+2,hamming_distance.index(sorted_distance[4]) - 38+2)

def extract_byte(elements, index):
    first_bytes = []
    for element in elements:
        first_byte = element[index] if isinstance(element, bytes) else ord(element[index])
        first_bytes.append(chr(first_byte).encode())
    return first_bytes

def check_hamming_distance():
    # Make sure that hamming distance algo is working.
    str1 = b"this is a test"
    str2 = b"wokka wokka!!!"
    hamming_distance = calculate_hamming_distance(str1, str2)
    print(hamming_distance)

def has_special_characters(string):
    pattern = r"[^a-zA-Z0-9,.: '\n!-]"
    match = re.search(pattern, string)
    if match:
        return True
    return False

def xor_data2(xor1, xor2):
    set_bin1 = []
    set_bin2 = []
    for byte1 in xor1:
        set_bin1.append("{:0>8}".format(bin(byte1)[2:]))
    for byte2 in xor2:
        set_bin2.append("{:0>8}".format(bin(byte2)[2:]))

    result = ""

    for byte1 in set_bin1:
        result += str("{:0>2}".format(hex(int("".join(["0" if (byte1[i] == set_bin2[0][i]) else "1" for i in range(8)]), 2))[2:]))

    return(result)

def main():
    #check_hamming_distance()

    with open("temp_input") as input_file:
        byte_data = base64.b64decode(input_file.read())

    # ret_key_sizes = sorted(find_key_size(byte_data))
    # key_sizes = list(dict.fromkeys(ret_key_sizes))
    # print(key_sizes)

    key_sizes = [10, 12, 14, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 42, 46, 48, 50, 51, 54, 56, 60, 62, 63, 64, 65, 70, 72, 75, 76, 78, 80, 81, 88, 90, 96, 98]

    key_backed = ""
    
    for z in key_sizes:
        chunked_data = get_chunk(byte_data, z)
        # chunked_data[len(chunked_data) - 1] += b'\x00'*(z-len(chunked_data[len(chunked_data) - 1]))
        for y in range(0, z):
            data_block = extract_byte(chunked_data, y)
            for i in range(1, 128):
                res = xor_data(b"".join(data_block), chr(i).encode())
                if has_special_characters(bytes.fromhex(res).decode()) == False:
                    key_backed += chr(i)
                    print("Key is now : ", key_backed)
                    break
        print("Final key is for key_size", z, "is :", key_backed)

    print(key_backed)
    len_added = 29 - (len(byte_data) % 29)
    data2 = "".join(key_backed for i in range(0, len(byte_data), 29))[:-1]
    res = xor_data2(data2.encode(), byte_data)
    print(bytes.fromhex(res).decode())


if __name__ == "__main__":
    main()