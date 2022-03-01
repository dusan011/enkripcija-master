from Crypto.Cipher import AES
import hashlib
from cryptography.fernet import Fernet
import os


file = open('key.key', 'rb')
#password = b'mypassword'
password = file.read()
file.close()
fajl = 'test.txt' #ovo je fajl za enkripciju

algoritam = input("Izaberite algoritam za kriptovanje fajlova aes/fernet")

if algoritam == 'aes':
    print("izabrali ste aes algoritam")
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    IV = 'This is an IV456'

    def pad_message(file):
        while len(file) % 16 != 0:
            file = file + b'0'
        return file

    cipher = AES.new(key, mode, IV)

    with open(fajl, 'rb') as f:
        orig_file = f.read()

    padded_file = pad_message(orig_file)

    encrypted_message = cipher.encrypt(padded_file)

    with open('encrypted_file', 'wb') as e:
        e.write(encrypted_message)
else:
    print("izabratli ste fernet algoritam")
    with open(fajl, 'rb') as f:
        data = f.read()

    fernet = Fernet(password)
    encrypted = fernet.encrypt(data)

    # Write the encrypted file
    with open('test.txt.encrypted', 'wb') as f:
        f.write(encrypted)


