import numpy as np
from PIL import Image, ImageDraw, ImageOps
from load_image import ft_load


def zoom_image(path: str) -> np.ndarray | None:
    """
    Load an image, print its pixel data, number of channel, pixel content and display it after zooming in the center of the image. Also, print the new shape of the image after slicing.
    """
    rgb_format = ft_load(path)
    if rgb_format is None:
        return None
    print(rgb_format)

    try:
        img = Image.fromarray(rgb_format)
        width, height = img.size

        if width < 400 or height < 400:
            print("Error: Image dimensions are too small for zooming.")
            return None

        crop_size = 400
        left = (width - crop_size) // 2
        top = (height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size

        cropped_img = img.crop((left, top, right, bottom))
        gray_img = ImageOps.grayscale(cropped_img)

        zoomed_array = np.expand_dims(np.array(gray_img), axis=-1)
        print(f"New shape after slicing: {zoomed_array.shape}")

        display_img = gray_img.copy()
        draw = ImageDraw.Draw(display_img)
        crop_w, crop_h = display_img.size
        interval = 50

        for x in range(0, crop_w, interval):
            draw.line([(x, 0), (x, 10)], fill=0, width=1)
            draw.text((x + 2, 12), str(x), fill=0)

        for y in range(0, crop_h, interval):
            draw.line([(0, y), (10, y)], fill=0, width=1)
            draw.text((12, y + 2), str(y), fill=0)

        display_img.show()
        return zoomed_array

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    print(zoom_image("animal.jpeg"))
