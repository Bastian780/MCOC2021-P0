import matplotlib.pylab as plt
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib as mpl
from numpy import *
from matplotlib import pyplot
from scipy.interpolate import lagrange
import string



fid= open("complejidad_matmul_completa.txt" ,"r")
fid_1=open("complejidad_matmul_dispersa.txt" ,"r")
N=[2,3,6,10,20, 50, 80, 140, 280, 350, 550, 780, 1000, 1300, 1800, 2500, 3000, 5000, 7000]


total_dts1=[]
total_dts2=[]
total_dts11=[]
total_dts22=[]
dts1_0=[]
dts1_1=[]
dts1_2=[]
dts1_3=[]
dts1_4=[]
dts1_5=[]
dts1_6=[]
dts1_7=[]
dts1_8=[]
dts1_9=[]
dts2_0=[]
dts2_1=[]
dts2_2=[]
dts2_3=[]
dts2_4=[]
dts2_5=[]
dts2_6=[]
dts2_7=[]
dts2_8=[]
dts2_9=[]
dts1_00=[]
dts1_11=[]
dts1_22=[]
dts1_33=[]
dts1_44=[]
dts1_55=[]
dts1_66=[]
dts1_77=[]
dts1_88=[]
dts1_99=[]
dts2_00=[]
dts2_11=[]
dts2_22=[]
dts2_33=[]
dts2_44=[]
dts2_55=[]
dts2_66=[]
dts2_77=[]
dts2_88=[]
dts2_99=[]
N11=[]
N21=[]
N31=[]
N41=[]
constante1=[]
N10=[]
N20=[]
N30=[]
N40=[]
constante0=[]
N110=[]
N210=[]
N310=[]
N410=[]
constante10=[]
N100=[]
N200=[]
N300=[]
N400=[]
constante00=[]



dts1=[dts1_0, dts1_1, dts1_2, dts1_3, dts1_4, dts1_5, dts1_6, dts1_7, dts1_8, dts1_9]
dts2=[dts2_0, dts2_1, dts2_2, dts2_3, dts2_4, dts2_5, dts2_6, dts2_7, dts2_8, dts2_9]
dts10=[dts1_00, dts1_11, dts1_22, dts1_33, dts1_44, dts1_55, dts1_66, dts1_77, dts1_88, dts1_99]
dts20=[dts2_00, dts2_11, dts2_22, dts2_33, dts2_44, dts2_55, dts2_66, dts2_77, dts2_88, dts2_99]


for line in fid:
	s1=line.split()
	dt1=float(s1[1])
	dt2=float(s1[2])
	total_dts1.append(dt1)
	total_dts2.append(dt2)

for line in fid_1:
	s1=line.split()
	dt1=float(s1[1])
	dt2=float(s1[2])
	total_dts11.append(dt1)
	total_dts22.append(dt2)

a=0
for i in range(10):
	for p in range(len(N)):
		dts1[i].append(total_dts1[a])
		dts2[i].append(total_dts2[a])
		a+=1

a=0
for i in range(10):
	for p in range(len(N)):
		dts10[i].append(total_dts11[a])
		dts20[i].append(total_dts22[a])
		a+=1


def ecuaciones_constante(y1,grado,Ni,N):
	for i in (N):
		Ni.append(y1)
	return(True)

#def ecuaciones_grad1(x01,y01,x10,y10,Ni,N):
#	x1=x01[0]
#	x2=x10[18]
#	y1=y01[0]
#	y2=y10[18]
#	x=[x1,x2]
#	y=[y1,y2]
#	p=lagrange(x,y,)
#	for i in N:
#		Ni.append(p(i))




ecuaciones_constante(y1=dts1_9[18],grado=0,Ni=constante0,N=N)
ecuaciones_constante(y1=dts2_9[18],grado=0,Ni=constante1,N=N)
ecuaciones_constante(y1=dts1_99[18],grado=0,Ni=constante00,N=N)
ecuaciones_constante(y1=dts2_99[18],grado=0,Ni=constante10,N=N)
#ecuaciones_grad1(x01=N,y01=dts2_9,x10=N,y10=dts1_9,Ni=N10,N=N)




def graficos1(N, dts1, dts2, a, constante1,constante0, N10):

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
	plt.loglog(N,dts1[0],"o-",color="black", alpha=0.2)
	plt.loglog(N,dts1[1],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts1[2],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts1[3],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts1[4],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts1[5],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts1[6],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts1[7],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts1[8],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts1[9],"o-",color="black",alpha=0.2)
	plt.loglog(N,constante0,"--")
	pyplot.plot([N[0],N[18]],[dts1_9[0],dts1_9[18]],"--")
	pyplot.plot([10,N[18]],[0.00000001,dts1_9[18]],"--")
	pyplot.plot([100,N[18]],[0.00000001,dts1_9[18]],"--")
	pyplot.plot([400,N[18]],[0.00000001,dts1_9[18]],"--")
	
	
	
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
	plt.ylabel("Tiempo de solución")
	#plt.axhline(,color="k", linestyle="--")

	plt.loglog(N,constante1,"--")
	pyplot.plot([N[0],N[18]],[dts2_9[0],dts2_9[18]],"--")
	pyplot.plot([10,N[18]],[0.00000001,dts2_9[18]],"--")
	pyplot.plot([100,N[18]],[0.00000001,dts2_9[18]],"--")
	pyplot.plot([400,N[18]],[0.00000001,dts2_9[18]],"--")
	

	pyplot.legend(["Constante","O(N)","O({}²)".format("N"),"O({}³)".format("N"),"O({}⁴)".format("N")], loc="lower left")

	plt.loglog(N,dts2[0],"o-", color="black",alpha=0.2)

	plt.loglog(N,dts2[1],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts2[2],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts2[3],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts2[4],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts2[5],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts2[6],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts2[7],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts2[8],"o-", color="black",alpha=0.2)
	plt.loglog(N,dts2[9],"o-", color="black",alpha=0.2)

	plt.grid(False)
	plt.xticks(tam_0,tam_1)
	plt.yticks(tp_tra0,tp_tra_1)
	plt.show()



def graficos2(N, dts1, dts2, a, constante1,constante0, N10):

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
	plt.loglog(N,dts10[0],"o-",color="black", alpha=0.2)
	plt.loglog(N,dts10[1],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts10[2],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts10[3],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts10[4],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts10[5],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts10[6],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts10[7],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts10[8],"o-",color="black",alpha=0.2)
	plt.loglog(N,dts10[9],"o-",color="black",alpha=0.2)
	plt.loglog(N,constante0,"--")
	pyplot.plot([N[0],N[18]],[dts1_9[0],dts1_99[18]],"--")
	pyplot.plot([10,N[18]],[0.00000001,dts1_99[18]],"--")
	pyplot.plot([100,N[18]],[0.00000001,dts1_99[18]],"--")
	pyplot.plot([400,N[18]],[0.00000001,dts1_99[18]],"--")
	
	
	
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
	plt.ylabel("Tiempo de solución")
	#plt.axhline(,color="k", linestyle="--")

	plt.loglog(N,constante10,"--")
	pyplot.plot([N[0],N[18]],[dts2_9[0],dts2_99[18]],"--")
	pyplot.plot([10,N[18]],[0.00000001,dts2_99[18]],"--")
	pyplot.plot([100,N[18]],[0.00000001,dts2_99[18]],"--")
	pyplot.plot([400,N[18]],[0.00000001,dts2_99[18]],"--")
	

	pyplot.legend(["Constante","O(N)","O({}²)".format("N"),"O({}³)".format("N"),"O({}⁴)".format("N")], loc="lower left")

	plt.loglog(N,dts20[0],"o-", color="black",alpha=0.2)

	plt.loglog(N,dts20[1],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts20[2],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts20[3],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts20[4],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts20[5],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts20[6],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts20[7],"o-",  color="black",alpha=0.2)
	plt.loglog(N,dts20[8],"o-", color="black",alpha=0.2)
	plt.loglog(N,dts20[9],"o-", color="black",alpha=0.2)

	plt.grid(False)
	plt.xticks(tam_0,tam_1)
	plt.yticks(tp_tra0,tp_tra_1)
	plt.show()

graficos1(N, dts1, dts2, a="Complejidad MATMUL de matriz completa",constante1=constante1, constante0=constante0,N10=N10)
graficos2(N, dts10, dts20, a="Complejidad MATMUL de matriz dispersa",constante1=constante10, constante0=constante00,N10=N10)