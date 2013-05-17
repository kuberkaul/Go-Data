#!/usr/bin/python

import Tkinter, Tkconstants, tkFileDialog
from tkFileDialog import askopenfilename
from Tkinter import *
import Tkinter as tk
import sys, Tkinter
sys.modules['tkinter'] = Tkinter
from tkinter import *
import tkFileDialog
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
import Tkinter, Tkconstants, tkFileDialog
from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style
from ttk import Entry
import client
import cache2
import sys
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import os
import urllib
import urllib2
import cookielib
import re
import getpass
import requests


FileInfo={}
FileInfo['Filename']=[]
FileInfo['Size']=[]
FileInfo['User']=[]
FileInfo['Time']=[]
FileInfo['ContentType']=[]
class TkFileDialogExample(Tkinter.Frame):
	def __init__(self, root):
		register_openers()
		Tkinter.Frame.__init__(self, root)
		self.root = root
		self.root.title("GoData Client Module")
		self.grid()
		Style().configure("TButton", padding=(0, 5, 0, 5), 
          	font='serif 10')
        
       		self.root.columnconfigure(0, pad=3)
        	self.root.columnconfigure(1, pad=3)
        	self.root.columnconfigure(2, pad=3)
        	self.root.columnconfigure(3, pad=3)
		self.root.columnconfigure(4, pad=3)
        
       		self.root.rowconfigure(0, pad=3)
        	self.root.rowconfigure(1, pad=3)
        	self.root.rowconfigure(2, pad=3)
        	self.root.rowconfigure(3, pad=3)
        	self.root.rowconfigure(4, pad=3)
		self.root.rowconfigure(5, pad=3)
		self.root.rowconfigure(6, pad=3)
		self.root.rowconfigure(7, pad=3)
		self.root.rowconfigure(8, pad=3)
		self.root.rowconfigure(9, pad=3)
		self.root.rowconfigure(10, pad=3)
		self.root.rowconfigure(11, pad=3)
		self.root.rowconfigure(12, pad=3)
		self.root.rowconfigure(13, pad=3)
		self.root.rowconfigure(14, pad=3)
		self.root.rowconfigure(15, pad=3)
		self.root.rowconfigure(16, pad=3)
		self.root.rowconfigure(17, pad=3)
		self.root.rowconfigure(18, pad=3)
		self.root.rowconfigure(19, pad=3)
		self.root.rowconfigure(20, pad=3)
		self.root.rowconfigure(21, pad=3)
		self.root.rowconfigure(22, pad=3)

		self.root.rowconfigure(0, weight=1)
        	self.root.columnconfigure(0, weight=1)
		global e
		e = Entry(self, width=4)
		e.grid(row=16, column=4)
		e.focus_set()
		
		#self.button = Button(self, text="Upload", fg="red", command=self.logout)
		#self.button.pack(side = RIGHT)
		
		
  		button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
		a = Tkinter.Button(self, text='Browse', command=self.askopenfilename)#.pack(**button_opt)
		a.grid(row =1 , column =4)		
		b = Tkinter.Button(self, text='Upload', command=self.upload)#.pack(**button_opt)
		b.grid(row = 3, column =4)		
		
		f=client.doCmd({"cmd":"view"})
		for i in f:
			FileInfo[i.split(":")[0]].append(i.split(":")[1].split("/")[-1])		
		
		print FileInfo
       		t = SimpleTable(self, len(f)/5,5)
		t.grid(row = 4, column =4)
		
		#MyButton1 = Button(self, text="Download 5", width=14, command=self.Download)
		#MyButton1.grid(row=15, column=4)

		#MyButton2 = Button(self, text="Download 6", width=14, command=self.Download)
		#MyButton2.grid(row=15, column=5)

		#MyButton3 = Button(self, text="Download 7", width=14, command=self.Download)
		#MyButton3.grid(row=15, column=6)	
	
		#MyButton4 = Button(self, text="Download 4", width=14, command=self.Download)
		#MyButton4.grid(row=15, column=3)

		#MyButton5 = Button(self, text="Download 3", width=14, command=self.Download)
		#MyButton5.grid(row=15, column=2)

		#MyButton6 = Button(self, text="Download 2", width=14, command=self.Download)
		#MyButton6.grid(row=15, column=1)

		#MyButton7 = Button(self, text="Download 1", width=14, command=self.Download)
		#MyButton7.grid(row=15, column=0)

		#MyButton8 = Button(self, text="Download 8", width=14, command=self.Download)
		#MyButton8.grid(row=15, column=7)

		MyButton9 = Button(self, text="Download", width=14, command=self.callback)
		MyButton9.grid(row=17, column=4)

		creation = tk.Label( self, text = "Created by Kuber, Digvijay, Anahita & Payal", borderwidth =5, width =45)
		creation.grid(row=50 , column = 4)
		

	
		self.file_opt = options = {}		
  		options['defaultextension'] = '.txt'
  		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
  	        options['initialdir'] = 'C:\\'
  		options['initialfile'] = 'myfile.txt'
  	        options['parent'] = root
  	        options['title'] = 'Browse'

		self.dir_opt = options = {}
  		options['initialdir'] = 'C:\\'
  		options['mustexist'] = False
  		options['parent'] = root
  		options['title'] = 'Browse'

		image = Image.open("./header.png")
		photo = ImageTk.PhotoImage(image)
		label = Label(image=photo)
		label.image = photo # keep a reference!
		label.place(width=768, height=576)
		label.grid(row = 0 , column = 0 )
		label.pack(side = TOP)

		self.centerWindow()
		self.master.columnconfigure(10, weight=1)
		#Tkinter.Button(self, text='upload file', command=self.Fname).pack(**button_opt)	
		t = self.file_name = Text(self, width=39, height=1, wrap=WORD)
		t.grid(row = 2, column =4)
		extra1 = tk.Label(self, text = "please give a file number", borderwidth = 5, width =45)
		extra1.grid(row =15, column =4)
		#self.file_name.pack()
		#self.txt = Text(self)
     		#self.txt.pack(fill= BOTH, expand=1)
	
	def askopenfilename(self):
   
      	 """Returns an opened file in read mode.
       	This time the dialog just returns a filename and the file is opened by your own code.
       	"""
   
       # get filename
       	 filename = tkFileDialog.askopenfilename(**self.file_opt)
   
       # open file on your own
       	 if filename:
         	self.file_name.insert(0.0, filename)
		
	def upload(self):
		print "enter logout logic here"
		f=client.doCmd({"cmd":"upload"})
	   	url=f
	    	print url
		fl=str(self.file_name.get("1.0", END)).strip()
	    	datagen, headers = multipart_encode({"sublet": open(fl, "rb")})
	   	request = urllib2.Request(url, datagen, headers)
		print urllib2.urlopen(request).read() 
	    	cache2.getRequest(fl)
		del FileInfo['Filename'][:]
		del FileInfo['Size'][:]
		del FileInfo['User'][:]
		del FileInfo['Time'][:]
		del FileInfo['ContentType'][:]
		f=client.doCmd({"cmd":"view"})
		count = 1
		count1 = 1		
		for i in f:
			count += 1
			#if count < 10:
			FileInfo[i.split(":")[0]].append(i.split(":")[1].split("/")[-1])
			count1 += 1		
		print FileInfo
       		t = SimpleTable(self, len(f)/5,5)
        	t.pack(side="bottom", fill="y")


		
	def callback(self):
		print "enter Download logic here"
		print FileInfo['Filename'][int(e.get())-1]
    		if (not cache2.inCache(FileInfo['Filename'][int(e.get())-1])):
			(fid,filename)=client.doCmd({"cmd":"getFile","filename":FileInfo['Filename'][int(e.get())-1]})
    			print fid
    			url='http://godatacloud.appspot.com/file/'+fid+'/download'
    			print url
			cache2.updateCache(filename,url)
		else:
			print "File served from cache folder.Please check"

		
		
	

	def centerWindow(self):
      
       	 w = 290
       	 h = 150

       	 sw = self.master.winfo_screenwidth()
       	 sh = self.master.winfo_screenheight()
        
       	 x = (sw - w)/2
       	 y = (sh - h)/2
       	 self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=6, columns=4):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="blue")
        self._widgets = []
        for row in range(rows):
	    print row
	    current_row = []
	    if row == 0:
		for column in range(columns):
			label1 = tk.Label(self, text = "Filename" , borderwidth = 3, width =20)
			label1.grid(row = 0, column = 0, sticky = "nsew", padx =4, pady =4)
           		label2 = tk.Label(self, text = "Size" , borderwidth = 3, width =20)
			label2.grid(row = 0, column = 1, sticky = "nsew", padx =4, pady =4)
           		label3 = tk.Label(self, text = "User" , borderwidth = 3, width =20)
			label3.grid(row = 0, column = 2, sticky = "nsew", padx =4, pady =4)
           		label4 = tk.Label(self, text = "Time" , borderwidth = 3, width =20)
			label4.grid(row = 0, column = 3, sticky = "nsew", padx =4, pady =4)
           		label5 = tk.Label(self, text = "ContentType" , borderwidth = 3, width =20)
			label5.grid(row = 0, column = 4, sticky = "nsew", padx =4, pady =4)
            
	    else:
		for column in range(columns):
		# insert what you want to insert in here
			#print FileInfo['Filename'][column]
                	label = tk.Label(self, text="%s" % (FileInfo['Filename'][row-1]), borderwidth=2, width=20)
			#button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
			#Tkinter.Button.self.pack()
			#button = Button(self, text='Download File', command=self.Download).pack()
			#label4 = tk.Label( self, text = "%s/%s" % (row, column), borderwidth =2, width =20)
			#label4.grid(row = row, column = column, sticky = "nsew", padx=2, pady=2)
                	label.grid(row=row, column=0, sticky="nsew", padx=2, pady=2)
			#button.bind('button', get_value)  
                	current_row.append(label)
			label4 = tk.Label( self, text = "%s" % (FileInfo['Size'][row-1]), borderwidth =2, width =20)
			label4.grid(row = row, column = 1, sticky = "nsew", padx=2, pady=2)
			label2 = tk.Label( self, text = "%s" % (FileInfo['User'][row-1]), borderwidth =2, width =20)
			label2.grid(row = row, column = 2, sticky = "nsew", padx=2, pady=2)
			label3 = tk.Label( self, text = "%s" % (FileInfo['Time'][row-1]), borderwidth =2, width =20)
			label3.grid(row = row, column = 3, sticky = "nsew", padx=2, pady=2)
			label5 = tk.Label( self, text = "%s" % (FileInfo['ContentType'][row-1]), borderwidth =2, width =20)
			label5.grid(row = row, column = 4, sticky = "nsew", padx=2, pady=2)

			#retag("special", a_frame, a_label, a_button)
			#tk.bind_class("special", "<Button>", on_frame_click)
          		self._widgets.append(current_row)
		

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)
	
    def Download(self):
		print "enter Download logic here"
		 
    def get_value(self):
		print " Get value "


if __name__=='__main__':
     root = Tkinter.Tk()
     TkFileDialogExample(root).pack()
     root.mainloop()
   
