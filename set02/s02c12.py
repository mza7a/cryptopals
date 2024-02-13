from s02c10 import encrypt_ecb, encrypt_cbc
from Crypto.Util.Padding import pad
import base64
import os

"""
Oracle Padding Attack
"""

KEY = os.urandom(16)

def get_encryption(data):
    ciphertext = encrypt_ecb(pad(data, 16), KEY)
    return ciphertext.hex()

def perform_oracle_attack(b64_data):
    final_text = ''
    for i in range(len(b64_data)):
        padded_attack = b'A'*(143-i) + b64_data
        orig_ct = get_encryption(padded_attack)
        orig_ct_blocks = [orig_ct[index:index+32] for index in range(0, len(orig_ct), 32)]
        for char in range(10, 126):
            new_attack = b'A'*(143-i) + final_text.encode() + chr(char).encode() + b64_data
            new_ct = get_encryption(new_attack)
            new_ct_blocks = [new_ct[index:index+32] for index in range(0, len(orig_ct), 32)]
            if orig_ct_blocks[8] == new_ct_blocks[8]:
                final_text += chr(char)
                break
    print(f'The final text is :\n{final_text}', end="")



def main():
    b64_data = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
    to_append = base64.b64decode(b64_data)
    ciphertext = get_encryption(b'A'*144 + to_append)

    perform_oracle_attack(to_append)


if __name__ == "__main__":
    main()