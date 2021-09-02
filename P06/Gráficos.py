import matplotlib.pylab as plt
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib as mpl
from numpy import *
from matplotlib import pyplot
from scipy.interpolate import lagrange
import string


#Archivos por leer
fid_0= open("complejidad_inv_completa.txt" ,"r")

fid_1=open("complejidad_inv_dispersa.txt" ,"r")

fid_2=open("complejidad_solve_completa.txt", "r")

fid_3=open("complejidad_solve_dispersa.txt" ,"r")

#Archivos para guardar información

ens_0=[]
ens_1=[]
ens_2=[]
ens_3=[]
inv_0=[]
inv_1=[]
inv_2=[]
inv_3=[]
ens_0_total=[]
ens_1_total=[]
ens_2_total=[]
ens_3_total=[]
inv_0_total=[]
inv_1_total=[]
inv_2_total=[]
inv_3_total=[]


N=[2,3,6,10,20, 50, 80, 140, 280, 350, 550, 780, 1000, 1300, 1800, 2500, 3000, 5000, 7000]

#################
for line in fid_0:
	s1=line.split()
	e_0=float(s1[1])
	i_0=float(s1[2])
	ens_0.append(e_0)
	inv_0.append(i_0)

for line in fid_1:
	s2=line.split()
	e_01=float(s2[1])
	i_01=float(s2[2])
	ens_1.append(e_01)
	inv_1.append(i_01)

for line in fid_2:
	s3=line.split()
	e_02=float(s3[1])
	i_02=float(s3[2])
	ens_2.append(e_02)
	inv_2.append(i_02)

for line in fid_3:
	s4=line.split()
	e_03=float(s4[1])
	i_03=float(s4[2])
	ens_3.append(e_03)
	inv_3.append(i_03)


k=0
for j in range(10):
	a=[]
	b=[]
	c=[]
	d=[]
	h=[]
	l=[]
	m=[]
	n=[]
	for i in range(len(N)):
		a.append(ens_0[k])
		b.append(ens_1[k])
		c.append(ens_2[k])
		d.append(ens_3[k])
		h.append(inv_0[k])
		l.append(inv_1[k])
		m.append(inv_2[k])
		n.append(inv_3[k])
		k+=1


	ens_0_total.append(a)
	inv_0_total.append(h)
	ens_1_total.append(b)
	inv_1_total.append(l)
	ens_2_total.append(c)
	inv_2_total.append(m)
	ens_3_total.append(d)
	inv_3_total.append(n)

constante00=[]
constante01=[]
constante10=[]
constante11=[]
constante20=[]
constante21=[]
constante30=[]
constante31=[]

for i  in range(len(N)):
	constante00.append(inv_0_total[9][18])
	constante01.append(ens_0_total[9][18])
	constante10.append(inv_1_total[9][18])
	constante11.append(ens_1_total[9][18])
	constante20.append(inv_2_total[9][18])
	constante21.append(ens_2_total[9][18])
	constante30.append(inv_3_total[9][18])
	constante31.append(ens_3_total[9][18])




###################
def graficos1(N, lista1, lista2, a, b, constante1, constante2):

	tp_tra0=[1*10**-4, 1*10**-3, 10**-2, 10**-1, 1, 10, 60, 600]
	tp_tra_1=["0.1ms", "1ms", "10ms","0.1s", "1s", "10s", "1min", "10min"]
	mem_0=[10**3,10**4,10**5,10**6, 10**7,10**8, 10**9, 10**10]
	mem_1=["1KB", "10KB", "100KB", "1MB", "10MB", "100MB", "8GB", "10GB"]
	tam_0=[10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
	tam_1=["10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000", "20000"]


	plt.figure(1)
	params = {'xtick.labelsize': 8, 'ytick.labelsize': 8}
	mpl.rcParams.update(params)
	plt.subplot(2, 1, 1)
	plt.ylabel("Tiempo de ensamblado")
	plt.title(a)
	plt.loglog(N,constante1,"--")
	pyplot.plot([N[0],N[18]],[lista1[3][0],lista1[9][18]],"--")
	pyplot.plot([10,N[18]],[0.00000001,lista1[9][18]],"--")
	pyplot.plot([100,N[18]],[0.00000001,lista1[9][18]],"--")
	pyplot.plot([400,N[18]],[0.00000001,lista1[9][18]],"--")
	pyplot.legend(["Constante","O(N)","O({}²)".format("N"),"O({}³)".format("N"),"O({}⁴)".format("N")], loc="lower left")

	plt.loglog(N,lista1[0],"o-",color="black", alpha=0.2)
	plt.loglog(N,lista1[1],"o-",color="black",alpha=0.2)
	plt.loglog(N,lista1[2],"o-",color="black",alpha=0.2)
	plt.loglog(N,lista1[3],"o-",color="black",alpha=0.2)
	plt.loglog(N,lista1[4],"o-",color="black",alpha=0.2)
	plt.loglog(N,lista1[5],"o-",color="black",alpha=0.2)
	plt.loglog(N,lista1[6],"o-",color="black",alpha=0.2)
	plt.loglog(N,lista1[7],"o-",color="black",alpha=0.2)
	plt.loglog(N,lista1[8],"o-",color="black",alpha=0.2)
	plt.loglog(N,lista1[9],"o-",color="black",alpha=0.2)
	
	
	
	plt.tick_params(
	    axis='x',          # changes apply to the x-axis
	    which='both',      # both major and minor ticks are affected
	    bottom=False,      # ticks along the bottom edge are off
	    top=False,         # ticks along the top edge are off
	    labelbottom=False)
	plt.yticks(tp_tra0,tp_tra_1)
	plt.grid(False)



	plt.subplot(2, 1, 2)
	params = {'xtick.labelsize': 8, 'ytick.labelsize': 8}
	mpl.rcParams.update(params)
	plt.xlabel("Tamaño matriz N")
	plt.ylabel(b)
	
	


	plt.loglog(N,constante2,"--")
	pyplot.plot([N[0],N[18]],[lista2[3][0],lista2[9][18]],"--")
	pyplot.plot([10,N[18]],[0.0001,lista2[9][18]],"--")
	pyplot.plot([100,N[18]],[0.0001,lista2[9][18]],"--")
	pyplot.plot([400,N[18]],[0.0001,lista2[9][18]],"--")
	pyplot.legend(["Constante","O(N)","O({}²)".format("N"),"O({}³)".format("N"),"O({}⁴)".format("N")], loc="lower left")


	plt.loglog(N,lista2[0],"o-", color="black",alpha=0.2)
	
	plt.loglog(N,lista2[1],"o-",  color="black",alpha=0.2)
	plt.loglog(N,lista2[2],"o-",  color="black",alpha=0.2)
	plt.loglog(N,lista2[3],"o-",  color="black",alpha=0.2)
	plt.loglog(N,lista2[4],"o-",  color="black",alpha=0.2)
	plt.loglog(N,lista2[5],"o-",  color="black",alpha=0.2)
	plt.loglog(N,lista2[6],"o-",  color="black",alpha=0.2)
	plt.loglog(N,lista2[7],"o-",  color="black",alpha=0.2)
	plt.loglog(N,lista2[8],"o-", color="black",alpha=0.2)
	plt.loglog(N,lista2[9],"o-", color="black",alpha=0.2)
	
	

	plt.grid(False)
	plt.xticks(tam_0,tam_1)
	plt.yticks(tp_tra0,tp_tra_1)
	plt.show()

graficos1(N, lista2=inv_0_total, lista1= ens_0_total, a="Invertir matriz completa", b="Tiempo de inversión", constante1=constante01,constante2=constante00 )
graficos1(N, lista2=inv_1_total, lista1= ens_1_total, a="Invertir matriz dispersa", b="Tiempo de inversión",constante1=constante11,constante2=constante10 )
graficos1(N, lista2=inv_2_total, lista1= ens_2_total, a="Solve con matriz completa", b= "tiempo de solución",constante1=constante21,constante2=constante20)
graficos1(N, lista2=inv_3_total, lista1= ens_3_total, a="Solve con matriz dispersa", b="tiempo de solución",constante1=constante31,constante2= constante30)



