import numpy as np
from PIL import Image, ImageDraw, ImageOps
from load_image import ft_load


def rotate_image(path: str) -> np.ndarray | None:
    """
    Load an image, print its pixel data, number of channel, pixel content
    and display it after rotating.
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
        rotated_img = gray_img.rotate(90, expand=True)
        print(f"The shape of rotated image is: {rotated_img.size}")
        rotated_array = np.expand_dims(np.array(rotated_img), axis=-1)

        display_img = rotated_img.copy()
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
        return rotated_array.transpose()

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    img = rotate_image("animal.jpeg")
    print(img)
