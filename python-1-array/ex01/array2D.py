import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice the input list 'family' from index 'start' to index 'end' and return
    the sliced portion as a list. Also, print the shape of the original and
    sliced arrays.
    """
    try:
        arr = np.array(family)
        print(f"My shape is : {arr.shape}")
        trunc_arr = arr[start:end]
        print(f"My new shape is : {trunc_arr.shape}")
        return trunc_arr.tolist()
    except ValueError as e:
        print(f"Invalid slicing indices: {e}")
        return []
    except IndexError as e:
        print(f"Index out of bounds: {e}")
        return []
    except TypeError as e:
        print(f"Invalid input type: {e}")
        return []


if __name__ == "__main__":
    pass
