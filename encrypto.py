import random
import math


def generate_prime(k):
    '''
    Generates a k-bit prime number

    :param k: int
    :return: int
    '''
    r = 100 * (math.log(k, 2) + 1)
    r_ = r
    while r > 0:
        n = random.randrange(2 ** (k - 1), 2 ** (k))
        r -= 1
        if __is_prime(n) == True:
            return n
    return 0


def generate_encryption_key(p, q):
    '''
    Generates an rsa-encryption key from two prime numbers

    :param p: int
    :param q: int
    :return: int
    '''
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = __gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = __gcd(e, phi)
    return e


def generate_decryption_key(e, p, q):
    '''
    Generates a rsa-decryption key from a given encryption key, and its two prime number.

    :param e: int
    :param p: int
    :param q: int
    :return: int
    '''
    n = p * q
    phi = (p - 1) * (q - 1)
    d = __modinv(e, phi)
    return d


def encrypt(byte_array, encryption_key, public_key):
    '''
    Encrypts the byte array using the encryption key provided and returns an encrypted string.

    :param byte_array: list(bytes)
    :param encryption_key: int
    :param public_key: int
    :return: str
    '''
    encrypted_text = ''
    for byte in byte_array:
        encrypt_num = pow(byte, encryption_key, public_key)
        encrypted_text += str(encrypt_num) + '\n'
    return encrypted_text[:-1]


def decrypt(decryption_text, decryption_key, public_key):
    '''
    Decrypts the encrypted string using the decryption key provided and returns a byte array.
    The string can only be decrypted using the correct decryption key.

    :param decryption_text: str
    :param decryption_key: int
    :param public_key: int
    :return: list(bytes)
    '''
    decrypted_bytes = []
    for line in decryption_text.splitlines():
        decryptedNum = pow(int(line), decryption_key, public_key)
        if decryptedNum < 256:
            decrypted_bytes.append(decryptedNum)
    return decrypted_bytes


# Rabin Miller Primality Test (Online Code)
def __prime_test(n):
    s = n - 1
    t = 0
    while s & 1 == 0:
        s = s // 2
        t += 1
    k = 0
    while k < 128:
        a = random.randrange(2, n - 1)
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % n
        k += 2
    return True


# Online Code
def __is_prime(n):
    low_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        , 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179
        , 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269
        , 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367
        , 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461
        , 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571
        , 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661
        , 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773
        , 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883
        , 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if (n >= 3):
        if (n & 1 != 0):
            for p in low_primes:
                if (n == p):
                    return True
                if (n % p == 0):
                    return False
            return __prime_test(n)
    return False


def __gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def __egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = __egcd(b % a, a)
        return g, x - (b // a) * y, y


def __modinv(a, m):
    g, x, y = __egcd(a, m)
    if g != 1:
        raise Exception('Cannot find Modular Inverse')
    else:
        return x % m
