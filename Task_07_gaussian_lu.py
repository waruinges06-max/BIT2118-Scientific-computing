import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
measurement_sets = [
    np.array([15., 10., 10.]),
    np.array([16., 11., 9.]),
    np.array([14., 12., 11.])
]
lu, piv = lu_factor(A)
print("BASE CASE: factor A once and reuse it")
for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    print(f"Set {i} solution:", np.round(x, 4))
    print("Residual norm:", np.linalg.norm(b - A @ x))

# Changed input: new measurement vector
new_b = np.array([20., 12., 8.])
print("\nCHANGED CASE: new sensor measurements")
print("Solution:", np.round(lu_solve((lu, piv), new_b), 4))

# Related case: repeated balance calculations in a small mixing process
mix_A = np.array([[3., 1.], [1., 2.]])
mix_lu = lu_factor(mix_A)
for amounts in ([10., 8.], [12., 7.]):
    print("\nRELATED CASE: mixture proportions", np.round(lu_solve(mix_lu, np.array(amounts)), 4))
