import os

from icrawler.builtin import BingImageCrawler

def download(keyword: str, number: int, imgdir: str) -> None:
    for filename in os.listdir(imgdir):
        """
        Deletes old images from the target directory before uploading new ones.
        """
        os.remove(os.path.join(imgdir, filename))
        """
        A function for uploading images using the Google Image Crawler library.
        """
    my_crawler = BingImageCrawler(
    storage={"root_dir": imgdir, "backend": "FileSystem"},
    feeder_threads=2,
    parser_threads=2,
    downloader_threads=8)
    my_crawler.crawl(keyword=keyword, max_num=number)

'''    import os

    from icrawler.builtin import BingImageCrawler

    def download_images(keyword: str, number_of_images: int, imgdir: str) -> None:
        """
        Download images in special directory
        :param keyword: word for searching
        :param number_of_images:number of images for download
        :param imgdir: directory with images
        :return:
        """
        if not (os.path.isdir(imgdir)):
            os.mkdir(imgdir)
        for filename in os.listdir(imgdir):
            os.remove(os.path.join(imgdir, filename))
        bing_crawler = BingImageCrawler(storage={'root_dir': imgdir})
        bing_crawler.crawl(keyword=keyword, max_num=number_of_images)'''