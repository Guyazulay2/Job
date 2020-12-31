#!/bin/python

import os 
from time import sleep
import zipfile

VERSION = os.environ.get("VERSION")

array = ["a","b","c","d"]

def Create():
    for letter in array:
        file = open(f"{letter}.txt", "w") 
        file.close()
        assert os.path.exists(os.path.abspath(f"{letter}.txt")), "Failed.. "

        zip_file = open(f"{letter}_{VERSION}.zip", "w") 
        zip_file.close()
        assert os.path.exists(os.path.abspath(f"{letter}_{VERSION}.zip")), "Failed.. "
        
        myZipFile = zipfile.ZipFile(f"{letter}_{VERSION}.zip", "w")
        myZipFile.write(f"{letter}.txt",f"{letter}.txt" , zipfile.ZIP_DEFLATED)
        os.remove(f"{letter}.txt")

Create()