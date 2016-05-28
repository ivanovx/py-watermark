#!/usr/bin/env python

import datetime
import argparse
from PIL import Image, ImageEnhance

def reduce_opacity(image, opacity):
    assert opacity >= 0 and opacity <= 1

    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    else:
        image = image.copy()

    alpha = image.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    image.putalpha(alpha)

    return image


def watermark(image, mark, opacity=1):
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    layer = Image.new('RGBA', image.size, (0, 0, 0, 0))

    """"if position == 'tile':
        for y in range(0, image.size[1], mark.size[1]):
            for x in range(0, image.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    elif position == 'scale':
        ratio = min(
            float(image.size[0]) / mark.size[0], float(image.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark, ((image.size[0] - w) / 2, (image.size[1] - h) / 2))
    else:
        layer.paste(mark, position)
    """

    ratio = min(float(image.size[0]) / mark.size[0], float(image.size[1]) / mark.size[1])
    w = int(mark.size[0] * ratio)
    h = int(mark.size[1] * ratio)
    mark = mark.resize((w, h))
    layer.paste(mark, ((image.size[0] - w) / 2, (image.size[1] - h) / 2))

    return Image.composite(layer, image, layer)

def main():
    parser = argparse.ArgumentParser(description='Add watermark to image')
    parser.add_argument('-i', '--image', help='The image')
    parser.add_argument('-w', '--watermark', help='The watermark')
    args = parser.parse_args()

    if args.image:
        image = Image.open(args.image)

        if args.watermark:
            mark = Image.open(args.watermark)
            date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

            watermark(image, mark, 0.5).save(date + ".jpg", "JPEG")
   
if __name__ == '__main__':
    main()