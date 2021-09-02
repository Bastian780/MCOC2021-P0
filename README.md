# MCOC2021-P0

# Mi computador principal

* Marca/modelo: huawei NBLK-WAX9X
* Tipo: Notebook
* Año adquisición: 2021
* Procesador:
  * Marca/Modelo: AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx     
  * Velocidad Base: 2.1 GHz
  * Velocidad Máxima: 4.40 GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 4
  * Arquitectura: x64
  * Set de instrucciones:
* Tamaño de las cachés del procesador
  * L1: 384KB
  * L2: 2MB
  * L3: 4MB
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR4
  * Velocidad 2400 MHz
  * Numero de (SO)DIMM: 4
* Tarjeta Gráfica
  * Marca / Modelo: AMD Radeon(TM) Vega 8 Graphics
  * Memoria dedicada: 4560 MB
  * Resolución: 1920 x 1080

* Disco 1: 
  * Marca: huawei
  * Tipo: SSD
  * Tamaño: 476.92 GB
  * Particiones: 2
  * Sistema de archivos: NTFS,NTFS

  
* Dirección MAC de la tarjeta wifi: 28-CD-C4-6B-0C-** (relleno con asteriscos por privecidad, porque estoy casi seguro de que la nasa está tras mis pasos) 
* Dirección IP (Interna, del router): 192.168.1.1
* Dirección IP (Externa, del ISP): 181.161.205.4 
* Proveedor internet: Telefónica chile S.A

<<<<<<< HEAD

=======
**DESEMPEÑO MATMUL**

![Figure_1](https://user-images.githubusercontent.com/88339083/128527683-968d27c8-e2a1-4484-abaf-aeb1bd255a37.png)
1.-El gráfico difiere en que : 
           pc  del ayudante/profesor tiene 10gb ram y yo tengo 8gb  ram
           grafican 24  valores  entre 0 y 10000 (que determinan que tan grandes sonn las matrices que se estan multiplicando)  yo solo grafico 16 (entre 0 y  6500) porque sino se demora demaciado.
2. Las diferencias en los tiempos de cada corrida se debe a que "otra funcion está ejecutando el computador" puesto que  toda acción y orden realizada o recibida, respectivamente, por el ordenador se  graduará y ejecutará según su nivel de urgencia(en otras palabras, el pc prioriza realizar ciertas operaciones, por tanto  según la prioridad de la acción será cuanto se demore en realizarla.
3. el gráfico de uso de memoria es lineal puesto que representa el espacio que usa en la memoria la matriz generada, por tanto entre mas grande la matriz, mas grande será el espacio que usa.  Mientras que el tiempo  transcurrido no lo es por la razón mencionada en el punto 2).
4. Uso el PYTHON 3.9.6(64bits)
5. Numpy versión  1.21.1
6.![image](https://user-images.githubusercontent.com/88339083/128532899-3157f791-f4ae-4258-90b3-a2f8ae0a2f10.png)
Corrí el programa 10 veces por separado, por  tanto el estado de la cpu correspondiente a la ejecucion del código corresponde a cuando alcanza su máximo utilizando los 2 hilos de cada uno de los 4 nucleos, utilizando un total de 8 procesadores lógicos. (o 4 procesadores fiscos de dos hilos c/u).
>>>>>>> 0487218469bcdb34b0bf5ff0f63af70636a360ec

***DESEMPEÑO  INVERSIÓN DE MATRIZ A, USANDO SCIPY.LINALG Y NUMPY.LINALG*** 
1.-DESEMPEÑO DE SCIPY.LANALG Y NUMPY.LINALG PARA TAMAÑO CRECIENTE DE MATRICES:
CON EL OBJETIVO DE ANILZAR Y COMPARAR EL DESEMPEÑO, SE GENERARON 60  ARCHIVOS QUE CONTIENEN  (TAMAÑO DE MATRIZ, TIEMPO DE INVERSIÓN DE A, BYTS TOTALES UTILIZADOS), PARA LUEGO GRAFICAR Y COMPARAR VISUALMENTE LO OBTENIDO. 
LOS ARCHIVOS FUERON GENERADOS CON LOS CODIGOS  SCIPY.LINALG.INV_8_16_32_64BITS.PY Y NUMPY.LINALG.INV_8_16_32_64BITS.PY, PARA LUEGO SER GRAFICADOS CON  GENERACION_DE_GRAFICOS.PY OBTENIENDO LO SIGUIENTE:
![Rendimiento_invA_scipy_half](https://user-images.githubusercontent.com/88339083/129815687-c2e98c8c-886a-45f2-a0c6-3d1da76bcc34.png)![Rendimiento_invA_scipy_float16](https://user-images.githubusercontent.com/88339083/129815745-f185d4c7-e18f-4036-8f64-fd15c5f19d3b.png)





![Rendimiento_invA_scipy_float32](https://user-images.githubusercontent.com/88339083/129815754-a60fb95c-951e-4304-b46e-18a80853b357.png)


![Rendimieno_scipy_float64](https://user-images.githubusercontent.com/88339083/129815800-242667bc-e0d7-48fe-93dc-ad22bf1917bb.png)

**EL PROGRAMA  NUMPY.LINALG.INV_8_16_32_64BITS.PY NO FUE CAPAS DE RESOLVER LA INVERSIÓN PARA DTYPE=HALF Y 16BITS**
SCIPY ES UNA LIBRERÍA CON MUCH MÁS ALCANCE QUE NUMPY, DE HECHO ESTA ÚLTIMA  ES UNO DE LOS ELEMENTOS QUE COMPONEN A SCIPY . ES POR ESTA RAZÓN  QUE SCIPY ES CAPAZ DE GENERAR TODOS LOS ARCHIVOS DE TEXTOS, INDEPENDIENTE EL DTYPE, MIENTRAS QUE NUMPY SOLO FUNCIONA CON DTYPE=FLOAT64 Y FLOAT32, PUESTO QUE VIENE PROGRAMADO PARA  TRABAJAR CON UN FLOAT32.  SIN EMBARGO, NUMPY NO SOPORTA LOS DTYPE=HALF Y FLOAT16 PUESTO QUE  SI BIEN REQUIERE MENOS MEMORIA, REALIZA UNA MAYOR CANTIDAD DE APROXIMACIONES PARA CUMPLIR CON LA CANTIDAD DE INFORMACIÓN SOLICITADA NO SIENDO SOPORTADO POR EL COMPUTADOR.
![Rendimiento_invA_Numpy_float32](https://user-images.githubusercontent.com/88339083/129973894-2a968227-f89c-4aaf-b4d7-7924146b1864.png)

![Rendimiento_invA_numpy_float64](https://user-images.githubusercontent.com/88339083/129973904-87a9b6a8-aafc-43cd-875f-96817177e623.png)
LUEGO DE GRAFICAR LO OBTENIDO, SE OBSERVA QUE A TIPO DE DATOS, SCIPY ES MUCHO MAS EFICIENTE QUE NUMPY PUESTO QUE HACE POSIBLE TRABAJAR CON LOS 4 EVALUADOS.  MIENTRAS QUE A  USO DE MEMORIA  SE OBSERVA ALGO SIMILAR, PERO EN CUANTO A TIEMPO TRANSCURRIDO, LO TARDADO POR SCIPY AL AUMENTAR EL TAMAÑO DE LA MATRIZ TIENE UN COMPORTAMIENTO MUCHO MAS ESTABLE QUE NUMPY.

2.-USO  OVERWRITE_A=TRUE
EL USO DEL OVERWRIITE_A=TRUE EFICTIVAMENTE RESULTA COMO GANANCIA DE  DESEMPEÑO PUESTO QUE PERMITE REESCRIBIR SOBRE DATOS YA EXISTENTES, SIN LA NECESIDAD DE UTILIZAR MÁS ESPACIO  PARA NUEVOS DATOS.

3.-TAMAÑO EN MEMORIA DE LOS DTYPES
LOS TAMAÑOS  EN MEMORIA DE CADA TIPO DE DATO SON:
1.- HALF= 1BYTS=8BITS
2.- SINGLE= 2BYTS=16BITS
3.-DOUBLE=4BYTS=32BITS
4.-LONG DOUBLE=8BYTS=64BITS

4.-EFICIENCIA CON NUMPY.LINALG.INV, SCIPY.LINALG.OVERWRITE_A=TRUE Y SCIPY.LANLG.OVERWRITE_A=FALSE

PARA ANALIZAR LA EFICIENCIA, SE PROGRAMÓ Y GRAFICÓ CADA CASO OBTENIENDO LO SIGUIENTE
![Rendimiento_invA_scipy_overwrite_a=False_half](https://user-images.githubusercontent.com/88339083/129988539-fe289f70-c58c-450a-b73a-b82730f6f3c9.png)
![Rendimiento_invA_scipy_overwrite_a=False_float16](https://user-images.githubusercontent.com/88339083/129988551-de13ac0f-5397-4680-aa31-7c15946c85a5.png)
![Rendimiento_invA_scipy_overwrite_a=False_float32](https://user-images.githubusercontent.com/88339083/129988559-c9bdad72-a381-4d80-8b61-3d07fff699c0.png)
![Rendimiento_invA_scipy_overwrite_a=False_float64](https://user-images.githubusercontent.com/88339083/129988570-abee910e-5e3b-48fe-bde8-0e79304a1760.png)
![Rendimiento_invA_scipy_overwrite_a=True_half](https://user-images.githubusercontent.com/88339083/129988604-a33fd4a9-5d92-4f17-a72f-4bd49e487714.png)
![Rendimiento_invA_scipy_overwrite_a=True_float16](https://user-images.githubusercontent.com/88339083/129988619-9a7a5408-9580-4998-8f9c-7143f1a37b6d.png)
![Rendimiento_invA_scipy_overwrite_a=True_float32](https://user-images.githubusercontent.com/88339083/129988629-2a6c7e13-c410-4b3e-b136-0f7a7ec4889d.png)
![Rendimiento_invA_scipy_overwrite_a=True_float64](https://user-images.githubusercontent.com/88339083/129988642-ea9da0b2-78d8-428e-866e-68798435341f.png)
CONCLUYENDO QUE EN CUANTO A EFICIENCIA, EL RANKING CORRESPONDE AL SIGUIENTE:
1.-SCIPY.LINALG.OVERWRITE_A=TRUE
2.-SCIPY.LINALG.OVERWRITE_A=FALSE
3.-NUMPY.LINALG.INV
PUESTO QUE WRITE_A=TRUE OPTIMIZA ESPACIO REESCRIBIENDO SOBRE ARCHIVOS EXISTENTES, WRITE_A=FALSE SI BIEN UTILIZA MÁS ESPACIO, SU RENDIMIENTO SIGUE SIENDO MÁS ESTABLE QUE EL DE NUMPY.LINALG Y TAMBIEN FUNCIONA CON TODOS LOS DTYPES (NUMPY NO).

LA UTILIZACIÓN DE CPU DURANTE EL PROCESO FUE DEL 100%, MIENTRAS QUE DE LA DE MEMORIA FUE DEL 65%
![image](https://user-images.githubusercontent.com/88339083/129989059-91b83ff3-7bb4-4483-afe7-6cf29cdcca68.png)
![image](https://user-images.githubusercontent.com/88339083/129989002-ee0c46dc-eb3c-4709-847f-3aeaf49cf79e.png)


¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 
ambos utilizan el método gauss jordan

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 
INCIDE EN QUE EL COMPUTADOR JERAQUIZA LAS TAREAS QUE UNO LE ORDENA  Y VA REALIZANDO SEGÚN SU PRIORIDAD. POR TANTO, EL PARALELISMO PUEDE FAVORECER O PERJUDICAR EL RENDIMIENTO DEL COMPUTADOR SEGÚN LA LISTA DE "TAREAS" PENDIENTES.
**ENTREGA P04**

Tras realizar las 10 iteraciones y calcular el promedio en cada caso, se obtuvo lo siguiente:

**Para las iteraciones en las que se usó un dtype=Double:
![TIMMING DOUBLE CASO 1-2](https://user-images.githubusercontent.com/88339083/130309059-ded18877-383b-4cca-ba43-875fbd821d01.png)
![TIMMING_DOUBLE_CASO5-6](https://user-images.githubusercontent.com/88339083/130309062-850e2985-3ec6-46a7-a499-e390960ab3af.png)
![TIMMING_DOUBLE_CASO6-7](https://user-images.githubusercontent.com/88339083/130309063-56b72cac-aac9-4b31-8ab9-b3843b6e35bf.png)
![TIMMING_DOUBLE_CASO2-3](https://user-images.githubusercontent.com/88339083/130309064-4451a14c-b584-4d39-beea-ad0252797da1.png)
![TIMMING_DOUBLE_CASO3-4](https://user-images.githubusercontent.com/88339083/130309065-55a80d78-cff4-4b89-a4c3-e319a2cfd4d9.png)
![TIMMING_DOUBLE_CASO4-5](https://user-images.githubusercontent.com/88339083/130309066-0a146ccf-6f71-4ff5-bde8-ca08daca1a96.png)

**Mientras que para los casos en que se usó dtype=float32:

![TIMMING_FLOAT32_CASO5-6](https://user-images.githubusercontent.com/88339083/130309083-09119c3b-ae3d-4b8f-9e5e-aff0ec254885.png)
![TIMMING_FLOAT32_CASO6-7](https://user-images.githubusercontent.com/88339083/130309084-d8678a3f-8e78-4c99-a814-63f265cb3a96.png)
![TIMMING_FLOAT32_CASO1-2](https://user-images.githubusercontent.com/88339083/130309085-624bde7f-f447-4c33-b849-ded4e7e735f7.png)
![TIMMING_FLOAT32_CASO2-3](https://user-images.githubusercontent.com/88339083/130309086-f604b6d3-c3b4-4ed5-8ef3-0c437ce96b46.png)
![TIMMING_FLOAT32_CASO3-4](https://user-images.githubusercontent.com/88339083/130309087-e4a98a30-e8f3-4a9e-99bd-cd7676503307.png)
![TIMMING_FLOAT32_CASO4--5](https://user-images.githubusercontent.com/88339083/130309088-017bbc92-4772-45f5-be68-c576e8639256.png)

Finalmente, para obtener una mayor claridad, se graficaron todos los casos en que se usó Double y float32 juntos (cada uno por separado):
![TIMMING_CASOS_TOTALES_FLOAT32](https://user-images.githubusercontent.com/88339083/130309172-fb3e284f-e789-4a91-a4fa-c3edee3b4240.png)
![TIMMING_CASOS_TOTALES_DOUBLE](https://user-images.githubusercontent.com/88339083/130309175-cf426d89-edd8-4120-8f9f-beacf1692cd6.png)

De dónde se observa claramente que  para el caso en que se uso double fue el caso 3, probablemente porque  al imponer que la matriz es definida positiva, las opciones de resultados se reducen practicamente a la mitad. Por tanto, solo se deben evaluar los valores positivos , requeriendo menos memoria y procesamiento.

Lo mismo ocurre para el caso de cuando se utilizó float32

Por otro lado, utilizando la función EIGH , NUEVAMENTE ITERANDO 10 VECES Y GRAFICANDO EL PROMEDIO, SE OBTUVO LO SIGUIENTE:
![EIGH_CASOS_TOTALES_FLOAT32](https://user-images.githubusercontent.com/88339083/130309466-c83e6822-3627-46bb-aa7f-2678a20c0229.png)



![EIGH_CASOS_TOTALES_DOUBLE](https://user-images.githubusercontent.com/88339083/130309470-14f46ca3-bd21-4878-95e9-188b2a9e8957.png)
Donde se observa que los mejores rendimientos fueron alcanzados por  el caso 7, donde se utiliza  driver evx, quien plantea un intervalo semi abierto  en el que , si los hay, solo devuelve los valores propios. Ocurre algo similar que en el caso anterior, puesto que  nuevamente estamos acotando la búsqueda de información a la función y por tanto es lógico que esta tarde menos en solucionar.

El rendimiento del algoritmo dependerá de múltiples factore tales como:
 El tamaño de la matriz (influye muchisimo) 
 Cantidad de iteraciones 
 Característica de la función utilizada (algunas acotan la búsqueda de soluciones)La
 etc.
 Mi computador utiliza sus 8 procesadores lógicos al momento de correr el programa.
La gran diferencia en el rendimiento de  casa caso va en que tanto se restringe la busqueda de soluciones a la función. Entre mayores restricciones, menor es el tiempo que tardará en encontrarlas.



**ENTREGA P05**
El código utilizado para formar la matriz Laplaciana  es el siguiente:


def Laplaciana_completa(N, tipo):

	
	e=eye(N)-eye(N,N,1)

	return(tipo(e+e.T))

def Laplaciana_dispersa(N, tipo):
	
	e=eye(N)-eye(N,N,1)

	return(sparse.csr_matrix(tipo(e+e.T)))

En las cuales se genera una matriz identidad con "eye" , a la cual se le resta otra matriz identidad con  unos en la diagonal superior  y finalmente a todo lo anterior  se le suma una  matriz identidad traspuesta.
Este mecanismo resulta mucho más eficiente que  darle forma a la matriz laplaciana con ciclos for.
en "def Laplaciana_dispersa" se utiliza el comando "csr_matrix"  que  a diferencia de la matriz completa , utiliza los índices iniciales y finales, por finalas para indicar las posiciones en las que existen valores dentro de la matriz que son distintos a 0 lo que es mucho más eficiente. Sin embargo, existen otra funciones aun más eficientes puesto que esta en particular incluye los valores que son 0ros y que se encuentran entre el índice inicial y final  corresponddientes a las posiciones de los valores distintos de 0.

Luego, graficando los archivos txt generados se obtuvo lo siguiente:
1. Para el caso de matriz llena:
![COMPLEJIDAD_MATMUL_COMPLETA](https://user-images.githubusercontent.com/88339083/131202890-11d17592-333c-4297-b05e-bc6f7b51d49b.png)
Del gráfico anterior, se observa que la complejidad  del algoritmo para ensamblar las matrices y resolver la multiplicación, se ve representada por una función cuadrática

2.Para el caso de matriz dispersa
![COMPLEJIDAD_MATMUL_DISPERSA](https://user-images.githubusercontent.com/88339083/131204483-557c635e-abcb-402e-ab2d-9ad74a01db3d.png)

Del gráfico anterior, se observa que la complejidad  del algoritmo para ensamblar las matrices y resolver la multiplicación, se ve representada por una  función constante. Lo que significa que el programa es mucho más eficiente que el anterior. Esto se debe a que se están guardando muchos menos datos que en el caso de la matriz completa, por tanto lógicamente el programa tardará menos.

Además, se observa una especie de discontinuidad  al mmento de correr el programa puesto que el valor inicial  para una matriz de N pequeño tarda más que para Ns mayores. Esta anomalía corresponde a la iniciación del algoritmo( es decir cuanto se demora el programa en entrar al sistema operativo).
** ENTREGA 6**
las matrices laplacianas utilizadas fueron las siguiente:

Para las matrices completas-->
def Laplaciana_completa(N, tipo):
	
	e=eye(N)-eye(N,N,1)
	return tipo(e+e.T)

Para la matriz disperas:
1.- Caso de invertir matriz 
def Laplaciana_dispersa_csc(N, tipo):
	
	e=eye(N)-eye(N,N,1)

	return(sparse.csc_matrix(tipo(e+e.T)))
La característica de esta función es que, con el comando sparce.csc, voy almacenando por la matriz por columna, ignorando algunos de los 0 
2.- Caso Resolver sistema:
def Laplaciana_dispersa_csr(N, tipo):
	
	e=eye(N)-eye(N,N,1)

	return(sparse.csr_matrix(tipo(e+e.T)))
La caeacterística de esta función es que con el comando sparce csr, voy almacenando la matriz por fila, ignorando algunos de los ceros

Luego, generando, almacenando y graficando los archivos .txt se obtiene lo siguiente:

![Inversión de matriz completa](https://user-images.githubusercontent.com/88339083/131906865-4fc8761e-1c0a-46ca-9d0e-2dd3242510cb.png)
![Inversión de matriz dispersa](https://user-images.githubusercontent.com/88339083/131906871-474ccfbf-c932-41cb-ade5-4c7c453ab4ed.png)
![solve con matriz dispersa](https://user-images.githubusercontent.com/88339083/131906875-a0ca70e6-2c86-492c-b230-9252141b83aa.png)
![Solve matriz completa](https://user-images.githubusercontent.com/88339083/131906879-c34401c4-ff49-4126-9d9e-0faeef8437a5.png)

Análisis:
1.- Para los casos  de inversión, la  el uso de la matriz dispera, disminuye levemente el tiempo de inversiónn y  ensamblaje dematrices. Lo mismo ocurre para los casos de solución de sistemas(solve)

2.-casos:
   1.- Ensamblaje matriz compleja -> Asintótico a  o(n2)
   2 .- Ensamblaje matriz dispersa-> Asintótico a  o (n)
   3.- Inversión matriz completa .-> Asintótico a o (n2)
   4.- Inversiónn matriz dispersa-> Asintótico a o (n)
   5.- Solve matriz completa-> Asintótico a o(n2)
   6.- Solve matriz dispersa->Asintótico a o ( n)
  En sintesis, el utilizar matrices complejas reduce en almenos un grado la complejidad del algoritmo.
  
 3.- El tamaño de la matriz  logicamente complejiza el trabajo, puesto que el programa debe trabajar con más datos, y por tanto con byts. Por tanto, cualquier método como sparse, facilita el proceso puesto que en gran parte de los casos, permite solo guardar los datos relevantes.  Esto se observa puesto que al observar la parte más a la derecha de los N(matrices mas grandes) la pendiente delos gráficos aumenta.
 
 4.- No siempre son estables, pero en general los resultados obtenidos utilizando la matriz dispersa son mas estables que los obtenidos con la matriz completa. La variación en el tiempo puede encontrar razon de ser debido a que quizas que cuando se corrió el programa, tambien se estaba ejecutando otra orden (musica, navegador, etc). y como el computador jerarquiza sus tareas, puede que haya encontrado otra que era más urgente que resolver el solver o la inversa.
 
 
   


