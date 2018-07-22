import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import pdb
sets=[('Adachi','train'),('Adachi','val'), ('Chiba','train'), ('Chiba','val'),('Ichihara','train'), ('Ichihara','val'),('Muroran','train'), ('Muroran','val'), ('Nagakute','train'), ('Nagakute','val') ,('Numazu','train'), ('Numazu','val'), ('Sumida','train'), ('Sumida', 'val')]

classes = ["D00", "D01", "D10", "D11", "D20", "D40", "D43", "D44"]

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(location, image_id):
    in_file = open('RoadDamageDataset/%s/Annotations/%s.xml'%(location, image_id))
    out_file = open('RoadDamageDataset/%s/labels/%s.txt'%(location, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()
#pdb.set_trace()
for location, image_set in sets:
    if not os.path.exists('RoadDamageDataset/%s/labels/'%(location)):
        os.makedirs('RoadDamageDataset/%s/labels/'%(location))
    image_ids = open('RoadDamageDataset/%s/ImageSets/Main/%s.txt'%(location, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(location, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/RoadDamageDataset/%s/JPEGImages/%s.jpg\n'%(wd, location, image_id))
            #convert_annotation(year, image_id)
    list_file.close()

os.system("cat Adachi_train.txt Chiba_train.txt Chiba_val.txt Ichihara_train.txt Ichihara_val.txt Muroran_train.txt Muroran_val.txt Nagakute_train.txt Nagakute_val.txt Numazu_train.txt Numazu_val.txt Sumida_train.txt Sumida_val.txt > train.txt")
os.system("cat Adachi_train.txt Chiba_train.txt Ichihara_train.txt Muroran_train.txt Nagakute_train.txt Numazu_train.txt Sumida_train.txt > train_all.txt")


