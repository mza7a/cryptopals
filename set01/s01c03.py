
def xor_data(xor1, xor2):
    set_bin1 = []
    set_bin2 = []
    for byte1 in xor1:
        set_bin1.append("{:0>8}".format(bin(byte1)[2:]))
    for byte2 in xor2:
        set_bin2.append("{:0>8}".format(bin(byte2)[2:]))

    result = ""

    for byte1, byte2 in zip(set_bin1, set_bin2):
        result += str("{:0>2}".format(hex(int("".join(["0" if (byte1[i] == byte2[i]) else "1" for i in range(8)]), 2))[2:]))

    return(result)

def main():
    data = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    for i in range(1, 128):
        print(chr(i).encode())
        xor_data(bytes.fromhex(data), chr(i).encode())

if __name__ == "__main__":
    main()
