#!/usr/local/bin/python3
import os
import filetype
from PIL import Image, ImageOps


def process_picture(path: str, outpath: str, border_color: str, min_border_percent: int, keepOriginal: bool):
    if filetype.is_image(path):
        img = Image.open(path)
        width, height = img.size

        if width >= height:
            min_border = int(height * min_border_percent)
        else:
            min_border = int(width * min_border_percent)

        diff = int((abs(width - height) / 2) + min_border)
        if width > height:
            border = (min_border, diff, min_border, diff)
        elif height > width:
            border = (diff, min_border, diff, min_border)
        else:
            border = min_border

        imgWithBorder = ImageOps.expand(img, border=border, fill=border_color)
        if not keepOriginal:
            imgWithBorder.save(outpath)
        else:
            dir = os.path.dirname(outpath)
            base = os.path.basename(outpath)
            new_base = os.path.splitext(
                base)[0] + "_border" + os.path.splitext(base)[1]
            new_path = os.path.join(dir, new_base)
            imgWithBorder.save(new_path)
    else:
        return


def process_picture_dir(path: str, outpath: str, border_color: str, min_border_percent: int, keepOriginal: bool):
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    for file in files:
        file_path = os.path.join(path, file)
        file_outpath = os.path.join(outpath, file)
        process_picture(file_path, file_outpath, border_color,
                        min_border_percent, keepOriginal)
