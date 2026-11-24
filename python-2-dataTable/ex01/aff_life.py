import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load
import pandas as pd


def aff_life(data: pd.DataFrame, country: str):
    """
    Plots the life expectancy of a given country over the years.
    """
    if country not in data.index:
        print(f"Error: The country '{country}' is not in the dataset.")
        return

    years = data.columns
    values = data.loc[country]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, values, marker="o", linewidth=2, markersize=1)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))

    ax.set_title(f"{country} Life Expectancy Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Life Expectancy")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    data = load("life_expectancy_years.csv")
    aff_life(data, country="Morocco")
