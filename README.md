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


![Uploading Rendimiento_invA_scipy_float16.png…]()


![Rendimiento_invA_scipy_float32](https://user-images.githubusercontent.com/88339083/129815754-a60fb95c-951e-4304-b46e-18a80853b357.png)


![Rendimieno_scipy_float64](https://user-images.githubusercontent.com/88339083/129815800-242667bc-e0d7-48fe-93dc-ad22bf1917bb.png)

**EL PROGRAMA  NUMPY.LINALG.INV_8_16_32_64BITS.PY NO FUE CAPAS DE RESOLVER LA INVERSIÓN PARA DTYPE=HALF Y 16BITS**
LA RAZÓN DE ESTO SE DEBE A  LIBRERIA





