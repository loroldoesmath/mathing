import numpy as np
import matplotlib.pyplot as plt
from sympy import isprime

# Function to generate special primes (twin, cousin, sexy primes)
def generate_special_primes(n, gap):
    special_primes = []
    p = 2
    while len(special_primes) < n:
        if isprime(p) and isprime(p + gap):
            special_primes.append(p)
        p += 1
    return special_primes

# Function to compute the prime-counting function π(x)
def prime_count(x):
    primes = [p for p in range(2, x + 1) if isprime(p)]
    return len(primes)

# Function to compute the asymptotic density of primes for twin, cousin, and sexy primes
def asymptotic_density_special_primes(max_x, n_primes):
    x_values = np.arange(2, max_x, 10)  # Range of x values (adjust step size as needed)
    density_values_twin = []
    density_values_cousin = []
    density_values_sexy = []
    
    for x in x_values:
        # Get special primes up to x
        twin_primes = generate_special_primes(n_primes, 2)
        cousin_primes = generate_special_primes(n_primes, 4)
        sexy_primes = generate_special_primes(n_primes, 6)
        
        # Count the number of special primes less than x
        twin_count = sum(1 for p in twin_primes if p <= x)
        cousin_count = sum(1 for p in cousin_primes if p <= x)
        sexy_count = sum(1 for p in sexy_primes if p <= x)
        
        # Compute asymptotic density for each
        density_twin = twin_count / x
        density_cousin = cousin_count / x
        density_sexy = sexy_count / x
        
        density_values_twin.append(density_twin)
        density_values_cousin.append(density_cousin)
        density_values_sexy.append(density_sexy)
    
    return x_values, density_values_twin, density_values_cousin, density_values_sexy

# Plotting the asymptotic density of twin, cousin, and sexy primes
def plot_asymptotic_density_special_primes(max_x=10000, n_primes=100):
    x_values, density_values_twin, density_values_cousin, density_values_sexy = asymptotic_density_special_primes(max_x, n_primes)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, density_values_twin, label='Twin Primes', color='blue')
    plt.plot(x_values, density_values_cousin, label='Cousin Primes', color='green')
    plt.plot(x_values, density_values_sexy, label='Sexy Primes', color='red')
    
    plt.xlabel('x')
    plt.ylabel('Asymptotic Density')
    plt.title('Asymptotic Density of Twin, Cousin, and Sexy Primes')
    plt.grid(True)
    plt.legend()
    plt.show()

# Call the function to plot the asymptotic densities
plot_asymptotic_density_special_primes(10000, n_primes=100)
