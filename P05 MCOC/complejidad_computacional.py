from time import perf_counter
from numpy import zeros
#from numpy.linalg import inv
from Laplaciana import Laplaciana_completa,Laplaciana_dispersa
#from scipy.linalg import inv
from numpy import ones, eye, half, float16, float32, float64, double
import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve

N=[2,3,6,10,20, 50, 80, 140, 280, 350, 550, 780, 1000, 1300, 1800, 2500, 3000, 5000, 7000]
#fid= open("complejidad_matmul_completa.txt","w")


#for i in range(10):

#	for trail in N:
#		print(trail)

#		t1=perf_counter()
	
#		A=Laplaciana_completa(trail, tipo=double)
	
#		B=Laplaciana_completa(trail, tipo=double)
		
#		t2=perf_counter()

#		x=A@B

#		t3=perf_counter()

#		dts1_comp=t2-t1  #ensamblado completo
#		dts2_comp=t3-t2  #solución completo
		
#		fid.write(f"{trail} {dts1_comp} {dts2_comp} \n")
		
#fid.close()

fid1=open("complejidad_matmul_dispersa.txt","w")

for i in range(10):
	print(i)
	for trail in N:
		t4=perf_counter()

		A1=Laplaciana_dispersa(trail, tipo=double)
		
		B1=Laplaciana_dispersa(trail, tipo=double)

		t5=perf_counter()

		x1=A1@B1
		
		t6=perf_counter()
		dts1_dis=t5-t4 #ensamblado disperso
		dts2_dis=t6-t5 #solución disperso

		fid1.write(f"{trail} {dts1_dis} {dts2_dis} \n")

fid1.close()






