import sys
from Crypto.Cipher import DES
from Crypto import Random


# XOR a with b
def xor(a,b):
    x = []
    i = 0
    d = int
    while i < 8:
        d = ord(b[i])
        x.append(a[i] ^ d)
        i = i+1
    return x


# Check length/pad
def pad(x):
    while len(x) % 8 != 0:
        x = x + '='
    return x


# Get plaintext
p = open(sys.argv[2], "r")
plain = p.read()
p.close()


# Get key
key = sys.argv[1]
print ('Key:', key)
e = DES.new(key, DES.MODE_ECB)

# Initial Vector
iv = Random.new()
iv = iv.read(8)
#iv = b'0x00x00x00x00x00x00x00x0'   # Test Initial Vector
print('Initial Vector:', iv)


#CBC Loop
def cbc(p,iv):
    #First round (initial vector plus plain)
    cNew = xor(iv, p[0:8])

    # Make c_i a string of hex, not a list
    cHex = ''.join('{:02X}'.format(a) for a in cNew)

    # Encrypte with DES 
    c = e.encrypt(cHex)
    cPre = cNew
    
    j = 8
    while j < len(p):
        # Slice plaintext into 8 byte pieces
        plainSect = p[j:j+8]
        
        # Xor c_i-1 with m_i
        cNew = xor(cPre, plainSect)

        # Make c_i a string of hex, not a list
        cHex = ''.join('{:02X}'.format(a) for a in cNew)
 
        # Encrypt with DES and add to c
        c = c + (e.encrypt(cHex))

        cPre = cNew
        j = j+8    
    return c


plainPad = pad(plain)

ciphertext = str(cbc(plainPad,iv))
# Set up ciphertext file
output = open('ciphertext.txt', 'w')
output.write(ciphertext)
output.close()