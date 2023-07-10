def xor_data(xor1, xor2):
    results = ""

    print(xor1)
    print(xor2)
    for i in range(len(xor1)):
        results += "{:0>2}".format(hex(xor1[i] ^ xor2[i])[2:])

    return (results)

def main():
    key = ["ICE"]
    data1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    len_added = 3 - (len(data1) % 3)
    data2 = "".join(key[0] for i in range(0, len(data1), 3))[:-1]
    print(data2)

    print(xor_data(data1.encode(), data2.encode()))


if __name__ == "__main__":
    main()
