p = 563036103490583
q = 1063300642915937
e = 372585779765210097553647509959
n = p * q
phi = (p - 1) * (q - 1)
x1 = 399754188907643924420059310699

def powByMod(num: int, power: int, mod: int):
    ans = 1
    while power > 0:
        if power % 2 == 1:
            ans *= num
            ans %= mod
        num *= num
        num %= mod
        power >>= 1
    return ans

def gcd(ee: int, phii: int):
    if ee == 0:
        return phii, 0, 1
    d, x1, y1 = gcd(phii % ee, ee)
    x = y1 - (phii // ee) * x1
    y = x1
    return d, x, y

def encryptAndDecrypt(msg: int, key: int):
    if key >= 0:
        return powByMod(msg, key, n)
    return powByMod(powByMod(msg, phi - 1, n), -key, n)

def generateKey():
    nod, c1, c2 = gcd(e, phi)
    if nod != 1:
        print('Error')
    return c1

def main():
    d = generateKey()
    y1 = encryptAndDecrypt(x1, e)
    print('Program start!')
    while True:
        print('Choice the operation:\n1 - Gen\n2 - Encr\n3 - Decr\n4 - Exit\n')
        print('Enter: ', end='')
        choicePerson = int(input())

        if choicePerson == 1:
            print('---------------------------------------------------------------------')
            print('Key =', d)
            print('---------------------------------------------------------------------')
        elif choicePerson == 2:
            print('---------------------------------------------------------------------')
            print('x1 =', x1)
            print('y1 =', y1)
            print('---------------------------------------------------------------------')
        elif choicePerson == 3:
            print('---------------------------------------------------------------------')
            print('y1 =', y1)
            print('x1 =', encryptAndDecrypt(y1, d))
            print('---------------------------------------------------------------------')
        elif choicePerson == 4:
            print('---------------------------------------------------------------------')
            print('Exit')
            print('---------------------------------------------------------------------')
            break
    print('End of program')

main()
