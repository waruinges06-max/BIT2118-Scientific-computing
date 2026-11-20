import numpy as np
from scipy.optimize import root

def equations(z):
    x, y = z
    return [x**2 + y**2 - 4, y - (x**2 - 1)]

print("BASE CASE: circle x^2+y^2=4 and parabola y=x^2-1")
for guess in ([1., 1.], [-1., 1.]):
    result = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection:", np.round(result.x, 6))
    print("Residuals:", np.round(equations(result.x), 10))
    print("Converged:", result.success)

# Changed parameter: use a circle with radius 2.5 instead of 2
def changed_equations(z):
    x, y = z
    return [x**2 + y**2 - 2.5**2, y - (x**2 - 1)]
changed = root(changed_equations, [1., 1.])
print("\nCHANGED CASE: circle radius increased to 2.5")
print("One intersection:", np.round(changed.x, 6))

# Related case: intersection of a circular irrigation boundary and a ground profile
def irrigation(z):
    x, y = z
    return [x**2 + y**2 - 9, y - 0.5*x]
irrigation_result = root(irrigation, [2., 1.])
print("\nRELATED CASE: irrigation boundary/profile intersection:", np.round(irrigation_result.x, 5))
