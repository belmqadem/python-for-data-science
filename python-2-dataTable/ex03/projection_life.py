from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def project_life(life_data: pd.DataFrame, income_data: pd.DataFrame):
    """
    Projects the life expectancy of the year 1900 for each country
    based on income data.
    """
    selected_year = '1900'

    income_values = income_data[selected_year]
    life_values = life_data[selected_year]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(income_values, life_values, alpha=0.7)
    ax.set_title(selected_year)
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life Expectancy")
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    life_data = load("life_expectancy_years.csv")
    income_data = \
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    project_life(life_data, income_data)
