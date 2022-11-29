import subprocess
import os
import shutil
import time
from PIL import Image
from trans import has_transparency
import options

def downloader(download_folder, kept_folder):
    if(options.sort_only[0] is False):
        #full downloader
        downloader_process = subprocess.Popen('scrapy crawl chanCrawler', shell=True)

        #test downloader
        #downloader = subprocess.Popen('scrapy crawl testCrawler', shell=True)

        downloader_process.wait()


    for file in os.listdir(download_folder):
        filename = os.fsdecode(file)
        if filename.endswith(".png"):
            image = Image.open(download_folder + "\\" + file, 'r')
            image.load() #file is loaded so that it closes once sorting of images finishes, even if the image itself is not sorted
            if has_transparency(image):
                shutil.move(download_folder + "\\" + file, kept_folder + "\\" + file)
                print(filename + " is transparent!")

                
    #remove any files not matching your criteria
    if(options.delete_after[0] is True):
        shutil.rmtree(download_folder)
