from time import perf_counter
from numpy import zeros
from scipy import linalg
import matplotlib.pyplot as plt
from numpy import ones, eye, half, float16, float32, float64, double
from scipy.linalg import solve
import scipy.sparse as sparse 
import scipy.sparse.linalg as lin

def Laplaciana_completa(N, tipo):
	
	e=eye(N)-eye(N,N,1)
	return tipo(e+e.T)

def Laplaciana_dispersa_csr(N, tipo):
	
	e=eye(N)-eye(N,N,1)

	return(sparse.csr_matrix(tipo(e+e.T)))

def Laplaciana_dispersa_csc(N, tipo):
	
	e=eye(N)-eye(N,N,1)

	return(sparse.csc_matrix(tipo(e+e.T)))




	
	