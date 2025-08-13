# generate_ratio_plot.py
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

# Proportionality constant
K = (4 * np.pi * G * m_p) / (hbar * c * delta_s_rg)

# Example masses
masses_msun = np.linspace(0.5, 2.2, 20)
ratios = K * masses_msun * msun_kg

plt.figure(figsize=(8,6))
plt.plot(masses_msun, ratios, label="Theory: K*M", color='blue')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel("Mass (M$_\\odot$)")
plt.ylabel(r"$S_{BH} / S_{QCD}$")
plt.title("BH/QCD Entropy Ratio Scaling")
plt.legend()
plt.grid(True, which="both", ls="--", lw=0.5)
plt.tight_layout()
plt.savefig("../paper/figures/ratio_plot.png", dpi=300)
plt.show()
