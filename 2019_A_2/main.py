# Lancer le scripte : python3 run.py < in.txt > out.txt
# Imports
from time import time
#import pyximport
#pyximport.install()
import functions

# Reads number of test cases
t = int(input())






# Writes in out.txt



for k in range(1, t + 1):
    # n = int(input())
    # n, m = [int(s) for s in input().split(" ")]
    # v = [int(s) for s in input().split(" ")]
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    R,C = [int(s) for s in input().split(" ")]
    grid = []
    for i in range(R):
        grid.append([int(s) for s in input()])
    #print(grid)
    time1=time()
    print("Case #{}: {}".format(k, functions.main(grid,R,C)))
    print(time()-time1)