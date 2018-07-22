import os
import re
from natsort import natsorted
from tqdm import tqdm
PATH_TO_FOLDER = "/home/yijian/alexnet/darknet/road_preprocess/road_5/Annotations/"
if not os.path.exists('/home/yijian/alexnet/darknet/road_preprocess/road_5/Annotations_2/'):
        os.makedirs('/home/yijian/alexnet/darknet/road_preprocess/road_5/Annotations_2/')
PATH_TO_SAVE = "/home/yijian/alexnet/darknet/road_preprocess/road_5/Annotations_2/"

# for road_3 and road_5 uncomment below
wid = (5 / 16)
hgt = (5 / 9)

# #for road_1 2 and 4 uncomment below
#hgt = (5/6)
#wid = (15/32)

_HEIGHT_SUB_PATTERN = r'<height>{}</height>'
_WIDTH_SUB_PATTERN = r'<width>{}</width>'
_XMIN_SUB_PATTERN = r'<xmin>{}</xmin>'
_YMIN_SUB_PATTERN = r'<ymin>{}</ymin>'
_XMAX_SUB_PATTERN = r'<xmax>{}</xmax>'
_YMAX_SUB_PATTERN = r'<ymax>{}</ymax>'


def search(b):
    nline = None
    try:
        nline = re.sub(_HEIGHT_SUB_PATTERN.format("\d+"),
                       _HEIGHT_SUB_PATTERN.format(
                           int(int(re.search(_HEIGHT_SUB_PATTERN.format("(\d+)"), b).group(1)) * hgt)), b)

    except AttributeError:
        pass

    try:
        nline = re.sub(_WIDTH_SUB_PATTERN.format("\d+"),
                       _WIDTH_SUB_PATTERN.format(
            int(int(re.search(_WIDTH_SUB_PATTERN.format("(\d+)"), b).group(1)) * wid)), b)
    except AttributeError:
        pass

    try:
        nline = re.sub(_XMIN_SUB_PATTERN.format("\d+"),
                       _XMIN_SUB_PATTERN.format(
            int(int(re.search(_XMIN_SUB_PATTERN.format("(\d+)"), b).group(1)) * wid)), b)
    except AttributeError:
        pass

    try:
        nline = re.sub(_YMIN_SUB_PATTERN.format("\d+"),
                       _YMIN_SUB_PATTERN.format(
            int(int(re.search(_YMIN_SUB_PATTERN.format("(\d+)"), b).group(1)) * hgt)), b)
    except AttributeError:
        pass

    try:
        nline = re.sub(_XMAX_SUB_PATTERN.format("\d+"),
                       _XMAX_SUB_PATTERN.format(
            int(int(re.search(_XMAX_SUB_PATTERN.format("(\d+)"), b).group(1)) * wid)), b)
    except AttributeError:
        pass

    try:
        nline = re.sub(_YMAX_SUB_PATTERN.format("\d+"),
                       _YMAX_SUB_PATTERN.format(
            int(int(re.search(_YMAX_SUB_PATTERN.format("(\d+)"), b).group(1)) * hgt)), b)
    except AttributeError:
        pass

    if nline is not None:
        return nline
    else:
        return b


if __name__ == '__main__':
    for file in (os.listdir(os.chdir(PATH_TO_FOLDER))):
        # fn = open(file,'r')
        # ff = open(os.path.join(PATH_TO_SAVE,file),'a')
        print('file: {}'.format(file))
        if re.search(r'.xml', file):
            with open(file, 'r') as f:
                with open(os.path.join(PATH_TO_SAVE, file), 'w') as ff:
                    b = f.readline()
                    while b != "":
                        nline = search(b)
                        ff.write(nline)
                        b = f.readline()
