# Makes base 64
def encode64(m):
    alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
    # number 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31, 
    base64 = range(0,64)
    m_num = [0 for i in range(0,len(m))]
    i=0
    while i < len(m):
        j=0
        while j <= 63:
            if m[i] == alph[j]:
                m_num[i] = base64[j]
            j = j + 1
        i = i+1
    return m_num



# 6 bytes to 8 bytes
def changeBinary(m_num):
    #bin String function
    get_bin = lambda x, n: format(x, 'b').zfill(n)
    
    #convert to binary string
    m_bin = get_bin(m_num[0],6)

    i = 1
    while i < len(m_num):
       m_bin = m_bin + get_bin(m_num[i],6)
       i = i+1 
       # New binary
    c = [m_bin[i:i+8] for i in range(0, len(m_bin), 8)]
    i = 0
    while i < len(c):
        c[i] = int(c[i],2)
        i = i+1
    return c

# Changes numbers to letters
def decodeASCII(m_num):
    m = [0 for i in range(0,len(m_num))]
    i=0
    while i < len(m_num):
        m[i] = chr(m_num[i])
        i = i+1
    return m




#def alphPerm(m,t):
   # from itertools import permutations 
    #perms = permutations(range(0, 64))
    #return perms


def decodeMac(c):
    m = encode64(c)
    base64 = range(0,64)

    #m = changeBinary(m)
    p = decodeASCII(m)
    return p


runCaesar('LE2hSM27bp26')