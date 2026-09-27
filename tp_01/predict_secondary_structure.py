#!/usr/bin/env python3
"""
predict_secondary_structure.py
Challenge V: Simple secondary structure prediction of proteins (H, B, L).
"""

import argparse
import os

# Conformational propensities based on amino acid preferences:
# H: Alpha helix (favored by Glu, Ala, Leu, Met, Gln, Lys, Arg)
# B: Beta sheet (favored by Val, Ile, Tyr, Phe, Trp, Thr, Cys)
# L: Loop / Coil (favored by Gly, Pro, Asn, Asp, Ser, His)
PROPENSITIES: dict[str, str] = {
    'E': 'H', 'A': 'H', 'L': 'H', 'M': 'H', 'Q': 'H', 'K': 'H', 'R': 'H',
    'V': 'B', 'I': 'B', 'Y': 'B', 'F': 'B', 'W': 'B', 'T': 'B', 'C': 'B',
    'G': 'L', 'P': 'L', 'N': 'L', 'D': 'L', 'S': 'L', 'H': 'L'
}

def normalize_sequence(sequence: str) -> str:
    """Cleans whitespace and converts the sequence to uppercase."""
    return "".join(sequence.upper().split())

def load_sequence_from_file(file_path: str) -> str:
    """Reads the sequence content from a plain text file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def predict_secondary_structure(sequence: str) -> str:
    """
    Predicts secondary structure conformation (H, B, L) for each amino acid.
    Unrecognized or non-standard residues are flagged as '?'.
    """
    clean_sequence = normalize_sequence(sequence)
    return "".join(PROPENSITIES.get(aa, '?') for aa in clean_sequence)

def count_conformations(predicted_structure: str) -> dict[str, int]:
    """Calculates frequency of each secondary structure conformation."""
    return {c: predicted_structure.count(c) for c in ('H', 'B', 'L', '?')}

def display_composition(predicted_structure: str) -> None:
    """Displays formatted statistics of the structural composition in Spanish."""
    total = len(predicted_structure)
    print("-" * 60)
    print("Composición estimada:")
    if total == 0:
        print("  Secuencia vacía (sin residuos para predecir).")
        print("=" * 60)
        return

    labels: dict[str, str] = {
        'H': 'Hélice (H)',
        'B': 'Hoja Beta (B)',
        'L': 'Bucle (L)',
        '?': 'No reconocido (?)'
    }
    counts = count_conformations(predicted_structure)

    for conformation in ('H', 'B', 'L'):
        count = counts[conformation]
        pct = (count / total) * 100
        print(f"  - {labels[conformation]:18s}: {count:3d} ({pct:5.1f}%)")

    unknown_count = counts['?']
    if unknown_count > 0:
        pct = (unknown_count / total) * 100
        print(f"  - {labels['?']:18s}: {unknown_count:3d} ({pct:5.1f}%)")

    print("=" * 60)

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Predice la estructura secundaria (H: Hélice, B: Hoja Beta, L: Loop) de una secuencia de aminoácidos."
    )
    parser.add_argument(
        "entrada",
        help="Secuencia proteica directa o ruta a un archivo de texto plano."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Muestra estadísticas de composición estructural."
    )

    args = parser.parse_args()
    raw_input: str = str(args.entrada)

    if ("." in raw_input or "/" in raw_input) and not os.path.isfile(raw_input):
        print(f"Error: No se encontró el archivo '{raw_input}'.")
        return

    if os.path.isfile(raw_input):
        raw_sequence = load_sequence_from_file(raw_input)
    else:
        raw_sequence = raw_input

    sequence = normalize_sequence(raw_sequence)
    if not sequence:
        print("Secuencia vacía (sin residuos para predecir).")
        return

    predicted_structure = predict_secondary_structure(sequence)

    print("=" * 60)
    print(" PREDICCIÓN DE ESTRUCTURA SECUNDARIA")
    print("=" * 60)
    print(f"Longitud de secuencia: {len(sequence)} residuos\n")
    print(f"Secuencia:  {sequence}")
    print(f"Estructura: {predicted_structure}\n")

    if args.verbose:
        display_composition(predicted_structure)

if __name__ == "__main__":
    main()
