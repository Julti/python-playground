import sys
def main():
    vals = []
    t=0
    data = []
    fix=True
    while fix:
        try:
            a=int(input())
            vals.append(a)
            x = 2020-a
            if x in vals:
                data.append(a*x)
        except:
            fix=False
    print(data)
    solve_for_three(vals)
def solve_for_three(vals):
    data2 = []
    print(len(vals))
    for x in range(len(vals)):
        for j in range(len(vals)):
            for k in range(len(vals)):
                if((x!=j and j!=k) and (vals[x]+vals[j]+vals[k]==2020)):
                    data2.append(vals[x]*vals[j]*vals[k])
    print(data2)
if __name__ == '__main__':
    main()



