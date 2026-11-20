import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)
times = np.arange(8, 14 + 1/6, 1/6)

print("BASE CASE")
print(f"Linear estimate at 10:30: {float(linear(10.5)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(10.5)):.2f} C")

# Changed input: replace the 12:00 sensor reading
changed_temp = temperature.copy()
changed_temp[4] = 28.0
changed_linear = interp1d(hours, changed_temp, kind="linear")
print("\nCHANGED CASE: 12:00 reading changed from 25 to 28 C")
print(f"New linear estimate at 10:30: {float(changed_linear(10.5)):.2f} C")

plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(times, linear(times), label="Linear")
plt.plot(times, cubic(times), label="Cubic spline")
plt.xlabel("Hour of day"); plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation"); plt.legend(); plt.grid(True); plt.tight_layout()
plt.savefig("results/Task_13_interpolation.png")
plt.show()

# Related case: estimate water level between manual readings
water_hours = np.array([0, 2, 4, 6], dtype=float)
water_cm = np.array([40, 44, 51, 55], dtype=float)
water_interp = interp1d(water_hours, water_cm)
print("\nRELATED CASE: estimated water level at hour 3:", float(water_interp(3)), "cm")
