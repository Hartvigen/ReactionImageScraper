from pickle import FALSE

#download folder is set in settings.py, kept folder is defined by user through ui
download_folder = "DownloadedImages/full"
kept_folder = ""

#Various options for how to handle the downloaded files
#Options are defined as lists to make them mutable and avoid having to create a seperate function for each in the UI to alter their values through check button
#It is an ugly solution but python sucks when it comes to passing by reference

#Option to only sort pictures and not download
sort_only = [False]

#Deletes pictures without found transparency after run
delete_after = [False]

selected_crawler = "Full Chan Crawler"
