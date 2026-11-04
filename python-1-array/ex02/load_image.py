import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    try:
        img = np.array(Image.open(path))
        print(f"The shape of image is: {img.shape}")
        return img
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    pass
