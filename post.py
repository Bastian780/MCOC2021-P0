import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np

Ns=[]
dts=[]
mems=[]
x=["rendimiento1.txt", "rendimiento2.txt", "rendimiento3.txt", "rendimiento4.txt", "rendimiento5.txt", "rendimiento6.txt", "rendimiento7.txt", "rendimiento8.txt", "rendimiento9.txt", "rendimiento10.txt"]
for i in x:
    Ns_0=[]
    dts_0=[]
    mems_0=[]
    fid= open(i,"r")
    for line in fid:
        sl=line.split()
        N=int(sl[0])
        dt=float(sl[1])
        mem=float(sl[2])
        
        Ns_0.append(N)
        dts_0.append(dt)
        mems_0.append(mem)
    fid.close()   
    Ns.append(Ns_0)
    dts.append(dts_0)
    mems.append(mems_0)        
tp_tra0=[1*10**-4, 1*10**-3, 10**-2, 10**-1, 1, 10, 60, 600]
tp_tra_1=["0.1ms", "1ms", "10ms","0.1s", "1s", "10s", "1min", "10min"]
mem_0=[10**3,10**4,10**5,10**6, 10**7,10**8, 10**9, 10**10]
mem_1=["1KB", "10KB", "100KB", "1MB", "10MB", "100MB", "8GB", "10GB"]
tam_0=[10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
tam_1=["10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000", "20000"]




plt.figure(1)
plt.subplot(2, 1, 1)
plt.ylabel("Tiempo transcurrido")
plt.title("Rendimiento A@B")
plt.loglog(Ns[0],dts[0],"o-")
plt.loglog(Ns[1],dts[1],"o-")
plt.loglog(Ns[2],dts[2],"o-")
plt.loglog(Ns[3],dts[3],"o-")
plt.loglog(Ns[4],dts[4],"o-")
plt.loglog(Ns[5],dts[5],"o-")
plt.loglog(Ns[6],dts[6],"o-")
plt.loglog(Ns[7],dts[7],"o-")
plt.loglog(Ns[8],dts[8],"o-")
plt.loglog(Ns[9],dts[9],"o-")
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)
plt.yticks(tp_tra0,tp_tra_1)
plt.grid(True)



plt.subplot(2, 1, 2)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria")
plt.axhline(y=8**10,color="k", linestyle="--")
plt.loglog(Ns[0],mems[0],"o-")
plt.grid(True)
plt.xticks(tam_0,tam_1)
plt.yticks(mem_0,mem_1)
plt.show()
