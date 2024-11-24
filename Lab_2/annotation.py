import csv
import os


def annotation(imgdir: str, csv_path: str) -> None:
    """
    Creates a CSV annotation file with relative and absolute paths to images in the specified directory.
    :param imgdir: The directory containing the images.
    :param csv_path: The path to the CSV file being created.
    :raises PermissionError: If an error occurs accessing files or directories.
    """
    try:
        with open(csv_path, mode='w', newline='', encoding='utf-8') as annotation_file:
            writer = csv.writer(annotation_file)
            headers = ['Relative path', 'Absolute path']
            writer.writerow(headers)

            for file in os.listdir(imgdir):
                relative_path = os.path.relpath(file, start=imgdir)
                absolute_path = os.path.abspath(file)
                writer.writerow([relative_path, absolute_path])
    except:
        raise PermissionError("There is no necessary file")