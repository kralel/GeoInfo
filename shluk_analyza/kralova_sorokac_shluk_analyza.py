# Shluková analýza
import numpy as np
from math import *
from matplotlib import pyplot as plt
import sklearn.cluster


#Generate ramdom points in 5 cluster
np.random.seed(3)
ax = np.asarray(np.random.uniform(12, 25, 50))
ay = np.asarray(np.random.uniform(8, 15, 50))
bx = np.asarray(np.random.uniform(-10, 2, 50))
by = np.asarray(np.random.uniform(-10, 5, 50))
cx = np.asarray(np.random.uniform(2, 10, 50))
cy = np.asarray(np.random.uniform(-2, 10, 50))
dx = np.asarray(np.random.uniform(-5, 10, 50))
dy = np.asarray(np.random.uniform(12, 25, 50))
ex = np.asarray(np.random.uniform(10 , 25, 50))
ey = np.asarray(np.random.uniform(-2, 5, 50))

#Join x-coordnite and y-coordinte of all points
x = np.concatenate((ax, bx, cx, dx, ex))
y = np.concatenate((ay, by, cy, dy, ey))

#print(ax, ay, bx, by, cx, cy, dx, dy, ex, ey)

#Plot of generated points
plt.scatter(ax, ay, c="r", s=10)
plt.scatter(bx, by, c="b", s=10)
plt.scatter(cx, cy, c="y", s=10)
plt.scatter(dx, dy, c="g", s=10)
plt.scatter(ex, ey, c="m", s=10)
plt.show()


#Turn coordinets into set of points
points = list(zip(x, y))


#Kmeans clustering
kmeans = sklearn.cluster.KMeans(n_clusters = 5)
kmeans.fit(points)

plt.scatter(x, y, c=kmeans.labels_, s=10)
plt.show()


#Hierarchical Clustering
hierarchical_cluster = sklearn.cluster.AgglomerativeClustering(n_clusters = 5)
hierarchical_cluster.fit(points)

plt.scatter(x, y, c=hierarchical_cluster.labels_, s=10)
plt.show()