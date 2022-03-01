from cryptography.fernet import Fernet

#Get the key from the file
file = open('key.key', 'rb')
key = file.read() #The key will be type bytes
file.close()

#Open the file to encrypt
with open('test.txt.encrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

#Write the encrypted file
with open('test.txt.decrypted', 'wb') as f:
    f.write(encrypted)
