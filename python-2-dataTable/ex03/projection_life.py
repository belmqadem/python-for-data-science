from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



def aff_life(life_data: pd.DataFrame, income_data: pd.DataFrame, country: str, year: int):
		life_expectancy = life_data.loc[country, str(year)]
		income_per_person = income_data.loc[country, str(year)]

		print(f"In {year}, the life expectancy in {country} was {life_expectancy} years, and the income per person was ${income_per_person:.2f}.")

if __name__ == '__main__':
		life_data = load("life_expectancy_years.csv")
		income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
		aff_life(life_data, income_data, country="Morocco", year=1900)

