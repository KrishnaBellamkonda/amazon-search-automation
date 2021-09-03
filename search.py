# Basic imports
import os 
import sys
import time  
import selenium
from selenium import webdriver

# Importing constants and paths 
from utils import *
from webscraping import scrape_and_print

# Get the folderName & args
folderName = sys.argv[1]
keywords = sys.argv[2:5]

try:
   flag = sys.argv[5]
except IndexError:
    flag = False
else:
    flag = int(flag)

# Create the folder in the searches folde
newFolderPath = os.path.join(searchesFolderPath, folderName)
if not os.path.exists(newFolderPath):
    os.mkdir(newFolderPath)
    print(f"Folder created - path {newFolderPath}")
else: 
    timestamp = int(time.time())
    folderName += "_"+str(timestamp)
    newFolderPath = os.path.join(searchesFolderPath, folderName)
    os.mkdir(newFolderPath)
    print(f"A folder existed with the name. Create another folder with {folderName}")

# Path for data saving 
jsonPath = os.path.join(newFolderPath, dataName)

# Opening Web Browser 
scrape_and_print(keywords, jsonPath, flag)