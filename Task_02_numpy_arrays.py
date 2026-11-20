import numpy as np

# 24 hourly weather-station readings in degrees Celsius
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

print("BASE CASE")
print(f"Mean: {np.mean(temperatures_c):.2f} C")
print(f"Minimum: {np.min(temperatures_c):.2f} C")
print(f"Maximum: {np.max(temperatures_c):.2f} C")
temperatures_f = 1.8 * temperatures_c + 32
print("First six Fahrenheit readings:", np.round(temperatures_f[:6], 2))

# Changed input: replace the 13:00 reading with a hotter value
changed = temperatures_c.copy()
changed[13] = 35.0
print("\nCHANGED CASE (13:00 reading changed to 35 C)")
print(f"New mean: {np.mean(changed):.2f} C")
print(f"New maximum: {np.max(changed):.2f} C")

# Related case: water-quality sensor readings, summarize pH values
ph_readings = np.array([6.8, 7.0, 7.1, 6.9, 7.2, 7.0])
print("\nRELATED CASE: water-quality pH")
print(f"Average pH: {ph_readings.mean():.2f}")
print(f"Minimum/maximum pH: {ph_readings.min():.2f}/{ph_readings.max():.2f}")
