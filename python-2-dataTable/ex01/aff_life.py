import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load
import pandas as pd


def aff_life(data: pd.DataFrame, country: str):
    years = data.columns
    values = data.loc[country]

    fig, ax = plt.subplots()
    ax.plot(years, values, marker="o")

    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))

    ax.set_title(f"{country} Life Expectancy Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Life Expectancy")
    plt.show()


if __name__ == "__main__":
    data = load("life_expectancy_years.csv")
    aff_life(data, country="Morocco")
