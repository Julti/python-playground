import sys
from math import sqrt
input = lambda: sys.stdin.readline()

def Main():
	cases = int(input())
	for i in range(cases):
		days = int(input())
		p = int(input())
		parties = []
		for j in range(p):
			parties.append(int(input()))
		solve(days,parties)
	
def solve(days,parties):
	count = 0;
	for i in range(1,days+1):
		if i%7!=0 and i%7!=6:
			for j in range(len(parties)):
				if i%parties[j]==0:
					count=count+1
					break
	print(count)
if __name__ == '__main__':
	Main()
