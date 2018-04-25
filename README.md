# ConvertCOCO
## Description
This project is the toolbox to convert your own dataset to COCO dataset.

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
&lt;DataPath&gt;  
&emsp;gt+&lt;category name1&gt;  
&emsp;&emsp;image1.&lt;ImgFmt&gt;  
&emsp;&emsp;image2.&lt;ImgFmt&gt;  
&emsp;&emsp;image3.&lt;ImgFmt&gt;  
&emsp;gt+&lt;category name2&gt;  
&emsp;&emsp;image1.&lt;ImgFmt&gt;  
&emsp;&emsp;image2.&lt;ImgFmt&gt;  
&emsp;&emsp;image3.&lt;ImgFmt&gt;  
&emsp;gt+&lt;category name3&gt;  
&emsp;&emsp;image1.&lt;ImgFmt&gt;  
&emsp;&emsp;image2.&lt;ImgFmt&gt;  
&emsp;&emsp;image3.&lt;ImgFmt&gt;  
&emsp;SourceIMG  
&emsp;&emsp;image1.&lt;ImgFmt&gt;  
&emsp;&emsp;image2.&lt;ImgFmt&gt;  
&emsp;&emsp;image3.&lt;ImgFmt&gt;  
### Generate gt.json  
Please run gt2json.py, if anything above is done.
