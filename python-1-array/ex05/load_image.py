import numpy as np
from PIL import Image

VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')


def ft_load(path: str) -> np.ndarray | None:
    """
    Load an image from the specified path, print its format and its pixels
    in RGB, and return it as a NumPy array.
    """
    if not path.endswith(VALID_EXTENSIONS):
        print("Error: Invalid image format")
        return None

    try:
        img = Image.open(path)
        rgb_format = np.array(img)
        print(f"The shape of image is: {rgb_format.shape}")
        print(rgb_format)
        return rgb_format
    except (ValueError, TypeError, IndexError, FileNotFoundError) as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    pass
