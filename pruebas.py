import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons
import math


start_epsilon = 0.01
end_epsilon = 10
step_epsilon = 0.05
epsilon = np.arange(start_epsilon, end_epsilon,step_epsilon)
square= np.arange(start_epsilon, end_epsilon,step_epsilon)
# Corresponding electric permittivity values (example)
n=math.sqrt(cons.epsilon_0*cons.mu_0)
square=np.multiply(epsilon,n)


# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(epsilon, square, marker='o', linestyle='-')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Electric Permittivity (ε)')
plt.title('Electric Permittivity vs. Frequency')
plt.grid(True)
plt.show()

