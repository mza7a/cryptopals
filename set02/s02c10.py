from Crypto.Cipher import AES
from pwn import xor
import base64


def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt(ciphertext, key):
    plain = AES.new(key, AES.MODE_ECB)
    plaintext = plain.decrypt(ciphertext)
    return plaintext


def main():
    KEY = b'YELLOW SUBMARINE'
    IV = b'\x00'*16
    is_first = 0
    with open('s02c09_input', 'r') as f:
        ciphertext = f.read()
    ciphertext = base64.b64decode(ciphertext)
    cipherblocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    plainblocks = []
    for block in cipherblocks:
        dec_block = decrypt(block, KEY)
        plainblocks.append(xor(dec_block, IV))
        IV = block
    plaintext = b''.join(plainblocks)
    print(plaintext.decode())


if __name__ == "__main__":
    main()