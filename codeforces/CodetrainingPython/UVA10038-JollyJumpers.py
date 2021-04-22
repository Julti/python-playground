import sys
input = lambda: sys.stdin.readline()
def Main():
	while True:
		try:
			x = input().split(' ')
			if len(x)==0:
				break
			s = set()
			n = int(x[0])
			data = "Jolly"
			if n==1:
				data = "Jolly"
			else:
				for i in range(1,len(x)-1):
					s.add(abs(int(x[i])-int(x[i+1])))
				contains = True
				for i in range(1,n):
					if not(i in s):
						contains=False
				if contains:
					data = "Jolly"
				else:
					data = "Not jolly"
			print(data)
		except:
			break

if __name__ == '__main__':
	Main()
