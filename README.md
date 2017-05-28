# encrypto-gray
A small Python script test for encrypting a directory using a 32-bit deterministic RSA encryption scheme.
## Usage
Place the required files into a local directory. Run the script <b>encrypto-run.py</b> and all accessible files within 
the directory will be rsa-encrypted with a generated rsa-encryption key of 32-bit. The public key and 32-bit rsa-decryption
key will also be generated and saved to a text file.

To decrypt the files, simply run <b>decrypto.py</b> and all .encrypted files will be decrypted using the given rsa-decryption
key.

<i> The files CANNOT be decrypted otherwise without the proper decryption key </i>

## Notes
The script takes a fair amount of time to run and is recommended to not encrypt any files that are larger than 100KB.

The encryption bit (key size) can also be changed although not advised.
