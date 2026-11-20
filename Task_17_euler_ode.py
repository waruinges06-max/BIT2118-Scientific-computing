import numpy as np
import matplotlib.pyplot as plt

ambient = 25.0
initial = 90.0
k = 0.12
h = 1.0
end_time = 30.0

def cooling_rate(T):
    return -k * (T - ambient)

time = np.arange(0, end_time+h, h)
temperature = np.zeros_like(time)
temperature[0] = initial
for i in range(len(time)-1):
    temperature[i+1] = temperature[i] + h * cooling_rate(temperature[i])
exact = ambient + (initial-ambient)*np.exp(-k*time)

print("BASE CASE")
print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1]-exact[-1]):.4f} C")

# Changed parameter: reduce step size from 1 minute to 0.5 minute
h2 = 0.5
t2 = np.arange(0, end_time+h2, h2)
T2 = np.zeros_like(t2); T2[0] = initial
for i in range(len(t2)-1):
    T2[i+1] = T2[i] + h2*cooling_rate(T2[i])
print("\nCHANGED CASE: step size reduced to 0.5 minute")
print(f"Euler final temperature: {T2[-1]:.3f} C")
print(f"Absolute error: {abs(T2[-1]-exact[-1]):.5f} C")

plt.plot(time, temperature, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)"); plt.ylabel("Temperature (C)")
plt.title("Cooling of a hot object"); plt.legend(); plt.grid(True); plt.tight_layout()
plt.savefig("results/Task_17_cooling.png")
plt.show()

# Related case: model cooling of a cup of tea under a different starting temperature
tea_initial = 80.0
tea_final = ambient + (tea_initial-ambient)*np.exp(-k*20)
print("\nRELATED CASE: tea temperature after 20 minutes:", round(tea_final, 2), "C")
