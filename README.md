# A Universal Entropy Bridge Between QCD and Gravity — Paper 6

**Author:** Johann Anton Michael Tupay  
**Affiliation:** Independent Researcher, London, United Kingdom  
**Date:** August 2025

## Overview
This repository contains the LaTeX source, figures, tables, and final PDF for:

> **A Universal Entropy Bridge Between QCD and Gravity: Linking the 9.81 k_B Constant to Black Hole Thermodynamics**

The paper establishes a closed-form relation between the universal QCD renormalization-group entropy ceiling per baryon (ΔS_RG ≈ 9.81 k_B) and the Bekenstein–Hawking entropy of black holes of the same mass, expressed entirely in terms of fundamental constants with no astrophysical inputs.

## Contents
- `main.tex` — LaTeX manuscript (REVTeX 4.2, APS PRD style)
- `main.pdf` — final compiled paper
- `figures/` — all figures used in the paper
- `tables/` — LaTeX and CSV data tables
- `scripts/` — replication code (Python)
  - `generate_table.py`
  - `generate_ratio_plot.py`
  - `bh_catalog_validation.py`

## Quick Start (reproduce figures/tables)
From the repo root, create the expected folders (if not present):
```bash
mkdir -p paper/figures paper/tables data
```

Then run the scripts from `scripts/`:
```bash
python3 scripts/generate_table.py
python3 scripts/generate_ratio_plot.py
python3 scripts/bh_catalog_validation.py
```

Outputs will be written to:
- `data/eos_variation.csv`
- `paper/tables/eos_variation.tex`
- `paper/figures/ratio_plot.png`
- `paper/figures/bh_catalog_validation.png`

> Note: These filenames and paths match those referenced in the paper.

## How to Compile
```bash
pdflatex main.tex
bibtex main    # only if using BibTeX
pdflatex main.tex
pdflatex main.tex
```

## PDF
The final compiled PDF is `main.pdf` in this repository.

## Citation
If you use this work, please cite it as described in `CITATION.cff`.

## License
This work is released under the MIT License (see `LICENSE`).
