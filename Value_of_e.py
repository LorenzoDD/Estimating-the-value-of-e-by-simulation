import random

d = []
for i in range(100000):
    j = 0
    n = 0
    while(j<1):
        n = n+1
        j = j + random.random()
    d.append(n)
    
print(sum(d)/len(d))
