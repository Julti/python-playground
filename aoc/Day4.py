import sys
import re
def main():
    vals = []
    fix=True
    while fix:
        a=input()
        if a=='\n' or a =='':
            break
        else:
            vals.append(a)
    x=0
    y=0
    count = 0
    while(y+1<len(vals)):
        y+=1
        x+=3
        if(vals[y][x%len(vals[0])]=='#'):
            count+=1
    print(count)
if __name__ == '__main__':
    main()