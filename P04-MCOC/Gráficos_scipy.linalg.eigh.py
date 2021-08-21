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

def graficos_numpy_scipy_8_16_32_64(archivo1,archivo2, archivo3, archivo4, archivo5,archivo6,archivo7,archivo8,archivo9,Ns1,dts1,Ns2,dts2,Ns3,dts3,Ns4,dts4,Ns5,dts5,Ns6,dts6,Ns7,dts7,Ns8,dts8,Ns9,dts9,a,p,k,r,s,t,v,w,x,y):
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
	for i in archivo3:
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
		Ns3.append(Ns_0)
		dts3.append(dts_0)
	for i in archivo4:
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
		Ns4.append(Ns_0)
		dts4.append(dts_0)
	for i in archivo5:
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
		Ns5.append(Ns_0)
		dts5.append(dts_0)
	for i in archivo6:
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
		Ns6.append(Ns_0)
		dts6.append(dts_0)
	for i in archivo7:
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
		Ns7.append(Ns_0)
		dts7.append(dts_0)
	for i in archivo8:
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
		Ns8.append(Ns_0)
		dts8.append(dts_0)
	for i in archivo9:
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
		Ns9.append(Ns_0)
		dts9.append(dts_0)

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
	plt.loglog(Ns3[0],dts3[0],"o-")
	plt.loglog(Ns4[0],dts4[0],"o-")
	plt.loglog(Ns5[0],dts5[0],"o-")
	plt.loglog(Ns6[0],dts6[0],"o-")
	plt.loglog(Ns7[0],dts7[0],"o-")
	plt.yticks(tp_tra0,tp_tra_1)
	plt.xticks(tam_0,tam_1)                                            
	plt.grid(True)
	pyplot.legend([p, k,r, s,t,v,w,x,y])
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
p=[]
k=[]
r=[]
s=[]
a.append("scipy.linalg_eigh_double_caso1.txt")
b.append("scipy.linalg_eigh_float32_caso1.txt")
c.append("scipy.linalg_eigh_driver=ev_overwrite=false_double_caso2.txt")
d.append("scipy.linalg_eigh_driver=ev_overwrite=true_double_caso2.txt")
e.append("scipy.linalg_eigh_driver=ev_overwrite=false_float32_caso2.txt")
f.append("scipy.linalg_eigh_driver=ev_overwrite=true_float32_caso2.txt")
g.append("scipy.linalg_eigh_driver=evd_overwrite=false_double_caso3.txt")
h.append("scipy.linalg_eigh_driver=evd_overwrite=true_double_caso3.txt")
i.append("scipy.linalg_eigh_driver=evd_overwrite=false_float32_caso3.txt")
j.append("scipy.linalg_eigh_driver=evd_overwrite=true_float32_caso3.txt")
k.append("scipy.linalg_eigh_driver=evr_overwrite=false_double_caso4.txt")
l.append("scipy.linalg_eigh_driver=evr_overwrite=true_double_caso4.txt")
m.append("scipy.linalg_eigh_driver=evr_overwrite=false_float32_caso4.txt")
n.append("scipy.linalg_eigh_driver=evr_overwrite=true_float32_caso4.txt")
p.append("scipy.linalg_eigh_driver=evx_overwrite=false_double_caso5.txt")
k.append("scipy.linalg_eigh_driver=evx_overwrite=true_double_caso5.txt")
r.append("scipy.linalg_eigh_driver=evx_overwrite=false_float32_caso5.txt")
s.append("scipy.linalg_eigh_driver=evx_overwrite=true_float32_caso5.txt")

graficos_numpy_scipy_8_16_32_64(a,c,d,g,h,k,l,p,k,Ns1,dts1,Ns2,dts2,Ns3,dts3,Ns4,dts4,Ns5,dts5,Ns6,dts6,Ns7,dts7,Ns8,dts8,Ns9,dts9,"COMPARACIÓN EIGH CASOS TOTALES DOUBLE","Eigh_double_caso1","Eigh_double_caso2","Eigh_double_caso3","Eigh_double_caso4","Eigh_double_caso5","Eigh_double_caso6","Eigh_double_caso7","Eigh_double_caso8","Eigh_double_caso9")
graficos_numpy_scipy_8_16_32_64(b,e,f,i,j,m,n,r,s,Ns1,dts1,Ns2,dts2,Ns3,dts3,Ns4,dts4,Ns5,dts5,Ns6,dts6,Ns7,dts7,Ns8,dts8,Ns9,dts9,"COMPARACIÓN EIGH CASOS TOTALES FLOAT32","Eigh_float32_caso1","Eigh_float32_caso2","Eigh_float32_caso3","Eigh_float32_caso4","Eigh_float32_caso5","Eigh_float32_caso6","Eigh_float32_caso7","Eigh_dfloat32_caso8","Eigh_float32_caso9")