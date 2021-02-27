# dxaconv
## Convert DICOM files from DXA scans to other image formats, and parse the corresponding metadata files

Originally intended for DXA scans, but can also be used on any other DICOM formatted image as well (i.e. MRI).

Convert .dcm files to .jpg (or .png), preview images via matplotlib, and convert each file's corresponding metadata to a .txt file. Organize the output by anatomy (built in extensions compatible with dicom files from the United Kingdom National Health Service). Example dicom files used in this repo can be found [here](https://biobank.ctsu.ox.ac.uk/crystal/field.cgi?id=20158) as "eg_20158_dxa.zip".

This code builds upon the pydicom library and OpenCV libraries. Please refer [here](https://pydicom.github.io/pydicom/0.9/pydicom_user_guide.html) and [here](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html) for additional information on dependencies, the pydicom and OpenCV documentation.

![](img/readme_example.jpg)

Example: 
```Python
from dxaconv import dcm_preview

dcm_preview('path/to/your.dcm')

```
