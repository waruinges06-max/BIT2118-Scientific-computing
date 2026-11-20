import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

Vs = 5.0
R = 1000.0
C = 0.001
V0 = 0.0

def rc_circuit(t, V):
    return [(Vs - V[0]) / (R*C)]

t_eval = np.linspace(0, 5, 200)
solution = solve_ivp(rc_circuit, (0, 5), [V0], t_eval=t_eval, rtol=1e-9, atol=1e-11)
exact = Vs * (1 - np.exp(-solution.t/(R*C)))
print("BASE CASE")
print("Solver success:", solution.success)
print(f"Voltage at 5 s: {solution.y[0, -1]:.4f} V")
print(f"Maximum error: {np.max(np.abs(solution.y[0]-exact)):.3e} V")

# Changed parameter: double capacitance, which increases charging time
C2 = 0.002
def slower_rc(t, V):
    return [(Vs - V[0])/(R*C2)]
slower = solve_ivp(slower_rc, (0, 5), [V0], t_eval=[5])
print("\nCHANGED CASE: capacitance doubled to 0.002 F")
print(f"Voltage after 5 s: {slower.y[0, -1]:.4f} V")

plt.plot(solution.t, solution.y[0], label="solve_ivp")
plt.plot(solution.t, exact, "--", label="Exact")
plt.xlabel("Time (s)"); plt.ylabel("Capacitor voltage (V)")
plt.title("RC circuit charging"); plt.legend(); plt.grid(True); plt.tight_layout()
plt.savefig("results/Task_18_rc_circuit.png")
plt.show()

# Related case: battery-powered sensor capacitor with a 3 V supply
def sensor_rc(t, V):
    return [(3.0 - V[0])/(2000*0.001)]
sensor = solve_ivp(sensor_rc, (0, 5), [0.0], t_eval=[5])
print("\nRELATED CASE: sensor circuit voltage after 5 s:", round(sensor.y[0, -1], 4), "V")
