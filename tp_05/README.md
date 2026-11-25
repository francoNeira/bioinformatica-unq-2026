# Inferencias Evolutivas: El misterio del Moscahumano

Este trabajo práctico corresponde a la actividad [Inferencias Evolutivas](https://github.com/AJVelezRueda/Introduccion_a_la_Bioinformatica/blob/master/Teorico_Practicos/Inferencias_evolutivas/inferencias_evolutivas.md) (*Introducción a la Bioinformática*, UNQ).

---

## 🧗🏻‍♀️ Desafío I: Comparación de Secuencias y Metodología

> **Detalla las tácticas y/o metodologías que deberían utilizarse para darles una respuesta a los padres del niño.**

Para evaluar la muestra y acercar una respuesta a los padres, podemos plantear un proceso de inferencia en dos etapas:
- Realizar un alineamiento de secuencias para comparar la proteína de Bartmosca con las de humano y mosca, evaluando su grado de similitud.
- Construir el árbol filogenético utilizando ese alineamiento como insumo, para inferir su relación de parentesco y observar con qué linaje se agrupa.

---

> **Dadas las secuencias de Mosca, Humano y Moscahumano, ¿qué criterios se les ocurren para comparar las secuencias? ¿Qué resultados obtienen del análisis anterior?**

Para comparar las secuencias podemos evaluar la longitud de las cadenas y alinearlas posición a posición, considerando los aminoácidos idénticos, los cambios con propiedades fisicoquímicas similares y la penalización por gaps.
Al aplicar estos criterios entre las tres secuencias, observamos que Bartmosca presenta una notable coincidencia con la humana (compartiendo gran parte de la cadena sin cambios), mientras que frente a la mosca muestra diferencias a lo largo de toda la proteína.

---

> **¿Qué resultado esperaría obtener si utilizara el resto de las secuencias en el análisis? ¿Por qué?**

Al incorporar el resto de los organismos esperaríamos que Bartmosca, el humano y la mosca formen un grupo dentro de los animales, mientras que las plantas y el alga formarían linajes separados y la bacteria quedaría en la base como grupo externo.
Esto se debe a que las secuencias acumulan cambios de acuerdo al tiempo de divergencia desde un ancestro común: los animales compartirán una rama común frente al resto de los organismos y, dentro de ellos, Bartmosca y el humano quedarán más próximos por su mayor grado de similitud.

---

## 🧗🏻‍♀️ Desafío II: Alineamiento Múltiple de Secuencias (Clustal Omega)

Se realizó el alineamiento múltiple con Clustal Omega entre los nueve organismos. El resultado se encuentra en [`data/clustal/clustalo-I20261124-060142-0113-60514728-p1m.aln-clustal_num`](data/clustal/clustalo-I20261124-060142-0113-60514728-p1m.aln-clustal_num).

A partir del alineamiento se observa que:
- Bartmosca y humano presentan una identidad del 92,37% sobre las 131 posiciones (121 coincidencias).
- Humano y mosca presentan una identidad del 77,86% sobre las 131 posiciones (102 coincidencias).
- Las diferencias entre Bartmosca y humano se concentran principalmente en el inicio de la proteína, mientras que gran parte de la región final permanece idéntica.

---

## 🧗🏻‍♀️ Desafío III: Inferencia Filogenética (IQ-TREE y FigTree)

> **Como vemos, el servidor nos permite elegir el modelo de sustitución. ¿A qué se refiere?**

Es una descripción matemática de los cambios de aminoácidos que pueden ocurrir durante la evolución (para este análisis, IQ-TREE seleccionó por defecto el modelo DAYHOFF+G4).

---

> **¿Qué es el Bootstrap? ¿De qué manera nos habla de la calidad de nuestro árbol? ¿Cómo influye el número de Bootstraps en el resultado?**

El bootstrap es una técnica que vuelve a muestrear columnas del alineamiento y reconstruye árboles para estimar el respaldo de sus ramas.
La calidad del árbol se evalúa observando el soporte de cada rama: un valor alto indica que la agrupación se recupera con frecuencia y tiene mayor respaldo; un valor bajo señala una relación menos segura.
Al aumentar el número de réplicas, la estimación de los soportes se vuelve más estable.

En este análisis usamos 1000 réplicas para cada medida: UFBoot, que estima con qué frecuencia se recupera cada rama, y SH-aLRT, que compara cada rama con otras agrupaciones cercanas.

---

> **Interpreten los resultados obtenidos mediante la visualización de los árboles con FigTree. ¿Es necesario realizar algún paso extra previo a la interpretación del árbol? ¿Por qué?**

Es necesario enraizar el árbol para orientar la interpretación de sus ramas. Usamos Rhizobium sp. como grupo externo porque es la única bacteria del conjunto; los demás organismos son eucariotas (animales, plantas y un alga). Al ubicar la raíz en la rama de la bacteria, podemos interpretar cómo se agrupan los eucariotas entre sí. En FigTree seleccionamos esa rama y aplicamos Reroot.

El árbol resultante es [`data/iqtree3/tree.nwk`](data/iqtree3/tree.nwk); como entrada de IQ-TREE usamos el alineamiento completo en formato FASTA ([`data/clustal/clustalo-I20261124-060142-0113-60514728-p1m.fa`](data/clustal/clustalo-I20261124-060142-0113-60514728-p1m.fa)).

Humano y Bartmosca se agrupan directamente, y la mosca se une después. Sus soportes son 75,3% / 74% para humano–Bartmosca y 83,1% / 84% para el grupo de los tres (SH-aLRT / UFBoot). Los demás organismos quedan fuera de este grupo.
