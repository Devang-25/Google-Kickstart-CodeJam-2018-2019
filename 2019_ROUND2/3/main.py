# Lancer le scripte : python3 main.py < input.txt > out.txt
# Imports
# Reads number of test cases



def getCondition(c1,c2):
    couple = c1[0]-c2[0],c1[1]-c2[1]
    if(couple[0]<=0 and couple[1]<=0):
        return 0,0
    elif(couple[0]>=0 and couple[1]>=0):
        return 2,0
    elif(couple[0]>0):
        return 1,-1*couple[1]/couple[0]
    else:
        return -1,-1*couple[0]/couple[1]

def difference(c1,c2):
    return c1[0]-c2[0],c1[1]-c2[1]
    



def mainAux(n,v):
    conditionGlobal = 2
    alpha = 0
    for i in range(n-1):
        condition,value = getCondition(v[i+1],v[i])
        if(condition == 0):
            return 0,0
        elif(condition == 1 or condition == -1):
            if(conditionGlobal == -1*condition):
                return 0,0
            conditionGlobal = condition
            alpha = max(alpha,value)
    return conditionGlobal,alpha

def main(n,v):
    condition,alpha = mainAux(n,v)
    if(condition == 0):
        return('IMPOSSIBLE')
    elif(condition == 2):
        return('1 1')
    elif(condition == 1):
        x = int(alpha + 1)
        return str(x)+' 1'
    else:
        y = int(alpha + 1)
        return '1 '+str(y)



t = int(input())
# Writes in out.txt
for i in range(1, t + 1):
    n = int(input())
    # n, m = [int(s) for s in input().split(" ")]
    # v = [int(s) for s in input().split(" ")]
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    v = []
    for j in range(n):
        a,b = input().split(" ")
        v.append((int(a),int(b)))
    print("Case #{}: {}".format(i, main(n,v)))