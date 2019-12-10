# Lancer le scripte : python3 main.py < input.txt > out.txt
# Imports
# Reads number of test cases


def remaining(adversaires,i,program):
    P = []
    R = []
    S = []
    for s,n in adversaires:
        c = s[i%n]
        if(c=='P'):
            P.append((s,n))
        elif(c=='R'):
            R.append((s,n))
        else:
            S.append((s,n))
    empty = 0
    moveEmpty = []
    if(P==[]):
        empty+=1
        moveEmpty.append('P')
    if(R==[]):
        empty+=1
        moveEmpty.append('R')
    if(S==[]):
        empty+=1
        moveEmpty.append('S')

    if(empty==0):
        return(False,adversaires,program)
    elif(empty==2):
        if(not('P' in moveEmpty)):
            return(True,[],program+'S')
        elif(not('R' in moveEmpty)):
            return(True,[],program+'P')
        else:
            return(True,[],program+'R')
    else:
        if(moveEmpty==['P']):
            return(True,R,program+'R')
        elif(moveEmpty==['R']):
            return(True,S,program+'S')
        else:
            return(True,P,program+'P')


def main(A,adversaires):
    i=0
    possible=True
    program = ''
    while(possible and adversaires!=[] and i<500):
        possible,adversaires,program = remaining(adversaires,i,program)
        i+=1
    
    if(not possible):
       return 'IMPOSSIBLE'
    return program



t = int(input())
# Writes in out.txt
for i in range(1, t + 1):
    A = int(input())
    # n, m = [int(s) for s in input().split(" ")]
    # v = [int(s) for s in input().split(" ")]
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    adversaires=[]
    for k in range(A):
        s=input()
        adversaires.append((s,len(s)))
    print("Case #{}: {}".format(i, main(A,adversaires)))