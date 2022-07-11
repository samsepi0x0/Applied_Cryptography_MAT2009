'''
    2 - EXTENDED EUCLIDEAN implementation in Python.
    Author: Mohammad Nadir Khan
'''
import sys

def extendedEuclidean(a,b):
    '''
        r1 --> GCD of two numbers
        s1 --> coefficient of equation
        t1 --> multiplicative inverse (?)
    '''
    a, b = abs(a), abs(b)
    r1 = max(a, b)
    r2 = min(a, b)
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        r1 = r2
        r2 = r

        s = s1 - q*s2
        s1 = s2
        s2 = s

        t = t1 - q*t2
        t1 = t2
        t2 = t
        #print(t1, t2, t)

    return (r1, s1, t1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("\tUsage: python3", sys.argv[0], "%d %d")
        print("[!]Expected 2 arguments, got: ", len(sys.argv)-1)
        sys.exit(0)
    try:
        arg1 = int(sys.argv[1])
        arg2 = int(sys.argv[2])
        d, x, y = extendedEuclidean(arg1, arg2)
        print("[+]GCD: ", d)
        print("[!]General Equation: Ax + By = D")
        print("[+]Value of X: ", x, "\n[+]Value of Y: ", y)
    except ValueError:
        print("[!]Error: Invalid DataType supplied.")
