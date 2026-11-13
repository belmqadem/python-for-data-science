from pathlib import Path
import pandas as pd
import numpy as np

def load(path: str) -> pd.DataFrame:
	file_path = Path(path)

	data = pd.read_csv(file_path, index_col=0)

	print(f"Loading dataset of dimensions {data.shape}")

	return data

if __name__ == '__main__':
		print(load("life_expectancy_years.csv"))
