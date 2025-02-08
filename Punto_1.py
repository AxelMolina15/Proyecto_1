import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
#
# Parámetros de la distribución Weibull
lambda_ = 50  # Escala

k = 10  # Forma
P0 = 51  # Precio de referencia

# Generar valores de la distribución
x = np.linspace(0, 100, 1000)  # Rango de valores
pdf = weibull_min.pdf(x, k, scale=lambda_)

# Graficar la distribución
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f'Weibull(λ={lambda_}, K={k})', color='blue')
plt.axvline(P0, color='red', linestyle='--', label=f'P0 = {P0}')
plt.xlabel('Precio (P)')
plt.ylabel('Densidad de Probabilidad')
plt.title('Distribución Weibull del Precio')
plt.legend()
plt.grid()
plt.show()