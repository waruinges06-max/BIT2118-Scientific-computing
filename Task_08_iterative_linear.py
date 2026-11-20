import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2., -1., 0., 0., 0.],
              [-1., 2., -1., 0., 0.],
              [0., -1., 2., -1., 0.],
              [0., 0., -1., 2., -1.],
              [0., 0., 0., -1., 2.]])
b = np.array([100., 0., 0., 0., 20.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        new = (b - R @ x) / D
        error = np.linalg.norm(new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return new, errors
        x = new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

xj, ej = jacobi(A, b)
xg, eg = gauss_seidel(A, b)
print("BASE CASE")
print("Jacobi:", np.round(xj, 6), "iterations:", len(ej))
print("Gauss-Seidel:", np.round(xg, 6), "iterations:", len(eg))
print("Direct solution:", np.linalg.solve(A, b))

# Changed parameter: stricter convergence tolerance
x_strict, e_strict = jacobi(A, b, tol=1e-10)
print("\nCHANGED CASE: Jacobi tolerance 1e-10")
print("Iterations:", len(e_strict), "solution:", np.round(x_strict, 8))

plt.semilogy(ej, label="Jacobi")
plt.semilogy(eg, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence of iterative temperature solution")
plt.legend(); plt.grid(True); plt.tight_layout()
plt.savefig("results/Task_08_convergence.png")
plt.show()

# Related case: estimate temperatures along a short insulated pipe section
pipe_b = np.array([80., 0., 0., 0., 10.])
pipe_solution, _ = gauss_seidel(A, pipe_b)
print("\nRELATED CASE: pipe temperature profile:", np.round(pipe_solution, 3))
