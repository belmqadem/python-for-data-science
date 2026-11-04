import numpy as np
from PIL import Image


def ft_load(path: str):
    img = np.array(Image.open(path))
    print(f"The shape of image is: {img.shape}")
    return img


if __name__ == '__main__':
    pass
