# BIT 2118: SCIENTIFIC COMPUTING – GROUP WORK
## Tasks 2–20

This report follows the assignment requirements: identify inputs and mathematical operations, change at least one input or parameter and explain the effect, explain outputs and interpret graphs where applicable, and modify each program for a related real-world case. The code files are in the `code` folder.

## Task 2 – NumPy Arrays and Numerical Computation
**Concept and problem.** A NumPy array stores the 24 hourly temperature readings from a weather station. Array operations calculate descriptive statistics and convert every Celsius value to Fahrenheit.

**Inputs and operations.** The input is 24 temperature values in °C. `np.mean`, `np.min` and `np.max` calculate the average, lowest and highest readings. The vectorized conversion is F = 1.8C + 32.

**Parameter change and effect.** The 14:00 reading is changed to 35°C. The daily maximum increases to 35°C and the daily mean also increases because one observation is higher. The other readings remain unchanged.

**Output interpretation.** The mean describes the general daily temperature, while the minimum and maximum show the coldest and hottest readings. Fahrenheit values are the same measurements expressed in another unit.

**Related case.** The program also summarizes water-quality pH readings. Its assumptions are that the sensor readings are valid pH values from one sampling period. The output gives the average and range, helping an operator identify whether readings vary substantially.

## Task 3 – Mathematical Functions and Vectorization
**Concept and problem.** Vectorization applies one mathematical expression to an entire array rather than processing each value with a Python loop. The scenario processes one million network-latency observations.

**Inputs and operations.** A seeded random generator creates one million latency values between 5 and 250 milliseconds. Each value is divided by 1,000 to convert milliseconds to seconds, then squared. `timeit` compares loop and vectorized execution.

**Parameter change and effect.** The comparison is repeated conceptually on the first 100,000 values. A smaller data set contains fewer operations and should require less processing time. The mean squared latency is also calculated for this subset.

**Output interpretation.** The first values show the transformed measurements. The timing results show how long each implementation takes on the current computer; the speed-up is the loop time divided by vectorized time. Actual timings vary by machine.

**Related case.** A second calculation converts file sizes from MB to GB by dividing by 1,024. It assumes binary units and returns the converted sizes as an array.

## Task 4 – Floating-Point Arithmetic and Numerical Errors
**Concept and problem.** Floating-point numbers are stored with finite binary precision. Consequently, some decimal fractions cannot be represented exactly.

**Inputs and operations.** The program evaluates 0.1 + 0.2, compares it with 0.3, uses `np.isclose`, and calculates absolute and relative errors for an approximation to √2. It also compares a cancellation-prone expression with an algebraically stable equivalent.

**Parameter change and effect.** The approximation 1.414 is replaced by 1.41421356. The absolute error becomes much smaller because the new value is closer to √2.

**Output interpretation.** Exact equality may be false even when two values are practically equal. A tolerance-based comparison is more appropriate for numerical calculations. The stable expression avoids subtracting two nearly equal numbers and therefore reduces loss of significant digits.

**Related case.** The program checks whether an invoice and payment total agree within one cent. The assumption is that a one-cent tolerance is acceptable for this reconciliation. The Boolean result indicates whether the difference falls within that tolerance.

## Task 5 – Matrix Algebra and Matrix Operations
**Concept and problem.** Matrices organize coordinates and transformations. Matrix multiplication combines scaling and rotation into one transformation.

**Inputs and operations.** Four two-dimensional points represent the corners of a square. A 45-degree rotation matrix and a scaling matrix are multiplied. The points are transformed using matrix multiplication. The determinant indicates the area-scaling factor for the transformation.

**Parameter change and effect.** The rotation angle is changed from 45 degrees to 90 degrees. The points rotate further around the origin, while the scale factors remain the same.

**Output interpretation.** The transformed coordinates show the new positions of the square's corners. A non-zero determinant means the transformation is invertible; its absolute value indicates the area scale factor.

**Related case.** The program converts local map coordinates into a larger grid coordinate system using scaling and translation. It assumes a fixed scale and known grid offset. The output gives transformed coordinates suitable for a simplified mapping example.

## Task 6 – Solution of Systems of Linear Equations
**Concept and problem.** A system Ax = b represents simultaneous linear relationships. The unknowns are the number of active Type A and Type B servers.

**Inputs and operations.** Type A uses 4 CPU units and 8 GB memory; Type B uses 2 CPU units and 12 GB memory. The observed totals are 20 CPU units and 72 GB memory. `np.linalg.solve` finds the two unknowns and `A @ solution` verifies the result.

**Parameter change and effect.** Total CPU usage is changed from 20 to 24 while memory remains 72 GB. The estimated server mix changes to satisfy the new pair of totals.

**Output interpretation.** The solution gives the calculated number of each server type. The verification should reproduce the supplied totals and the residual should be close to zero. In a real deployment, server counts should be whole numbers; this model assumes the measurements are consistent with the two-equation system.

**Related case.** Two products consume machine hours and raw material. The same linear-system approach estimates the number of batches of each product from available resource totals.

## Task 7 – Gaussian Elimination and LU Decomposition
**Concept and problem.** Gaussian elimination reduces a linear system to triangular form. LU decomposition factors a coefficient matrix so the factors can be reused when the right-hand-side vector changes.

**Inputs and operations.** A 3×3 coefficient matrix and three measurement vectors are supplied. `lu_factor` factors the matrix once and `lu_solve` solves each system. Residual norms check the accuracy.

**Parameter change and effect.** A new measurement vector [20, 12, 8] is supplied. The same LU factors are reused, so a new solution is obtained without factoring the matrix again.

**Output interpretation.** Each solution is the set of unknown values consistent with its measurement vector. A residual norm close to zero indicates that the solution satisfies the original equations closely.

**Related case.** A small mixing process uses a fixed coefficient matrix and changing ingredient totals. The factors are reused for each new mixture requirement.

## Task 8 – Iterative Methods for Linear Systems
**Concept and problem.** Jacobi and Gauss-Seidel repeatedly improve an initial estimate of a solution. They are useful for large sparse systems. The example represents steady-state temperatures at five interior grid points.

**Inputs and operations.** The matrix A represents neighboring-point relationships, while b represents boundary influence from 100°C on the left and 20°C on the right. Both methods iterate until the maximum change is below tolerance or the iteration limit is reached. A direct NumPy solution is used for comparison.

**Parameter change and effect.** The Jacobi tolerance is tightened from 10⁻⁸ to 10⁻¹⁰. A stricter tolerance generally requires additional iterations and produces a more tightly converged result.

**Output interpretation and graph.** The printed arrays are the estimated temperatures. The convergence graph plots maximum change against iteration on a logarithmic vertical axis. A decreasing curve indicates convergence. The method with the faster decrease reaches the tolerance in fewer iterations for this example.

**Related case.** The boundary values are changed to 80°C and 10°C to represent a short pipe section. The calculated vector estimates the temperature distribution along that section.

## Task 9 – Eigenvalues and Eigenvectors
**Concept and problem.** An eigenvector of A keeps its direction after multiplication by A; its eigenvalue gives the scale factor. The dominant eigenvector of an adjacency matrix can be used as a network-importance measure.

**Inputs and operations.** A four-node undirected network is represented by a 4×4 adjacency matrix. NumPy calculates eigenvalues and eigenvectors. The eigenvector belonging to the largest real eigenvalue is converted to non-negative normalized scores.

**Parameter change and effect.** A connection is added between nodes A and D. This changes the adjacency matrix and can change the dominant eigenvector scores, because the pattern of connections has changed.

**Output interpretation.** A larger normalized score indicates a node that is connected to other influential nodes. The verification error checks the eigenvector equation Av = λv.

**Related case.** A three-junction road network is represented by another adjacency matrix. The resulting scores provide a simple structural importance ranking of the junctions.

## Task 10 – Root Finding: Bisection and Fixed-Point Methods
**Concept and problem.** A root is a value where a function equals zero. Bisection repeatedly halves a bracket containing a sign change. Fixed-point iteration repeatedly evaluates a rearranged equation T = g(T).

**Inputs and operations.** The heat-balance function is f(T) = T − 25 − 10 exp(−T/20). Bisection uses the interval [20, 40]. Fixed-point iteration begins at 30°C and stops when successive estimates differ by less than 10⁻¹⁰.

**Parameter change and effect.** The baseline term is raised from 25 to 28. The equilibrium root moves to a higher temperature because the balance equation now includes a higher baseline.

**Output interpretation and graph.** The root is the temperature at which the heat-balance function crosses zero. The plotted horizontal zero line and vertical root marker identify the equilibrium point. Agreement between bisection and fixed-point results supports the calculation.

**Related case.** A similar balance equation is used to estimate a machine's operating equilibrium temperature. The assumed coefficients represent a simplified machine heat model.

## Task 11 – Root Finding: Newton-Raphson and Secant Methods
**Concept and problem.** Newton-Raphson uses a derivative to update an estimate; the secant method estimates the derivative from two points. Both are used to find the rate at which net present value is zero.

**Inputs and operations.** The cash flows are −10,000, 3,000, 3,500, 4,000 and 2,500. NPV discounts each cash flow by (1+r)^t. Newton-Raphson uses the derivative of NPV; the secant method uses two initial guesses.

**Parameter change and effect.** The final cash inflow increases from 2,500 to 3,500. A larger future inflow generally raises the investment's internal rate of return, since a higher discount rate is needed to reduce NPV back to zero.

**Output interpretation.** The IRR is the rate that makes NPV approximately zero. The NPV printed at the Newton solution should be very close to zero. The two methods should produce closely matching roots when they converge to the same root.

**Related case.** A second cash-flow series represents a solar-equipment investment. The secant method estimates its IRR using the same NPV definition.

## Task 12 – Polynomial and Nonlinear Equation Solving
**Concept and problem.** A nonlinear solver searches for values that make a set of residual equations close to zero. The example finds intersections of a circle and a parabola.

**Inputs and operations.** The equations are x² + y² − 4 = 0 and y − (x² − 1) = 0. `scipy.optimize.root` is run from two initial guesses. Residual values and convergence status are printed.

**Parameter change and effect.** The circle radius is increased from 2 to 2.5. The intersection coordinates change because the circle boundary is larger.

**Output interpretation.** Each returned pair (x, y) is an estimated intersection. Residuals close to zero mean both equations are satisfied closely. Different initial guesses can lead to different intersections.

**Related case.** A circular irrigation boundary is intersected with a simplified sloping ground profile. The assumptions are a circular boundary of radius 3 and a straight profile y = 0.5x.

## Task 13 – Interpolation
**Concept and problem.** Interpolation estimates values between known measurements. Linear interpolation joins adjacent readings with straight lines; cubic splines use smooth cubic segments.

**Inputs and operations.** Hourly temperatures from 08:00 to 14:00 are supplied. `interp1d` builds the linear interpolator and `CubicSpline` builds the spline. Both estimate values every ten minutes and at 10:30.

**Parameter change and effect.** The 12:00 temperature is changed from 25°C to 28°C. Estimates in the neighboring interval are affected because interpolation uses the supplied measurement points.

**Output interpretation and graph.** The dots show recorded hourly measurements. The two lines show the estimates between readings. The linear result has straight segments; the cubic result is smoother. Interpolation estimates within the measured time range and should not be confused with reliable extrapolation beyond it.

**Related case.** Water level readings are supplied every two hours and the program estimates the level at hour 3. It assumes the level changes smoothly between the measurements.

## Task 14 – Curve Fitting and Approximation
**Concept and problem.** Curve fitting selects model parameters that minimize the difference between measured values and model predictions. The example models server response time as a quadratic function of concurrent users.

**Inputs and operations.** Seven user-load values and their measured response times are supplied. `curve_fit` estimates coefficients a, b and c in y = ax² + bx + c. RMSE summarizes the typical fitting error.

**Parameter change and effect.** An additional observation of 390 ms at 400 users is added. The fitted coefficients and predictions change because the fitting process now includes the extra observation.

**Output interpretation and graph.** Points are the measured response times and the curve is the fitted model. A rising curve indicates that response time grows with load. RMSE closer to zero indicates a closer fit to the supplied observations. Predictions beyond the measured range are less certain.

**Related case.** A linear model is fitted between population and daily water demand. The slope estimates the additional demand associated with one more person under the assumed trend.

## Task 15 – Numerical Differentiation
**Concept and problem.** A derivative measures a rate of change. Finite differences estimate derivatives from sampled values. Central differences use a point on each side and are often more accurate than a one-sided difference.

**Inputs and operations.** GPS time samples and vehicle positions are supplied. Forward difference is used at the first sample, central differences at interior samples, and backward difference at the final sample.

**Parameter change and effect.** The final position is changed from 38 m to 42 m. The final backward-difference speed increases because the distance covered in the last one-second interval is larger.

**Output interpretation and graph.** The printed speed values estimate the vehicle's speed at each sample time. The graph shows how speed changes over the observation period. Differentiation can amplify measurement noise, so GPS estimates may fluctuate.

**Related case.** The program estimates the rate at which water level changes from a sequence of level readings. The output is in centimetres per hour.

## Task 16 – Numerical Integration
**Concept and problem.** Integration estimates accumulated quantities, such as electrical energy from power over time. The trapezoidal rule approximates areas using trapezoids; Simpson's rule uses parabolic segments.

**Inputs and operations.** Power readings in kW are recorded every two hours. Time is in hours. Integrating kW over hours gives kWh. NumPy's trapezoidal rule and SciPy's Simpson rule are compared.

**Parameter change and effect.** Every power reading is increased by 10%. Since integration is linear in the measured power, both energy estimates increase by approximately 10%.

**Output interpretation.** The two printed values are estimates of energy consumed over the 12-hour interval. Their difference shows how much the numerical methods disagree for the supplied measurements.

**Related case.** Flow rate in litres per minute is integrated over minutes to estimate the volume of water collected. The result is in litres.

## Task 17 – Ordinary Differential Equations: Euler Method
**Concept and problem.** An ordinary differential equation describes how a quantity changes with time. Euler's method advances the solution using the current rate of change and a selected step size.

**Inputs and operations.** Newton's cooling law is dT/dt = −k(T − Tambient). The initial temperature is 90°C, ambient temperature is 25°C, k is 0.12 per minute, and the time step is one minute. The numerical result is compared with the exact solution.

**Parameter change and effect.** The time step is reduced from 1 minute to 0.5 minute. Smaller steps generally reduce Euler's discretization error, although they require more calculations.

**Output interpretation and graph.** Temperature decreases toward ambient temperature. The Euler curve should follow the exact curve; the gap between them represents numerical error. The final error is printed.

**Related case.** A cup of tea starts at 80°C and cools under the same simplified ambient temperature and cooling coefficient. The program estimates its temperature after 20 minutes.

## Task 18 – Numerical Solution of ODEs Using SciPy
**Concept and problem.** `solve_ivp` numerically solves an initial-value problem using an adaptive numerical method. The example models voltage across a charging capacitor in an RC circuit.

**Inputs and operations.** Supply voltage is 5 V, resistance is 1,000 ohms, capacitance is 0.001 F and initial voltage is zero. The differential equation is dV/dt = (Vs − V)/(RC). The numerical result is compared with the exact charging curve.

**Parameter change and effect.** Capacitance is doubled to 0.002 F. The time constant RC becomes larger, so the capacitor charges more slowly and its voltage after five seconds is lower.

**Output interpretation and graph.** Voltage rises toward the supply voltage. The numerical and exact curves should nearly overlap. The printed maximum error measures their difference.

**Related case.** A sensor circuit with a 3 V supply, 2,000-ohm resistor and 0.001 F capacitor is simulated. The output is its estimated voltage after five seconds.

## Task 19 – Numerical Optimization
**Concept and problem.** Optimization finds values that minimize or maximize an objective while respecting constraints. The example minimizes server operating cost subject to a minimum processing capacity.

**Inputs and operations.** Type A costs 12 units and provides 100 capacity units; Type B costs 18 and provides 170. The minimum capacity is 1,000. SLSQP minimizes total cost with non-negative bounds and an inequality constraint. A separate search checks whole-number allocations.

**Parameter change and effect.** Required capacity increases from 1,000 to 1,200. The allocation must provide more capacity, so the minimum cost cannot decrease and will normally increase.

**Output interpretation.** The continuous solution may contain fractional server units because the optimizer treats the variables as continuous. The integer search is more realistic where only whole servers can be purchased. Capacity must meet or exceed the required amount.

**Related case.** The same mathematical structure can plan generator capacity: minimize operating cost while meeting a minimum output requirement. The cost and capacity coefficients would be replaced with generator-specific data.

## Task 20 – Random Numbers and Monte Carlo Methods
**Concept and problem.** Monte Carlo simulation estimates probabilities by generating many random scenarios and measuring how often an event occurs.

**Inputs and operations.** Server demand is sampled from a normal distribution with mean 850, standard deviation 120 and 100,000 simulations. Capacity is 1,000. The overload probability is the fraction of simulated demands above capacity.

**Parameter change and effect.** Mean demand increases from 850 to 900 while capacity and standard deviation remain fixed. A greater proportion of scenarios is expected to exceed capacity, so the estimated overload probability increases.

**Output interpretation and graph.** The probability is an estimate based on the simulated sample, not an exact guarantee. The convergence graph shows the running estimate as the number of simulations increases. It should generally settle around a stable value as more trials are performed.

**Related case.** A reservoir-risk example simulates daily water demand and estimates the probability that demand exceeds a storage capacity of 1,100 units. The assumed demand is normally distributed with mean 920 and standard deviation 100.

## General conclusion
The tasks demonstrate how Python libraries support numerical computation, linear algebra, root finding, interpolation, differentiation, integration, differential equations, optimization and simulation. Numerical outputs depend on the quality of input data, assumptions, parameter choices and numerical tolerances. Graphs help communicate trends, convergence and model fit, but they should always be interpreted alongside the underlying assumptions.
