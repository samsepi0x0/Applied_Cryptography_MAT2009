'''
    1 - EUCLIDEAN ALGORITHM implementation in Python.
    Author: Mohammad Nadir Khan
'''

import sys

def euclidean(a, b):
    '''
        EUCLIDEAN ALGORITHM: 
            r1 = max(a, b)
            r2 = min(a, b)
            while r2 > 0:
                q = r1 / r2 --> quotient
                r = r1 % r2 --> remainder
                r1 = r2
                r2 = r
            wait till remainder is 0, then return r2, that is the GCD of the two numbers.
    '''
    a, b = abs(a), abs(b)
    r1 = max(a,b)
    r2 = min(a,b)
    if r2 == 0:
        return r1
    while r2 > 0:
        q = r1 // r2
        r = r1 % r2
        r1 = r2
        r2 = r
    return r1

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("\tUsage: python3 ", sys.argv[0], " %d %d")
        print("[!] Expected 2 Arguments, got: ", len(sys.argv) - 1)
        sys.exit(0)
    try:
       	arg1 = int(sys.argv[1])
       	arg2 = int(sys.argv[2])
        print("[+]GCD: ", euclidean(arg1, arg2))
    except ValueError:
        print("[-]Error: Invalid Datatype of arguments supplied.")
        
