from math import *
from time import *

def loadPoints(file):
    #Load file
    X, Y, Z = [], [], [] 
    
    with open(file) as f:
        
        for line in f:
            x, y, z = line.split('\t')
            
            X.append(float(x))
            Y.append(float(y))
            Z.append(float(z))
    
    return X, Y, Z

def  getNN(xq, yq, zq, X, Y, Z):
    #Find nearest point
    dmin = inf
    xn, yn, zn = X[0], Y[0], Z[0]
    
    for i in range(len(X)):
        #Compute distance
        dx = xq - X[i]
        dy = yq - Y[i]
        dz = zq - Z[i]
        d = (dx*dx + dy*dy + dz * dz)**0.5
        
        #Actualize minimum
        if d < dmin:
            dmin = d
            xn = X[i]
            yn = Y[i]
            zn = Z[i]
    return xn, yn, zn, dmin

def init_Index(X, Y, Z, nr):
    #Extreme values
    xmin, xmax = min(X), max(X)
    ymin, ymax = min(Y), max(Y)
    zmin, zmax = min(Z), max(Z)
    #Minmax box dimensions
    dx = xmax - xmin
    dy = ymax - ymin
    dz = zmax - zmin
    #Cell sizes
    bx = dx / nr
    by = dy / nr
    bz = dz / nr
    
    return xmin, ymin, zmin, dx, dy, dz, bx, by, bz

def get3DIndex(x, y, z, dx, dy, dz, nr):
    #Return 3D spatial index
    xr = (x - xmin)/dx
    yr = (y - ymin)/dy
    zr = (z - zmin)/dz
    
    #Spatial indexes
    c = 0.99
    jx = int(c*xr*nr)
    jy = int(c*yr*nr)
    jz = int(c*zr*nr)
    
    return jx, jy, jz

def Hash(jx, jy, jz, nr):
    # Compute 3D index to 1D index
    nr = int(nr)
    return jx + jy * nr + jz * nr**2

def inverseHash(j, nr):
    #Compute 1D to 3D
    nr = int(nr)
    # j=jx+jy*nr+jz*nr**2
    jx = j
    jy = j/nr
    jz = j/(nr**2)
    return jx, jy ,jz

def indexPoints(X, Y, Z, xmin, ymin, zmin, dx, dy, dz):
    #Index point cloud
    H = {}
    for i in range(len(X)):
        #Compute 3D index
        jx, jy, jz = get3DIndex(X[i], Y[i], Z[i], dx, dy, dz, nr)
        #Compute hash
        j = Hash(jx, jy, jz, nr)
        #Add to hash table
        if j not in H:
            H[j] = [i]
        else:
            H[j].append(i)
    return H

#Load points
X, Y, Z = loadPoints('points3.txt')

#Initialize index
n = len(X)
nr = int(n**(1/9))
xmin, ymin, zmin, dx, dy, dz, bx, by, bz = init_Index(X, Y, Z, nr)

#3D index
x, y, z = 500, 500, 500
jx, jy, jz = get3DIndex(x, y, z, dx, dy, dz, nr)
print(jx, jy, jz)

j = Hash(jx, jy, jz, nr)
print(j)

#Index point cloud
H = indexPoints(X, Y, Z, xmin, ymin, zmin, dx, dy, dz)

#NN search, v1
for i in range(len(X)):
    xn, yn, zn, dmin = getNN(X[i], Y[i], Z[i], X, Y, Z)
    print(xn, yn, zn, dmin)

#NN search, v2
for i in range(len(X)):
    #Compute 3D index
    jx, jy, jz = get3DIndex(X[i], Y[i], Z[i], dx, dy, dz, nr)
    #Hash
    j = Hash(jx, jy, jz, nr)
    #Indexes of points
    ixd = H[j]
    
    #Compute idx to coordinates
    #1D index to 3D index
    XC, YC, ZC = inverseHash(ixd, nr)
    xn, yn, zn, dmin = getNN(X[i], Y[i], Z[i], XC, YC, ZC)
    print(xn, yn, zn, dmin)