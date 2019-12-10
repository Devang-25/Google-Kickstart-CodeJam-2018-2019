# Lancer le scripte : python3 run.py < in.txt > out.txt
# Imports

# Reads number of test cases

t = int(input())
def main(N,P,team):

    
         
      
    team.sort()
    hours=0
    hoursList=[]  
    
    strongest=team[P-1]
    for k in range(P-1):
        hours+=(strongest-team[k])
    hoursList.append(hours)
    
    for k in range(P,N):
        new = team[k]
        strongest = team[k-1]
        weakest = team[k-P]

        change= (P-1)*(new - strongest) - (strongest-weakest)
        hours+=change
        hoursList.append(hours)
    #print(hours)
    #print(N,P,team,hoursList)
    return(min(hoursList))
    
    
# Writes in out.txt


for i in range(1, t + 1):
    N,P = [int(s) for s in input().split(" ")]
    team = [int(s) for s in input().split(" ")]
    print("Case #{}: {}".format(i,main(N,P,team)))
