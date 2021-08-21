import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from numpy import *
from matplotlib import pyplot

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

def graficos_numpy_scipy_8_16_32_64(archivo1,archivo2,Ns1,dts1,Ns2, dts2,a,p,k):
	for i in archivo1:
		Ns_0=[]
		dts_0=[]
		
		fid1=open(i,"r")
		for line in fid1:
			s1=line.split()
			N1=int(s1[0])
			dt1=float(s1[1])
			

			Ns_0.append(N1)
			dts_0.append(dt1)
			
		fid1.close()
		Ns1.append(Ns_0)
		dts1.append(dts_0)
	
	for i in archivo2:
		Ns_0=[]
		dts_0=[]
		fid1=open(i,"r")
		for line in fid1:
			s1=line.split()
			N1=int(s1[0])
			dt1=float(s1[1])
			

			Ns_0.append(N1)
			dts_0.append(dt1)
			
		fid1.close()
		Ns2.append(Ns_0)
		dts2.append(dts_0)

	tp_tra0=[1*10**-4, 1*10**-3, 10**-2, 10**-1, 1, 10, 60, 600]
	tp_tra_1=["0.1ms", "1ms", "10ms","0.1s", "1s", "10s", "1min", "10min"]
	
	tam_0=[10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
	tam_1=["10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000", "20000"]


	params = {'xtick.labelsize': 8, 'ytick.labelsize': 8}
	mpl.rcParams.update(params)
	plt.figure(1)
	plt.subplot(1, 1, 1)
	plt.ylabel("Tiempo transcurrido")
	plt.xlabel("Tamaño matriz N")
	plt.title(a)
	plt.loglog(Ns1[0],dts1[0],"o-")
	plt.loglog(Ns2[0],dts2[0],"o-")
	plt.yticks(tp_tra0,tp_tra_1)
	plt.xticks(tam_0,tam_1)
	plt.grid(True)
	pyplot.legend([p,k])
	plt.show()
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
j=[]
k=[]
l=[]
m=[]
n=[]
a.append("timing_solve_double_caso1.txt")
b.append("timing_solve_double_caso2.txt")
c.append("timing_solve_double_caso3.txt")
d.append("timing_solve_double_caso4.txt")
e.append("timing_solve_double_caso5.txt")
f.append("timing_solve_double_caso6.txt")
g.append("timing_solve_double_caso7.txt")
h.append("timing_solve_float32_caso1.txt")
i.append("timing_solve_float32_caso2.txt")
j.append("timing_solve_float32_caso3.txt")
k.append("timing_solve_float32_caso4.txt")
l.append("timing_solve_float32_caso5.txt")
m.append("timing_solve_float32_caso6.txt")
n.append("timing_solve_float32_caso7.txt")



graficos_numpy_scipy_8_16_32_64(a,b,Ns1,dts1,Ns2,dts2,"COMPARACIÓN TIMMING DOUBLE CASO 1 Y 2","timing_solve_double_caso1","timing_solve_double_caso2")
graficos_numpy_scipy_8_16_32_64(b,c,Ns2,dts2,Ns3,dts3,"COMPARACIÓN TIMMING DOUBLE CASO 2 Y 3 ","timing_solve_double_caso2","timing_solve_double_caso3")
graficos_numpy_scipy_8_16_32_64(c,d,Ns3,dts3,Ns4,dts4,"COMPARACIÓN TIMMING DOUBLE CASO 3 Y 4","timing_solve_double_caso3","timing_solve_double_caso4")
graficos_numpy_scipy_8_16_32_64(d,e,Ns4,dts4,Ns5,dts5,"COMPARACIÓN TIMMING DOUBLE CASO 4 Y 5","timing_solve_double_caso4","timing_solve_double_caso5")
graficos_numpy_scipy_8_16_32_64(e,f,Ns5,dts5,Ns6,dts6,"COMPARACIÓN TIMMING DOUBLE CASO 5 Y 6","timing_solve_double_caso5","timing_solve_double_caso6")
graficos_numpy_scipy_8_16_32_64(f,g,Ns6,dts6,Ns7,dts7,"COMPARACIÓN TIMMING DOUBLE CASO 6 Y 7","timing_solve_double_caso6","timing_solve_double_caso7")


graficos_numpy_scipy_8_16_32_64(h,i,Ns8,dts8,Ns9,dts9,"COMPARACIÓN TIMMING 	FLOAT32 CASO 1 Y 2","timing_solve_float32_caso1","timing_solve_float32_caso2")
graficos_numpy_scipy_8_16_32_64(i,j,Ns9,dts9,Ns10,dts10,"COMPARACIÓN TIMMING FLOAT32 CASO 2 Y 3 ","timing_solve_float32_caso2","timing_solve_float32_caso3")
graficos_numpy_scipy_8_16_32_64(j,k,Ns10,dts10,Ns11,dts11,"COMPARACIÓN TIMMING FLOAT32 CASO 3 Y 4","timing_solve_float32_caso3","timing_solve_float32_caso4")
graficos_numpy_scipy_8_16_32_64(k,l,Ns11,dts11,Ns12,dts12,"COMPARACIÓN TIMMING FLOAT32 CASO 4 Y 5","timing_solve_float32_caso4","timing_solve_float32_caso5")
graficos_numpy_scipy_8_16_32_64(l,m,Ns12,dts12,Ns13,dts13,"COMPARACIÓN TIMMING FLOAT32 CASO 5 Y 6","timing_solve_float32_caso5","timing_solve_float32_caso6")
graficos_numpy_scipy_8_16_32_64(m,n,Ns13,dts13,Ns14,dts14,"COMPARACIÓN TIMMING FLOAT32 CASO 6 Y 7","timing_solve_float32_caso6","timing_solve_float32_caso7")


