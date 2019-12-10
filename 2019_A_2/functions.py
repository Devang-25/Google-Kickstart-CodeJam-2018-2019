from time import time
from collections import deque

def neighbours(a,b,R,C):
    neighbours=[]
    if(a>0):
        neighbours.append((a-1,b))
    if(a<R-1):
        neighbours.append((a+1,b))
    if(b>0):
        neighbours.append((a,b-1))
    if(b<C-1):
        neighbours.append((a,b+1))
    return(neighbours)

def grid_to_distances(grid,R,C):

    distance,nodes = [[-1 for j in range(C)]for i in range(R)],[]

    i=0
    for row in grid:
        j=0
        for value in row:
            if value :
                nodes.append((i,j))
                distance[i][j]=0
            j+=1
        i+=1
    
    queue=deque(nodes)
    visited=set(nodes)

    while(queue):
        a,b = queue.popleft()
        neighboursList=neighbours(a,b,R,C)
        currentDistance = distance[a][b]

        for n in neighboursList:
            if(not n in visited):
                visited.add(n)
                queue.append(n)
                na,nb=n
                distance[na][nb]=currentDistance+1

    return(distance)


# compute the change in distance by inserting node into the grid
def change_distance(distanceReal,a,b,R,C,betterMax,actualMax):

    distance = [distanceReal[i].copy() for i in range(R)]
    
    queue=deque([(a,b)])
    visited=set([(a,b)])

    distance[a][b]=0

    while(queue):
        a,b = queue.popleft()
        neighboursList=neighbours(a,b,R,C)
        currentDistance = distance[a][b]
        changeMax=False
        for n in neighboursList:
            na,nb=n
            d=distance[na][nb]
            if((not n in visited) and currentDistance+1<d):
                if(currentDistance+1 >= betterMax):
                    return betterMax
                visited.add(n)
                queue.append(n)
                changeMax=(d==actualMax)
                distance[na][nb]=currentDistance+1
    if(not changeMax):
        return actualMax
    
    return(overall_time(distance,R,C))

def overall_time(distance,R,C):
    return(max([max(v) for v in distance]))

def main(grid,R,C):
    
    distanceMatrix = grid_to_distances(grid,R,C)
    #print(distanceMatrix)
    
    trueOverallTime=overall_time(distanceMatrix,R,C)
    overallTime=trueOverallTime
    
    for i in range(R):
        for j in range(C):
            
            if(distanceMatrix[i][j]>0):
                overallTime2 = change_distance(distanceMatrix,i,j,R,C,overallTime,trueOverallTime)
                overallTime = min(overallTime,overallTime2)
    
    #print(t2-t1,t3-t2)
    #print(distanceMatrix)
    return overallTime
