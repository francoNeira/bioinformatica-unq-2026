# Archivos de datos

Este índice describe los archivos y subcarpetas incluidos en `data/`.

## `clustal/`

Contiene los resultados del alineamiento múltiple realizado con Clustal Omega.

- [`clustalo-I20261124-060142-0113-60514728-p1m.aln-clustal_num`](clustal/clustalo-I20261124-060142-0113-60514728-p1m.aln-clustal_num): alineamiento completo de los nueve organismos en formato CLUSTAL con numeración de posiciones.
- [`clustalo-I20261124-060142-0113-60514728-p1m.fa`](clustal/clustalo-I20261124-060142-0113-60514728-p1m.fa): el mismo alineamiento completo en formato FASTA, utilizado como entrada para IQ-TREE.

## `iqtree3/`

Contiene el árbol enraizado en FigTree y los archivos generados por las corridas locales de IQ-TREE.

- [`tree.nwk`](iqtree3/tree.nwk): árbol exportado desde FigTree después de enraizarlo con *Rhizobium sp.* como grupo externo.

### `iqtree3/model_selection/`

Contiene los resultados de la corrida que seleccionó el modelo de sustitución.

- [`iqtree3_local.bionj`](iqtree3/model_selection/iqtree3_local.bionj): árbol inicial calculado mediante el método BioNJ.
- [`iqtree3_local.ckp.gz`](iqtree3/model_selection/iqtree3_local.ckp.gz): checkpoint comprimido con el estado del análisis, útil para reanudar la corrida.
- [`iqtree3_local.contree`](iqtree3/model_selection/iqtree3_local.contree): árbol consenso calculado a partir de las réplicas de bootstrap.
- [`iqtree3_local.iqtree`](iqtree3/model_selection/iqtree3_local.iqtree): reporte con el modelo seleccionado, los resultados y el árbol inferido.
- [`iqtree3_local.log`](iqtree3/model_selection/iqtree3_local.log): registro de los mensajes y pasos de esta corrida.
- [`iqtree3_local.mldist`](iqtree3/model_selection/iqtree3_local.mldist): matriz de distancias estimadas por máxima verosimilitud entre las secuencias.
- [`iqtree3_local.model.gz`](iqtree3/model_selection/iqtree3_local.model.gz): archivo comprimido con resultados internos de la evaluación de modelos.
- [`iqtree3_local.splits.nex`](iqtree3/model_selection/iqtree3_local.splits.nex): archivo NEXUS con los soportes de las ramas calculados en esta corrida.
- [`iqtree3_local.treefile`](iqtree3/model_selection/iqtree3_local.treefile): árbol de máxima verosimilitud con los soportes de las ramas.

### `iqtree3/outgroup_run/`

Contiene los resultados de la corrida de IQ-TREE que usó *Rhizobium sp.* como grupo externo.

- [`iqtree3_local_rooted.bionj`](iqtree3/outgroup_run/iqtree3_local_rooted.bionj): árbol inicial calculado mediante el método BioNJ.
- [`iqtree3_local_rooted.ckp.gz`](iqtree3/outgroup_run/iqtree3_local_rooted.ckp.gz): checkpoint comprimido con el estado del análisis, útil para reanudar la corrida.
- [`iqtree3_local_rooted.contree`](iqtree3/outgroup_run/iqtree3_local_rooted.contree): árbol consenso calculado a partir de las réplicas de bootstrap.
- [`iqtree3_local_rooted.iqtree`](iqtree3/outgroup_run/iqtree3_local_rooted.iqtree): reporte con los resultados y los valores de soporte de las ramas.
- [`iqtree3_local_rooted.log`](iqtree3/outgroup_run/iqtree3_local_rooted.log): registro de los mensajes y pasos de esta corrida.
- [`iqtree3_local_rooted.mldist`](iqtree3/outgroup_run/iqtree3_local_rooted.mldist): matriz de distancias estimadas por máxima verosimilitud entre las secuencias.
- [`iqtree3_local_rooted.splits.nex`](iqtree3/outgroup_run/iqtree3_local_rooted.splits.nex): archivo NEXUS con los soportes de las ramas calculados en esta corrida.
- [`iqtree3_local_rooted.treefile`](iqtree3/outgroup_run/iqtree3_local_rooted.treefile): árbol de máxima verosimilitud con los soportes de las ramas y *Rhizobium sp.* indicado como grupo externo.

## Este índice

- [`README.md`](README.md): este archivo, que resume el contenido de `data/` y sus subcarpetas.
