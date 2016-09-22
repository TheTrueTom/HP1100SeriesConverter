# -*- coding: utf-8 -*-

import struct
import csv
import os
import tkinter as tk
from decrypter import *
from tkinter.filedialog import askdirectory

ext = "ch"


class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.instructionLabel = tk.Label(self)
		self.instructionLabel.config(text="Welcome ! Please select a folder to start a conversion")
		self.instructionLabel.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=5)

		self.selectButton = tk.Button(self)
		self.selectButton["text"] = "Select folder"
		self.selectButton["command"] = self.selectFolder
		self.selectButton.grid(row=1, column=0, sticky='W')

		self.convertButton = tk.Button(self)
		self.convertButton["text"] = "Convert files"
		self.convertButton["command"] = self.convert
		self.convertButton.grid(row=1, column=1, sticky='W')
		self.convertButton.config(state='disabled')

		self.statusText = tk.Label(self)
		self.statusText.config(text="No job in progress")
		self.statusText.config(width=40)
		self.statusText.grid(row=1, column=2)

		self.quit = tk.Button(self, text="Quit", fg="red", command=root.destroy)
		self.quit.grid(row=1, column=3, sticky='E')

	def convert(self):
		#print("Converting")
		self.convertButton.config(state='disabled')
		if self.selectedPath != None:
			decrypter = Decrypter(self.selectedPath, self)

	def selectFolder(self):
		#print("Selecting folder")
		self.selectedPath = askdirectory(parent=root, title='Choose a folder')

		if self.selectedPath != None:
			self.convertButton.config(state='normal')

			experimentList = []

			for fRoot, subFolders, files in os.walk(self.selectedPath):
				for fichier in files:
					if fichier[-2:] == '.B':
						# New experiment
						experimentList.append(fRoot)

			text = "Found " + str(len(experimentList)) + " experiments"
			self.instructionLabel.config(text="Click on the 'Convert files' button to transform files into CSV files or select another folder")
			self.statusText.config(text=text)

# Create windows reference
root = tk.Tk()

# Change app icon
basePath = sys._MEIPASS
prepath = os.path.join(basePath, 'icon')
path = os.path.join(prepath, 'icon.ico')
root.iconbitmap(default=path)

# Create application
app = Application(master=root)
app.master.title("Agilent Data Converter")
app.master.minsize(500,60)
app.master.maxsize(650,60)

# Run Application
app.mainloop()
