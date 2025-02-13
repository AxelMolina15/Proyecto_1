from Price_distribution import plot_weibull_distribution
from Bid_Ask_Model import Bid_Ask
from Expected_revenue import optimize_revenue


if __name__ == "__main__":
    plot_weibull_distribution()
    Bid_Ask()
    optimize_revenue(lambda_ = 50, k = 10, P0 = 51)
    # Optimizar ingresos esperados
    K_A_opt, K_B_opt, max_revenue = optimize_revenue(lambda_ = 50, k = 10, P0 = 51)
    print(f'K_A óptimo: {K_A_opt:.2f}')
    print(f'K_B óptimo: {K_B_opt:.2f}')
    print(f'Máximo Expected Revenue: {max_revenue:.2f}')
    print("✅ Análisis completado.")