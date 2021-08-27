import numpy as np 
import scipy.sparse as sparse 
import scipy.sparse.linalg as lin

def matriz_laplaciana(N,t=np.float32):
	e=sparse.eye(N, dtype=t)-np.eye(N,N,1, dtype=t)
	return t(e+e.T)

N=100
A=matriz_laplaciana(N)
A[0,-1]=1.
A[1,-1]=1.
A[2,-1]=1.
A[3,-1]=1.
A[4,-1]=1.

#print(f"A= \n{A}")
# Ahora convertimos la matria A en CSR
Acsr= sparse.csr_matrix(A)
Acsc= sparse.csc_matrix(A)
Acoo= sparse.coo_matrix(A)
Adia= sparse.dia_matrix(A)
Alil= sparse.lil_matrix(A)

#print(f"Acsr= \n{Acsr}")
#print(f"Acsc= \n{Acsc}")
#print(f"Acoo= \n{Acoo}")
#print(f"Diagonal= \n{Adia}")
#print(f"lil= \n{Alil}")

print(f"Acsr.getnnz()= \n{Acsr}")
print(f"Acsc.getnnz()= \n{Acsc}")
print(f"Acoo.getnnz()= \n{Acoo}")
print(f"Diagonal.getnnz()= \n{Adia}")
print(f"lil.getnnz()= \n{Alil}")





#ANCHO DE BANDA= CANTIDAD DE NUMEROS DISTINTOS DE 0 DESDE LA DIAGONAL PRINCIPAL

#CSRow --> hartos ceros y matriz bandeada (ponemos indice inicial y final de cada fila)
#0 1 2 -1      (inicial, final, valores)
#0 2 -1 2 -1
#index- based format --> bueno para anchos de banda no definidos (conn hartos 0)

#CSC --> VOY ALMACENANDO POR COLUMNA

# LIBRERIA SCIPY.SPARSE 

#ALMACENAMIENTO DIAGONAL 
#-->N=4 (DIAGONAL PRINCIPAL, DIAGONAL SUPERIOR, DIAGONAL INFERIOR) 
#2 2 2 2 -1 -1 -1 -1 -1 -1


#scipy.sparce.linalg--> para matrices dispersas(matriz que no guarda ceros)
