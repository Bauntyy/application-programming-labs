import os

import cv2
import matplotlib.pyplot as plt
import numpy as np


def histogram_of_channels(image:np.ndarray) -> tuple:
    red = cv2.calcHist([image], [2], None, [256], [0, 255])
    blue = cv2.calcHist([image], [0], None, [256], [0, 255])
    green = cv2.calcHist([image], [1], None, [256], [0, 255])
    return red, green, blue


def create_histogram(red:np.ndarray, green:np.ndarray, blue:np.ndarray,) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot( red, label='Красная линия', color='red')
    plt.plot( green, label='Зеленая линия', color='green')
    plt.plot( blue, label='Синяя линия', color='blue')
    plt.xlim([0, 255])
    plt.title('Гистограмма цвета изображения')
    plt.xlabel('Интенсивность цвета')
    plt.ylabel('Частота')
    plt.grid()
    plt.legend()
    plt.show()


def change_size(image:np.ndarray, width:int, height:int) -> np.ndarray:
    return cv2.resize(image, (height, width))


def save_image(new_image, new_image_path) -> None:
    os.chdir(new_image_path)
    cv2.imwrite('new_image.jpg', new_image)


def show_image(image: np.ndarray, new_image: np.ndarray) -> None:
    cv2.imshow('image', image)
    cv2.imshow('new_image', new_image)
    cv2.waitKey(0)