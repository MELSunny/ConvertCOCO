
import os
import cv2
import numpy

import json
import io
DATA_PATH=r"Test"
GT_PATH=os.path.join(DATA_PATH,"gt")
IMG_FMT=".png"

class myimage:
    def __init__(self):
        self.file_name=None
        self.id=None
        self.width=None
        self.height=None

class mycategory:
    def __init__(self):
        self.id=None
        self.name=None
        self.supercategory=None

class myannotation:
    def __init__(self):
        self.segmentation=None
        self.area=None
        self.image_id=None
        self.bbox=None
        self.category_id=None
        self.id=None
        self.iscrowd=0


class mysegmentation:
    def __init__(self):
        self.counts=None
        self.size=None

class root:
    def __init__(self):
        self.info=None
        self.images=None
        self.licences=None
        self.annotations=None
        self.categories=None

catepolyp=mycategory()
catepolyp.id=1
catepolyp.name=""
catepolyp.supercategory=""
annoid=0

imageslist=[]
annolist=[]
gtfiles = [f for f in os.listdir(GT_PATH) if os.path.isfile(os.path.join(GT_PATH, f)) and f.endswith(IMG_FMT)]
for file in gtfiles:
    myimg=myimage()
    myimg.file_name=file
    dbname, rest = file.split('_')
    imgnum, _ = rest.split('.')
    if dbname=="CVC-300":
        myimg.id=1*10000+int(imgnum)
    elif dbname=="CVC-612":
        myimg.id = 2 * 10000 + int(imgnum)
    img_path = os.path.join(GT_PATH, file)

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    myimg.height,myimg.width = img.shape
    imageslist.append(myimg)
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, 2)
    if len(contours)>1:
        print("warn: find more than 1 object on",dbname ,imgnum)

    for cnt in contours:
        if(cv2.contourArea(cnt)>20):
            myanno = myannotation()
            myanno.bbox = cv2.boundingRect(cnt)
            myanno.area= cv2.contourArea(cnt)
            myanno.category_id=1
            myanno.image_id=myimg.id
            myanno.id=annoid
            annoid=annoid+1
            annolist.append(myanno)
        else:
            print("skip 1 object (area:",cv2.contourArea(cnt)+1,") on", dbname, imgnum)
print "totalnum=",annoid



jsonfile=root()
jsonfile.annotations=annolist
jsonfile.images=imageslist
jsonfile.categories=[catepolyp]

def obj_dict(obj):
    return obj.__dict__

with io.open('gt.json', 'w', encoding='utf-8') as f:
    f.write(unicode(json.dumps(jsonfile,default=obj_dict)))

    # img = cv2.imread(img_path, as_grey=True)
    # img=img_as_ubyte(img)
    # myimg.height,myimg.width = img.shape
    # imageslist.append(myimg)
    # arrimg = numpy.asfortranarray(img)
    #
    # encoded = encode(arrimg)
    # # areas=area(encoded)
    # bboxes=toBbox(encoded)
    # print (dbname, imgnum)
    # if (areas.size>1):
    #     print ('Warn:',dbname,imgnum,"has more than 1 object")
    # for i in range(0,areas.size):
    #     myanno = myannotation()
    #     if areas.size==1:
    #         myanno.area=areas
    #         myanno.bboxes=bboxes
    #     else:
    #         myanno.area=areas[i]
    #         myanno.bboxes=bboxes[i]
    #     myanno.category_id=1
    #     myanno.imageid=myimg.id
    #     myanno.id=annoid
    #     annoid=annoid+1
    #     annolist.append(myanno)
