# generate_table.py
import numpy as np
import os

# Constants
kB = 1.380649e-23
msun_kg = 1.98847e30
m_p = 1.67262192369e-27
delta_s_rg = 9.81  # kB per baryon

# EOS models and (M, R) in M_sun and km
eos_models = {
    "APR":   [(1.4, 11.5), (2.0, 10.9), (2.2, 10.7)],
    "SLy":   [(1.4, 11.7), (2.0, 11.0), (2.2, 10.8)],
    "BSk21": [(1.4, 12.6), (2.0, 11.8), (2.2, 11.6)],
    "GM1":   [(1.4, 13.8), (2.0, 12.5), (2.2, 12.2)]
}

# Create output dirs
os.makedirs("../data", exist_ok=True)
os.makedirs("../paper/tables", exist_ok=True)

# CSV output
with open("../data/eos_variation.csv", "w") as f:
    f.write("EOS,Mass(Msun),Radius(km),S_QCD(J/K)\n")
    for eos, entries in eos_models.items():
        for m, r in entries:
            m_kg = m * msun_kg
            n_baryons = m_kg / m_p
            S_qcd = delta_s_rg * n_baryons * kB
            f.write(f"{eos},{m},{r},{S_qcd:.6e}\n")

# LaTeX table output
with open("../paper/tables/eos_variation.tex", "w") as f:
    f.write("\\centering
\begin{tabular}{lccc}\n\\hline\n")
    f.write("EOS & $M$ ($M_\\odot$) & $R$ (km) & $S_{QCD}$ (J/K) \\\\\n\\hline\n")
    for eos, entries in eos_models.items():
        for m, r in entries:
            m_kg = m * msun_kg
            n_baryons = m_kg / m_p
            S_qcd = delta_s_rg * n_baryons * kB
            f.write(f"{eos} & {m:.2f} & {r:.2f} & ${S_qcd:.2e}$ \\\\\n")
    f.write("\\hline\n\\end{tabular}\n")
