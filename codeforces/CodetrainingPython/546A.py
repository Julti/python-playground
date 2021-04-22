import sys
def Main():
    k,n,w = input().split(' ')
    k=int(k)
    n=int(n)
    w=int(w)
    req = ((w*(w+1))/2)*k
    if req>n:
        print(int(req-n))
    else:
        print(0)

if __name__ == '__main__':
	Main()