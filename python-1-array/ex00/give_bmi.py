import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """
    Calculate BMI values for given heights and weights.
    """
    with np.errstate(divide='raise', invalid='raise'):
        try:
            height_arr = np.array(height)
            weight_arr = np.array(weight)
            bmi_values = weight_arr / (height_arr ** 2)
            return bmi_values.tolist()
        except (ValueError, TypeError, FloatingPointError) as e:
            print(f"Error: {e}")
            return []
    


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to the BMI values and return a list of booleans indicating
    whether each BMI value exceeds the limit.
    """
    return [True if val > limit else False for val in bmi]


if __name__ == "__main__":
    pass
