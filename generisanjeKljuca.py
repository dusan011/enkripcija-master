from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("ovo je kljuc ",key)

file = open('key.key', 'wb')
file.write(key) #kljuc je u bajtovima
file.close()