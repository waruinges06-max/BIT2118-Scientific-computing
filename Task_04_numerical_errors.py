import numpy as np

calculated = 0.1 + 0.2
expected = 0.3
print("BASE CASE")
print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance comparison:", np.isclose(calculated, expected))

true_value = np.sqrt(2)
approx_value = 1.414
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

print("\nNumerically unstable and stable expressions")
for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")

# Changed parameter: tighter approximation to sqrt(2)
better_approx = 1.41421356
print("\nCHANGED CASE: improved approximation")
print("New absolute error:", abs(true_value - better_approx))

# Related case: check whether two financial totals agree within one cent
invoice_total = 1250.30
payment_total = 1250.30 + 1e-10
print("\nRELATED CASE: financial reconciliation")
print("Totals agree within one cent:", np.isclose(invoice_total, payment_total, atol=0.01))
