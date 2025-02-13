import numpy as np
import matplotlib.pyplot as plt

# Number of trials
num_trials = 10**5

# Simulating die rolls
die_rolls = np.random.randint(1, 7, num_trials)

# Event D: Number less than 4
D = (die_rolls < 4)

# Event E: Even number greater than 4
E = ((die_rolls > 4) & (die_rolls % 2 == 0))

# Event D - E (Elements in D but not in E)
D_E = D & ~E

# Probabilities
P_D = np.mean(D)
P_E = np.mean(E)
P_D_E = np.mean(D_E)

# Plotting
labels = ['P(D)', 'P(E)', 'P(D - E)']
values = [P_D, P_E, P_D_E]
annotations = ['1/2', '1/6', '1/2']

plt.bar(labels, values, color=['blue', 'red', 'green'], width=0.1)
plt.ylim(0, 1)
plt.ylabel('Probability')
plt.title('Simulated Probabilities of events D,E and D-E')

# Annotating bars
for i, (label, value) in enumerate(zip(labels, values)):
    plt.text(i, value + 0.02, annotations[i], ha='center', fontsize=12)

plt.show()

