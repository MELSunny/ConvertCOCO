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
### Configuration
Edit your [settings.json](https://github.com/MELSunny/ConvertCOCO/blob/master/settings.json) to adapt your own dataset.  

envs&emsp;&emsp;//Basic environment  
&emsp;DataPath&emsp;&emsp;//Your own dataset path  
&emsp;ImgFmt&emsp;&emsp;//Your own dataset image format  
&emsp;IgnoreSize&emsp;&emsp;//ignore the small region which the size is below than IgnoreSize  
category&emsp;&emsp;//Your dataset category description  
&emsp;id&emsp;&emsp;//Category id  
&emsp;name&emsp;&emsp;//Category name  
&emsp;supercategory&emsp;&emsp;//Super Category. For example: For category: boy,girl,man,woman. Their super category is human.  
info&emsp;&emsp;//Just modify it whatever you like
### Structure of dataset path
Dataset
&emsp;gt+<category name1>
&emsp;&emsp;gtimage1.<ImgFmt>
&emsp;&emsp;gtimage2.<ImgFmt>
&emsp;&emsp;gtimage3.<ImgFmt>
&emsp;gt+<category name2>
&emsp;&emsp;gtimage1.<ImgFmt>
&emsp;&emsp;gtimage2.<ImgFmt>
&emsp;&emsp;gtimage3.<ImgFmt>
&emsp;gt+<category name3>
&emsp;&emsp;gtimage1.<ImgFmt>
&emsp;&emsp;gtimage2.<ImgFmt>
&emsp;&emsp;gtimage3.<ImgFmt>
After finish editing settings.json, please run gt2json.py
