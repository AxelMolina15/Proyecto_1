import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
from scipy.optimize import minimize
#
# Parámetros de la distribución Weibull
lambda_ = 50  # Escala
k = 10  # Forma
P0 = 51  # Precio de referencia
p_I = 0.4  # Probabilidad de información

# Función de densidad de la distribución Weibull
def weibull_pdf(S):
    return weibull_min.pdf(S, k, scale=lambda_)

# Función de revenue esperada
def expected_revenue(params):
    K_A, K_B = params

    # Filtrar valores de S para cada integral
    S_KA = S[S >= K_A]  # Valores S >= K_A
    S_KB = S[S <= K_B]  # Valores S <= K_B

    # Calcular integrales con los límites correctos
    int_KA = np.trapz((S_KA - K_A) * weibull_pdf(S_KA), S_KA)
    int_KB = np.trapz((K_B - S_KB) * weibull_pdf(S_KB), S_KB)

    term1 = (1 - p_I) * (0.5 * (K_A - P0) + 0.5 * (P0 - K_B))
    term2 = p_I * (int_KA + int_KB)

    return -(term1 - term2)  # Negativo porque scipy.minimize minimiza por defecto


# Definir límites para la optimización
bounds = [(P0 - 10, P0 + 10), (P0 - 10, P0 + 10)]
S = np.linspace(0, 100, 1000)  # Valores para simular los precios

# Optimización de K_A y K_B
initial_guess = [P0 + 2, P0 - 2]
result = minimize(expected_revenue, initial_guess, bounds=bounds)
K_A_opt, K_B_opt = result.x
max_revenue = -result.fun

# Generar valores de la distribución
x = np.linspace(0, 100, 1000)
pdf = weibull_pdf(x)

# Graficar la distribución y los valores óptimos
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f'Weibull(λ={lambda_}, K={k})', color='blue')
plt.axvline(P0, color='red', linestyle='--', label=f'P0 = {P0}')
plt.axvline(K_A_opt, color='green', linestyle='--', label=f'K_A_opt = {K_A_opt:.2f}')
plt.axvline(K_B_opt, color='purple', linestyle='--', label=f'K_B_opt = {K_B_opt:.2f}')
plt.xlabel('Precio (P)')
plt.ylabel('Densidad de Probabilidad')
plt.title('Distribución Weibull y valores óptimos de K_A y K_B con p_I=0.4')
plt.legend()
plt.grid()
plt.show()

# Imprimir resultados
print(f'K_A óptimo: {K_A_opt:.2f}')
print(f'K_B óptimo: {K_B_opt:.2f}')
print(f'Máximo Expected Revenue: {max_revenue:.2f}')