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

sets = ['road_1','road_2','road_3','road_4','road_5','Adachi','Chiba','Ichihara','Muroran','Nagakute','Numazu','Sumida']
#path = getcwd()+'/road_preprocess/road_1/JPEGImages_2/'
# #files= os.listdir(path)  

# for root, dirs, files in os.walk(path):  
#  	#pdb.set_trace()
#  	for f in files:  
#  		if f == '.DS_Store':
#  			pass
#  		else:
#  			fp = os.path.join(root, f)  
#  			img = Image.open(fp)  
#  			img.resize((600, 600)).save(os.path.join(path, f), "JPEG")  
#  			print ('fp')  
num = 0
R_channel = 0  
G_channel = 0  
B_channel = 0 
for set in sets:
    filepath = getcwd() + '/road_preprocess/'+ set + '/JPEGImages/'
    pathDir = os.listdir(filepath)  
    w,h = 600,600
    for idx in range(len(pathDir)):  
    	filename = pathDir[idx]
    	if filename == '.DS_Store':
    		pass
    	else:  
    		img = imread(os.path.join(filepath, filename))  
    		R_channel = R_channel + np.sum(img[:,:,0])  
    		G_channel = G_channel + np.sum(img[:,:,1])  
    		B_channel = B_channel + np.sum(img[:,:,2])  
    	#pdb.set_trace()
    num += len(pathDir) * w * h # image size  
R_mean = R_channel / num  
G_mean = G_channel / num  
B_mean = B_channel / num  

print("R_mean is %f, G_mean is %f, B_mean is %f" %(R_mean, G_mean, B_mean))  

#
#for set in sets:
#	filepath = getcwd() + '/road_preprocess/'+ set + '/JPEGImages/'
#	pathDir = os.listdir(filepath) 
#	for idx in range(len(pathDir)):  
#		filename = pathDir[idx]
#		if filename == '.DS_Store':
#			pass
#		else: 
#			img = cv2.imread(os.path.join(filepath, filename), cv2.IMREAD_UNCHANGED).astype(np.float32)
#			img[0] -= R_mean
#			img[1] -= G_mean
#			img[2] -= B_mean
#			cv2.imwrite(os.path.join(getcwd()+ '/road_preprocess/' + set + '/JPEGImages_new/' , filename),img)
#
#
