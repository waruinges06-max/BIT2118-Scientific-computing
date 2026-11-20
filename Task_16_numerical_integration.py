import numpy as np
from scipy.integrate import simpson

time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
trap = np.trapezoid(power_kw, time_hours)
simp = simpson(power_kw, x=time_hours)
print("BASE CASE")
print(f"Trapezoidal energy: {trap:.3f} kWh")
print(f"Simpson energy: {simp:.3f} kWh")
print(f"Difference: {abs(simp-trap):.3f} kWh")

# Changed input: increase each power reading by 10 percent
higher_power = power_kw * 1.10
print("\nCHANGED CASE: power readings increased by 10%")
print(f"New trapezoidal energy: {np.trapezoid(higher_power, time_hours):.3f} kWh")
print(f"New Simpson energy: {simpson(higher_power, x=time_hours):.3f} kWh")

# Related case: integrate water flow rate in litres per minute over time
minutes = np.array([0, 10, 20, 30, 40], dtype=float)
flow_lpm = np.array([5, 6, 8, 7, 5], dtype=float)
volume_litres = np.trapezoid(flow_lpm, minutes)
print("\nRELATED CASE: water volume collected:", volume_litres, "litres")
