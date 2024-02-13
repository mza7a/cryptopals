from s02c10 import encrypt_ecb, decrypt_ecb
from Crypto.Util.Padding import pad, unpad
import re
import os
import random

KEY = os.urandom(16)

def sanitize_email(email):
    not_allowed_chars = set("&=")

    if all(char in not_allowed_chars for char in email):
        return False
    return True

def check_parsed_role(data):
    role = (data.split('&')[2]).split('=')[1]
    if role == 'admin':
        return True
    return False

def profile_for(email):
    if sanitize_email(email) == False:
        return("You can't use & or = in email !")
    
    return "email="+email.decode()+"&uid="+str(random.randint(1, 100))+"&role=user"

def main():
    email = b'h@hffff.hh'
    payload = email + pad(b'admin', 16) + b'aka'
    cookie = profile_for(payload)
    ciphertext = encrypt_ecb(pad(cookie.encode(), 16), KEY).hex()
    print(f"Here's your cookie : {ciphertext}")
    data = bytes.fromhex(input("Check if you are admin or not : "))
    plaintext = unpad(decrypt_ecb(data, KEY), 16)
    if check_parsed_role(plaintext.decode()) == True:
        print("Welcome back admin ! Here's your flag : AKASEC{d3bug_fl4g}")
    else:
        print("Welcome back user ! No flag for you :(")


if __name__ == "__main__":
    main()