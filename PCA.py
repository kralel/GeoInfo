import numpy as np
from matplotlib import pyplot as plot

X = []
Y = []

#Convert the input to an array
matrix = np.asarray([X, Y])

#Compute a covariance matrix
cov_matrix = np.cov(matrix)

#Compute the eigenvalues and eigenvectors
eval, evec = np.linalg.eig(cov_matrix)