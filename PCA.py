import numpy as np
from matplotlib import pyplot as plot

X = [1, -2, 3, 4, 5, 6, -7, 8, -9, 10, 11, 12, -13, 14, -15, -16, 17, 18, 19, 20]
Y = [1, 2, -3, -4, 3, 6, -5, 8, -7, 10, 1, 12, -11, 4, 15, -14, -7, 8, 19, 20]

#X = [1, 2, 3, 4, -4, 6, 7, 24, 9, 20, 11, -13, 13, 14, 5, 17, 17, 18, 13, 20]
#Y = [-1, 16, -3, 35, -5, 76, 2, 68, 9, 10, -11, 12, -12, -40, 15, 16, -21, 5, 19, 44]

#Convert the input to an array
matrix = np.asarray([X, Y])

#Compute a covariance matrix
cov_matrix = np.cov(matrix)

print("kovarianční matice: \n", cov_matrix)

#Compute the eigenvalues and eigenvectors
eval, evec = np.linalg.eig(cov_matrix)

print("vlastní čísla: \n", eval)
print("vlastní vektory: \n", evec)

#Compute amount of information in PCA in %
#For 1. principal component - (1. eigenvalue/sum of eigenvalues)
info = eval[0]/(sum(eval))*100
print(f"První hlavní komponenta obsahuje: \n {info:.2f} %")

#Create and draw a scatter plot
plot.scatter(X, Y, c = "r", marker = ".", s = 50)
plot.title("Datová sada")
plot.xlabel("Souřadnice x")
plot.ylabel("Souřadnice y")
plot.show()