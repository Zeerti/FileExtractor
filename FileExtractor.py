import tarfile
import zipfile
import glob
import os


def _get_List_Of_Files():
	
	os.chdir(os.curdir)

	for file in glob.glob("*.tar.gz"):
		tarFileList.append(file)

	for file in glob.glob("*.zip"):
		zipFileList.append(file)

		
	#for file in glob.glob("*.gz"):
	#	tarFileList.append(file)

	#Convert list array to string
	",".join(str(x) for x in tarFileList)
	",".join(str(x) for x in zipFileList)

def _untar(fileName):
	tar = tarfile.open(fileName)
	tar.extractall()
	tar.close()
	print("Untared File {}".format(fileName))

def _unzip(fileName):

	zip = zipfile.ZipFile(fileName, 'r')
	zip.extractall(os.curdir)
	zip.close()
	print("Unzipped File {}".format(fileName))
	
	'''
	zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
	zip_ref.extractall(directory_to_extract_to)
	zip_ref.close()
	'''




if __name__ == '__main__':

	tarFileList = list()
	zipFileList = list()

	_get_List_Of_Files()

	if(len(tarFileList) >= 1):
		for i in range(len(tarFileList), 0, -1) :
			_untar(tarFileList[i-1])
	else:
		print("No Tar Files Found")

	if(len(zipFileList) >= 1):
		for i in range(len(zipFileList), 0, -1) :
			_unzip(zipFileList[i-1])
	else:
		print("No Tar Files Found")


