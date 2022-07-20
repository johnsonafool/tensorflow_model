# consider about using process to handle "dark image"
import requests
from pycocotools.coco import COCO

coco = COCO('./test.json')
cat_Ids = coco.getCatIds(catNms=['person'])
imgIds = coco.getImgIds(catIds=cat_Ids)
print(imgIds)
