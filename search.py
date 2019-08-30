#Importing Libraries
from src.hashing import *
import argparse
import pickle
import time
import cv2

#Construct arugment parser and parse the arguments
ap = argparse.ArgumentParser()

#Creating Argument to read vptree.pickle file
ap.add_argument("-t", "--tree", required = True, type = str, help = "path to pre build VP Tree")

#Creating Argument to read hashes.pickle file
ap.add_argument("-a", "--hashes", required = True, type = str, help = "path to hashes dictionary")

#Creating Argument for reading query image
ap.add_argument("-q", "--query", required = True, type = str, help = "path of the query image")

#Creating Argument for treshold value for checking
ap.add_argument("-d", "--distance", type = int, default = 15, help= "maximum hamming distance")
args = vars(ap.parse_args())

#Load the VP Tree and Hashes
print("Loading VP-Tree and hashes...")
tree = pickle.loads(open(args["tree"], "rb").read())
hashes = pickle.loads(open(args["hashes"], "rb").read())

#Loading the Query image
image = cv2.imread(args["query"])

#Printig the Query Imge
cv2.imshow("Query", image)

#Computing the hash value
queryHash = dhash(image)

#Converting the hash value
queryhash = convert_hash(queryHash)

#Searching and Matching
print("Searching...")

#Sorting all image with hamming distance less than threshold value
results = tree.get_all_in_range(queryHash, args["distance"])

#Sorting the list to get ordered output
results = sorted(results)

#Checking all the images in results
for (d, h) in results:
	
	#getting path of all images in results
	resultpath = hashes.get(h, [])
	print("{} total image(s) with d: {}".format(len(resultpath), d))
	
	# loop over the result paths
	for rp in resultpath:
		
			# load the result image and display it to our screen
		result = cv2.imread(rp)
		cv2.imshow("Result", result)
		cv2.waitKey(0)
