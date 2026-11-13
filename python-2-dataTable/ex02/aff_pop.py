from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

def aff_pop(data: pd.DataFrame, your_country: str, other_country: str):
		years = data.columns
		your_values = data.loc[your_country]
		other_values = data.loc[other_country]

		fig, ax = plt.subplots()
		ax.plot(years, your_values, marker="o", label=your_country)
		ax.plot(years, other_values, marker="o", label=other_country)

		ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
		ax.yaxis.set_major_locator(ticker.MultipleLocator(100))

		ax.set_title(f"Population Comparison: {your_country} vs {other_country}")
		ax.set_xlabel("Year")
		ax.set_ylabel("Population")
		ax.legend()
		plt.show()


if __name__ == '__main__':
		data = load("population_total.csv")
		aff_pop(data, your_country="Morocco", other_country="Egypt")
