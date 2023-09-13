import numpy as np
import matplotlib.pyplot as plt

# Generate a range of frequencies
start_frequency = 1e6
end_frequency = 1e10
step_frequency = 1e9  # Adjust this step size as needed
frequencies = np.arange(start_frequency, end_frequency, step_frequency)

# Corresponding electric permittivity values (example)
permittivity_values = np.array([4.5, 4.2, 4.0, 3.8, 3.5, 3.2, 2.9, 2.6, 2.3, 2.0])

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(frequencies, permittivity_values, marker='o', linestyle='-')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Electric Permittivity (ε)')
plt.title('Electric Permittivity vs. Frequency')
plt.grid(True)
plt.show()

