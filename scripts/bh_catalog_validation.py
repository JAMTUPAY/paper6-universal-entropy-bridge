# bh_catalog_validation.py
import numpy as np
import matplotlib.pyplot as plt

# Constants
kB = 1.380649e-23
G = 6.67430e-11
c = 299792458
lp = 1.616255e-35
msun_kg = 1.98847e30
m_p = 1.67262192369e-27
hbar = 1.054571817e-34
delta_s_rg = 9.81

# K from theory
K = (4 * np.pi * G * m_p) / (hbar * c * delta_s_rg)

# Observed BH masses (M_sun)
bh_masses_msun = [
    6.9, 10.5, 6.55, 10.4, 8.5, 4.9, 7.0, 4.9, 6.6, 5.1,
    7.7, 12.0, 6.95, 12.9, 7.6, 5.31, 5.1, 10.0, 14.8, 10.91,
    7.0, 23.1, 20.0, 15.65
]

# Compute ratios
ratios = []
for m in bh_masses_msun:
    m_kg = m * msun_kg
    r_s = 2 * G * m_kg / c**2
    area = 4 * np.pi * r_s**2
    S_bh = kB * area / (4 * lp**2)
    N_baryons = m_kg / m_p
    S_qcd = delta_s_rg * N_baryons * kB
    ratios.append(S_bh / S_qcd)

masses = np.array(bh_masses_msun)
ratios = np.array(ratios)

# Fit slope in log-log space
log_m = np.log10(masses)
log_r = np.log10(ratios)
slope, intercept = np.polyfit(log_m, log_r, 1)

# Plot
plt.figure(figsize=(8,6))
plt.scatter(masses, ratios, color='red', label='Observed BH binaries')
masses_sorted = np.linspace(masses.min(), masses.max(), 200)
plt.plot(masses_sorted, K * masses_sorted * msun_kg,
         color='blue', label='Theory: K*M')
fit_line = 10**intercept * masses_sorted**slope
plt.plot(masses_sorted, fit_line, '--', color='green',
         label=f'Best-fit slope={slope:.3f}')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel("Black Hole Mass (M$_\\odot$)")
plt.ylabel(r"$S_{BH} / S_{QCD}$")
plt.title("BH/QCD Entropy Ratio for Observed Black Holes")
plt.legend()
plt.grid(True, which="both", ls="--", lw=0.5)
plt.tight_layout()
plt.savefig("../paper/figures/bh_catalog_validation.png", dpi=300)
plt.show()
