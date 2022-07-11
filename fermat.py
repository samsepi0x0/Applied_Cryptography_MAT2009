'''
    5 - FERMAT THEOREM implementation in Python.
    Author: Mohammad Nadir Khan
'''

from euc import euclidean
import sys

def prime(n):
    freq = 0
    for i in range(1, int(n // 2)):
        if n % i == 0:
            freq += 1
    return freq == 1

def fermat(a, p):
    if a % p == 0:
        print("[!]In Fermat Theorem, p ∤ a is necessary.")
        return False
    if not prime(p):
        print("[!]Solve using Euler theorem!")
        return False
    return (a ** (p-1)) % p == 1

def solve(a, power, p):
    new_power = power % (p-1)

    if fermat(a, p):
        #print(a, p, new_power)
        return (a**new_power) % p
    else:
    	return None

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 ", sys.argv[0], "a p m")
        print("\ta: number\n\tp:power\n\tm: mod (prime)")
        print("[+]\t\tEquation: a ** p (mod m)")
        print("[-]Error: Required 3 arguments, got: ", len(sys.argv)-1)
        sys.exit(0)
    try:
        a = int(sys.argv[1])
        power = int(sys.argv[2])
        mod = int(sys.argv[3])
        print("[!]Equation:\n\t",a , "**", power, "(mod ", mod, ")")
        result = solve(a, power, mod)
        if result is None:
            print("[!]No possible solution.")
        print("[+]Solution: ", result)
    except ValueError:
        print("[-]Error: Invalid Datatypes Supplied.")
