import pandas as pd
import cv2
import matplotlib.pyplot as plt


def create_dataframe(csv_path: str) -> pd.DataFrame:
    """
    Загружает пути к изображениям из файла CSV, считывает изображения и записывает их высоту, ширину и глубину. Также печатает статистическую информацию.
    :param csv_path: Путь к CSV-файлу, содержащему пути к изображениям.
    :return: DataFrame, содержащий свойства изображений, пути и статистическую информацию.
    """
    df = pd.read_csv(csv_path)
    df.columns = ['Relative_path', 'Absolute_path']
    return df

def add_hwd_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет столбцы 'Height', 'Width' и 'Depth' в DataFrame,
    используя информацию о размере изображений.

    :param df: Исходный DataFrame, содержащий путь к изображению в колонке 'Relpath'.
    :return: Обновленный DataFrame с новыми столбцами.
    """

    heights = []
    widths = []
    depths = []


    for absolute_path in df["Absolute_path"]:
        img = cv2.imread(absolute_path)
        height, width, depth = img.shape
        heights.append(height)
        widths.append(width)
        depths.append(depth)
    df["Height"] = heights
    df["Width"] = widths
    df["Depth"] = depths
    dk = df.take([2, 3, 4], axis=1)
    return dk

def filter_dataframe(df: pd.DataFrame, max_height: int, max_width: int)-> pd.DataFrame:
    """
    Фильтрует DataFrame по максимальной высоте и ширине.
    :param df: DataFrame, содержащий свойства и пути изображений.
    :param max_height: Максимально допустимая высота изображений.
    :param max_width: Максимально допустимая ширина изображений.
    :return: Отфильтрованный DataFrame, содержащий только изображения указанных размеров.
    """
    filtered_df = df[(df['Width'] <= int(max_width)) & (df['Height'] <= int(max_height))]
    return filtered_df

def add_area_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Вычисляет площадь изображения
    :param df: DataFrame, содержащий свойства и пути изображений.
    :return: DataFrame, содержащий свойства изображений, пути и площади.
    """
    df['Area'] = df['Height'] * df['Width']
    return df

def plot_area_distribution(df: pd.DataFrame) -> None:
    """
    Рисует гистограмму по площади
    :param df: DataFrame, содержащий свойства изображений, пути и площади.
    """
    if 'Area' in df.columns:
        df.hist(column="Area", bins=len(df))
        plt.title("Histogram by area")
        plt.xlabel("Area")
        plt.ylabel("Count")
        plt.show()
    else:
        print("Column 'Area' is missing from DataFrame.")
