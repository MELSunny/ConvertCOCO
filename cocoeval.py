import numpy as np
import pylab

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

pylab.rcParams['figure.figsize'] = (10.0, 8.0)
annType = ['segm','bbox','keypoints']
annType = annType[1]      #specify type here
prefix = 'person_keypoints' if annType=='keypoints' else 'instances'
print('Running demo for *%s* results.' % (annType))

annFile = 'gt.json'
cocoGt=COCO(annFile)
resFile = 'result.npy'
res=np.load(resFile)
cocoDt=cocoGt.loadRes(res)

cocoEval = COCOeval(cocoGt,cocoDt,annType)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
