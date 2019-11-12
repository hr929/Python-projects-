from numpy import *
m=[[1,3,2],[2,3,1],[3,2,1]]
def accessij(o,i,j):
    return [row[:j] + row[j+1:] for row in (o[:i]+o[i+1:])]
def Determinant(o):
    if len(o) == 1:
        return o[0][0]

    d=0
    for c in range(len(o)):
        d+=((-1)**c)*o[0][c]*Determinant(accessij(o,0,c))
    return d
cp=[]
for r in range(len(m)):
        cr= []
        for c in range(len(m)):
            minor = accessij(m,r,c)
            cr.append((((-1)**(r+c)) *Determinant(minor))/Determinant(m))
        cp.append(cr)
g=matrix(cp)
g=g.T
print(g)
print("Matrix inverse directly using numpy:")
print(linalg.inv(m))
