import numpy as np

# x = Type A servers, y = Type B servers
# CPU: 4x + 2y = 20; memory: 8x + 12y = 72
A = np.array([[4., 2.], [8., 12.]])
b = np.array([20., 72.])
solution = np.linalg.solve(A, b)
print("BASE CASE")
print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification:", A @ solution)
print("Residual:", b - A @ solution)

# Changed input: increase total CPU usage from 20 to 24 units
b_changed = np.array([24., 72.])
changed = np.linalg.solve(A, b_changed)
print("\nCHANGED CASE: CPU total increased to 24")
print(f"Type A: {changed[0]:.2f}; Type B: {changed[1]:.2f}")

# Related case: two products consume machine hours and raw material
# x = product X batches, y = product Y batches
A2 = np.array([[2., 1.], [1., 3.]])
b2 = np.array([10., 12.])
print("\nRELATED CASE: production planning")
print("Product X and Y batches:", np.linalg.solve(A2, b2))
