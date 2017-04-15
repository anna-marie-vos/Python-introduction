import datetime
import os
import glob

# replace listFiles with glob2
# def listFiles ():
#     '''
#     listFiles lists the current directory's
#     files that contain .txt in a list.
#     '''
#     fileList = os.listdir(".")
#     textFiles = []
#     for itemName in fileList:
#         if ".txt" in itemName:
#             textFiles.append(itemName)
#     return textFiles

def createCombinedFile (filesArray,fileName):
    '''
    createCombinedFile takes 2 arguments,
    an array/list of files such as [file1.txt,file2.txt]
     and the fileName which is the current timestamp.txt
     then it combines the files content and adds to the niew
     .txt file.
     '''
    with open(fileName,"a+") as combinedFile:
        for fle in filesArray:
            content = open(fle,'r+').read()
            combinedFile.write(content +"\n")

listFiles = glob.glob("*.txt")
fileName = str(datetime.datetime.now())+".txt"

createCombinedFile(listFiles,fileName)
