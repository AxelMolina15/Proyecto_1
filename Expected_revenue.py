import numpy as np
from scipy.stats import weibull_min
from scipy.optimize import minimize
from scipy.integrate import quad


def optimize_revenue(lambda_, k, P0, p_I=0.4):
    def weibull_pdf(S):
        return weibull_min.pdf(S, k, scale=lambda_)

    def expected_revenue(params):
        K_A, K_B = params
        S_KA = K_A - P0
        S_KB = P0 - K_B
        PLB = np.clip(0.5 - 0.08 * S_KA, 0, 0.5)
        PLS = np.clip(0.5 - 0.08 * S_KB, 0, 0.5)
        int_KA = quad(lambda s: weibull_pdf(s) * (s - P0), K_A, np.inf)[0]
        int_KB = quad(lambda s: weibull_pdf(s) * (P0 - s), 0, K_B)[0]
        term1 = (1 - p_I) * ((K_A - P0) * PLB + PLS * (P0 - K_B))
        term2 = p_I * (int_KA + int_KB)
        return -(term1 - term2)

    bounds = [(P0, None), (0, P0)]
    initial_guess = [P0 + 2, P0 - 2]
    result = minimize(expected_revenue, initial_guess, bounds=bounds)
    K_A_opt, K_B_opt = result.x
    max_revenue = -result.fun

    return K_A_opt, K_B_opt, max_revenue