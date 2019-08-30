#Importing Libraries
import cv2
import numpy as np


#Function to find hash value
def dhash(image, hashSize = 8):
	
	#Converting to Grey Scale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	#Resiing the image
	resized = cv2.resize(gray, (hashSize+1, hashSize))
	
	#Computing Horizontal Gradient between adjacent columns
	diff = resized[:, 1:] > resized[:, :-1]
	
	#Converitng to HashValue
	return sum([2 ** i for (i,v) in enumerate(diff.flatten()) if v])


#Function to Convert hashvalue to suitable type	
def convert_hash(h):

	#Converting to numpy's 64 bit float and back to python's efault int
	return int(np.array(h, dtype = "float64"))
	

#Function to find hamming Distance
def hamming(a, b):
	
	#Return the hamming distance between images
	return bin(int(a) ^ int(b)).count("1")
	

