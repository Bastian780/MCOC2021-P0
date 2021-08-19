from time import perf_counter
from numpy import zeros
#from numpy.linalg import inv
from laplaciana import laplaciana
from scipy.linalg import inv
from numpy import half, float16, float32, float64
import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np

Ns=[10, 30, 50, 80, 100, 200, 350, 500, 1000, 1500, 2000]
dts_inv=[]
mems=[]

for i in range(10):
	fid= open(f"rendimientoA_scipy_overgrite_a=False_float16_{i}.txt","w")

	for N in Ns:
		  uso_memoria_total=0

		  t1=perf_counter()

		  A= laplaciana(N, dtype=float16)
	#print(f "{A}")
	#dtype indica la presición que deseo utilizar
	#exit(0)
		  t2=perf_counter()

		  #print(A)

		  Am1= inv(A, overwrite_a=False)

		  t3=perf_counter()

		  dt_ensablaje=t2-t1
		  dt_inversion=t3-t2
		  dts_inv.append(dt_inversion)
		  bytes_total=A.nbytes + Am1.nbytes
		  mems.append(bytes_total)
		  fid.write(f"{N} {dt_inversion} {bytes_total} \n")

	fid.close()