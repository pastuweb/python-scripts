
#Script: move all file of a SOURC Dir in a DESTINATION Dir. You can also waht group of file through the third paramater: type

import os, sys
from sys import platform as _platform

num_args = len(sys.argv)

def move(f,src,dst):
	real_dst = dst
	fdst = f
	if f == 'special_file.jar':
		fdst = 'file.jar'
		if _platform == 'win32':
			real_dst = "c:\\"
		else:
			real_dst = "/tmp/folder"
		
	if _platform == 'win32':
		fullPath = src + "\\" + f
		destFullPath = real_dst + "\\" + fdst
		os.system ("move"+ " " + fullPath + " " + destFullPath)
	else:
		fullPath = src + "/" + f
		destFullPath = real_dst + "/" + fdst
		os.system ("mv"+ " " + fullPath + " " + destFullPath)

if num_args <= 3:
    print("Info comando: ", os.path.basename(sys.argv[0]), " source_folder destination_folder type[ tipo1 | tipo2]" )
else:
	src = sys.argv[1]
	dst = sys.argv[2]
	type = sys.argv[3]
	if type in ['tipo1', 'tipo2']:
		if type == 'tipo1':
			listOfFiles = os.listdir(src)
			for f in listOfFiles:
				if f in ['file1.war','file2.war','file3.war','file4.war','file5.war']:
					print(f)
					move(f,src,dst)
				
		elif type == 'tipo2':
			listOfFiles = os.listdir(src)
			for f in listOfFiles:
				if f in ['file6.war','file7.war','file8.war','file9.war']:
					print(f)
					move(f,src,dst)
					
						
	else:
		print("type value can be ONLY tipo1 or tipo2" )

