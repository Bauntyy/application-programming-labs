import argparse
def parser() -> argparse.Namespace:
    """Reads arguments from terminal    :return: Arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="Keyword of search request")
    parser.add_argument("number", type=int, help="Number of images that you want to download (default: 2)")
    parser.add_argument("imgdir", type=str)
    parser.add_argument("--csv_path", type=str, default="C:\\Users\\tches\\Desktop\\PP\\lab_2\\Lab_2\\annotation.csv", help="Path to the folder, where you want to save images")
    arguments = parser.parse_args()
    return arguments