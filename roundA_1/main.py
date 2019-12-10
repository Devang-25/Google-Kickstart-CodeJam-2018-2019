# Lancer le scripte : python3 main.py < input.txt > out.txt
# Imports
# Reads number of test cases

def intersect(S,valueS,N,valueN):
    Y = []
    print(S,N)

    while(S!=[] and N !=[]):
        if(N[0]<=S[0]):
            value = N.pop(0)
            Y.append(value)
        else:
            value = S.pop(0)
            Y.append(-value)
    if(S==[]):
        Y+=N
    else:
        for s in S:
            Y.append(-s)
    longu = len(Y)+1
    valueY = [0 for i in range(longu)]
    for j in range(longu-1):
        if(Y[j]<0):
            for k in range(j+1):
                valueY[k]+=1
        else:
            for k in range(j+1,longu):
                valueY[k]+=1

    
    i=0
    j=0
    trueY=[]
    trueValueY=[]

    while(i<longu-1):
        j=i
        current = 0
        trueY.append(abs(Y[i]))
        trueValueY.append(valueY[i])
        while(j<longu-1 and abs(Y[j])==abs(Y[i])):
            j+=1
            if(valueY[j]>current):
                current = valueY[j]
        if(j>i):
            trueValueY.append(current)
            trueY.append(abs(Y[i]))
            i=j
        else:
            i+=1
        


    return((trueY,trueValueY))

        


def main(P,Q,testcase):

    E = []
    valueE = [0]
    longE = 0
    W = []
    valueW = [0]
    longW = 0
    N = []
    valueN = [0]
    longN = 0
    S = []
    valueS = [0]
    longS = 0

    for i in range(P):
        x,y,d = testcase.pop()
        
        if(d == 'N'):
            j=0
            while(j<longN and N[j]<y+1):
                j+=1
            if(True):
                N.insert(j,y+1)
                longN+=1
                valueNaux = valueN.copy()
                valueN = valueNaux[:j+1]+([valueNaux[k]+1 for k in range(j,longN)])
            else:
                for k in range(j,longN+1):
                    valueN[k]+=1
  
        if(d == 'S'):
            j=0
            while(j<longS and S[j]<y-1):
                j+=1
            
            if(True):
                S.insert(j,y-1)
                longS+=1
                
                valueSaux = valueS.copy()
                valueS = ([valueSaux[k]+1 for k in range(0,j+1)])+valueSaux[j:]
            
            else:
                for k in range(j):
                    valueS[k]+=1

    Y,valueY = intersect(S,valueS,N,valueN)
    return(Y,valueY)
                

            
            

    
    




t = int(input())
# Writes in out.txt
for i in range(1, t + 1):
    #n = int(input())
    P,Q = [int(s) for s in input().split(" ")]
    testcase = []
    for j in range(P):
        aux = input().split(" ")
        testcase.append([int(s) for s in aux[:2]]+[aux[2]])
    # v = [int(s) for s in input().split(" ")]
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    print("Case #{}: {}".format(i, main(P,Q,testcase)))