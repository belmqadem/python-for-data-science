
import numpy as np
from PIL import Image, ImageDraw
from load_image import ft_load


def rotate_image(path: str) -> np.ndarray | None:
    """
    Load an image, print its pixel data, number of channel, pixel content
    and display it after rotating.
    """
    rgb_format = ft_load(path)
    if rgb_format is None:
        return None

    try:
        zoomed = rgb_format[100:500, 450:850, 0]

        img = Image.fromarray(zoomed.astype(np.uint8))

        zoomed_array = np.expand_dims(np.array(img), axis=-1)

        print(f"The shape of image is: {zoomed_array.shape}")
        print(zoomed_array)

        rotated_image = img.rotate(90, expand=True)

        rotated_array = np.array(rotated_image)

        display_img = rotated_image.copy()
        draw = ImageDraw.Draw(display_img)

        width, height = display_img.size
        interval = 50

        for x in range(0, width, interval):
            draw.line([(x, 0), (x, 10)], fill=0, width=1)
            draw.text((x + 2, 12), str(x), fill=0)

        for y in range(0, height, interval):
            draw.line([(0, y), (10, y)], fill=0, width=1)
            draw.text((12, y + 2), str(y), fill=0)

        display_img.show()

        transposed_array = rotated_array.T

        print(f"New shape after Transpose: {transposed_array.shape}")

        return transposed_array

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    img = rotate_image("animal.jpeg")
    print(img)
