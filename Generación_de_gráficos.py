import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np

Ns1=[]
dts1=[]
mems1=[]
Ns2=[]
dts2=[]
mems2=[]
Ns3=[]
dts3=[]
mems3=[]
Ns4=[]
dts4=[]
mems4=[]
Ns5=[]
dts5=[]
mems5=[]
Ns6=[]
dts6=[]
mems6=[]
Ns7=[]
dts7=[]
mems7=[]
Ns8=[]
dts8=[]
mems8=[]
Ns9=[]
dts9=[]
mems9=[]
Ns10=[]
dts10=[]
mems10=[]
Ns11=[]
dts11=[]
mems11=[]
Ns12=[]
dts12=[]
mems12=[]
Ns13=[]
dts13=[]
mems13=[]
Ns14=[]
dts14=[]
mems14=[]

def graficos_numpy_scipy_8_16_32_64(archivo,Ns,dts,mems,a):
	for i in archivo:
		Ns_0=[]
		dts_0=[]
		mems_0=[]
		fid=open(i,"r")
		for line in fid:
			s1=line.split()
			N=int(s1[0])
			dt=float(s1[1])
			mem=int(s1[2])

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
	plt.title(a)
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

archivos_scipy_half=[]
for i in range(10):
	archivos_scipy_half.append(f"rendimientoA_scipy_half_{i}.txt")

archivos_scipy_float_16=[]
for i in range(10):
	archivos_scipy_float_16.append(f"rendimientoA_scipy_float16_{i}.txt")

archivos_scipy_float_32=[]
for i in range(10):
	archivos_scipy_float_32.append(f"rendimientoA_scipy_float32_{i}.txt")

archivos_scipy_float_64=[]
for i in range(10):
	archivos_scipy_float_64.append(f"rendimientoA_scipy_float64_{i}.txt")

#numpy_half no corre
#numpy_float_16 no corre

archivos_numpy_float_32=[]
for i in range(10):
	archivos_numpy_float_32.append(f"rendimientoA_numpy_float32_{i}.txt")

archivos_numpy_float_64=[]
for i in range(10):
	archivos_numpy_float_64.append(f"rendimientoA_numpy_float64_{i}.txt")

archivo_scipy_overwriteT_half=[]
for i in range(10):
	archivo_scipy_overwriteT_half.append(f"rendimientoA_scipy_overgrite_a=True_half_{i}.txt")


archivo_scipy_overwriteT_float16=[]
for i in range(10):
	archivo_scipy_overwriteT_float16.append(f"rendimientoA_scipy_overgrite_a=True_float16_{i}.txt")


archivo_scipy_overwriteT_float32=[]
for i in range(10):
	archivo_scipy_overwriteT_float32.append(f"rendimientoA_scipy_overgrite_a=True_float32_{i}.txt")

archivo_scipy_overwriteT_float64=[]
for i in range(10):
	archivo_scipy_overwriteT_float64.append(f"rendimientoA_scipy_overgrite_a=True_float64_{i}.txt")


	archivo_scipy_overwriteF_half=[]
for i in range(10):
	archivo_scipy_overwriteF_half.append(f"rendimientoA_scipy_overgrite_a=False_half_{i}.txt")


archivo_scipy_overwriteF_float16=[]
for i in range(10):
	archivo_scipy_overwriteF_float16.append(f"rendimientoA_scipy_overgrite_a=False_float16_{i}.txt")


archivo_scipy_overwriteF_float32=[]
for i in range(10):
	archivo_scipy_overwriteF_float32.append(f"rendimientoA_scipy_overgrite_a=False_float32_{i}.txt")

archivo_scipy_overwriteF_float64=[]
for i in range(10):
	archivo_scipy_overwriteF_float64.append(f"rendimientoA_scipy_overgrite_a=False_float64_{i}.txt")


def graficos_numpy_scipy_8_16_32_64(archivo,Ns,dts,mems,a):
	for i in archivo:
		Ns_0=[]
		dts_0=[]
		mems_0=[]
		fid=open(i,"r")
		for line in fid:
			s1=line.split()
			N=int(s1[0])
			dt=float(s1[1])
			mem=int(s1[2])

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
	plt.title(a)
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

graficos_numpy_scipy_8_16_32_64(archivos_scipy_half,Ns1,dts1,mems1,"Rendimiento inversión A usando scipy y dtype half")
graficos_numpy_scipy_8_16_32_64(archivos_scipy_float_16,Ns2,dts2,mems2,"Rendimiento inversión A, uasando scipy y dtype float16")
graficos_numpy_scipy_8_16_32_64(archivos_scipy_float_32,Ns3,dts3,mems3,"Rendimiento inversión A, uasando scipy y dtype float32")
graficos_numpy_scipy_8_16_32_64(archivos_scipy_float_64,Ns4,dts4,mems4,"Rendimiento inversión A, uasando scipy y dtype float64")
graficos_numpy_scipy_8_16_32_64(archivos_numpy_float_32,Ns5,dts5,mems5,"Rendimiento inversión A, usando numpy y dtype float32")
graficos_numpy_scipy_8_16_32_64(archivos_numpy_float_64,Ns6,dts6,mems6,"Rendimiento inversión A, usando numpy y dtype float64")

graficos_numpy_scipy_8_16_32_64(archivo_scipy_overwriteF_half,Ns7,dts7,mems7,"Rendimiento inversión A usando scipy,overwrite_a=True y dtype half")
graficos_numpy_scipy_8_16_32_64(archivo_scipy_overwriteF_float16,Ns8,dts8,mems8,"Rendimiento inversión A, uasando scipy,overwrite_a=True y dtype float16")
graficos_numpy_scipy_8_16_32_64(archivo_scipy_overwriteF_float32,Ns9,dts9,mems9,"Rendimiento inversión A, uasando ,overwrite_a=True y dtype float32")
graficos_numpy_scipy_8_16_32_64(archivo_scipy_overwriteF_float64,Ns10,dts10,mems10,"Rendimiento inversión A, uasando scipy,overwrite_a=True y dtype float64")

graficos_numpy_scipy_8_16_32_64(archivo_scipy_overwriteT_half,Ns7,dts7,mems7,"Rendimiento inversión A usando scipy,overwrite_a=False y dtype half")
graficos_numpy_scipy_8_16_32_64(archivo_scipy_overwriteT_float16,Ns8,dts8,mems8,"Rendimiento inversión A, uasando scipy,overwrite_a=False y dtype float16")
graficos_numpy_scipy_8_16_32_64(archivo_scipy_overwriteT_float32,Ns9,dts9,mems9,"Rendimiento inversión A, uasando ,overwrite_a=False y dtype float32")
graficos_numpy_scipy_8_16_32_64(archivo_scipy_overwriteT_float64,Ns10,dts10,mems10,"Rendimiento inversión A, uasando scipy,overwrite_a=False y dtype float64")