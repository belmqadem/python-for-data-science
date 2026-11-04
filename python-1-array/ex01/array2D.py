import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        arr = np.array(family)
        print(f"My shape is : {arr.shape}")
        trunc_arr = arr[start:end]
        print(f"My new shape is : {trunc_arr.shape}")
        return trunc_arr.tolist()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    pass
