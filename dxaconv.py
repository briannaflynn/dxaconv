#!/usr/bin/python

# before you run, pip install pydicom, pip install pillow # optional

import sys
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
def ext_only(directory, extension='dcm'):
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
	
# This function parses a dcm file's metadata 
# Set the absolute file path if not in the same directory as the images, otherwise, default is the current directory
	
def metadata_parser(dcm_file:str, output_destination):
	#dcm_file_path = abs_directory_path + dcm_file
	ds = dicom.read_file(dcm_file)
	f = Path(dcm_file).name
	f = f[:-4]
	y = "_metadata.txt"
	fname = f + y
	metadata = print(ds, file=open(os.path.join(output_destination, fname), "w"))
	
	return metadata

# This function converts individual dcm files to jpg format

def dxaconv_single(dcm_file:str, output_destination):
	ds = dicom.dcmread(dcm_file)
	pixel_array_np = ds.pixel_array
	f = Path(dcm_file).name
	img = f.replace('.dcm', '.jpg')
	cv2.imwrite(os.path.join(output_destination, img), pixel_array_np)
	print("File ", img, "converted to JPG")
	
# This function converts dcm by directory, specified in "img_type" parameter (jpg or png)
# takes the path to the directory with images, path to output destination, and the image file type as parameters

# Use only if you have a directory with only .dcm files, or pass the files through the ext_only function first to check

def dxaconv_dir(dcm_folder_path, img_output_path, img_type='.jpg'):
	images_path = os.listdir(dcm_folder_path)
	#images_path = ext_only(dcm_folder_path) # uncomment this if you want to make sure you're only listing DICOM files from a directory
	for n, image in enumerate(images_path):
		ds = dicom.dcmread(os.path.join(dcm_folder_path, image))
		pixel_array_numpy = ds.pixel_array
		image = image.replace('.dcm', img_type)
		cv2.imwrite(os.path.join(img_output_path, image), pixel_array_numpy)

# given a list of directories, convert contents output to destination

def dxaconv_dirlist(directory_list:list, output_destination:str):
	files = []
	for d in directory_list:
		fnames = ext_only(d)
		for f in fnames:
			files.append(os.path.join(abs_dir(d), f))
	for f in files:
		dxaconv_single(f, output_destination)
		
# take dcm file and convert most useful metadata information into a nested dictionary
# nested dict includes information on the type of image, the 
def advanced_metadata_tools(full_path_dcm):
	ds = dicom.read_file(full_path_dcm)
	
	# Image Info
	exam_type = ds.StudyDescription
	img_type = ds.SeriesDescription
	
	# dictionary of image info
	img_dict = {"Exam_Type": exam_type, "Image_Type": img_type}
	
	# Patient Info
	age = ds.PatientAge
	ID = ds.PatientID
	orientation = ds.PatientOrientation
	sex = ds.PatientSex
	size = ds.PatientSize
	weight = ds.PatientWeight
	protocol = ds.ProtocolName
	acquisition = ds.AcquisitionDate
	ethnicity = ds.EthnicGroup
	
	# dictionary of patient info
	patient_dict = {'Patient_Age': age, 'Patient_Protocol': protocol, 'Patient_Sex': sex, 'Ethnic_Group': ethnicity, 'Patient_Orientation': orientation, 'Patient_Size': size, 'Patient_Weight': weight, 'PatientID': ID, 'Acquisition_Date': acquisition}
	
	# Pixel Info
	pixdata = ds.PixelData ## pixel data is not human readable, can use to plot image in other functions
	represent = ds.PixelRepresentation
	samp = ds.SamplesPerPixel
	rows = ds.Rows
	columns = ds.Columns
	phot = ds.PhotometricInterpretation
	
	# dictionary of pixel info
	pixel_dict = {'Samples_per_Pixel': samp, 'Pixel_Rows': rows, 'Pixel_Columns': columns, 'Photomeric_Interpretation': phot, 'Pixel_Representation': represent}
	
	# Bit Info
	allocated = ds.BitsAllocated
	stored = ds.BitsStored
	highbit = ds.HighBit
	
	# dictionary of bit info
	bit_dict = {'Bits_Allocated': allocated, 'Bits_Stored': stored, 'High_Bit': highbit}
	
	# Nested Dict with all Information
	dicom_super = {'Image':img_dict, 'Patient':patient_dict, 'Pixel':pixel_dict, 'Bit':bit_dict}
	
	return dicom_super

try:
    dxaconv_dir(sys.argv[1], sys.argv[2])
except BaseException as error:
    print('An exception occurred and a dcm file of this directory did not successfully convert: {}'.format(error))
