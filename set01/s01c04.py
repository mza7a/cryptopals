from s01c03 import xor_data


def main():
    with open('./s01c04.input') as f:
        lines = f.read().splitlines()

    y = 0
    for line in lines:
        for i in range(1, 128):
            print(line)
            xor_data(bytes.fromhex(line), chr(i).encode())

if __name__ == "__main__":
    main()
