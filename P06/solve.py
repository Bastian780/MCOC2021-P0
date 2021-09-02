#sp.solve es lo que usaremos para solver sparse 
#scipy.sparse.lanlg.spsolve
import scipy.sparse as sp 
import scipy.sparse.linalg as lin
from scipy.sparse import lil_matrix
from numpy import double, ones
from time import perf_counter
from Laplaciana import Laplaciana_completa, Laplaciana_dispersa_csc, Laplaciana_dispersa_csr
import scipy.sparse as sparse 


N=[2,3,6,10,20, 50, 80, 140, 280, 350, 550, 780, 1000, 1300, 1800, 2500, 3000, 5000, 7000]
#fid= open("complejidad_solve_completa.txt","w")

#for i in range(10):

#	for trail in N:

#		t1=perf_counter()
		
#		A=Laplaciana_completa(N=trail, tipo=double)
		
		
#		b=ones(trail)
		
#		t2=perf_counter()

#		x=lin.spsolve(A,b)

#		t3=perf_counter()

#		t_ens=t2-t1  #ensamblado completo
		
#		t_inv=t3-t2  #inversión completa
		
#		fid.write(f"{trail} {t_ens} {t_inv} \n")
		
#fid.close()

fid1= open("complejidad_solve_dispersa.txt","w")

for i in range(10):

	for trail in N:

		t1=perf_counter()
		
		A=Laplaciana_dispersa_csr(N=trail, tipo=double)
		print(trail)
		
		b=ones(trail)
		
		t2=perf_counter()

		x=lin.spsolve(A,b)

		t3=perf_counter()

		t_ens=t2-t1  #ensamblado completo
		
		t_inv=t3-t2  #inversión completa
		
		fid1.write(f"{trail} {t_ens} {t_inv} \n")
		
fid1.close()





















