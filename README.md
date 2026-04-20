# Mathematical Applications - Assignment 4
## Functional Approximation: Taylor Series & Legendre Polynomials

### Submitting Students:
* **Tomer Todria** - 318784709
* **Asaf Katz** - 323841338

---

### Project Description
This assignment explores two advanced methods for approximating complex functions: **Taylor Series Expansion** and **Legendre Polynomials**. The project demonstrates how to approximate the function $f(x) = \ln(1 + \sin x)$ using calculus-based and orthogonal polynomial techniques.

---

### Implementation Details

#### Part 1: Taylor Series Approximation
The function `taylor_series_ln_sinx` computes the Taylor polynomial of order $n$ around a reference point $x_0$.
* **Logic:** The approximation is built by calculating the $k$-th derivative of the function, evaluating it at $x_0$, and constructing the power series:
  $T_f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k$
* **Tools:** Utilizes the `sympy` library for symbolic differentiation and `lambdify` for efficient numerical evaluation.

#### Part 2: Legendre Polynomials & Approximation
This part involves a more sophisticated approximation using orthogonal polynomials over the interval $[-1, 1]$.

* **Legendre Polynomials:** Implemented via the recursive formula:
  $P_n(x) = \frac{(2n-1)x P_{n-1}(x) - (n-1)P_{n-2}(x)}{n}$
* **Coefficients ($\lambda_i$):** Each coefficient is calculated using a definite integral:
  $\lambda_j = \frac{2j+1}{2} \int_{-1}^{1} f(x) \cdot P_j(x) dx$
* **Final Approximation:** The function is reconstructed as a weighted sum of Legendre polynomials, providing a robust approximation often superior to Taylor series over a specific interval.

---

### Technologies Used
* **Python 3.x**
* **SymPy:** For symbolic mathematics (derivatives and integrals).
* **Math Library:** For factorial calculations and basic constants.

---

### How to Run
1. Ensure you have the necessary libraries installed:
   ```
   pip install sympy
   ```
2. Run The Script:
   ```
   python aas4_318784709_323841338.py
   ```
### Important Notes:
1. The code follows the strict requirement of using the provided skeleton and specific function signatures.
2. Integration is performed numerically using ``` sympy.integrate ``` to ensure precision in calculating Legendre coefficients.

