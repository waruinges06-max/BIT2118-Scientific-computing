import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])
speed = np.zeros_like(position)
speed[0] = (position[1] - position[0]) / (time[1] - time[0])
for i in range(1, len(time)-1):
    speed[i] = (position[i+1] - position[i-1]) / (time[i+1] - time[i-1])
speed[-1] = (position[-1] - position[-2]) / (time[-1] - time[-2])

print("BASE CASE: GPS position and estimated speed")
for t, p, v in zip(time, position, speed):
    print(f"t={t:.0f}s position={p:.1f}m speed={v:.2f}m/s")

# Changed input: alter the last recorded position
changed_position = position.copy()
changed_position[-1] = 42.0
changed_speed = (changed_position[-1] - changed_position[-2]) / (time[-1] - time[-2])
print("\nCHANGED CASE: final GPS position changed from 38 to 42 m")
print("New final speed estimate:", changed_speed, "m/s")

plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)"); plt.ylabel("Estimated speed (m/s)")
plt.title("Speed estimated from GPS position data"); plt.grid(True); plt.tight_layout()
plt.savefig("results/Task_15_speed.png")
plt.show()

# Related case: calculate rate of change in water level
water_time = np.array([0, 2, 4, 6], dtype=float)
water_level = np.array([30, 34, 41, 45], dtype=float)
water_rate = np.gradient(water_level, water_time)
print("\nRELATED CASE: water-level change rate (cm/hour):", water_rate)
