# Lancer le scripte : python3 main.py < input.txt > out.txt
# Imports
# Reads number of test cases

import copy 

def countOccurences(possible):
    unique = []
    count = []
    for Maux in possible:
        if not Maux in unique:
            unique.append(Maux)
            count.append(1)
        else:
            index = unique.index(Maux)
            count[index]+=1
    return (unique,count)

def coupIsOk(R,C,M,x,y,direction):
    Maux = copy.deepcopy(M)
    Maux[x][y]=-1
    if direction=='V' :
        isOkSouth = True
        for i in range(x+1,R):
            if(Maux[i][y]==1):
                isOkSouth = False
            elif(Maux[i][y]==-1):
                break
            else:
                Maux[i][y]=-1
        isOkNorth = True
        for i in range(x-1,-1,-1):
            if(Maux[i][y]==1):
                isOkNorth = False
            elif(Maux[i][y]==-1):
                break
            else:
                Maux[i][y]=-1
        if(isOkSouth and isOkNorth):
            return Maux
    
    else:
        isOkEast = True
        for j in range(y+1,C):
            if(Maux[x][j]==1):
                isOkEast = False
            elif(Maux[x][j]==-1):
                break
            else:
                Maux[x][j]=-1
        isOkWest = True
        for j in range(y-1,-1,-1):
            if(Maux[x][j]==1):
                isOkWest = False
            elif(Maux[x][j]==-1):
                break
            else:
                Maux[x][j]=-1
        if(isOkEast and isOkWest):
            return Maux
    return False
    

def possibleCoups(R,C,M):
    possible = []
    empty = []
    for i in range(R):
        for j in range(C):
            if(M[i][j]==0):
                empty.append((i,j))
    
    for e in empty:
        x,y = e
        MV = coupIsOk(R,C,M,x,y,'V')
        if(MV): #and not(MV in possible)):
            possible.append(MV)
        MH= coupIsOk(R,C,M,x,y,'H')
        if(MH): #and not(MH in possible)):
            possible.append(MH)
    

    return possible
        
        

def victory(R,C,M,bettyIsPlaying):
    possible = possibleCoups(R,C,M)
    if(possible == []):
        return 0
    else:
        possible,count = countOccurences(possible)

        canBettyWin = 0
        index = 0
        for Maux in possible:
            canTerryWin = victory(R,C,Maux,False)>=1
            if(not canTerryWin):
                if(not bettyIsPlaying):
                    return 1
                canBettyWin+=count[index]
            index+=1
        return canBettyWin



def main(R,C,M):

    return victory(R,C,M,True)


t = int(input())
# Writes in out.txt
for i in range(1, t + 1):
    # n = int(input())
    R, C = [int(s) for s in input().split(" ")]
    M = []
    for k in range(R):
        s=input()
        M.append([])
        for j in range(C): 
            M[-1].append(int(s[j]=='#'))
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    print("Case #{}: {}".format(i, main(R,C,M)))