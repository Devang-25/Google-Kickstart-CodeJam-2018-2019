# Lancer le scripte : python3 main.py < input.txt > out.txt
# Imports
# Reads number of test cases




def main(n):
    l=[]
    while(n>0):
        l.append(n%10)
        n=n//10
    
    A=0
    B=0
    multi=1
    #print(l)
    for k in l:
        a,b=k,0
        if k==4:
            a,b=2,2
        A+=a*multi
        B+=b*multi
        multi*=10
    return str(A)+' '+str(B)


t = int(input())
# Writes in out.txt
for i in range(1, t + 1):
    n = int(input())
    # n, m = [int(s) for s in input().split(" ")]
    # v = [int(s) for s in input().split(" ")]
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    print("Case #{}: {}".format(i, main(n)))