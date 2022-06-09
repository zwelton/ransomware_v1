import os
import glob
import shutil
import hashlib
from cryptography.fernet import Fernet

loop = True
while loop:
    print("")
    print('Choose an option:')
    print("""
[1] - generate key
[2] - encrypt
[3] - decrypt
[4] - exit
""")

    choice = str(input('choice: '))

    if choice == '1':
#        generate key
        newkey = Fernet.generate_key()
        file = open('new.key', 'wb')
        file.write(newkey)
        file.close()
        print("new key created")
        print("")

        with open('new.key', 'rb') as filekey:
            key = filekey.read()
        encrypt = Fernet(key)
        decrypt = Fernet(key)

    elif choice == '2':
#        encrypt
        directory = "/home/username/"
        for files in os.listdir(directory):
            os.chdir(directory)
            with open(files, 'rb') as rb:
                enc_dados = rb.read()
                encrypt_e = encrypt.encrypt(enc_dados)
                new_arq='[enc]'+ os.path.basename (files)
                with open(new_arq, 'wb') as new:
                    new.write(encrypt_e)
                    new.close()
                    rb.close()
                    os.remove(files)
                    print("sucess encrypt")

    elif choice == '3':
#        decrypt
        directory = "/home/username/"
        for files in os.listdir(directory):
            os.chdir(directory)
            with open(files, 'rb') as rb:
                dec_dados = rb.read()
                decrypt_d = decrypt.decrypt(dec_dados)
                new_arq='[dec]'+ os.path.basename (files)
                with open(new_arq, 'wb') as new:
                    new.write(decrypt_d)
                    new.close()
                    rb.close()
#                    os.remove(files)
                    print("sucess decrypt")

    elif choice == '4':
#        exit
        loop = False
        break

    else:
        print("")
        print("invalid option")
        print("")
        loop = False
        break
