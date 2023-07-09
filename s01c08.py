from s01c01 import get_chunk

def main():

    file = open("s01c08_input", 'r')
    data = file.readlines()

    for i in range(len(data)):
        data[i] = data[i][:-1]
    
    i = 0
    for lines in data:
        chunked_data = get_chunk(bytes.fromhex(lines), 16)
        # print(chunked_data)
        if len(chunked_data) != len(set(chunked_data)):
            print(i)
            print(lines)
            print("TRUE")
        else:
            print("FALSE")
        i += 1

if __name__ == "__main__":
    main()