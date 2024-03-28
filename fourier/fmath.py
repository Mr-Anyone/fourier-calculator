import numpy as np 
import matplotlib.pyplot as plt

# fourier series coefficient
# A_n = 2/p int p s(x)cos(2pin/px) dx 
# B_n = 2/p int p s(x) sin(2pin/px) dx
# A_o = 1/p int p s(x) dx
def compute_a_zero(y, p):
    integral = (1/2* y[0] + np.sum(y[1:-1]) + 1/2*y[-1]) * p/len(y)

    return 1/p* integral

def calculate_b_sub_n(y, n, p):
    x = np.linspace(0, p, len(y))
    _cos_term = np.sin(2*np.pi*n / p *x)
    integrand = _cos_term * y
    delta_x = p/len(y)
    integral = delta_x * (integrand[0] * 1/2 + np.sum(integrand[1:-1])+ integrand[-1] * 1/2)

    return  integral * 2/p


def calculate_a_sub_n(y, n, p):
    x = np.linspace(0, p, len(y))
    _cos_term = np.cos(2*np.pi*n / p *x)
    integrand = _cos_term * y
    delta_x = p/len(y)
    integral = delta_x * (integrand[0] * 1/2 + np.sum(integrand[1:-1])+ integrand[-1] * 1/2)

    return  integral * 2/p

def get_an_and_bn(x, p, N):
    a_n = []
    b_n = []
    for i in range(1, N + 1):
        a_n.append(calculate_a_sub_n(x, i, p)) 
        b_n.append(calculate_b_sub_n(x, i, p))

    return a_n, b_n, compute_a_zero(x, p)

def compute_one_value_at_x(a_n, b_n, a_o, p, x):
    current_y = a_o
    for j in range(1, len(a_n) + 1):
        current_y += a_n[j - 1] * np.cos(2*np.pi* j / p * x) + b_n[j - 1] * np.sin(2*np.pi* j / p * x)
    
    return current_y
