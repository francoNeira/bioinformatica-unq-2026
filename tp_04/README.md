# ¿En qué se parecen una gallina y una mosca?

Este trabajo práctico corresponde a la actividad [¿En qué se parecen una gallina y una mosca?](https://github.com/AJVelezRueda/Introduccion_a_la_Bioinformatica/blob/master/Teorico_Practicos/Bioinform%C3%A1tica_Primeros_pasos/En_que_se_parece_una_mosca_y_una_gallina.md) (*Bioinformática: Primeros pasos*).

A partir de la proteína **citocromo c**, involucrada en la respiración celular, comparamos secuencias de distintas especies mediante bases de datos (**NCBI Protein**), alineamientos múltiples (**Clustal Omega**) y árboles filogenéticos.

---

## 🧬 Tabla de Organismos

A partir de la búsqueda en NCBI, se completó la tabla con las secuencias del citocromo c seleccionadas y sus nombres comunes:

| Secuencia | Nombre taxonómico | Nombre común |
| :--- | :--- | :--- |
| **NP_061820.1** | *Homo sapiens* | Humano |
| **NP_001072946.1** | *Gallus gallus* | Gallo / Gallina |
| **NP_001065289.1** | *Pan troglodytes* | Chimpancé común |
| **NP_001157486.1** | *Equus caballus* | Caballo |
| **NP_001183974.1** | *Canis lupus familiaris* | Perro |
| **AEP27192.1** | *Gorilla gorilla* | Gorila |
| **XP_024245566.1** | *Oncorhynchus tshawytscha* | Salmón real |
| **NP_001086101.1** | *Xenopus laevis* | Rana de uñas africana |
| **NP_477164.1** | *Drosophila melanogaster* | Mosca de la fruta |

---

## ✍️ Alineamiento Manual y Conceptos Evolutivos

> **¿Cuán sencillo será alinear dos o más secuencias a mano? ¿Cuánto influirán el número de secuencias a alinear, su longitud, y la similitud entre ellas?**

Poco sencillo. La dificultad crece con la cantidad de secuencias y su longitud. Es más simple si tienen igual longitud (evita definir *gaps* obligados) y resulta más intuitivo cuanto mayor es la similitud entre ellas.

---

> **¿Son parecidos los citocromos c de humano y gallo?**

Muy parecidos. Comparten la mayor parte de la secuencia y solo difieren en 13 de los 105 aminoácidos, mostrando una alta conservación e identidad.

---

> **¿Qué teorías subyacen a este análisis?**

La **teoría de la evolución** y el **ancestro común**. El citocromo c es vital para la respiración celular, por lo que su presencia universal refleja un origen compartido. En especies muy cercanas como humano, chimpancé y gorila, la secuencia es idéntica.

---

> **¿Cómo nos ayuda la evolución a explicar sus similitudes y diferencias?**

* **Similitudes:** Por restricciones funcionales. Al ser esencial para la respiración celular, la selección natural conserva las regiones críticas del gen.
* **Diferencias:** Por mutaciones acumuladas en el ADN a lo largo del tiempo desde la divergencia entre linajes.

---

## 🌐 Alineamiento Múltiple de Secuencias (Clustal Omega)

> **¿Qué indican los colores?**

Indican las **propiedades físico-químicas y estructurales** de los aminoácidos (hidrofóbicos, polares, con carga), permitiendo evaluar la conservación de características aun ante cambios puntuales de residuos.

---

> **¿Qué indican el guión (-), los dos puntos (:) y el asterisco (*)?**

* **Guión (`-`):** *Gap* (inserción o deleción).
* **Dos puntos (`:`):** Sustitución conservativa (aminoácidos con propiedades muy similares).
* **Asterisco (`*`):** Identidad total (mismo aminoácido en todas las secuencias).

---

> **A simple vista, ¿se conserva la secuencia del citocromo c en los organismos?**

Sí, fuertemente. Se evidencia en la abundancia de asteriscos (`*`), letras idénticas y bloques de colores coincidentes a lo largo del alineamiento.

---

> **¿Creeríamos que todos los organismos se asemejan por igual al resto, o se pueden identificar grupos de mayor similitud? Si es así, ¿tienen sentido?**

No se asemejan por igual; se observan grupos con distinta cercanía (primates idénticos entre sí, mamíferos muy próximos, vertebrados no mamíferos más distantes y la mosca como la más alejada).

Tiene pleno sentido evolutivo: no todos los grupos comparten el mismo ancestro común inmediato. Más secuencias aportarían una resolución mayor sobre clados completos.

---

> **¿Qué evidencias nos aportaría este análisis, a la luz de la evolución?**

Evidencia molecular directa: a mayor similitud de secuencia, mayor parentesco evolutivo entre los organismos.

---

## 🌳 Inferencia Filogenética (Árbol Filogenético)

> **A juzgar por los organismos participantes, ¿cuáles creería que deberían estar más agrupados en el árbol filogenético?**

Humano y primates en primer lugar, luego los demás mamíferos, después los restantes vertebrados, y finalmente la mosca como grupo más alejado.

---

> **Observemos el árbol filogenético. ¿Concuerda con lo esperado? ¿De qué organismos son los citocromos c más parecidos? ¿Cómo se explica?**

Sí, concuerda con lo esperado:
* Los citocromos c más parecidos son entre **humano y primates** (distancia 0), seguidos por mamíferos, con la mosca en la rama más distante.
* Se explica por la **divergencia evolutiva**: un ancestro común más reciente implica menor tiempo para acumular mutaciones en la secuencia respecto a linajes más antiguos.
