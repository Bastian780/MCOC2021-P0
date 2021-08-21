from scipy import matmul, rand 
from time import perf_counter
from scipy.linalg import solve, inv, eigh
from numpy import eye, float64, float32, double, ones


#assume_a="pos" --> establece quue la matriz es definida positiva
#todos valores  propios positivos

def laplaciana(N, tipo):
	e=eye(N)-eye(N,N,1)
	return tipo(e+e.T)

Ns=[2, 5, 10, 15, 17, 19, 25, 35, 45, 50, 65, 80, 90, 100, 140, 180, 240, 320, 490, 570, 670, 890]

typ= [double, float32]
tiempo_float32_it1=[]
tiempo_double_it1=[]
tiempo_float32_it2=[]
tiempo_double_it2=[]
tiempo_float32_it3=[]
tiempo_double_it3=[]
tiempo_float32_it4=[]
tiempo_double_it4=[]
tiempo_float32_it5=[]
tiempo_double_it5=[]
tiempo_double_it6=[]
tiempo_float32_it6=[]
tiempo_double_it7=[]
tiempo_float32_it7=[]
tiempo_double_it8=[]
tiempo_float32_it8=[]
tiempo_double_it9=[]
tiempo_float32_it9=[]
tiempo_float32_it10=[]
tiempo_double_it10=[]

iteraciones_float32=[tiempo_float32_it1, tiempo_float32_it2, tiempo_float32_it3, tiempo_float32_it4, tiempo_float32_it5, tiempo_float32_it6, tiempo_float32_it6, tiempo_float32_it8, tiempo_float32_it9, tiempo_float32_it10]
iteraciones_double=[tiempo_double_it1, tiempo_double_it2, tiempo_double_it3, tiempo_double_it4, tiempo_double_it5, tiempo_double_it6, tiempo_double_it7, tiempo_double_it8, tiempo_double_it9, tiempo_double_it10]

promedio_float32=[]
promedio_double=[]

fid1= open(f"scipy.linalg_eigh_driver=evx_overwrite=false_double_caso5.txt","w")
fid2= open(f"scipy.linalg_eigh_driver=evx_overwrite=false_float32_caso5.txt","w")


for i in range(1,11):
	for t in typ:
		for N in Ns:
			A= laplaciana(N, tipo=t)

			t1=perf_counter()
		
			w,v= eigh(A, driver="evx",overwrite_a=False)
		
			t2=perf_counter()
		
			dt=t2-t1
		
			#print(f"Tiempo transcurrido={dt} s y tipo{t} para matriz de {N} ")

			if t==double:
				iteraciones_double[i-1].append(dt)
			else:
				iteraciones_float32[i-1].append(dt)

#print(iteraciones_float32)


for a in range(len(Ns)):
	P=0
	for lista in iteraciones_float32:
		P+=lista[a]
	promedio_float32.append(P/(len(Ns)))

for l in range(len(promedio_float32)):
	fid2.write(f"{Ns[l]} {promedio_float32[l]} \n")

for b in range(len(Ns)):
	J=0
	for lista1 in iteraciones_double:
		J+=lista1[b]
	promedio_double.append(J/float(len(Ns)))

for l in range(len(promedio_double)):
	fid1.write(f"{Ns[l]} {promedio_double[l]} \n")
fid1.close()
fid2.close()
#Funcion eye genera una matriz identidad, está especificada entro de numpy)
#(eye(A,B,C)-->C es la posición donde quiero los 1 en la matriz identidad)
#laplaciana-->  La matriz identidad se le resta una identidad que tiene 1nos en la diagonal de arriba 
#Finalmente, a la matriz e se le suma su traspuesta, obteniendo la matriz deseada.

