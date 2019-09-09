# Image-Search-Engine
This program is used to generate image hashes and compare the input image from the dataset and tell similar images. 
Differece hashig is used to generate the hash code.

(The commands are to be used in Linux Terminal)
# Command to Run index_images and generate VP Tree 
>python index_images.py --images 101_ObjectCategories --tree vptree.pickle --hashes hashes.pickle

# Command to Check Query File
>python searxh.py --tree vptree.pickle --hashes hashes.pickle --query queries/file_name --distance nearer_distance
*distance is optional

