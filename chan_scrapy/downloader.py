import subprocess
import os
import shutil
import time
from PIL import Image
from trans import has_transparency
import options

def downloader(download_folder, kept_folder):
    if(options.sort_only[0] is False):
        downloader_process = subprocess
        
        print(options.selected_crawler)
        match options.selected_crawler:

            #full downloader
            case "Full Chan Crawler":
                downloader_process = subprocess.Popen('scrapy crawl chanCrawler -a start_url=' + options.op_board[0], shell=True)

            #test downloader
            case "Memory Chan Crawler":
                downloader_process = subprocess.Popen('scrapy crawl testCrawler', shell=True)

            #full downloader memory
            case "Test Crawler":
                downloader_process = subprocess.Popen('scrapy crawl chanCrawlerMemory', shell=True)
            
            case _:
                print("Something went wrong with chosing a crawler")

        

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
