#Importing Libraries
from src.hashing import *
from imutils import paths
import argparse
import pickle
import vptree
import cv2

#Construct Argument Parser and Parse the arguments
ap = argparse.ArgumentParser()

#Creating Argument for image dataset path
ap.add_argument("-i", "--images", required = True, type = str, help = "path to input directory of images")

#Creating Argument for output vptree.pickle file
ap.add_argument("-t", "--tree", required = True, type = str, help = "path to output VP Tree")

#Creating Argument for output hashes.pickle file
ap.add_argument("-a", "--hashes", required =True, type = str, help= "path pf output hashes dictionary")
args = vars(ap.parse_args())

#Read the input path of images
imagePath = list(paths.list_images(args["images"]))

#Initialising ahshes dictionary
hashes = {}

#Looping over all the images
for (i, imagePath) in enumerate(imagePath):

	print("[Processig image {}/{}".format(i+1, len(imagePath)))
	
	#Readig Image
	image = cv2.imread(imagePath)
	
	#Compute the HashValue
	h = dhash(image)
	
	#Converting the hash value
	h = convert_hash(h)
	
	#Updating dictionary of hashes
	l = hashes.get(h, [])
	
	#Storig Hash Value in the list
	l.append(imagePath)
	hashes[h] = l
	
#Building VP Tree
print("Building VP TREE...")
points = list(hashes.keys())
tree = vptree.VPTree(points, hamming)


# serialize the VP-Tree to disk
print("Serializing VP-Tree...")
f = open(args["tree"], "wb")
f.write(pickle.dumps(tree))
f.close()
 
# serialize the hashes to dictionary
print("Serializing hashes...")
f = open(args["hashes"], "wb")
f.write(pickle.dumps(hashes))
f.close()


