def rotations(l):
    out = []
    for i in range(len(l)):
        a = shift(l, i)
        out += [a]
    return out

def shift(l, n):
    return l[n:] + l[:n]

if __name__ == '__main__':
    l = [0,1,2,3,4]
    for x in rotations(l):
        print(x)