from Price_distribution import plot_weibull_distribution
from Expected_revenue import plot_expected_revenue
from Bid_Ask_Model import optimize_expected_revenue

if __name__ == "__main__":
    plot_weibull_distribution()
    plot_expected_revenue()
    optimize_expected_revenue()
    print("✅ Análisis completado.")