import random as rd
distance=[[int(rd.random()>0.5) for i in range(250)] for j in range(250)]
print('1')
print('250 250')
for i in range(250):
    print(''.join([str(j) for j in distance[i]]))

