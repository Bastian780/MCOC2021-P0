from numpy import zeros, float16, float32, float64
from time import perf_counter
import matplotlib.pylab as plt

#TAMAÑO
N = 1000

Ns = [10, 30, 50, 80, 100, 200, 350, 500, 1000, 1500, 2000, 2500, 3000, 4500, 5500, 6500]
dts=[]
mems=[]
fid= open("rendimiento10.txt","w")

for N in Ns:
    
    uso_memoria_total=0
     
    A = zeros((N, N), dtype=float16 ) + 1
    B = zeros((N, N)) + 2
    
    t1 = perf_counter()
    C= A@B
    t2= perf_counter()
    
    uso_memoria_total = A.nbytes + B.nbytes + C.nbytes
    
    
    
    dt= t2-t1
    dts.append(dt)
    mems.append(uso_memoria_total)
    print(f"N = {N} dt = {dt} s mem = {uso_memoria_total} byts flops={N**3/dt} flops/s")
    fid.write(f"{N} {dt} {uso_memoria_total} \n")

fid.close
plt.figure(1)
plt.subplot(2, 1, 1)
plt.loglog(Ns,dts)
plt.subplot(2, 1, 2)
plt.loglog(Ns,mems)
#plt.show()