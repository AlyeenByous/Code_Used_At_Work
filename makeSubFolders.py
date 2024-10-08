# Use case: each road segment has an ID, and has culverts on the road with unique IDs.
# Using a text file with the culvert IDs listed,
# and using a file with all of the street segments listed,
# We're going to go to the root folder that will hold subfolders of every segment,
# Make sure they're already there,
# then iterate through every segment folder and add subfolders for every culvert on that segment.
# a dictionary holds a key for the segment ID and a list as the value that contains every culvert on that segment.
# Every culvert ID contains the segment ID it's on, with a unique identifier at the end.


import os
import re

# open file with all of the culverts listed 
# PDF report generated from PubWorks 
myfile = open('CULVERT_LIST_FILE.txt', 'r')

# open the file with all of the segment names
# Generated from the PDF report 
segmentnamefile = open('CULVERT_STREET_SEGMENTS.txt', 'w+')

# path to the segments folder
newpath=r'G:\\Culvert_Surveys\\_segments'

# all of the lines in myfile
# don't need anymore since we iterate through the lines later
# keeping for future reference if needed:
#lines = myfile.readlines() 


#dictionary to hold the segment ids and the culvert ids
segmentDict = {}

# lists to hold the segment ids and the culvert ids
segIdList = []  #segment IDs
culvIdList = []  #culvert IDs

# get the ids from the text files and save into the lists
segID = 'x' #placeholder value
segidx = 0 #placeholder value

# iterate through each line, find the segment and culvert ids according to criteria, then save to respective list.
for i,line in enumerate(myfile.readlines()):
	
	# finding the segment id
	if '/' in line:  
		if 'Features' in line:  
			continue
		segidx=0
		while not line[segidx].isspace():
			segidx += 1  
		segID = line[0:segidx] 
		if segID == 'Yes':
			continue
		segIdList.append(segID) 

	# find the culvert id
	if 'Yes' in line:  
		startIdx = line.find('SC')  
		idx = startIdx 
		endIdx = startIdx
		#print(startIdx)
		while not line[idx].isspace():  
			endIdx += 1
			idx += 1
		culvertId = line[startIdx:endIdx]  
		culvIdList.append(culvertId)  

# testing:
#print(culvIdList)
#print(segIdList)

# make a dictionary with the segId as the key
for elem in segIdList:
	segmentDict.update({elem: []})

# check each culvert id, if the culvid contains a segment id, add it to the value list in the dict for the corresponding key
for item in segIdList:
	for items in culvIdList:
		if item in items: 
			segmentDict[item] += [items] 

# testing:
#print(segmentDict['135S05'])

# check the path and verify the folders exist
rootpath='G:\\Culvert_Surveys\\_segments_add_culverts'
dir = os.listdir(rootpath)
if len(dir) == 0:
	print(" ROOT EMPTY")
else:
	print("ROOT NOT EMPTY")

# iterate through every segment folder in the root folder
for subdir in dir:

	# for each segment folder, check to see if it's empty, if it is empty, make the corresponding culvert folders.
	dirname = rootpath + '\\' + subdir  
	sdir = os.listdir(dirname)
	if len(sdir) == 0:  
		# testing:
		#print("Directory {0}: EMPTY".format(subdir))
		
		# get the segment id as sid
		sx=0
		while not subdir[sx].isspace():
			sx += 1
		sid = subdir[0:segidx]
		#print(sid)
		
		# find the key sid and make culvert folders within, checking again to make sure that it doesn't exist first
		for valu in segmentDict[sid]:
			newpath = dirname + '\\' + valu  
			#print(newpath)
			if not os.path.exists(newpath): 
				os.makedirs(newpath)
		
		
	# if the segments folder is not empty, do not make more culvert folders
	else:  
		print('dir has subdirs')
			

myfile.close()
segmentnamefile.close()
