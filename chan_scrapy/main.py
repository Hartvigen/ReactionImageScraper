from tkinter import *
from downloader import *

from tkinter import filedialog

import options

##Todo: 
#Allow for selection of which files are downloaded (for example if I only want gifs/webms I can choose that)
#Options should only be available for the full downloader, removed if another is chosen
#Check for duplicate files in the kept folder
#Create script that runs scraper once a day at a specific time, set it up on Raspberry Pi

main = Tk() 
main.title("Test")
main.geometry('200x250')

def select_folder():
    old = options.kept_folder
    options.kept_folder = filedialog.askdirectory()

    if options.kept_folder == "":
        options.kept_folder = old

    print(options.kept_folder)

def start_downloader():
    downloader(options.download_folder, options.kept_folder)

def change_crawler(crawler):
    options.selected_crawler = clicked.get()
    print(options.selected_crawler)


#Changes options through check buttons. To avoid boiler plate code, options are given as lists through parameters such that they are mutable
def check_command(check_button, options_variable):
    if check_button.get() == 1:
        options_variable[0] = True
        print(options.delete_after[0])
    else:
        options_variable[0] = False
        print(options.delete_after[0])

def change_board(*args):
    options.op_board[0] = board_field.get()

    if options.op_board[0] is "":
        options.op_board[0] = "a"



crawler_options = ["Full Chan Crawler", "Memory Chan Crawler", "Test Crawler"]

board_field = Entry(main)
board_field.pack()

board_field.bind('<KeyRelease>', change_board)

clicked = StringVar()
clicked.set("Select Crawler")

drop_menu = OptionMenu(main, clicked, *crawler_options, command=change_crawler)

sort_only = IntVar()
delete_after = IntVar()


folder_button = Button(main, text='Select Folder', command=lambda:select_folder())
download_button = Button(main, text = "Start Downloader", command=lambda:start_downloader())

sort_only_check = Checkbutton(main, text="Sort Only", variable=sort_only, command=lambda:check_command(sort_only, options.sort_only))
delete_after_check = Checkbutton(main, text="Delete After", variable=delete_after, command=lambda:check_command(delete_after, options.delete_after))

drop_menu.pack(side=TOP, pady=5)
folder_button.pack(side=TOP, pady=10)
download_button.pack(side=TOP, pady=10)

sort_only_check.pack(side=BOTTOM, pady=5)
delete_after_check.pack(side=BOTTOM, pady=5)

main.mainloop()




