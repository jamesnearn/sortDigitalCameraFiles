#   Sorts files from:
#   
#   File0001.jpg
#   File0002.jpg
#   File0003.jpg
#   File0004.jpg
#   File0005.jpg
#   
#   yyyy/yyyy mm dd/File0001.jpg
#   yyyy/yyyy mm dd/File0002.jpg
#   yyyy/yyyy mm dd/File0003.jpg
#   yyyy/yyyy mm dd/File0004.jpg
#   yyyy/yyyy mm dd/File0005.jpg

#   Todo:
#   add command line parameter
#   add awareness of OS to know which slash to use in the path

import getopt
import os
import time
import shutil
import sys

def sortFiles(givendir, separator):
    for (dirpath, dirnames, filenames) in os.walk(givendir):
        for filename in filenames:
            if (filename.lower().endswith(".jpg") or filename.lower().endswith(".mp4") or filename.lower().endswith(".mts") or filename.lower().endswith(".mov")):
                parseFile(dirpath, filename, separator)

def parseFile(givenDirectoryPath, givenFilename, separator):
    givenFullFilepath = os.path.join(givenDirectoryPath, givenFilename)
    print(givenFullFilepath)
    
    newPath = getDestinationPath(givenFullFilepath, separator)
    newPath = os.path.join(givenDirectoryPath, newPath)
    print(newPath)
    
    if not os.path.exists(newPath):
        os.makedirs(newPath)

    print(newPath + separator + givenFilename)
    os.rename(givenFullFilepath, newPath + separator + givenFilename)

def getDestinationPath(givenFullFilepath, separator):
    epochSec = os.path.getmtime(givenFullFilepath)
    convertedDate = time.ctime(epochSec)
    newPath = time.strftime('%Y' + separator + '%Y %m %d', time.localtime(epochSec))
    return newPath


def main(argv):
    separator = "\\"     #default value
    path = ""
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["separator=","path="])
    except getopt.GetoptError:
        print('SortFiles.py --separator <value> --path <path>')
        print('Number of arguments:', len(sys.argv), 'arguments.')
        print('Argument List:', str(sys.argv))
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--help':
            print('SortFiles.py --separator <value> --path <path>')
            sys.exit()
        elif opt in ("--separator"):
            separator = arg
        elif opt in ("--path"):
            path = arg

    print('Separator = ', separator)
    print('Path = ', path)
    sortFiles(path, separator)

if __name__ == "__main__":
    if (sys.argv[1] == "runtests"):
        print('Running tests')
    else:
        main(sys.argv[1:])  

#separator = '\\'
#separator = '/'

#sortFiles(".")
#sortFiles('C:\\_data\\104D7000\\100NIKON')
