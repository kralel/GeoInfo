# Shluková analýza
import numpy as np
from math import *
from matplotlib import pyplot as plt
import sklearn.cluster
#Generate ramdom points in 5 cluster
np.random.seed(42)
ax = np.asarray(np.random.uniform(5, 25, 20))
ay = np.asarray(np.random.uniform(5, 10, 20))
bx = np.asarray(np.random.uniform(-10, 2, 20))
by = np.asarray(np.random.uniform(-10, 5, 20))
cx = np.asarray(np.random.uniform(2, 10, 20))
cy = np.asarray(np.random.uniform(-2, 15, 20))
dx = np.asarray(np.random.uniform(-5, 10, 20))
dy = np.asarray(np.random.uniform(0, 15, 20))
ex = np.asarray(np.random.uniform(10 , 25, 20))
ey = np.asarray(np.random.uniform(-2, 5, 20))

#Join x-coordnite and y-coordinte of points
x = np.concatenate((ax, bx, cx, dx, ex))
y = np.concatenate((ay, by, cy, dy, ey))


print(ax, ay, bx, by, cx, cy, dx, dy, ex, ey)
plt.scatter(ax, ay, c="r", s=10)
plt.scatter(bx, by, c="b", s=10)
plt.scatter(cx, cy, c="y", s=10)
plt.scatter(dx, dy, c="g", s=10)
plt.scatter(ex, ey, c="m", s=10)
plt.show()
#Turn coordinets into set of points for kmeans fuction
points = list(zip(x, y))

#Kmeans
kmeans = sklearn.cluster.KMeans(n_clusters = 5)
kmeans.fit(points)


plt.scatter(x, y, c=kmeans.labels_, s=10)
plt.show
#Turn coordinets into set of points
points = list(zip(x, y))

#Hierarchical Clustering
hierarchical_cluster = sklearn.cluster.AgglomerativeClustering(n_clusters = 5)
hierarchical_cluster.fit(points)


plt.scatter(x, y, c=hierarchical_cluster.labels_, s=10)
plt.show
#Turn coordinets into set of points
points = list(zip(x, y))

#DBSCAN
dbscan = sklearn.cluster.DBSCAN(eps=2, min_samples=2)
dbscan.fit(points)


plt.scatter(x, y, c=dbscan.labels_, s=10)
plt.show