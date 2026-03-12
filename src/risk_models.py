
import numpy as np

def covariance_matrix(returns):
    return returns.cov()

def portfolio_volatility(weights, cov):

    return np.sqrt(
        weights.T @ cov @ weights
    )
