# Shluková analýza
import numpy as np
from math import *
from matplotlib import pyplot as plt
import sklearn.cluster


#Generate ramdom points in 5 cluster
np.random.seed(3)
ax = np.asarray(np.random.uniform(12, 25, 30))
ay = np.asarray(np.random.uniform(8, 15, 30))
bx = np.asarray(np.random.uniform(-10, 2, 30))
by = np.asarray(np.random.uniform(-10, 5, 30))
cx = np.asarray(np.random.uniform(2, 10, 30))
cy = np.asarray(np.random.uniform(-2, 10, 30))
dx = np.asarray(np.random.uniform(-5, 10, 30))
dy = np.asarray(np.random.uniform(12, 25, 30))
ex = np.asarray(np.random.uniform(10 , 25, 30))
ey = np.asarray(np.random.uniform(-2, 5, 30))

#Join x-coordnite and y-coordinte of all points
x = np.concatenate((ax, bx, cx, dx, ex))
y = np.concatenate((ay, by, cy, dy, ey))

#print(ax, ay, bx, by, cx, cy, dx, dy, ex, ey)

#Plot of generated points
plt.scatter(ax, ay, c="r", s=20)
plt.scatter(bx, by, c="b", s=20)
plt.scatter(cx, cy, c="y", s=20)
plt.scatter(dx, dy, c="g", s=20)
plt.scatter(ex, ey, c="m", s=20)
plt.show()


#Turn coordinets into set of points
points = list(zip(x, y))


#Kmeans clustering
kmeans = sklearn.cluster.KMeans(n_clusters = 5)
kmeans.fit(points)

plt.scatter(x, y, c=kmeans.labels_, s=20)
plt.show()


#Hierarchical Clustering
hierarchical_cluster = sklearn.cluster.AgglomerativeClustering(n_clusters = 5)
hierarchical_cluster.fit(points)

plt.scatter(x, y, c=hierarchical_cluster.labels_, s=20)
plt.show()