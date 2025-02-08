import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
#
# Parámetros de la distribución Weibull
lambda_ = 50  # Escala
k = 10  # Forma
P0 = 51  # Precio de referencia

# Calcular la desviación estándar de la distribución Weibull
sigma = weibull_min.std(k, scale=lambda_)

# Valores óptimos de K_A y K_B bajo el supuesto de traders motivados por liquidez
K_A = P0 + sigma
K_B = P0 - sigma

# Calcular el Expected Revenue
expected_revenue = 0.5 * (K_A - K_B)

# Generar valores de la distribución
x = np.linspace(0, 100, 1000)  # Rango de valores
pdf = weibull_min.pdf(x, k, scale=lambda_)

# Graficar la distribución y los valores óptimos
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f'Weibull(λ={lambda_}, K={k})', color='blue')
plt.axvline(P0, color='red', linestyle='--', label=f'P0 = {P0}')
plt.axvline(K_A, color='green', linestyle='--', label=f'K_A = {K_A:.2f}')
plt.axvline(K_B, color='purple', linestyle='--', label=f'K_B = {K_B:.2f}')
plt.xlabel('Precio (P)')
plt.ylabel('Densidad de Probabilidad')
plt.title('Distribución Weibull y valores óptimos de K_A y K_B')
plt.legend()
plt.grid()
plt.show()

# Imprimir resultados
print(f'K_A: {K_A:.2f}')
print(f'K_B: {K_B:.2f}')
print(f'Expected Revenue: {expected_revenue:.2f}')