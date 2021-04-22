import sys
input = lambda: sys.stdin.readline()

def Main():
	while True:
		try:
			step,mod = map(int,input().split(" "))
			s=set()
			s.add(0)
			v=[]
			v.append(0)
			for i in range(1,mod):
				v.append((v[i-1]+step)%mod)
				s.add((v[i-1]+step)%mod)
			ans = 'Bad Choice'
			if(len(s)==mod):
				ans = 'Good Choice'
			print("%10s%10s    %s"%(str(step),str(mod),str(ans)))
			print('')
		except:
			break

if __name__ == '__main__':
	Main()
