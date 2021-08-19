from time import perf_counter
from numpy import zeros
from numpy.linalg import inv
from laplaciana import laplaciana
#from scipy.linalg import inv
from numpy import half, float16, float32, float64
import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np

Ns=[10, 30, 50, 80, 100, 200, 350, 500, 1000, 1500, 2000]
dts_inv=[]
mems=[]

for i in range(10):
	fid= open(f"rendimientoA_numpy_float64_{i}.txt","w")

	for N in Ns:
		  uso_memoria_total=0

		  t1=perf_counter()

		  A= laplaciana(N, dtype=float64)
	#print(f "{A}")
	#dtype indica la presición que deseo utilizar
	#exit(0)
		  t2=perf_counter()

		  #print(A)

		  Am1= inv(A)

		  t3=perf_counter()

		  dt_ensablaje=t2-t1
		  dt_inversion=t3-t2
		  dts_inv.append(dt_inversion)
		  bytes_total=A.nbytes + Am1.nbytes
		  mems.append(bytes_total)
		  fid.write(f"{N} {dt_inversion} {bytes_total} \n")

	fid.close()



	  #print(f"Tiempo de ensamblaje:{dt_ensablaje} s")
      #print(f"Tiempo de inversion:{dt_inversion} s")
#graficar tiempo de inversión

#A --> half (1byts)
#      single (2bytes)=(16 bits (16 veces 1 y el resto 0))
#      double (4byts)(doble de espacio que el anterior )
#	   long doble(8 byts)=quad (mucha presición a costa de mucha memoria)
#	   para sumar double no hay problema, porque está incorporado en el sistema.
#	   Se especifica con el arcgumento de tipos de datos.
#		numpy viene programado para trabajar con 32 bits
#     scipy es una librería con mucho mas alcance, de hecho numpy forma parte de scipy 
#bytes_total=A.nbytes + Am1.nbytes
#print(f"Uso de memoria {bytes_total} bytes")