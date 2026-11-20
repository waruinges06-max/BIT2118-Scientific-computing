import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000
demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
probability = overloaded.mean()
print("BASE CASE")
print(f"Estimated overload probability: {probability:.4%}")
print(f"Overload cases: {overloaded.sum()} out of {N}")

# Changed parameter: increase average demand to 900
demand2 = rng.normal(900.0, std_demand, N)
probability2 = (demand2 > capacity).mean()
print("\nCHANGED CASE: mean demand increased from 850 to 900")
print(f"New overload probability: {probability2:.4%}")

running = np.cumsum(overloaded) / np.arange(1, N+1)
indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int))-1
plt.semilogx(indices+1, running[indices])
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.grid(True); plt.tight_layout()
plt.savefig("results/Task_20_monte_carlo.png")
plt.show()

# Related case: estimate risk that daily water demand exceeds reservoir capacity
water_demand = rng.normal(920, 100, N)
water_risk = (water_demand > 1100).mean()
print("\nRELATED CASE: reservoir overload probability:", f"{water_risk:.4%}")
