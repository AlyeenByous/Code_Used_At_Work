# found from geeksforgeeks and adjusted to fit my needs
from pypdf import PdfReader 

# creating a pdf reader object 
reader = PdfReader('G:\\Culvert_Surveys\\Culvert_List_Pubworks_Report.pdf') 

# testing:
# print the number of pages in the file:
#print(len(reader.pages)) 

# open file to write the data into
file1 = open("CULVERT_LIST_FILE.txt","w+")

for i in range(0,len(reader.pages),1):

	# reader on the page we're iterating to
	page = reader.pages[i]  

	# testing:
	#print(page.extract_text())
	#print("\n")

	# extract the text and write to file1 with blank lines for readability
	file1.write(page.extract_text())
	file1.write("\n\n")

