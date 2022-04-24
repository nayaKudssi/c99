import os
import shutil

source=input("Enter source: ")
destination=input("Enter destination: ")

source=source+'/'
destination=destination+'/'

list_off_files=os.listdir(source)
for file in list_off_files:
    shutil.copy((source+file),destination)
    