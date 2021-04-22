import sys
def Main():
    t = int(input())
    for i in range(t):
        k,n,w = input().split(' ')
        k=int(k)
        n=int(n)
        w=int(w)
        d = k+n+w
        x = int(d/7)
        c = d-(x*3)
        t = min(k,n,w)
        if(c%7==6 and t>x):
            print("YES")
        else:
            print("NO")



if __name__=='__main__':
    Main()