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
SE CREE QUE EL MÉTODO UTILIZADO ES  EL DE VECTORES DE BASES RECÍPROCAS Y EL USO DE USO DE LA MATRIZ IDENTIDAD

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 
INCIDE EN QUE EL COMPUTADOR JERAQUIZA LAS TAREAS QUE UNO LE ORDENA  Y VA REALIZANDO SEGÚN SU PRIORIDAD. POR TANTO, EL PARALELISMO PUEDE FAVORECER O PERJUDICAR EL RENDIMIENTO DEL COMPUTADOR SEGÚN LA LISTA DE "TAREAS" PENDIENTES.
