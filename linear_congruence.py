'''
    6 - SOLVING LINEAR CONGRUENCE in Python.
    Author: Mohammad Nadir Khan
'''

import sys
from euc import euclidean
from euler import euler_totient

def solve(a, b, m):
    d = euclidean(a, m)
    if b % d != 0:
        return list()
    if d != 1:
        a = a // d
        b = b // d
        m = m // d
    result = list()
    phi_m = euler_totient(m)

    x = b * (a ** (phi_m - 1)) % m

    for k in range(d):
        t = x + k * m
        result.append(t)

    return result
    

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 ", sys.argv[0], " A B M")
        print("Equation:\t AX = B (mod M)")
        print("A, B, M --> ints")
        print("[-]Error: Required 3 Arguments, got: ", len(sys.argv) - 1)
        sys.exit(0)
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        m = int(sys.argv[3])
        print("Equation: ", a, "X = ", b, "(mod", m,")") 
        result = solve(a, b, m)
        if len(result) == 0:
            print("No solution for the congruence equation.")
            sys.exit(0)
        print(len(result), " unique solution(s).")
        for i in result:
            print("\t", i, end='')
        print()
    except ValueError:
        print("[-]Error: Invalid Datatypes supplied.")

if __name__ == '__main__':
    main()
