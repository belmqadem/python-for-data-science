import numpy as np
from PIL import Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invert the color of the image received"""
    inverted = 255 - array
    Image.fromarray(inverted).show()
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel of the image received"""
    red = (array * [1, 0, 0]).astype(np.uint8)
    Image.fromarray(red).show()
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only the green channel of the image received"""
    green = array.copy()
    green[:, :, 0] = green[:, :, 2] - green[:, :, 2]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    Image.fromarray(green).show()
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only the blue channel of the image received"""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    Image.fromarray(blue).show()
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert the image to grayscale"""
    grey_ = np.sum(array, axis=2, keepdims=True) / 3
    grey = np.repeat(grey_, 3, axis=2).astype(np.uint8)
    Image.fromarray(grey).show()
    return grey


if __name__ == '__main__':
    pass
