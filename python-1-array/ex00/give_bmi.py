import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    try:
        height_arr = np.array(height)
        weight_arr = np.array(weight)

        bmi_values = weight_arr / (height_arr ** 2)
        return bmi_values.tolist()
    except Exception as e:
        print(f"Error: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        return [True if val > limit else False for val in bmi]
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    pass
