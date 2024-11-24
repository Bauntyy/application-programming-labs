import csv


class ImageIterator:
    def __init__(self, csv_path: str) -> None:
        """ Class constructor. Initializes the object and loads data from a CSV file.
        :param csv_path: Path to the CSV file containing the paths to the images. """
        self.csv_path = csv_path
        self.path_list = self.__load_csv__()
        self.limit = len(self.path_list)
        self.counter = 0

    def __iter__(self) -> 'ImageIterator':
        return self

    def __next__(self) -> str:
        """
        Method for getting the next element in the sequence.
        :return: The next path to the image.
        :raise StopIteration: Exception when the end of the list is reached.
        """
        if self.counter < self.limit:
            element = self.path_list[self.counter]
            self.counter += 1
            return element
        else:
            raise StopIteration

    def __load_csv__(self) -> list[str]:
        """
        An internal method for uploading data from a CSV file.
        :return: List of paths to images.
        :raise FileNotFoundError: Exception if the file is not found.
        :raise Exception: Any other exception when reading a file.
        """
        with open(self.csv_path, mode='r', encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            return [row[1] for row in reader]