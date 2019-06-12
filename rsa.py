import random

def mdc(a, b):
    if (b == 0):
        return a
    else:
        return mdc(b, a % b)

def epick(n, z):
    # passo 3 do algoritmo
    # escolhe e, tal que e < n e que não possua nenhumn fator em comum com z
    while (True):
        e = random.randrange(2, z)
        if (mdc(e, z) == 1):
            return e

def dpick(e, z):
    # passo 4 do algoritmo
    # escolhe d, tal que e*d-1 seja divisível exatamente por z
    d = 1
    while(True):
        d = (e*d)-1
        if(d % z == 0):
            return d
        else:
            d += 1

def main():
    p = 5
    q = 7
    n = p*q
    z = (p-1)*(q-1)
    e = epick(n, z)
    d = dpick(e, z)
    # print ("P:", p, "Q:", q, "N:", n, "Z:", z, "E:", e, "D:", d)
    publickey = n, e
    privatekey = n, d
    print(publickey)
    print(privatekey)

if __name__ == '__main__':
    main()
