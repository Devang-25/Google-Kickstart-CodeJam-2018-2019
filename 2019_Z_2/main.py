t=int(input())

def main():
    mas=[]
    for k in range(t):

        N=int(input())
        s=input()
        l=[int(c) for c in s]
        j = (N+1)//2
        i=0
        sums=[]
        while(j<N):
            sums.append(sum(l[i:j]))
            i+=1
            j+=1
        ma = max(sums)
        mas.append(ma)
    return(mas)


mas=main()
for k in range(t):
    print("Case #{}: {}".format(k+1, mas[k]))
    