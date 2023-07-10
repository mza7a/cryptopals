import base64
from Crypto.Util.Padding import pad,unpad
from Crypto.Cipher import AES

key = b"YELLOW SUBMARINE"

def decrypt(data):
    decryption = AES.new(key, AES.MODE_ECB)
    plain_text = decryption.decrypt(data)
    return plain_text

def main():

    with open("s01c07_input") as input_file:
        byte_data = base64.b64decode(input_file.read())
    
    res = decrypt(byte_data)
    print(res.decode())

if __name__ == "__main__":
    main()