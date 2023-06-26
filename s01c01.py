b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def get_chunk(data, length):
    return [data[i:i+length] for i in range(0, len(data), length)]

def convert_b64(data):
    padding_num = 0
    if len(data) % 3 != 0:
        padding_num = 3 - (len(data) % 3)
    data += b"\x00"*padding_num
    print(data)
    chunked_data = get_chunk(data, 3)
    total_bin = ""
    for chunk in chunked_data:
        for char in chunk:
            total_bin += "{:0>8}".format(bin(char)[2:])

    chunked_bin = get_chunk(total_bin, 6)
    result = ""
    for binary in chunked_bin:
        result += b64[int(binary, 2)]

    result = result[:-padding_num] + "="*padding_num
    return(result)

def main():
    convert = convert_b64(bytes.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d6d"))


if __name__ == '__main__':
    main()
