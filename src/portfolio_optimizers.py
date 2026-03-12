
import numpy as np

def min_variance_portfolio(cov):

    inv = np.linalg.inv(cov)

    ones = np.ones(len(cov))

    w = inv @ ones / (ones.T @ inv @ ones)

    return w
