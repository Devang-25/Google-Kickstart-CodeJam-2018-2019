# Lancer le scripte : python3 main.py < input.txt > out.txt
# Imports
# Reads number of test cases


alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main(n,l,p):
    
    pset=set(p)
    seen = set()
    d = {}
    k=2
    while(k<=n and pset):
        if not(k in seen) :
            toRemove=[]
            for number in pset:
                if number % k ==0:
                    d[number]=(k,number//k)
                    toRemove.append(number)
            for r in toRemove:
                pset.remove(r)        

            aux = n//k
            for i in range(1,aux+1):
                seen.add(i*k)
        k+=1

    #print(d)
    primes=[]
    for number in p:
        a,b=d[number]
        if not(a in primes):
            primes.append(a)
        if not(b in primes):
            primes.append(b)
    
    primes.sort()
    #print(len(primes))
    #print(primes)

    dictionary_alphabet={}
    i=0
    for number in primes:
        dictionary_alphabet[number]=alphabet[i]
        i+=1

    indexes = [1]
    p_aux=[p[0]]
    previous = p[0]
    for number in p[1:]:
        if(previous != number):
            p_aux.append(number)
            previous = number
            indexes.append(1)
        else:
            indexes[-1]+=1
    
    
    tuples = []
    longueur = len(p_aux)
    if(longueur>=2):
        for i in range(longueur-1):
            number1 = p_aux[i]
            number2 = p_aux[i+1]
            a1,b1 = d[number1]
            a2,b2 = d[number2]
            if(a1==b2 or a1==a2):
                tuples.append((b1,a1))
            else:
                tuples.append((a1,b1))
        
        number1 = p_aux[longueur-2]
        number2 = p_aux[longueur-1]
        a1,b1 = d[number1]
        a2,b2 = d[number2]
        if(a2==a1 or a2==b1):
            tuples.append((a2,b2))
        else:
            tuples.append((b2,a2))
    else:
        number=p_aux[0]
        tuples.append(d[number])

    #print(indexes)
    #print(tuples)
    #print(p_aux)

    
    
    result_numbers=[0]

    for i in range(longueur-1):
        iterations = indexes[i]
        a,b = tuples[i]
    
        for j in range(iterations-1):
            if((j+iterations)%2 == 0):
                result_numbers.append(a)
            else:
                result_numbers.append(b)
        result_numbers.append(b)

    i=longueur-1
    iterations = indexes[i]
    a,b = tuples[i]

    for j in range(iterations):
        if(result_numbers[-1]==a):
            result_numbers.append(b)
        else:
            result_numbers.append(a)

    result_numbers[0]=p_aux[0]//result_numbers[1]
    
            


    result=""
    for number in result_numbers:
        result+=dictionary_alphabet[number]
    

    return result
    

t = int(input())
# Writes in out.txt
for i in range(1, t + 1):
    # n = int(input())
    #s = input()
    n, l = [int(s) for s in input().split(" ")]
    p = [int(s) for s in input().split(" ")]
    # m = [[int(s) for s in input().split(" ")] for _ in range(n)]
    print("Case #{}: {}".format(i, main(n,l,p)))
