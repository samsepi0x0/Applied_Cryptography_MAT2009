'''
    4 - EULER THEOREM implementation in Python
    Author: Mohammad Nadir Khan
'''

from euc import euclidean
import sys

def euler_totient(n):
    if not n >= 1:
        print("[-]Error: Can't calculate Euler Totient function for -ve values.")
        sys.exit(0)
    phi = 0
    for i in range(1, n):
        if euclidean(n, i) == 1:
            phi += 1
    return phi

def euler_theorem(a, m):
    phi_m = euler_totient(m)
    if euclidean(a, m) != 1:
        print("[-]Error: GCD of ", a, ", ", m, " is not 1.\n[!]Euler Theorem only valid if gcd(a,m) = 1. \n[!]GCD: ", euclidean(a, m))
        sys.exit(0)
    if ((a ** phi_m) % m) == 1:
        return True
    return False

def solve(a, n, m):
    phi_m = euler_totient(m)
    new_n = n % phi_m

    if euler_theorem(a, m):
        return (a ** new_n) % m

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 ", sys.argv[0], "a p m")
        print("\ta: number")
        print("\tp: print")
        print("\tm: mod")
        print("\t\tEquation: a ** p (mod m)")
        print("[-]Error: Required 3 arguments, got: ", len(sys.argv) - 1)
        sys.exit(0)
    try:
        a = int(sys.argv[1])
        power = int(sys.argv[2])
        mod = int(sys.argv[3])
        print("[+]Equation:\n\t ", a, "**", power, " (mod ", mod, ")")
        result = solve(a, power, mod)
        print("[+]Solution: ", result)
    except ValueError:
        print("[-]Error: Invalid Datatypes Supplied.")
