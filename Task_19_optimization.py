import numpy as np
from scipy.optimize import minimize

# x and y are server capacity units; costs are per unit
def cost(z):
    x, y = z
    return 12*x + 18*y

def capacity_constraint(z):
    x, y = z
    return 100*x + 170*y - 1000

solution = minimize(cost, x0=[5, 3], method="SLSQP",
                    bounds=[(0, None), (0, None)],
                    constraints={"type": "ineq", "fun": capacity_constraint})
x, y = solution.x
print("BASE CASE")
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x+170*y:.2f}")
print(f"Planning cost: {solution.fun:.2f}")

# Changed parameter: increase required capacity from 1000 to 1200
def higher_capacity(z):
    return 100*z[0] + 170*z[1] - 1200
changed = minimize(cost, x0=[5, 4], method="SLSQP",
                   bounds=[(0, None), (0, None)],
                   constraints={"type": "ineq", "fun": higher_capacity})
print("\nCHANGED CASE: required capacity raised to 1200")
print("Allocation:", np.round(changed.x, 3), "cost:", round(changed.fun, 2))

# Whole-server check for original requirement
best = None
for a in range(21):
    for b in range(21):
        capacity = 100*a + 170*b
        if capacity >= 1000:
            total = 12*a + 18*b
            if best is None or total < best[0]:
                best = (total, a, b, capacity)
print("Best integer solution (cost, A, B, capacity):", best)

# Related case: choose low-cost generators to meet a minimum output requirement
# Same optimization structure, interpreted as generator capacity planning.
print("\nRELATED CASE: generator planning uses the same cost/capacity model.")
