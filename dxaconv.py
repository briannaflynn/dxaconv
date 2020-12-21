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

## returns a list of files that have the .dcm extension
def dcm_only(directory, extension='dcm'):
	return([f for f in listdir(directory) if f.endswith('.' + extension)])

## returns the absolute path of a directory 
def abs_dir(directory:str):
	absdir = os.path.abspath(directory)
	return absdir

# This function shows you a preview of the dicom image by plotting the image's pixel array with matplotlib 
# Just for an individual preview, but can write additional code to preview a whole folder

def dcm_preview(img_path:str):

	ds = dicom.dcmread(img_path)
	plt.imshow(ds.pixel_array)
	plt.show()
	

# This function converts dcm to jpg BY FOLDER, specified in "img_type" parameter
# takes the path to the directory with images, path to output destination, and the image file type as parameters

def dcm_converter(dcm_folder_path, img_output_path, img_type='.jpg'):

	images_path = os.listdir(dcm_folder_path)
	for n, image in enumerate(images_path):
		ds = dicom.dcmread(os.path.join(dcm_folder_path, image))
		pixel_array_numpy = ds.pixel_array
		image = image.replace('.dcm', img_type)
		cv2.imwrite(os.path.join(img_output_path, image), pixel_array_numpy)
	

# This function parses a dcm file's metadata 
# Set the absolute file path if not in the same directory as the images, otherwise, default is the current directory
	
def metadata_parser(dcm_file:str, output_destination):
	#dcm_file_path = abs_directory_path + dcm_file
	ds = dicom.read_file(dcm_file)
	f = Path(dcm_file).name
	f = f[:-4]
	y = "_metadata.txt"
	fname = f + y
	print(ds, file=open(os.path.join(output_destination, fname), "w"))
	
	
	

### Testing how it works

imagePath = '/Users/brie/Desktop/dxaconv-main/1.2.840.113619.2.110.210419.20150928115733.2.2.12.1.dcm'


# This function converts individual files to jpg format

def dcm2jpg_conv(dcm_file:str, output_destination):
	ds = dicom.dcmread(dcm_file)
	pixel_array_np = ds.pixel_array
	f = Path(dcm_file).name
	img = f.replace('.dcm', '.jpg')
	cv2.imwrite(os.path.join(output_destination, img), pixel_array_np)

Desktop = '/Users/brie/Desktop'
fname = '1.2.840.113619.2.110.210419.20150928115733.2.2.12.1.dcm'
#dcm2jpg_conv(imagePath, Desktop)

#metadata_parser(imagePath, Desktop)



directory = '/Users/brie/Desktop/1007323_20158_2_0/'	

## Pipeline draft
# First, get only the .dcm files from a directory, put into a list
#test = dcm_only(directory)

# then, get the full file paths of each file in directory
# files = []
# for f in test:
# 	files.append(os.path.join(abs_dir('../1007323_20158_2_0/'), f))

# then, convert each file and send to output destination
# for f in files:
# 	dcm2jpg_conv(f, Desktop)
	
#directoryList = ['List of Directories goes here', '.']

def dxaconv(directory_list:list, output_destination:str):
	files = []
	for d in directory_list:
		fnames = dcm_only(d)
		for f in fnames:
			files.append(os.path.join(abs_dir(d), f))
	for f in files:
		dcm2jpg_conv(f, output_destination)

# dirList = ['../1017520_20158_2_0', '../1007323_20158_2_0']		
# dxaconv(dirList, Desktop)

dxadcm = abs_dir('../50_dicom_folders/dxaImages_dcm')
files = [f for f in os.listdir(dxadcm)]

full_paths = []
for f in files:
	full_paths.append(os.path.join(dxadcm, f))
#print(full_paths)
destination = '/Users/brie/Desktop/50_dicom_folders/dxaImages_jpg'
metadata_destination = '/Users/brie/Desktop/50_dicom_folders/dxaMetadata_txt'

# for f in full_paths:
# 	print(f)
# 	dcm2jpg_conv(f, destination)
	
for f in full_paths:
	print(f)
	metadata_parser(f, metadata_destination)
		
	