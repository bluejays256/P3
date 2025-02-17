import numpy as np
from scipy.integrate import nquad

# Set a random seed for reproducibility
np.random.seed(42)

# Define the problem size
N = 3  # You can change this to test different dimensions

# Generate a random symmetric positive-definite matrix A
A = np.random.randn(N, N)
A = A.T @ A  # This ensures A is symmetric positive-definite

# Generate a random vector w
w = np.random.randn(N)

# Analytical solution
def analytical(A, w, N):
    A_inv = np.linalg.inv(A)
    det_A_inv = np.linalg.det(A_inv)
    return np.sqrt((2 * np.pi) ** N * det_A_inv) * np.exp(0.5 * w.T @ A_inv @ w)

# Define the function to integrate
def integrand(*v):
    v = np.array(v)
    exponent = -0.5 * v.T @ A @ v + v.T @ w
    return np.exp(exponent)

# Perform numerical integration over all N variables from -∞ to ∞
limits = [(-np.inf, np.inf)] * N
numerical_result, error = nquad(integrand, limits)

# Print results
print(f"Analytical Result: {analytical(A, w, 3)}")
print(f"Numerical Integration Result: {numerical_result} ± {error}")


## Part b ###
w = np.array([[1],[2],[3]])
A = np.array([[4, 2, 1], [2, 5, 3], [1, 3, 6]])
A_prime = np.array([[4, 2, 1], [2, 1, 3], [1, 3, 6]])
numerical_A, error_A = nquad(integrand, limits)

print(f"Analytical result for A: {analytical(A, w, 3)}")
print(f"Analytical result for A':  {analytical(A_prime, w, 3)}")




