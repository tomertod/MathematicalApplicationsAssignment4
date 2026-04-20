# Fill in your details
full_name1 = "Tomer Todria"           # Fill full name of 1st student here
student_ID1 = "318784709"               # Fill ID of 1st student here

full_name2 = "Assaf Katz"        # Fill full name of 2nd student here
student_ID2 = "323841338"               # Fill ID of 2nd student here




import math
from sympy import symbols, sin, ln, diff, lambdify, Symbol, integrate

# 1. Taylor Series Approximation 
def taylor_series_ln_sinx(x0, n, x):
    """
    Compute the Taylor polynomial of ln(1 + sin(x)) of order n around point x0.

    Args:
        x0 (float): Reference point.
        n (int): Order of the Taylor series.
        x (float): Point at which to evaluate the polynomial.

    Returns:
        float: Approximation of ln(1 + sin(x)) using the Taylor series.
    """
    x_sym = symbols('x')
    f_expr = ln(1 + sin(x_sym))
    total = 0

    for k in range(n + 1):
        f_k_deriv = diff(f_expr, x_sym, k)
        f_k_func = lambdify(x_sym, f_k_deriv, 'math')
        term = f_k_func(x0) * ((x - x0) ** k) / math.factorial(k)
        total += term

    return total



# 2a.Legendre Polynomials
def legendre_polynomial(n, x):
    """
    Compute the Legendre polynomial of degree n at point x.

    Args:
        n (int): Degree of the polynomial.
        x (float): Point at which to evaluate the polynomial.

    Returns:
        float: Value of the Legendre polynomial at x.
    """
    if n == 0:
        return 1
    elif n == 1:
        return x

    prev2 = 1
    prev1 = x

    for k in range(2, n + 1):
        curr = ((2 * k - 1) * x * prev1 - (k - 1) * prev2) / k
        prev2, prev1 = prev1, curr

    return prev1

# 2.b Legendre Approximation
def approximate_ln_sinx_with_legendre(n, x, x0):
    """
    Approximate ln(1 + sin(x)) using Legendre polynomials.

    Args:
        n (int): Number of terms in the approximation.
        x (float): Point at which to evaluate the approximation.
        x0 (float): Reference point.

    Returns:
        float: Approximation of ln(1 + sin(x)) using Legendre polynomials.
    """

    def compute_lambda(j):
        x_sym = Symbol('x')
        f_expr = ln(1 + sin(x_sym))
        P_j = legendre_polynomial(j, x_sym)
        integral = integrate(f_expr * P_j, (x_sym, -1, 1))
        integral_val = float(integral.evalf())
        return ((2 * j + 1) / 2) * integral_val

    approx = 0
    for i in range(n + 1):
        lam = compute_lambda(i)
        P_i_at_x = legendre_polynomial(i, x - x0)
        approx += lam * P_i_at_x

    return approx

if __name__ == "__main__":
    print (f"This work is the work of:\n{full_name1} &  {full_name1}({student_ID1}, {student_ID2})")

    # Example usage for Taylor series
    x0_taylor = 0
    n_taylor = 2
    x_value = 1
    taylor_result = taylor_series_ln_sinx(x0_taylor, n_taylor, x_value)
    print(f"Taylor series approximation: {taylor_result}")

    # Example usage for Legendre polynomial approximation
    n_legendre = 3
    x0_legendre = 0
    legendre_result = approximate_ln_sinx_with_legendre(n_legendre, x_value, x0_legendre)
    print(f"Legendre polynomial approximation: {legendre_result}")
    


