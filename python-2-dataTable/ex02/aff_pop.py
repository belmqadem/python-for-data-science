
from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd


def convert_population(value):
    """
    Converts a population string with suffixes (K, M, B) to a float.
    """
    value = str(value).strip().upper()

    if value.endswith('K'):
        return float(value[:-1]) * 1_000
    elif value.endswith('M'):
        return float(value[:-1]) * 1_000_000
    elif value.endswith('B'):
        return float(value[:-1]) * 1_000_000_000
    return float(value)


def aff_pop(data: pd.DataFrame, first_country: str, other_country: str):
    """
    Plots the population of two countries over the years.
    """
    if first_country not in data.index or other_country not in data.index:
        print("Error: One or both countries are not in the dataset.")
        return

    data = data.map(convert_population)

    years = [int(year) for year in data.columns
             if 1800 <= int(year) <= 2050]

    first_country_values = \
        data.loc[first_country, [str(year) for year in years]]
    other_country_values = \
        data.loc[other_country, [str(year) for year in years]]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(years, first_country_values, label=first_country,
            linewidth=2, markersize=1)
    ax.plot(years, other_country_values, label=other_country,
            linewidth=2, markersize=1)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20_000_000))
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, pos: f'{x / 1_000_000:.0f}M')
    )

    ax.set_title("Population Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    ax.legend()

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    data = load("population_total.csv")
    aff_pop(data, first_country="Morocco", other_country="Spain")
