from Crypto.Cipher import AES
import hashlib
from cryptography.fernet import Fernet

file = open('key.key', 'rb')
password = file.read()
file.close()

algoritam = input("Izaberite algoritam za dekriptovanje fajlova? aes/fernet")

if algoritam == 'aes':
    print("odabrali ste algoritam aes za dekriptiju")
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    IV = 'This is an IV456'

    cipher = AES.new(key, mode, IV)

    with open('Encrypted_file', 'rb') as e:
        encrypted_file = e.read()

    decrypted_file = cipher.decrypt(encrypted_file)

    with open('decrypted.txt', 'wb') as df:
        df.write(decrypted_file.rstrip(b'0'))
else:
    print("odabrali ste fernet algoritam za dekripciju")
    # Open the file to encrypt
    with open('test.txt.encrypted', 'rb') as f:
        data = f.read()

    fernet = Fernet(password)
    encrypted = fernet.decrypt(data)

    # Write the encrypted file
    with open('test.txt.decrypted', 'wb') as f:
        f.write(encrypted)

