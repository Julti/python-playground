import sys
input = lambda: sys.stdin.readline()
def Main():
	n = int(input())
	p = input().split(" ")
	r =[0]*n
	for i in range(n):
		r[int(p[i])-1]=i+1
	print(' '.join(map(str, r)))  

if __name__ == '__main__':
	Main()
