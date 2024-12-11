import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sympy import primefactors
def num_prime_factors(a,b):
    # prep data: list of numbers and their prime factors
    numbers = range(a, b)  # Example range of numbers
    data = {
        "Number": [],
        "Prime Factor": []
    }

    for num in numbers:
    factors = primefactors(num)
    for factor in factors:
        data["Number"].append(num)
        data["Prime Factor"].append(factor)

    # data to a DataFrame
    df = pd.DataFrame(data)

    # set Seaborn style
    sns.set_theme(style="whitegrid")

    # plot
    plt.figure(figsize=(12, 8))
    plot = sns.stripplot(
        data=df,
        x="Number",
        y="Prime Factor",
        hue="Prime Factor",
        palette="viridis",
        dodge=True,
        size=10,
        alpha=0.8
    )

    plot.set_title("Number of Prime Factors", fontsize=16, weight="bold")
    plot.set_xlabel("Number", fontsize=12)
    plot.set_ylabel("Prime Factors", fontsize=12)
    plt.legend(title="Prime Factor", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
    sns.despine()

    plt.tight_layout()
    plt.show()