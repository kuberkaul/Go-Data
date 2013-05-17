#Description: Modified Apriori Algorithm 
#Author: Anahita
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from dbtables import FileInfo,Apriori
import os
import re
import apriori1
import datetime
import operator

aprioridict={}
for i in range(0,60,5):
	aprioridict[i]=[]
alist=Apriori.all()
		
for a in alist:
	#print "All files:",a.timestamp
	if a.timestamp.date()==datetime.datetime.now().date():
		if a.timestamp.hour==datetime.datetime.now().hour:
			aprioridict[a.timestamp.minute-a.timestamp.minute%5].append(a.file_id)
print aprioridict

sequentialAccess=dict()
result=dict()
accessCount=dict()
sequentialAccess1=dict()

for akey in aprioridict.keys():
    values=aprioridict[akey]
    l=len(values)
    for i in range(0,l):
        x=''
        x=values[i]
        if x not in accessCount.keys():
            accessCount[x]=1
        else:
            accessCount[x]+=1
        t=i+1       
        while(t <= l-1):
            a=values[i]
            b=values[t]
            #print a,b
            if (a,b) not in sequentialAccess1.keys():
                sequentialAccess1[a,b]=1
            else:
                sequentialAccess1[a,b]+=1        
            t+=1
    sequentialAccess=(sorted(sequentialAccess1.iteritems(),key=operator.itemgetter(1),reverse=True)) 
    output=(sorted(accessCount.iteritems(),key=operator.itemgetter(1),reverse=True))
#------------Start of Function-------------------------------------------------------------------------   
def getElements():
    output=(sorted(accessCount.iteritems(),key=operator.itemgetter(1),reverse=True))
    sequentialAccess=(sorted(sequentialAccess1.iteritems(),key=operator.itemgetter(1),reverse=True)) 

    #case1: Less than or equal to 4 files ---> take all 4
    if len(accessCount)<=4:
        #print "--case1--"
        for key in output:
            t=key[0]
            result[t]=1
        return result.keys()
        
    #case2: when there are no sequential access instances---> take the 4 most frequent occuring files in logs
    if len(sequentialAccess)==0:
        #print "--case 2--"
        for key in output:
            t=key[0]
            result[t]=1 
            ctr=len(result)
            if ctr==4: 
                return result.keys()

    #case3: this is the general case ---> always selecting files that occur most number of times sequentially before looking at individual access to files per instance
    #print "--case3---"
    for key in sequentialAccess:
        t=key[0]
        a=t[0]
        b=t[1]
        ctr=len(result)
        if ctr<=4:
            result[a]=1
            result[b]=1
            ctr=len(result)
            if len(result)==4:
                return result.keys()                            
    ctr=len(result)
    for key in output:
        if ctr<4:
            t=key[0]
            if t not in result.keys():
                #print key
                result[t]=1    
                ctr+=1      
    return result.keys()
#-----------------------------------EOF------------------------------                                
fileList=getElements()
print fileList
#for fil in fileList:
#    print fil
#for fileName in fileList:
#s    print fileName
