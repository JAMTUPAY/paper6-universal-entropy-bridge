[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16849019.svg)](https://doi.org/10.5281/zenodo.16849019)

# A Universal Entropy Bridge Between QCD and Gravity — Paper 6

**Author:** Johann Anton Michael Tupay  
**Affiliation:** Independent Researcher, London, United Kingdom  
**Date:** August 2025

---

## 📄 Paper Access
- [**Final PDF**](paper/main.pdf)  
- [**LaTeX Source**](paper/main.tex)

---

## Overview
This repository contains the LaTeX source, figures, tables, and replication code for:

> **A Universal Entropy Bridge Between QCD and Gravity: Linking the 9.81 k<sub>B</sub> Constant to Black Hole Thermodynamics**

The paper establishes a closed-form relation between the universal QCD renormalization-group entropy ceiling per baryon (ΔS<sub>RG</sub> ≈ 9.81 k<sub>B</sub>) and the Bekenstein–Hawking entropy of black holes of the same mass, expressed entirely in terms of fundamental constants with no astrophysical inputs.

---

## Repository Structure
```
paper6-universal-entropy-bridge/
│
├── paper/
│   ├── main.tex              # LaTeX manuscript
│   ├── main.pdf              # Final compiled PDF
│   ├── figures/              # Figures used in the paper
│   ├── tables/               # Tables used in the paper
│
├── scripts/                  # Replication scripts
│   ├── generate_table.py
│   ├── generate_ratio_plot.py
│   ├── bh_catalog_validation.py
│
├── data/                     # Generated CSVs or intermediate outputs
│
├── README.md
├── CITATION.cff
├── LICENSE
```

---

## Replication Instructions
Create required directories (if not already present):
```bash
mkdir -p paper/figures paper/tables data
```

Run the replication scripts:
```bash
python3 scripts/generate_table.py
python3 scripts/generate_ratio_plot.py
python3 scripts/bh_catalog_validation.py
```

Outputs will be saved to:
- `data/eos_variation.csv`
- `paper/tables/eos_variation.tex`
- `paper/figures/ratio_plot.png`
- `paper/figures/bh_catalog_validation.png`

These outputs match exactly those referenced in the paper.

---

## How to Compile the Paper
```bash
cd paper
pdflatex main.tex
bibtex main      # only if using BibTeX
pdflatex main.tex
pdflatex main.tex
```

---

## License
This work is licensed under the [MIT License](LICENSE).

---

## Citation
If you use this work, please cite it as described in [`CITATION.cff`](CITATION.cff) or via the DOI badge above.
