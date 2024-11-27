import numpy as np
from matplotlib import pyplot as plot

X = []
Y = []

#Convert the input to an array
matrix = np.asarray([X, Y])

#Compute a covariance matrix
cov_matrix = np.cov(matrix)

print("kovarianční matice: \n", cov_matrix)

#Compute the eigenvalues and eigenvectors
eval, evec = np.linalg.eig(cov_matrix)

print("vlastní číslo: \n", eval)
print("vlastní vektor: \n", evec)

#Compute amount of information in PCA in %
info = eval[0]/(eval[0]+eval[1])*100
print(f"První hlavní komponenta obsahuje: \n {info:.2f} %")

#Create and draw a scatter plot
plot.scatter(X, Y, c = "r", marker = ".", s = 50)
plot.title("Metoda hlavních komponent")
plot.xlabel("Souřadnice x")
plot.ylabel("Souřadnice y")
plot.show()