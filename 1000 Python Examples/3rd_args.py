#change in the naming convention to easy the testing processing while using CMD 

#this is me first time implementing command line arguments 
#note that i have started with 1 instead of 0 as 0 holds the path/name of the file from the eyes sf compiler hence 1 

import sys

#print(sys.argv)
length = int(sys.argv[1])
Breadth = int(sys.argv[2])

print("This is used via command line ", length*Breadth)