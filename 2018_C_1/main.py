from collections import deque

def dfs(graph):
    visited, stack, previous= set(), [1],{}
    vertex = 1
    
    while stack:

        previous_vertex = vertex
        vertex = stack.pop()
        
            
        visited.add(vertex)
        previous[vertex]=previous_vertex
        inter=graph[vertex].intersection(visited)-{previous_vertex}
        if(bool(inter)):
            break
        else:
            stack.extend(graph[vertex] - visited)
    
    for e in inter:
        break
    
    v=vertex
    cycle=[v]
    while(v != e):
        v = previous[v]
        cycle.append(v)
    return cycle

def bfs(graph,cycle,N):
    l=[0 for i in range(N)]
    visited=set(cycle)
    queue=deque(cycle)
    while(queue):
        root=queue.popleft()
        new_elements=graph[root] - visited
        queue.extend(new_elements)
        for e in new_elements:
            visited.add(e)
            l[e-1]=l[root-1]+1
    return(l)

T=int(input())

for test in range(T):
    N=int(input())
    graph={}
    for i in range(N):
        l=input().split(' ')
        a,b=int(l[0]),int(l[1])
        if(a in graph.keys()):
            graph[a].add(b)
        else:
            graph[a]={b}
        if(b in graph.keys()):
            graph[b].add(a)
        else:
            graph[b]={a}

    cycle = dfs(graph)
    #print(cycle)
    l = bfs(graph,cycle,N) 

    print("Case #{}: {}".format(test+1, ' '.join(str(x) for x in l)))
