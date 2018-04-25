# ConvertCOCO
## Description
This project is the toolbox to convert our own dataset into COCO dataset.

## Installation
Please install the environment by anaconda

```bash
conda install -c conda-forge opencv cython pylab matplotlib
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
python setup.py install
```
## Usage
Edit your [settings.json](https://github.com/MELSunny/ConvertCOCO/blob/master/settings.json) to adapt your own dataset.
envs  //Basic environment
  DataPath  //Your own dataset path
  ImgFmt  //Your own dataset image format
  IgnoreSize  //ignore the small region which the size is below than IgnoreSize
category  //Your dataset category description
  id  //Category id
  name  //Category name
  supercategory  //Super Category. For example: For category: boy,girl,man,woman. Their super category is human.
info //Just modify it whatever you like
