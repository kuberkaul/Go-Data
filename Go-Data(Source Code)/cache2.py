#Description: Randomized Marking Cache Algorithm


#Changes to be made: Update the following variables: path, file_request, srcDirectory, descDirectory, replace shutil.copyfile(srcFile,destFile) on lines 74 and 88 so that you now copy a file from cloud to your cache

import random
import shutil
import threading
import os
from time import time, sleep
import urllib
import urllib2
import cookielib
import re
import getpass

path='/home/digvijay/Desktop/cache/'
cache={}

count=0
cacheHit=0
cacheMiss=0

#Initializes the cache for the first time... Check if you have any other junk file getting created as I have got .DS_Store and handle it as done below
def initCache():
    cacheCount=0
    #Check number of elements in cache
    for file in os.listdir(path):
        junk='.DS_Store'
        print file
        if file != junk:
            cacheCount+=1
            cache[file]=0
        #if(cacheCount==5):
            #break
    #print cache    

#This is the initial request that happens... Replace the string in file_request with the name of downloaded or uploaded file
def getRequest(filename):
    file_request='null'
    sleep(10)
    file_request=filename
    updateCache(file_request,"")
          
def inCache(file_request):
    if file_request in cache.keys():
	return True
    else:
        return False

def copyfile(file_request,url):
	response=urllib2.urlopen(url)
	localFile = open(file_request, 'w')
	localFile.write(response.read())
	response.close()
	localFile.close()

	
	
#This function updates the cache as per request received       
def updateCache(file_request,url):
    initCache()
    print cache
    count=0
    global cacheHit
    global cacheMiss
    cacheSize=5
    if file_request in cache.keys():
        print "file_request in cache.keys"
        cache[file_request]=1
        cacheHit+=1
    else:
        print "file_request NOT in cache.keys"
        cacheMiss+=1
        for value in cache.values():
            if value==1:
                count+=1
        #srcDirectory would now be from Cloud...Update it 
#        srcDirectory='/home/digvijay/Desktop/'
#        srcFile=srcDirectory+file_request
        #destDirectory---update this as per your directory structure
        destDirectory='/home/digvijay/Desktop/cache/'
        destFile=destDirectory+file_request.split('/')[-1]
        #print srcFile,destFile       
        if count==cacheSize:
            for eachKey in cache.keys():
                cache[eachKey]=0  
            keyToBeDeleted=random.choice(cache.keys())
            valueToBeDeleted=cache[keyToBeDeleted]
            del cache[keyToBeDeleted]
            fileToBeDeleted=destDirectory+keyToBeDeleted
            os.remove(fileToBeDeleted)
            print "Deleted from cache:",keyToBeDeleted   
            print "Current cache is:",cache   
            cache[file_request]=1
	    if (url!=""):
		copyfile(destFile,url)
	    else:
		shutil.copyfile(file_request,destFile)
            print "Added to cache:",file_request
            print "Current cache is:",cache
                      
        else:
        #When we have some zero marked elements, randomly delete one 
            for key in cache.keys():
                if(cache[key]==0):
                    del cache[key]
                    fileToBeDeleted=destDirectory+key
                    os.remove(fileToBeDeleted)
                    print "Deleted from cache:",fileToBeDeleted
                    print "Current cache is:",cache
                    cache[file_request]=1
       		    if (url!=""):
			copyfile(destFile,url)
		    else:
			shutil.copyfile(file_request,destFile)

                    print "Added to cache:",file_request
                    print "Current cache is:",cache
                    break
                
    print cache

def runTestCases():
    print "---------Running text cases---------"
    test4='data_usage.png'
    test2='graph.png'
    test1='graph_search.png'
    test3='noomq2.png'
    updateCache(test1)
    print "-------next case--------"
    updateCache(test2)
    print "-------next case--------"
    updateCache(test3)
    print "-------next case--------"
    updateCache(test4)
    print "Cache Hit",cacheHit
    print "Cache Miss",cacheMiss

#initCache()
#monitorCachefile3.txt()
#getRequest()
#monitorCache()
#runTestCases()
