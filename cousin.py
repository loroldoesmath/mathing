import sympy
import matplotlib.pyplot as plt

def count_cousin_primes_up_to(n):
    """Counts the number of cousin primes less than or equal to `n`."""
    cousin_prime_count = 0
    
    for p in range(2, n):
        if sympy.isprime(p) and sympy.isprime(p + 4):
            cousin_prime_count += 1
    
    return cousin_prime_count

def calculate_asymptotic_density(limit):
    """Calculates the asymptotic density of cousin primes up to the given limit."""
    n_values = list(range(2, limit + 1))  # Numbers from 2 to `limit`
    densities = []
    cousin_prime_count = 0
    
    for n in n_values:
        cousin_prime_count = count_cousin_primes_up_to(n)  # Count cousin primes up to `n`
        density = cousin_prime_count / n  # Calculate the density
        densities.append(density)
    
    return n_values, densities

def plot_asymptotic_density(limit):
    """Plots the asymptotic density of cousin primes up to `limit`."""
    n_values, densities = calculate_asymptotic_density(limit)
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, densities, 'g-', label="Asymptotic Density of Cousin Primes")
    plt.xlabel("n (Upper limit)")
    plt.ylabel("Asymptotic Density")
    plt.title("Asymptotic Density of Cousin Primes up to 1000")
    plt.grid(True)
    plt.legend()
    plt.show()

# Plot the asymptotic density of cousin primes up to 1000
plot_asymptotic_density(1000)
