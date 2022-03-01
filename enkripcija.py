from cryptography.fernet import Fernet

#Get the key from the file
file = open('key.key', 'rb')
key = file.read() #The key will be type bytes
file.close()

#Open the file to encrypt
with open('test.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Write the encrypted file
with open('test.txt.encrypted', 'wb') as f:
    f.write(encrypted)
