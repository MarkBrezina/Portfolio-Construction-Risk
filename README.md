# Portfolio optimisation

**661 different stocks. Run from 9/2/2026 to 6/4/2025, running for 8 weeks.**

## Piece 1 - Background research.
1. Analyse historical data for companies with high average returns and low risk
2. Analyse companies with good budgets and likely good chance for high returns
3. Analyse companies with cyclical behaviour around January to May.
4. Propose a set of trending or mean reverting strategies to implement. It needs to be a day-by-day setup.

## Piece 2 - portfolio optimisation
1. asset + strategy selector
2. Optimiser based on likely downside risk and expected return.
3. Return expected position sizes based on volatility targets

## Piece 3 - Inventory adjustment and risk plays.
1. Capital allocation adjusting for likelihood of returns
2. 25% set aside for event based plays.
3. Analysis of likelihoods of outcome, ...



Covariance/risk models (EWMA/shrinkage), vol targeting, factor exposures, VaR/CVaR, stress & scenario analysis, leverage/liquidity/concentration constraints.
mean-variance optimisation , concentration, covariance, cvar, var optimisation

# Systematic Portfolio Construction

This repository explores methods for constructing diversified portfolios
from multiple assets or trading strategies.

The goal of portfolio construction is to combine investments in a way that
maximizes expected return while controlling risk.

Key topics explored include:

• Risk models  
• Portfolio optimization  
• Strategy allocation  
• Dynamic portfolio rebalancing  

The project implements several classical and modern approaches to portfolio
construction and compares their performance.

---

# Methods Implemented

Mean–Variance Optimization  
Risk Parity  
Minimum Variance Portfolio  
Maximum Diversification Portfolio  
Volatility Targeting  
Strategy Allocation

---

# Example Results

Experiments demonstrate:

• diversification effects  
• volatility stabilization  
• differences between allocation methods  
• behavior during market stress

---

# Repository Structure

docs → theory and notes  \
notebooks → experiments  \
src → reusable portfolio framework  \
results → figures and outputs
