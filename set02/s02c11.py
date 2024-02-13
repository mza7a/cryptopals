from s02c10 import encrypt_ecb, encrypt_cbc
from Crypto.Util.Padding import pad
import random
import os

KEY = os.urandom(16)

def detect_encryption(ciphertext):
    cipherblocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

    if cipherblocks[1] == cipherblocks[2]:
        return "ECB"
    return "CBC"


def get_encryption():
    flag = b'A'*(32+11)
    prefix = b'\x00' * random.randint(5, 10)
    postfix = b'\x00' * random.randint(5, 10)
    mode = random.choice(["ECB", "CBC"])

    if mode == "ECB":
        ciphertext = encrypt_ecb(pad(prefix + flag + postfix, 16), KEY)
    else:
        iv = os.urandom(16)
        ciphertext = encrypt_cbc(KEY, iv, pad(prefix + flag + postfix, 16))

    return ciphertext, mode

def main():
    for i in range(10):
        ciphertext, mode = get_encryption()
        guessed_mode = detect_encryption(ciphertext)

        assert mode == guessed_mode

        print(f"Actual Mode : {mode} <====> Guessed Mode : {guessed_mode}")

if __name__ == "__main__":
    main()
