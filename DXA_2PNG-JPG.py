#!/usr/bin/python

# before you run, pip install pydicom, pip install pillow # optional

import pydicom as dicom
import PIL # optional
import pandas as pd
import matplotlib.pyplot as plt
import os
import cv2
import csv

'''
#Preview Images
    
# specify your image path
image_path = 5733.2.2.12.1.dcm'
ds = dicom.dcmread(image_path)
plt.imshow(ds.pixel_array)
plt.show()
 
'''


#File conversion

# True if you want PNG, false if you want JPG
PNG = False
# Specify the .dcm folder path
folder_path = "/Users/brie/Desktop/1007323_20158_2_0/"
# Specify the output jpg/png folder path
jpg_folder_path = "/Users/brie/Desktop/JPG_test2"
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
	print(n)
	print("")
	print(image)
	ds = dicom.dcmread(os.path.join(folder_path, image))
	pixel_array_numpy = ds.pixel_array
	image = image.replace('.dcm', '.jpg')
	cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)



	

'''
#Metadata to be parsed
#ds = dicom.read_file('test-image.dcm')
#print(ds)


# This function shows you a preview of the dicom image by plotting the image's pixel array with matplotlib 
# Just for an individual preview, but can write additional code to preview a whole folder
def dcm_preview(img_path:str):

	ds = dicom.dcmread(img_path)
	plt.imshow(ds.pixel_array)
	plt.show()
	

# This function converts dcm to jpg or png, specified in "img_type" parameter
# takes the path to the directory with images, path to output destination, and the image file type as parameters

def dcm_converter(dcm_folder_path, img_output_path, img_type='.jpg'):

	images_path = os.listdir(dcm_folder_path)
	for n, image in enumerate(images_path):
	ds = dicom.dcmread(os.path.join(dcm_folder_path, image))
	pixel_array_numpy = ds.pixel_array
	image = image.replace('.dcm', img_type)
	cv2.imwrite(os.path.join(img_output_path, image), pixel_array_numpy)

# This function parses a dcm file's metadata 
# Set the absolute file path if not in the same directory as the images, otherwise, 	
def metadata_parser(abs_directory_path:str = '.', dcm_file:str):
	dcm_file_path = abs_directory_path + dcm_file
	ds = dicom.read_file(dcm_file_path)
	print(head(ds))

'''
	