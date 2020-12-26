# dxaconv
## Convert DICOM files from DXA scans to other image formats, and parse the corresponding metadata files

Convert .dcm files to .jpg (or .png), preview images via matplotlib, and convert each file's corresponding metadata to a .txt file. Organize the output by anatomy (built in extensions compatible with dicom files from the United Kingdom National Health Service). Example dicom files used in this repo can be found [here](https://biobank.ctsu.ox.ac.uk/crystal/field.cgi?id=20158) as "eg_20158_dxa.zip".

![](img/readme_example.jpg)

Example: 
`dcm_preview('path/to/your.dcm')`
