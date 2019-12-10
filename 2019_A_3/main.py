# Lancer le scripte : python3 run.py < in.txt > out.txt
# Imports
# Reads number of test cases
t = int(input())


def main(bookings,N,Q):
    return dfs(bookings,N,Q)



def dfs(bookings,N,Q):
    values=[]
    if(Q==1):
        b=bookings[0]
        return(b[1]-b[0]+1)
    for i in range(Q):
        auxBookings=(bookings[:i]+bookings[i+1:]).copy()
        s=set()
        for b in auxBookings:
            for k in range(b[0],b[1]+1):
                s.add(k)
        s2=set()
        b=booking[i]
        for k in range(b[0],b[1]+1):
                s2.add(k)

        values.append(len(s2-s)+dfs(bookings,N,Q-1))
    return(min(values))


# Writes in out.txt
for i in range(1, t + 1):
    # n = int(input())
    # n, m = [int(s) for s in input().split(" ")]
    # v = [int(s) for s in input().split(" ")]
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    N,Q=[int(s) for s in input().split(" ")]
    bookings=[]
    for q in range(Q):
        l,r=[int(s) for s in input().split(" ")]
        bookings.append((l,r))
    
    
    print("Case #{}: {}".format(i, main(bookings,N,Q)))
