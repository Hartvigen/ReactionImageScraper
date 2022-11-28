from tkinter import *
from downloader import *

from tkinter import filedialog

import options

#Beware download folders, works differently on Linux systems and needs base folder location for desired functionality
download_folder = "DownloadedImages\\full"

main = Tk()
main.title("Test")
main.geometry('200x100')

def select_folder():
    options.kept_folder = filedialog.askdirectory()
    print(options.kept_folder)


def start_downloader():
    downloader(download_folder, options.kept_folder)

folder_button = Button(main, text='Select Folder', command=lambda:select_folder())
download_button = Button(main, text = "Start Downloader", command=lambda:start_downloader())

folder_button.pack(side=TOP, pady=10)

download_button.pack(side=TOP, pady=10)


main.mainloop()




