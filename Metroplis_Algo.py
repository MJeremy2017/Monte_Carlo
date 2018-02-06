import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

REPS = 200000


def cauchy(x, x0=0, gamma=1):
    return 1./(np.pi*gamma*(1+np.square((x-x0)/gamma)))


def metropolis(reps):
    np.random.seed(1)
    chain = []
    chain.append(0)

    for i in range(reps):
        proposal_point = chain[i] + np.random.normal(0, .5)
        u = np.random.rand()
        if u < cauchy(proposal_point) / cauchy(chain[i]):
            chain.append(proposal_point)
        else:
            chain.append(chain[i])
    return chain


x = np.linspace(-4, 4, 1000)
plt.plot(x, cauchy(x), label='actual')

chain = metropolis(reps=REPS)
density = stats.gaussian_kde(chain[100000:])
plt.plot(x, density(x), label='MH-sampling', linestyle='--')
plt.legend(loc='best')


