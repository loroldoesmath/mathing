import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sympy import primefactors
from prime_functions import count_prime_factors


def num_prime_factors(a,b):
    # prep data: list of numbers and their prime factors
    numbers = range(a, b)  # range of numbers
    data = {
        "Number": [],
        "Prime Factor Count": []
    }

    for num in numbers:
        prime_factor_count = count_prime_factors(num)
        data["Number"].append(num)
        data["Prime Factor Count"].append(prime_factor_count)

    # data to a DataFrame
    df = pd.DataFrame(data)

    # set Seaborn style
    sns.set_theme(style="whitegrid")

    # plot
    plt.figure(figsize=(12, 8))
    plot = sns.stripplot(
        data=df,
        x="Number",
        y="Prime Factor Count",
        hue="Prime Factor Count",
        palette="viridis",
        dodge=True,
        size=10,
        alpha=0.8,
        jitter = True # avoid overlapping 
    )

    # fix upside down issue
    # plt.gca().invert_yaxis

    plot.set_title("Visualization of Prime Factor Counts", fontsize=16, weight="bold")
    plot.set_xlabel("Number", fontsize=12)
    plot.set_ylabel("Prime Factors", fontsize=12)
    # plt.legend(title="Prime Factor", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
    # sns.despine()

    plt.tight_layout()
    plt.show()

num_prime_factors(2,100)