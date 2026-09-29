# Desafío V: Predicción de Estructura Secundaria (H, B, L)

Este desafío forma parte de la clase práctica de [Biomoléculas](https://github.com/AJVelezRueda/Introduccion_a_la_Bioinformatica/blob/master/Teorico_Practicos/Intro_a_la_Biolog%C3%ADa/Biomol%C3%A9culas.md) (*Introducción a la Biología*), correspondiente al Desafío V.

---

## 📋 Consigna del Desafío

> **Desafío V:** Escribí un script en Python que prediga la estructura secundaria que adoptará cada residuo (aminoácido) de la secuencia proteica dada, especificándola como `H` (si es una hélice), `B` (si es una hoja beta plegada) y `L` (si es un bucle o loop).
>
> **Preguntas disparadoras:**
> - ¿Qué inputs tendría tu programa?
> - ¿De qué modo se te ocurre configurar el output?

---

## 💡 Fundamento Teórico

La conformación secundaria que adopta una proteína depende principalmente de su estructura primaria (la secuencia de aminoácidos). Ciertos aminoácidos presentan mayores propensiones intrínsecas a formar hélices alfa, otros a constituir hojas beta y otros a formar giros o lazos desestructurados.

A partir de la frecuencia de aparición y la preferencia de cada uno de los 20 aminoácidos para formar parte de una u otra estructura secundaria, se categorizan las propensiones de la siguiente manera:

- **`H` (Hélice $\alpha$):** Preferida por `E` (Glu), `A` (Ala), `L` (Leu), `M` (Met), `Q` (Gln), `K` (Lys), `R` (Arg).
- **`B` (Hoja $\beta$ plegada):** Preferida por `V` (Val), `I` (Ile), `Y` (Tyr), `F` (Phe), `W` (Trp), `T` (Thr), `C` (Cys).
- **`L` (Bucle / Loop):** Preferida por `G` (Gly), `P` (Pro), `N` (Asn), `D` (Asp), `S` (Ser), `H` (His).

---

## 🐍 Script: predict_secondary_structure.py

La implementación computacional del desafío se encuentra en [`predict_secondary_structure.py`](./predict_secondary_structure.py).

### 🛠️ Requisitos
- **Python 3.10+**
- No requiere la instalación de librerías externas (utiliza exclusivamente módulos de la biblioteca estándar de Python, como `argparse`).

### ⚙️ Entrada y Salida
- **Input:** Secuencia proteica en formato de una letra (directa por terminal o mediante archivo de texto plano). Se admiten mayúsculas o minúsculas, y se descartan espacios y saltos de línea.
- **Output:** Cadena de texto de igual longitud con los símbolos `H`, `B` y `L` (los residuos no reconocidos se marcan con `?`). Con el flag opcional `-v` / `--verbose`, calcula además el porcentaje de composición de cada conformación.

### 💻 Ejemplos de Uso

#### Ejemplo 1: Secuencia directa por terminal (básico)

```bash
python3 predict_secondary_structure.py "ACDEFGHIKLMNPQRSTVWY"
```

**Salida generada:**

```text
============================================================
 PREDICCIÓN DE ESTRUCTURA SECUNDARIA
============================================================
Longitud de secuencia: 20 residuos

Secuencia:  ACDEFGHIKLMNPQRSTVWY
Estructura: HBLHBLLBHHHLLHHLBBBB
```

#### Ejemplo 2: Procesar archivo de texto con estadísticas (`-v`)
Ejecución utilizando el archivo de prueba [`sequence.txt`](./sequence.txt) (153 residuos):

```bash
python3 predict_secondary_structure.py sequence.txt -v
```

**Salida generada:**

```text
============================================================
 PREDICCIÓN DE ESTRUCTURA SECUNDARIA
============================================================
Longitud de secuencia: 153 residuos

Secuencia:  MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV
Estructura: HHLLHHHHHHHHBBHHHHHBLBLLLHLHHBHLHBHHBBLHHLHLHLBHLLHBLLLLLLBHBBBLBHHLBHHBBHHBBLHHHBBLBBHHLHLBBBHLBBHHLHHHBHBLLLBBBLBHBHBLHBBLLHHHHLLHBHBHLHHHHLBBHBLHLBLBB

------------------------------------------------------------
Composición estimada:
  - Hélice (H)        :  64 ( 41.8%)
  - Hoja Beta (B)     :  47 ( 30.7%)
  - Bucle (L)         :  42 ( 27.5%)
============================================================
```

#### Ayuda del comando:
Para consultar las opciones, reglas de propensión y sintaxis en cualquier momento (o ejecutando el script sin argumentos):

```bash
python3 predict_secondary_structure.py -h
```

**Salida de ayuda:**

```text
usage: predict_secondary_structure.py [-v] [-h] [entrada]

Predice la estructura secundaria (H: Hélice, B: Hoja Beta, L: Loop) de una secuencia de aminoácidos.

positional arguments:
  entrada        Secuencia proteica directa o ruta a un archivo de texto plano.

options:
  -v, --verbose  Muestra estadísticas de composición estructural.
  -h, --help     Muestra este mensaje de ayuda detallado y finaliza.

CONFORMACIONES Y REGLAS DE PROPENSIÓN:
  H  Hélice alfa      (Favorecida por: E, A, L, M, Q, K, R)
  B  Hoja beta        (Favorecida por: V, I, Y, F, W, T, C)
  L  Bucle / Loop     (Favorecida por: G, P, N, D, S, H)
  ?  No reconocido    (Cualquier carácter ajeno a los 20 aminoácidos estándar)

FORMATOS DE ENTRADA PERMITIDOS:
  1. Secuencia directa por terminal (ej: "ACDEFGHIKLMNPQRSTVWY")
  2. Archivo de texto plano con la secuencia (ej: sequence.txt)
  * Tolera minúsculas/mayúsculas, espacios y saltos de línea (se normalizan automáticamente).

EJEMPLOS DE USO:
  # 1. Predicción rápida por terminal:
  python3 predict_secondary_structure.py "MLPGLALLLLAAWTMRALEV"

  # 2. Predicción desde archivo con estadísticas (-v / --verbose):
  python3 predict_secondary_structure.py sequence.txt -v

  # 3. Consultar esta ayuda detallada:
  python3 predict_secondary_structure.py -h
```

