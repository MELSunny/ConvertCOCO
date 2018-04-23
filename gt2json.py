import json
import os
from time import gmtime, strftime

import cv2
import numpy
from pycocotools import mask

json_file = open('settings.json').read()
settings = json.loads(json_file)


class image:
    def __init__(self):
        self.file_name=None
        self.id=None
        self.width=None
        self.height=None
        self.coco_url = None
        self.date_captured = None
        self.flickr_url = None
        self.license = None


class category:
    def __init__(self):
        self.id=None
        self.name=None
        self.supercategory=None


class annotation:
    def __init__(self):
        self.segmentation=None
        self.area=None
        self.image_id=None
        self.bbox=None
        self.category_id=None
        self.id=None
        self.iscrowd = 1


class licenses:
    def __init__(self):
        self.name = None
        self.id = None
        self.url = None


class segmentation:
    def __init__(self):
        self.counts=None
        self.size=None


class info:
    def __init__(self):
        self.description = None
        self.url = None
        self.version = None
        self.year = None
        self.contributor = None
        self.date_created = None

class root:
    def __init__(self):
        self.info=None
        self.images=None
        self.licences=None
        self.annotations=None
        self.categories=None


def dict2class(dict, classname):
    object = eval(classname)()
    for key, _ in object.__dict__.items():
        setattr(object, key, dict[key])
    return object


catelist = []
for jcate in settings["category"]:
    catelist.append(dict2class(jcate, "category"))

objinfo = info()
objinfo.description = settings["info"]["description"]
objinfo.contributor = settings["info"]["contributor"]
objinfo.date_created = settings["info"]["date_created"]
objinfo.url = settings["info"]["url"]
objinfo.version = settings["info"]["version"]
objinfo.year = settings["info"]["year"]
if objinfo.date_created == "":
    objinfo.date_created = strftime("%Y-%m-%d %H:%M:%S", gmtime())

imglist = []
annolist=[]

imgidcount = 0

imgpath = os.path.join(settings["envs"]["DataPath"], 'SourceIMG')
imgfiles = [f for f in os.listdir(imgpath) if
            os.path.isfile(os.path.join(imgpath, f)) and f.endswith(settings["envs"]["ImgFmt"])]
for file in imgfiles:
    objimage = image()
    objimage.file_name = file
    img_path = os.path.join(imgpath, file)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    objimage.height, objimage.width = img.shape
    objimage.id = imgidcount
    imgidcount = imgidcount + 1
    imglist.append(objimage)

annoidcount = 0
for cate in catelist:
    gtpath = os.path.join(settings["envs"]["DataPath"], 'gt' + cate.name)
    gtfiles = [f for f in os.listdir(gtpath) if
               os.path.isfile(os.path.join(gtpath, f)) and f.endswith(settings["envs"]["ImgFmt"])]
    for file_name in gtfiles:
        currgtpath = os.path.join(gtpath, file_name)
        print(currgtpath)
        img = cv2.imread(currgtpath, cv2.IMREAD_GRAYSCALE)
        ret, thresh = cv2.threshold(img, 127, 255, 0)

        retval, labels, stats, _ = cv2.connectedComponentsWithStats(thresh)
        for i in range(1, retval):
            if (stats[i][4] > int(settings["envs"]["IgnoreSize"])):
                objanno = annotation()
                objanno.bbox = stats[i][0:3]
                objanno.area = stats[i][4]
                objanno.category_id = cate.id
                image = [f for f in imglist if f.file_name == file_name]
                if len(image) == 1:
                    objanno.image_id = image[0].id
                    objanno.id = annoidcount
                    annoidcount = annoidcount + 1
                    cate_thresh = numpy.zeros(labels.shape, dtype=numpy.uint8)
                    cate_thresh[labels == i] = 255
                    # cv2.imshow("cate",cate_thresh)
                    # cv2.waitKey()
                    encoded = mask.encode(numpy.asfortranarray(cate_thresh))
                    objanno.segmentation = encoded
                    annolist.append(objanno)
                else:
                    print("Error: Can not find image correspond to ", cate.name, " GT File: ", file_name)
            else:
                print("skip 1 object (area:", stats[i][4], ") on ", cate.name, " GT File:", file_name)

print("Total num=", annoidcount)


jsonfile=root()
jsonfile.info = objinfo
jsonfile.annotations=annolist
jsonfile.images = imglist
jsonfile.categories = catelist

def obj_dict(obj):
    return obj.__dict__

# with io.open('gt.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(jsonfile,default=obj_dict))
