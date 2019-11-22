from random import random as r

def avg_uses(n, it=100000):
    l = []
    prob = 1/n
    for i in range(it):
        a = 0
        while r() > prob:
            a += 1
        l.append(a)
    return l

def avg(l):
    return sum(l)/len(l)

l = avg_uses(5)

print(avg(l))