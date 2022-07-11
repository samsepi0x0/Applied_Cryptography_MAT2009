'''
	3 - CHINESE REMAINDER THEOREM implementation in Python.
	Author: Mohammad Nadir Khan
'''

from euc import euclidean
from exteuc import extendedEuclidean
import sys

def main():
	b = list()
	m = list()
	N = int(input("Number of Equations: "))
	
	if N <= 0:
		print("[-]Error: There must be more than 1 equation.")
		sys.exit(0)    
	
	for i in range(N):
		b1 = int(input("B" + str(i+1) + ": "))
		b.append(b1)
		
		m1 = int(input("M" + str(i+1) + ": "))
		m.append(m1)

	print("[!]Verifying the following set of equations...")

	for i in range(N):
		print("\tx ≡ ", b[i], "(mod ", m[i], ")")
	
	for i in range(len(m)-1):
		for j in range(i+1, len(m)):
			if m[i] < 0:
				print("[-]Error: ", m[i], " must be a +ve number.")
				sys.exit(0)
			if  m[j] < 0:
				print("[-]Error: ", m[j], " must be a +ve number.")
				sys.exit(0)
			gcd = euclidean(max(m[i], m[j]), min(m[i], m[j]))
			if gcd != 1:
				print("[-]Error: ", end='')
				print("GCD(", m[i], m[j], ") = ", gcd)
				print("[!]The values of M must be relatively prime.")
				sys.exit(0)
	M_product = 1
	for i in m:
		M_product *= i
	
	print("[+]Product of Modulos: ", M_product)
	
	M = list()
	
	for i in m:
		m1 = M_product // i
		print(m1)
		if euclidean(m1, i) ==	1:
			M.append(m1)
			
	print("[+]M[i] and Inverses: ")
	
	M_inverse = list()
	
	for val, m in zip(M, m):
		if(euclidean(val, m)) != 1:
			print("[-]Error: M/m and m must be relatively prime.")
			sys.exit(0)
		for x in range(1, m):
        		if (((val%m) * (x%m)) % m == 1):	
        			M_inverse.append(x)
	count = 0
	for i, j in zip(M, M_inverse):
		print("\tM", count+1, ": ", i, "\tM^-1", count+1, ": ", j)
		count += 1
	
	X = 0
	for i in range(N):
		X += b[i] * M[i] * M_inverse[i]
	
	print("[+]Solution: ")
	print("X = ", X%M_product)
		 
		

if __name__ == '__main__':
	main()
