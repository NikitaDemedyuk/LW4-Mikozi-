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

def writeToFile(filename, mode, x1, y1, type):
    file = open(filename, mode)
    if type == 1:
        file.write('Key =' + str(generateKey()))
    elif type == 2:
        file.write('x1 =' + x1 + '\n' + 'y1 =' + y1)
    elif type == 3:
        file.write('y1 =' + y1 + '\n' + 'x1 =' + x1)
    file.close()

def main():
    print('Program start!')
    while True:
        print('Choice the operation:\n1 - Gen\n2 - Encr\n3 - Decr\n4 - Exit\n')
        print('Enter: ', end='')
        choicePerson = int(input())

        if choicePerson == 1:
            print('---------------------------------------------------------------------')
            print('Key =', generateKey())
            writeToFile('Report.txt', 'w', '', '', choicePerson)
            print('---------------------------------------------------------------------')
        elif choicePerson == 2:
            print('---------------------------------------------------------------------')
            print('x1 =', x1)
            print('y1 =', encryptAndDecrypt(x1, e))
            writeToFile('Report.txt', 'w', str(x1), str(encryptAndDecrypt(x1, e)), choicePerson)
            print('---------------------------------------------------------------------')
        elif choicePerson == 3:
            print('---------------------------------------------------------------------')
            print('y1 =', encryptAndDecrypt(x1, e))
            print('x1 =', encryptAndDecrypt(encryptAndDecrypt(x1, e), generateKey()))
            writeToFile('Report.txt', 'w', str(encryptAndDecrypt(encryptAndDecrypt(x1, e), generateKey())), str(encryptAndDecrypt(x1, e)), choicePerson)
            print('---------------------------------------------------------------------')
        elif choicePerson == 4:
            print('---------------------------------------------------------------------')
            print('Exit')
            print('---------------------------------------------------------------------')
            break
    print('End of program')

main()
