import argparse


def parser() -> argparse.Namespace:
    """Reads arguments from terminal    :return: Arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv_path",default="C:\\Users\\tches\\Desktop\\PP\\lab_4\\Lab4\\annotation.csv", type=str)
    parser.add_argument("--max_width", default="1920", type=int)
    parser.add_argument("--max_height", default="1080", type=int)
    arguments = parser.parse_args()
    return arguments