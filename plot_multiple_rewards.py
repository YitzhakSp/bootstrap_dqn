import json
import matplotlib.pyplot as plt
import numpy as np

files=['simulations/no_advice/avg_rewards.npy',
        'simulations/advice/unlimited/avg_rewards.npy'
       ]
for f in files:
    x = np.load(f)
    plt.plot(x)
plt.savefig('rewards.png')