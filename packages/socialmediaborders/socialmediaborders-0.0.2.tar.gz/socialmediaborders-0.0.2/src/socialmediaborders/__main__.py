import os
import argparse

from socialmediaborders import create_borders


def main():
    parser = argparse.ArgumentParser(
        description='Adding colored borders to pictures for social media to bring them to a 1:1 format.')
    parser.add_argument("Path", metavar="path", type=str,
                        help='the path to the image')
    parser.add_argument('-c', "--color", type=str, default="white",
                        help='the color of the border')
    parser.add_argument('-bp', "--borderpercentage", type=int, default=5,
                        help='the percentage of the border size')
    parser.add_argument('-k', "--keepOriginal", action=argparse.BooleanOptionalAction, default=False,
                        help='keep the original image')
    args = parser.parse_args()

    path = args.Path
    outpath = args.Path
    border_color = args.color
    min_border_percent = args.borderpercentage / 100
    keepOriginal = args.keepOriginal

    if os.path.isfile(path):
        create_borders.process_picture(path, outpath, border_color,
                        min_border_percent, keepOriginal)
    elif os.path.isdir(path):
        create_borders.process_picture_dir(path, outpath, border_color,
                            min_border_percent, keepOriginal)


if __name__ == "__main__":
    main()
