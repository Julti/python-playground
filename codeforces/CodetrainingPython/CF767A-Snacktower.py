import sys
from math import sqrt
input = lambda: sys.stdin.readline()

def Main():
	a = int(input())
	sn = input().split(" ")
	c=a
	s=set()
	for i in range(a):
		if int(sn[i])==c:
			r=[]
			r.append(c)

			for j in range(c-1,0,-1):
				if j in s:
					r.append(j)
					c=j
				else:
					break
			c=c-1
			print(' '.join(map(str, r)))
		else:
			s.add(int(sn[i]))
			print('')

if __name__ == '__main__':
	Main()
