# Proyecto_1
# Analyzing Information Impact on the Bid-Ask Spread

This project investigates how information asymmetry affects the bid-ask spread in financial markets. Drawing inspiration from Bagehot's foundational work (*"The Only Game in Town"*) and Copeland & Galai's model (*"Information Effects on the Bid-Ask Spread"*), we aim to showcase that bid-ask spreads can persist even without transaction costs. By delving into these theoretical models, our objective is to optimize the market maker's profit function concerning bid and ask pricing. This analysis offers valuable insights into the dynamics influencing the bid-ask spread and enhances our understanding of market maker strategies in various trading environments.

## Project Guidelines

1. **Modeling Stock Prices with a Weibull Distribution:**
   - **Distribution:** $P \sim \text{Weibull}(\lambda = 50, k = 10)$
   - **Current Stock Price:** $51$

2. **Probability of Engaging with an Informed Trader:**
   - **Probability:** $\Pi_I = 0.4$
   - **Interpretation:** Represents a 40% chance that any given trade is informed, reflecting typical market conditions.

3. **Buy Limit Probability ($\Pi_{LB}$) as a Function of Price Deviation ($S$):**
   - **Formula:** $\Pi_{LB}(S) = 0.5 - 0.08S$
   - **Constraints:** $\Pi_{LB} \in [0, 0.5]$
   - **Explanation:** This defines the probability of placing a buy limit order based on the price deviation, where $S = (A - S_0)$, $A$ is the adjusted stock price, and $S_0$ represents the initial stock price.

4. **Sell Limit Probability ($\Pi_{LS}$) as a Function of Price Deviation ($S$):**
   - **Formula:** $\Pi_{LS}(S) = 0.5 - 0.08S$
   - **Constraints:** $\Pi_{LS} \in [0, 0.5]$
   - **Explanation:** This determines the probability of placing a sell limit order, with $S = (S_0 - B)$, where $S_0$ is the initial stock price and $B$ is the bid price.

## Key Deliverables

**Visualization 1:**
- Illustrate the stock price distribution using the Weibull model.

**Visualization 2:**
- Analyze expected revenue under different trading conditions:
  - When all trades are liquidity-driven.
  - When there is a 40% chance of an informed trade, maintaining the same liquidity trade probabilities.
  - Considering the probabilities of informed trading along with buy ($\Pi_{LB}$) and sell ($\Pi_{LS}$) limit order probabilities.

**Visualization 3:**
- Identify the optimal bid and ask prices based on the Copeland & Galai model, aiming to maximize the market maker's expected profits.

This project not only provides a quantitative exploration of bid-ask spread dynamics but also bridges theoretical concepts with practical trading strategies.
