# Код взят от сюда: https://translated.turbopages.org/proxy_u/en-ru.ru.b05a1d00-66c9fdf9-355f49d6-74722d776562/https/stackoverflow.com/questions/6313943/rsa-encryption-in-python
# solution t to a*t ≡ 1 (mod n) 
def multiplicative_inverse(a, n):

    t, newt = 0, 1
    r, newr = n, a

    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr

    if t < 0:
        t = t + n

    return t


p, q = 937, 353 # use large primes here
n = p*q
φ = (p-1)*(q-1)
e = 5 # choose public key e as a prime, s.t., gcd(φ, e) = 1
d = multiplicative_inverse(e, φ) # private key d
#print("Закрытый ключ: "+str(d))
#print("Открытый ключ: "+str(e))
public_key = e
private_key = d


def rsa_encrypt(plain_text, e, n):
    # ideally we should convert the plain text to byte array and 
    # then to a big integer which should be encrypted, but here for the sake of 
    # simplicity character-by-character encryption is done, which will be slow in practice
    cipher_text = [ord(x)**e % n for x in plain_text]        
    return cipher_text

def rsa_decrypt(cipher_text, d, n):
    decoded_text = ''.join([chr(x**d % n) for x in cipher_text])
    return decoded_text 


def encrypt_text(plain_text):
    cipher_text = rsa_encrypt(plain_text, e, n)
    return cipher_text

def decrypt_text(cipher_text):
    decoded_text = rsa_decrypt(cipher_text, d, n)
    return decoded_text