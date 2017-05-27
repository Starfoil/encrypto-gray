import encrypto
import os

DECRYPTION_KEY = 0
PUBLIC_KEY = 0

try:
    with open('rsa_final_decryption_key.txt', 'r') as fr:
        try:
            DECRYPTION_KEY = int(fr.read())
        except ValueError:
            print('Improper decryption key found')
            quit(2)
        finally:
            fr.close()
except FileNotFoundError:
    print('Decryption key not found')
    quit(1)

try:
    with open('rsa_public_encryption_key.txt', 'r') as fr:
        try:
            PUBLIC_KEY = int(fr.read())
        except ValueError:
            print('Improper public key found')
            quit(2)
        finally:
            fr.close()
except FileNotFoundError:
    print('Decryption key not found')
    quit(1)

for file in os.listdir():
    if file.endswith('.encrypted'):
        try:
            print('Opening file ' + file)
            with open(file, 'r') as fr:
                msg = fr.read()
            print('Decrypting file ' + file)
            with open(file[:-10], 'wb') as fw:
                fw.write(bytes(encrypto.decrypt(msg, DECRYPTION_KEY, PUBLIC_KEY)))
                fw.close()
            os.remove(file)
        except PermissionError:
            print('Cannot open ' + file)


os.remove('rsa_final_encryption_key.txt')
os.remove('rsa_final_decryption_key.txt')
os.remove('rsa_public_encryption_key.txt')

print('END')
