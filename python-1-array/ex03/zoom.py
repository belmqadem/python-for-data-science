import numpy as np
from PIL import Image, ImageDraw
from load_image import ft_load


def main(path: str):
    pixel_data = ft_load(path)
    print(pixel_data)
    img = Image.fromarray(pixel_data)

    width, height = img.size

    left = width * 0.25
    top = height * 0.25
    right = width * 0.75
    bottom = height * 0.75

    cropped_img = img.crop((left, top, right, bottom))
    zoomed_img = cropped_img.resize((width, height), Image.Resampling.LANCZOS)

    draw = ImageDraw.Draw(zoomed_img)
    interval = 50

    for x in range(0, width, interval):
        draw.line([(x, 0), (x, 10)], fill=(255, 0, 0), width=1)
        draw.text((x + 2, 12), str(x), fill=(255, 0, 0))

    for y in range(0, height, interval):
        draw.line([(0, y), (10, y)], fill=(255, 0, 0), width=1)
        draw.text((12, y + 2), str(y), fill=(255, 0, 0))

    zoomed_img.show()
    print(f"New shape after slicing: {zoomed_img.size}")
    print(np.array(zoomed_img))


if __name__ == "__main__":
    main("animal.jpeg")
