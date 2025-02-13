import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Parámetros Globales
lambda_ = 50
k = 10
P0 = 51

def weibull_pdf(S):
    return weibull_min.pdf(S, k, scale=lambda_)

def plot_weibull_distribution():
    x = np.linspace(0, 100, 1000)
    pdf = weibull_pdf(x)
    plt.figure(figsize=(8, 5))
    plt.plot(x, pdf, label=f'Weibull(λ={lambda_}, K={k})', color='blue')
    plt.axvline(P0, color='red', linestyle='--', label=f'P0 = {P0}')
    plt.xlabel('Precio (P)')
    plt.ylabel('Densidad de Probabilidad')
    plt.title('Distribución Weibull del Precio')
    plt.legend()
    plt.grid()
    plt.show()