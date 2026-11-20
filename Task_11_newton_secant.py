from scipy.optimize import root_scalar

cash_flows = [-10000, 3000, 3500, 4000, 2500]

def npv(rate):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(-t * cf / (1 + rate) ** (t + 1)
               for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
print("BASE CASE")
print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant: {secant.root:.6%}")
print(f"NPV at Newton solution: {npv(newton.root):.8f}")

# Changed input: increase the final cash inflow
changed_flows = cash_flows.copy()
changed_flows[-1] = 3500
def changed_npv(rate):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(changed_flows))
changed = root_scalar(changed_npv, x0=0.1, x1=0.2, method="secant")
print("\nCHANGED CASE: final cash inflow increased from 2500 to 3500")
print(f"New estimated IRR: {changed.root:.6%}")

# Related case: calculate the discount rate for a solar equipment investment
solar_flows = [-15000, 5000, 5500, 6000, 6500]
def solar_npv(rate):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(solar_flows))
solar_irr = root_scalar(solar_npv, x0=0.1, x1=0.3, method="secant")
print("\nRELATED CASE: solar equipment investment IRR:", f"{solar_irr.root:.4%}")
