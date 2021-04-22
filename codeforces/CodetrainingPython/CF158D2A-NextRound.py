import sys
from math import sqrt
input = lambda: sys.stdin.readline()

def Main():
	n,k = map(int,input().split(" "))
	p = input().split(" ")
	c=0
	for i in range(n):
		if int(p[i])>=int(p[k-1]) and int(p[i])>0:
			c=c+1
	print(c)

if __name__ == '__main__':
	Main()
