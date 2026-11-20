import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

def model(x, a, b, c):
    return a*x**2 + b*x + c

params, covariance = curve_fit(model, users, response_ms)
a, b, c = params
predicted = model(users, *params)
rmse = np.sqrt(np.mean((response_ms - predicted)**2))
print("BASE CASE")
print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400, *params):.2f} ms")

# Changed input: add a higher-load measurement
users2 = np.append(users, 400.)
response2 = np.append(response_ms, 390.)
params2, _ = curve_fit(model, users2, response2)
print("\nCHANGED CASE: add measurement 400 users, 390 ms")
print(f"New prediction at 450 users: {model(450, *params2):.2f} ms")

xplot = np.linspace(users.min(), 450, 300)
plt.scatter(users, response_ms, label="Measurements")
plt.plot(xplot, model(xplot, *params), label="Quadratic fit")
plt.xlabel("Concurrent users"); plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting"); plt.legend(); plt.grid(True); plt.tight_layout()
plt.savefig("results/Task_14_curve_fitting.png")
plt.show()

# Related case: fit a trend between daily water demand and population
population = np.array([1000, 1500, 2000, 2500, 3000], dtype=float)
demand = np.array([80, 115, 151, 190, 228], dtype=float)
slope, intercept = np.polyfit(population, demand, 1)
print("\nRELATED CASE: water demand model")
print(f"Demand = {slope:.4f}*population + {intercept:.2f}")
print("Predicted demand at 3500 people:", slope*3500 + intercept)
