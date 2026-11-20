import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)

solution = root_scalar(heat_balance, bracket=[20, 40], method="bisect", xtol=1e-10)

def g(T):
    return 25 + 10 * np.exp(-T / 20)

T = 30.0
history = [T]
for _ in range(100):
    new_T = g(T)
    history.append(new_T)
    if abs(new_T - T) < 1e-10:
        break
    T = new_T

print("BASE CASE")
print(f"Bisection equilibrium: {solution.root:.6f} C")
print(f"Fixed-point equilibrium: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history) - 1)

# Changed parameter: ambient baseline rises from 25 to 28 degrees
def changed_balance(T):
    return T - 28 - 10 * np.exp(-T / 20)
changed = root_scalar(changed_balance, bracket=[20, 45], method="bisect")
print("\nCHANGED CASE: baseline temperature increased to 28 C")
print(f"New equilibrium: {changed.root:.6f} C")

temps = np.linspace(20, 45, 300)
plt.plot(temps, heat_balance(temps))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--", label=f"Root = {solution.root:.2f} C")
plt.xlabel("Temperature (C)"); plt.ylabel("Heat-balance function")
plt.title("Equilibrium temperature"); plt.legend(); plt.grid(True); plt.tight_layout()
plt.savefig("results/Task_10_equilibrium.png")
plt.show()

# Related case: determine a machine's operating temperature threshold
def machine_balance(t):
    return t - 30 - 8 * np.exp(-t / 25)
machine_root = root_scalar(machine_balance, bracket=[25, 50], method="bisect")
print("\nRELATED CASE: machine operating equilibrium:", round(machine_root.root, 4), "C")
