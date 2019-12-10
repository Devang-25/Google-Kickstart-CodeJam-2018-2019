# Lancer le scripte : python3 main.py < input.txt > out.txt
# Imports
# Reads number of test cases




def main(s):
    sol=''
    for c in s:
        if(c=='E'):
            sol+='S'
        else:
            sol+='E'
    return sol


t = int(input())
# Writes in out.txt
for i in range(1, t + 1):
    n = int(input())
    s = input()
    # n, m = [int(s) for s in input().split(" ")]
    # v = [int(s) for s in input().split(" ")]
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    print("Case #{}: {}".format(i, main(s)))
