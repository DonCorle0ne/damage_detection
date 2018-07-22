from PIL import Image  
import os  
import os.path  
from os import listdir, getcwd
from os.path import join
import sys  
import pdb
import matplotlib.pyplot as plt  
import numpy as np  
from scipy.misc import imread 
import cv2

set = ['road_1','road_2','road_4','road_3','road_5']
road_720p = ['road_1','road_2','road_4']
road_1080p = ['road_3','road_5']

for road in set:
	path = getcwd()+'/road_preprocess/'+ road + '/JPEGImages/'  
	for root, dirs, files in os.walk(path):  
		for f in files:  
			if f == '.DS_Store':
				pass
			else:
				fp = os.path.join(root, f)  
				img = Image.open(fp)  
				img.resize((600, 600)).save(os.path.join(path, f), "JPEG")  
				print (fp)  
