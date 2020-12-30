import sys
import re
def main():
    count =0
    fix = True
    while fix:
        try:
            a=input()
            dat = a.split(':')
            char = dat[0].split(' ')[1]
            s = dat[1]
            min = int(dat[0].split(' ')[0].split("-")[0])
            max = int(dat[0].split(' ')[0].split("-")[1])
            counti=0
            for i in s:
                if i==char:
                    counti+=1
            if counti>=min and counti<=max:
                count+=1
        except:
            fix=False
    print(count)
def main2():
    count =0
    fix = True
    while fix:
        try:
            a=input()
            dat = a.split(':')
            char = dat[0].split(' ')[1]
            s = dat[1].replace(' ','')
            min = int(dat[0].split(' ')[0].split("-")[0])-1
            max = int(dat[0].split(' ')[0].split("-")[1])-1
            if ((s[min]==char or s[max]==char)and not(s[min]==char and s[max]==char)):
                count+=1
        except:
            fix=False
    print(count)
if __name__ == '__main__':
    main2()