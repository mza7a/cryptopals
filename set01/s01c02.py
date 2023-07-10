def xor_data(xor1, xor2):
    set_bin1 = []
    set_bin2 = []
    for byte1 in xor1:
        set_bin1.append("{:0>8}".format(bin(byte1)[2:]))
    for byte2 in xor2:
        set_bin2.append("{:0>8}".format(bin(byte2)[2:]))

    result = ""

    for byte1 in set_bin1:
        result += str(hex(int("".join(["0" if (byte1[i] == set_bin2[0][i]) else "1" for i in range(8)]), 2)))[2:]

    print(bytes.fromhex(result))
    return(result)

def main():
    xor1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    xor2 = bytes.fromhex("686974207468652062756c6c277320657965")

    xored_data = xor_data(xor1, b'\x10')

    if xored_data == "746865206b696420646f6e277420706c6179":
        print("great success !!")
if __name__ == "__main__":
    main()
