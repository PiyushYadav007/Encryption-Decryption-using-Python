from cryptography.fernet import Fernet

# This is the key that will be used to encrypt/decrypt the message


def encrypt():
    key = Fernet.generate_key()
    print("Key: ", key.decode())
    file = open("key.txt", "wb")
    file.write(key)
    f = Fernet(key)


    path = input("Enter File Name : ")
    file = open(path,"rb")
    message = file.read()
    encrypted = f.encrypt(message)
    encryp = input("Enter the name of the file to be saved as ")
    print("Encrypted message:", encrypted.decode())
    Enc = open(encryp, "wb")
    Enc.write(encrypted)
    return encrypted


def decrypt():
    key = input("Enter Key:")
    f = Fernet(key)
    path = input("Enter File Name: ")
    file = open(path,"rb")
    encrypted = file.read()
    decrypted = f.decrypt(encrypted)
    decryp = input("Enter the file name to be sabed as ")
    print("Decrypted message: ", decrypted.decode())
    Dec = open(decryp, "wb")
    Dec.write(decrypted)
    return decrypted


while True:
   print("ENCRYPTION AND DECRYPTION")
   print("\n1.Encrypt text\n2.Decrypt text\n3.Exit")
   a = int(input("\nEnter your option 1 or 2 or 3 :"))
   if a == 1:
     encrypt()
   if a == 2:
     decrypt()
   if a == 3:
        break
   
