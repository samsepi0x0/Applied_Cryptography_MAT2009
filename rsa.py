import sys
from fermat import prime
from euc import euclidean
from exteuc import extendedEuclidean

def rsa_check(p, q, e):
    p_prime, q_prime = prime(p), prime(q)
    if not p_prime:
        print("[-] ", p, " is not a prime number.")
        sys.exit(0)
    if not q_prime:
        print("[-] ", q, " is not a prime number.")
        sys.exit(0)
    n = p * q
    phi_n = (p-1) * (q-1)

    gcd = euclidean(phi_n, e)

    if gcd != 1:
        print("[-] ", e, " must be relatively prime to euler Φ(", n, ").")
        sys.exit(0)
    return True

def encrypt_rsa(p, q, e, m):
    check = rsa_check(p, q, e)
    n = p * q
    ct = list()
    if check:
        print("[?] Encryting message now...")
        for i in m:
            temp_ct = (ord(i) ** e) % n
            ct.append(temp_ct)
    return ct

def decrypt_rsa(p, q, e, ct):
    check = rsa_check(p, q, e)
    m = list()
    if check:
        n = p * q
        phi_n = (p-1) * (q-1)
        print("[?] Calculating private key...")
        _, _, d = extendedEuclidean(phi_n, e)
        print("[+] Decrypting message now...")
        for i in ct:
            m_temp = chr((int(i) ** d) % n)
            m.append(m_temp)
    return m

def main():
    try:
        p = int(input("P: "))
        q = int(input("Q: "))
        e = int(input("E: "))
        choice = int(input("\n1.Encrypt\n2.Decrypt\n>>> "))
        if choice == 1:
            message = input("Message: ")
            ct = encrypt_rsa(p, q, e, message)
            print("[+] Ciphertext: ", end='')
            for i in ct:
                print(i, end=' ')
            print()
        else:
            ct = input("Ciphertext: ").split(" ")
            message = decrypt_rsa(p, q, e, ct)
            print("[+] Plaintext: ", end='')
            for i in message:
                print(i, end='')
            print()
    except:
        print("[-] Exception Occured. Try again with proper inputs.")
        sys.exit(0)


if __name__ == '__main__':
    main()
