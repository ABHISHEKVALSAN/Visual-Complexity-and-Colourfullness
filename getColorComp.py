import sys
from imutils import build_montages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
def getComplexity(image):
	return 1
def getColorfullness(image):
	(B, G, R) = cv2.split(image.astype("float"))
	rg = np.absolute(R - G)
	yb = np.absolute(0.5 * (R + G) - B)
	(rbMean, rbStd) = (np.mean(rg), np.std(rg))
	(ybMean, ybStd) = (np.mean(yb), np.std(yb))
	stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
	meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))
	Colourfullness= stdRoot + (0.3 * meanRoot)
	return Colourfullness
def main(path,filename):
	image=cv2.imread(filename)
	Colourfullness=getColorfullness(image)
	path
	imgName=str(int(Colourfullness)).zfill(3)+'p'+str(int((Colourfullness-int(Colourfullness))*1000)).zfill(3)+'.png'
	cv2.imwrite(path+imgName,image)
	Complexity=1#getComplexity(image)

if __name__=="__main__":
	path='/home/abhiavk/git/Visual-Complexity-and-Colourfullness/Training/Webby18/'
	filenames=list(paths.list_images(path))
	for filename in filenames:
		main(path,filename)
