import pandas as pd
from sympy import primefactors, factorint

def count_prime_factors(n):
    factors = factorint(n) # prime factorization
    return sum(factors.values()) # sum of the counts of prime factors