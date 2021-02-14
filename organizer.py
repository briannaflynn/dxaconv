#!/usr/bin/python

# before you run, pip install pydicom, pip install pillow # optional

import pydicom as dicom
import PIL # optional
import pandas as pd
import matplotlib.pyplot as plt
import os
from os import listdir
import cv2
import csv
from pathlib import Path  

from dxaconv import *


src_directory = './exampleDicoms' # source of .dcm files
output_directory = '.' # where to output the converted files
      

def get_anatomy_extension(bodypart:str=None):

	body_dict = {'hip1': '8.12.1.jpg', 'hip2': '5.12.1.jpg', 'knee1': '9.12.1.jpg', 'knee2': '6.12.1.jpg', 'full_body_opaque': '11.12.1.jpg', 'full_body_transparent': '12.12.1.jpg', 'spine': '2.12.1.jpg', 'thoracic': '7.12.1.jpg'}
	extension = "No extension found"
	if bodypart != None:
		extension = "No extension found for " + bodypart
	for k, v in body_dict.items():
		if bodypart == None:
			print('Available keys: ', k)
		else:
			if bodypart == k:
				extension = v
	return extension
    		

## Organize the dicom files by the part of the body imaged

def organize_by_anatomy(dir_path:str, bodypart:str, extension:str):
	
	file_list = ext_only(dir_path, extension) ## get extension from get_anatomy_extension function
	txtName = bodypart + ".txt"
	with open(txtName, 'w') as f:
		for item in file_list:
			f.write("%s\n" % item)
	return file_list
			
	## fill a text file with the names of the files organized by anatomy

## returns a list from text file, can also use file_list as returned directly by organize_by_anatomy
def get_file(txt):

    text_file = open(txt).read().splitlines()
    
    return text_file #this is a list of files from a text file input

## input can be from the get_file function, or from organize_by_anatomy function (both produce lists)
## source directory = where are the files coming from
## destination directory = where are the files going

## input full paths for best results
def copier(file_list, source_dir, dest_dir):
    count = 0
    for f in file_list:
        source_path = source_dir + f
        dest_path = dest_dir + f
        copyfile(source_path, dest_path)

        count += 1

        print('file ' + str(f) + ' copied successfully: ' + str(count))

