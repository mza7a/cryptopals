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

def encrypt_cbc(key, iv, plaintext):
    IV = iv
    plainblocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    cipherblocks = []

    for block in plainblocks:
        xored_block = xor(block, IV)
        IV = encrypt(xored_block, key)
        cipherblocks.append(IV)
    ciphertext = b''.join(cipherblocks)
    return ciphertext

def decrypt_cbc(key, iv, ciphertext):
    KEY = key
    IV = iv
    cipherblocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    plainblocks = []
    for block in cipherblocks:
        dec_block = decrypt(block, KEY)
        plainblocks.append(xor(dec_block, IV))
        IV = block
    plaintext = b''.join(plainblocks)
    return plaintext

def main():
    key = b'YELLOW SUBMARINE'
    iv = b'\x00'*16
    with open('s02c10_input', 'r') as f:
        ciphertext = f.read()
    ciphertext = base64.b64decode(ciphertext)
    with open('s02c10_output', 'r') as e:
        plaintext = e.read()
    plaintext = bytes.fromhex(plaintext)
    ciphertext2 = encrypt_cbc(key, iv, plaintext)
    assert ciphertext == ciphertext2
    plaintext2 = decrypt_cbc(key, iv, ciphertext)
    assert plaintext == plaintext2
    print("Both encryption and decryption working fine !!")

if __name__ == "__main__":
    main()