from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def format_income(value):
    """
    Formats the income value for display on the x-axis.
    """
    if value >= 1_000:
        return f'{int(value / 1_000)}k'
    return str(value)


def project_life(life_data: pd.DataFrame, income_data: pd.DataFrame):
    """
    Projects the life expectancy of the year 1900 for each country
    based on income data.
    """
    selected_year = '1900'
    common_countries = life_data.index.intersection(income_data.index)

    combined = pd.DataFrame({
        'income': income_data.loc[common_countries, selected_year],
        'life': life_data.loc[common_countries, selected_year]
    }).dropna()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(combined['income'], combined['life'], alpha=0.7)
    ax.set_title(selected_year)
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life Expectancy")
    ax.set_xscale("log")
    formater = plt.FuncFormatter(lambda x, _: format_income(x))
    ax.xaxis.set_major_formatter(formater)
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    life_data = load("life_expectancy_years.csv")
    income_data = \
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    project_life(life_data, income_data)
