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
def main2():
    vals = []
    fix=True
    while fix:
        a=input()
        if a=='\n' or a =='':
            break
        else:
            vals.append(a)
    
    tot=1
    coor=[[1,1],[3,1],[5,1],[7,1],[1,2]]
    for c in coor:
        x=0
        y=0
        count = 0
        while(y+1<len(vals)):
            y+=c[1]
            x+=c[0]
            if(vals[y][x%len(vals[0])]=='#'):
                count+=1
        tot = tot*count
    print(tot)
if __name__ == '__main__':
    main()