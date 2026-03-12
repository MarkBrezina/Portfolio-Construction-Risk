
def risk_parity_weights(vol):

    inv_vol = 1 / vol

    w = inv_vol / inv_vol.sum()

    return w
