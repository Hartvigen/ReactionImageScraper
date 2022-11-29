from tkinter import *
from downloader import *

from tkinter import filedialog

import options

#Beware download folders, works differently on Linux systems and needs base folder location for desired functionality

def select_folder():
    old = options.kept_folder
    options.kept_folder = filedialog.askdirectory()

    if options.kept_folder == "":
        options.kept_folder = old

    print(options.kept_folder)

def start_downloader():
    downloader(options.download_folder, options.kept_folder)


#Changes options through check button, to avoid boiler plate options are given as lists
def check_command(check_button, options_variable):
    if check_button.get() == 1:
        options_variable[0] = True
        print(options.delete_after[0])
    else:
        options_variable[0] = False
        print(options.delete_after[0])


main = Tk()
main.title("Test")
main.geometry('200x150')

sort_only = IntVar()
delete_after = IntVar()


folder_button = Button(main, text='Select Folder', command=lambda:select_folder())
download_button = Button(main, text = "Start Downloader", command=lambda:start_downloader())

sort_only_check = Checkbutton(main, text="Sort Only", variable=sort_only, command=lambda:check_command(sort_only, options.sort_only))
delete_after_check = Checkbutton(main, text="Delete After", variable=delete_after, command=lambda:check_command(delete_after, options.delete_after))


folder_button.pack(side=TOP, pady=10)
download_button.pack(side=TOP, pady=10)

sort_only_check.pack(side=BOTTOM, pady=5)
delete_after_check.pack(side=BOTTOM, pady=5)

main.mainloop()




