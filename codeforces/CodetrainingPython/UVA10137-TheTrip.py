import sys
input = lambda: sys.stdin.readline()
def Main():
	while True:
		x = int(input())
		if x==0:
			break;
		sum = 0.00
		values =[]
		for i in range(x):
			index = float(input())
			values.append(index)
			sum+=index
		avg = float(round(sum/x, 2))
		resp = 0.00
		resn = 0.00
		for x in values:
			if x-avg<0:
				resn+=abs(x-avg)
			else:
				resp+=abs(x-avg)
		if(resp>resn):
			print("$%.2f"%resn)
		else:
			print("$%.2f"%resp)
if __name__ == '__main__':
	Main()
