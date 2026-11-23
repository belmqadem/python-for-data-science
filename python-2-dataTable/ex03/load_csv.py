import pandas as pd
from pandas.errors import EmptyDataError, ParserError


def load(path: str) -> pd.DataFrame | None:
    """
    Loads a CSV file into a pandas DataFrame and prints its dimensions.
    """
    try:
        data = pd.read_csv(path, index_col=0)
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")
        return None
    except PermissionError:
        print("Error: Insufficient permissions to read the file.")
        return None
    except EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()
    except ParserError:
        print("Error: Malformed CSV file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    print(f"Loading dataset of dimensions {data.shape}")
    return data


if __name__ == '__main__':
    load("life_expectancy_years.csv")
