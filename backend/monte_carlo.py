import numpy as np


def accumulate(
    years: int,
    contribution: float,
    stock_weight: float,
    bond_weight: float,
    sims: int = 2000
):
    stock_mu, stock_sigma = 0.085, 0.19
    bond_mu, bond_sigma = 0.025, 0.09

    paths = np.zeros((sims, years))

    for s in range(sims):
        wealth = 0.0
        for t in range(years):
            r_stock = np.random.normal(stock_mu, stock_sigma)
            r_bond = np.random.normal(bond_mu, bond_sigma)
            r_port = stock_weight * r_stock + bond_weight * r_bond

            wealth = (wealth + contribution) * (1 + r_port)
            paths[s, t] = max(wealth, 0)

    return paths


def decumulate(
    starting_wealth: float,
    years: int,
    withdrawal: float,
    stock_weight: float,
    bond_weight: float,
    sims: int = 2000
):
    stock_mu, stock_sigma = 0.085, 0.19
    bond_mu, bond_sigma = 0.025, 0.09

    paths = np.zeros((sims, years))
    ruined = 0

    for s in range(sims):
        wealth = starting_wealth
        for t in range(years):
            r_stock = np.random.normal(stock_mu, stock_sigma)
            r_bond = np.random.normal(bond_mu, bond_sigma)
            r_port = stock_weight * r_stock + bond_weight * r_bond

            wealth = wealth * (1 + r_port) - withdrawal
            wealth = max(wealth, 0)
            paths[s, t] = wealth

            if wealth == 0:
                ruined += 1
                break

    failure_probability = ruined / sims
    return paths, failure_probability
