import argparse

import cv2

from histogram import histogram_of_channels, create_histogram, change_size, save_image, show_image


def parsing_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_path", default="C:\\Users\\tches\\Desktop\\PP\\lab_3\\Images\\image.jpg", type=str, help="Path to the image")
    parser.add_argument("--new_image_path", default="C:\\Users\\tches\\Desktop\\PP\\lab_3\\Images", type=str, help="New path to the image")
    parser.add_argument("--height", default=120, type=str, help="Height of the new image")
    parser.add_argument("--width", default=120, type=str, help="Width of the new image")
    arguments = parser.parse_args()
    return arguments


def main():
    arguments = parsing_arguments()
    try:
        image = cv2.imread(arguments.image_path)
        print(image.shape)
        r,g,b = histogram_of_channels(image)
        create_histogram(r,g,b)
        new_image = change_size(image, arguments.height, arguments.width)
        save_image(new_image, arguments.new_image_path)
        show_image(image, new_image)
    except Exception as e:
        print(f"Error: {e} ")


if __name__ == "__main__":
    main()