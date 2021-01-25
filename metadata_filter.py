#!/usr/bin/python

import pandas as pd
import os
from os import listdir

EID_csv = "full/path/here"
df = pd.read_csv(OA_csv, delimiter = ",")

column_names = df.columns.tolist()

# coding = the number of your desired data coding
# eg. coding = 1465
	
def extract_rows(column_name, coding):
	eid_list = []
	user_rows = df.loc[df[column_name] == coding]
	eids = user_rows['eid'].tolist()
	for e in eids:
		eid_list.append(e)
		
	return eid_list
	
def all_rows(column_name_list, coding):
	big_list = []
	for c in column_name_list:
		eids = extract_rows(c, coding)
		for x in eids:
			big_list.append(x)
			
	return big_list


big_list = all_rows(column_names, coding)

output_destination = "."
fname = "EIDs.txt"

eid_list = print(big_list, file=open(os.path.join(output_destination, fname), "w"))
