# Lancer le scripte : python3 main.py < input.txt > out.txt
# Imports
# Reads number of test cases

import copy 

def getMatrix(n,v):
    m = [[0 for i in range(n)] for j in range(n)]
    i,j = -1,-1
    for a,b in v:
        i+=1
        j=-1
        for a2,b2 in v:
            j+=1
            couple = (a2-a),(b2-b)
            if(couple[0]==0 and couple[1]==0):
                continue
            elif(couple[0]>=0 and couple[1]>=0):
                m[i][j]=2
            elif(couple[0]>0):
                m[i][j]=1
            else:
                m[i][j]=-1
    return m

def getCondition(c1,c2):
    couple = c1[0]-c2[0],c1[1]-c2[1]
    if(couple[0]==0 and couple[1]==0):
        return 0
    elif(couple[0]>=0 and couple[1]>=0):
        return 2
    elif(couple[0]>0):
        return 1
    else:
        return -1


def canBeInserted(c1,c2,c3,cond3):
    cond1 = getCondition(c1,c2)
    cond2 = getCondition(c2,c3)
    if (cond1 == cond2 and (cond2 == cond3 or cond3==2)):
        return True
    return False

def difference(c1,c2):
    return c1[0]-c2[0],c1[1]-c2[1]
    
def compatibles(couple,m):
    x,y = couple
    newm=[]
    for path in m:
        condition = 2
        n = len(path)
        for i in range(n-1) :
            couple = difference(path[i+1],path[i])
            if(couple[0]>0 and couple[1]<0):
                condition = 1
                break
            elif(couple[0]<0 and couple[1]>0):
                condition = -1
                break
        pathaux = copy.deepcopy(path)
        pathaux.append((x+1,y+1))
        pathaux = [(0,0)]+pathaux
        for i in range(n+1) :
            #print(':)')
            if(canBeInserted(pathaux[i],(x,y),pathaux[i+1],condition)):
                pathaux2 = copy.deepcopy(path)
                pathaux2.insert(i,(x,y))
                newm.append(pathaux2)
                #break
    return newm

        




def everyChoices(n,v):
    if(n==1):
        return [[v[0]]]
    else:
        couple = v.pop()
        m = everyChoices(n-1,v)
        #print(m)
        return compatibles(couple,m)




def main(n,v):
    #m = getMatrix(n,v)
    #print(m)
    #print(n,v)
    m = everyChoices(n,v)
    print(m)
    return len(m)


t = int(input())
# Writes in out.txt
for i in range(1, t + 1):
    n = int(input())
    # n, m = [int(s) for s in input().split(" ")]
    
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    v = []
    for j in range(n):
        a,b = input().split(" ")
        v.append((int(a),int(b)))
    print("Case #{}: {}".format(i, main(n,v)))