import subprocess
import os
import shutil
import time
from PIL import Image
from trans import has_transparency

download_folder = "chan_scrapy\\DownloadedImages\\full"
kept_folder = "chan_scrapy\\KeptImages"

#downloader = subprocess.Popen('scrapy crawl chanCrawler', shell=True)
#downloader.wait()

for file in os.listdir(download_folder):
    filename = os.fsdecode(file)
    if filename.endswith(".png") or filename.endswith(".jpg"):
        im = Image.open(download_folder + "\\" + file, 'r')
        if has_transparency(im):
            shutil.move(download_folder + "\\" + file, kept_folder + "\\" + file)
            print(filename + " is transparent!")


shutil.rmtree(download_folder)
