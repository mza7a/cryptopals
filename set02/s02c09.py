def get_chunk(data, length):
    return [data[i:i+length] for i in range(0, len(data), length)]

def pkcs_7pad(data, size):

    padding_len = 0

    if len(data) % size != 0:
        padding_len = size - len(data) % size

    chunked_data = get_chunk(data, size)
    bytes_added = '\\x' + '{:0>2}'.format(str(padding_len))
    chunked_data[len(chunked_data) - 1] += bytes_added * padding_len

    return ''.join(chunked_data)


def main():
    plain_text = "YELLOW SUBMARINE"
    padded_text = pkcs_7pad(plain_text, 20)

    print(padded_text)

if __name__ == "__main__":
    main()