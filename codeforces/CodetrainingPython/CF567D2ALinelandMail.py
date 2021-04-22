import sys
input = lambda: sys.stdin.readline()
def Main():
	n = int(input())
	p = input().split(" ")
	for i in range(n):
		minv=0;
		maxv=0;
		if i==0:
			minv = abs(int(p[i])-int(p[i+1]))
			maxv = abs(int(p[i])-int(p[n-1]))
		elif i==n-1:
			minv = abs(int(p[i])-int(p[i-1]))
			maxv = abs(int(p[i])-int(p[0]))
		else:
			minv = min(abs(int(p[i])-int(p[i-1])),abs(int(p[i])-int(p[i+1])))
			maxv = max(abs(int(p[i])-int(p[0])),abs(int(p[i])-int(p[n-1])))
		print("%5d %5d"%(minv,maxv))
if __name__ == '__main__':
	Main()
