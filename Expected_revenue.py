import numpy as np
import matplotlib.pyplot as plt

# Parámetros
pi_I = 0.4
P0 = 51

def plot_expected_revenue():
    prices = np.linspace(P0, P0 + 10, 100)
    q_values = prices - P0
    r_values = q_values * (1 - pi_I)
    pli_values = np.clip(0.5 - 0.08 * (prices - P0), 0, 0.5)
    v_values = r_values * pli_values

    plt.figure(figsize=(8, 6))
    plt.plot(prices, q_values, linestyle='--', color='black', label="Q: Revenue si todos son de liquidez")
    plt.plot(prices, r_values, linestyle='-', color='blue', label="R: Revenue con 40% informados")
    plt.plot(prices, v_values, linestyle='-', color='green', label="V: Expected Revenue con PBL")
    plt.xlabel("Precio (P)")
    plt.ylabel("Revenue Esperado")
    plt.title("Expected Revenue en función del Precio")
    plt.legend()
    plt.grid()
    plt.show()
