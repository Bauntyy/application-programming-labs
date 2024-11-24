import downloader
import parser
import iterator
from annotation import annotation


def main() -> None:
    arg=parser.parser()
    try:
        downloader.download(arg.keyword, arg.number, arg.imgdir)
        annotation(arg.imgdir,arg.csv_path)
        myiterator = iterator.ImageIterator(arg.csv_path)
        for item in myiterator:
            print(item)
    except Exception as e:
        print( {e} )


if __name__ == "__main__":
    main()