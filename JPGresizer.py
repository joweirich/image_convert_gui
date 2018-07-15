import sys
from PyQt4 import QtCore, QtGui
from PictureResizeUI import Ui_PictureResize 
from os.path import isfile, splitext,split
from os import system
from numpy.core.fromnumeric import size

class PictureResize(QtGui.QMainWindow):
	def __init__(self, parent=None):
        	super(PictureResize,self).__init__()
     		#QtGui.QWidget.__init__(self, parent) #better to use super in order to use inheritance from QMainWindow
        	self.ui = Ui_PictureResize()
        	self.ui.setupUi(self)
        	self.show()
        	QtCore.QObject.connect(self.ui.button_open,QtCore.SIGNAL("clicked()"), self.file_dialog)
                QtCore.QObject.connect(self.ui.StartBtn,QtCore.SIGNAL("clicked()"),self.file_resize)
		QtCore.QObject.connect(self.ui.ChangeSaveDir,QtCore.SIGNAL("clicked()"),self.dir_change)
		#connect method connects signals with slots, signal coming from first argument, kind of signal is specified in second arg, and third argument contains slot, i.e. what should be carried out when signal is launched
	
	def file_dialog(self):
        	#read filenames from selection into self.openFiles
		fd = QtGui.QFileDialog(self)
        	self.openFiles = fd.getOpenFileNames()
           	#text=open(fn2).read()
		filenamestring=''
		#print(len(self.openFiles))	
		for k in range(0,len(self.openFiles)):
        		filenamestring=filenamestring+self.openFiles[k]+'\n'
		
		path, fileName=split(str(self.openFiles[0]))	
		self.ui.FileList.setText(filenamestring)
		self.ui.NewFilesSaveDir.setText(path)
           	#plik = open(fd.getOpenFileName()).read()
	
	def dir_change(self):
		fd=QtGui.QFileDialog(self)
		self.saveFolder=str(fd.getExistingDirectory(None, 'Select Folder'))
		self.ui.NewFilesSaveDir.setText(str(self.saveFolder))	
	
  	def file_resize(self):
		newRes=self.ui.comboBox.currentText()
		FileExtensions=['.JPG','.jpg','.bmp','.gif','.png']		
		#if isfile(self.openFiles[0]):	#check maybe if there are files at all		   
		
		for k in range(0,len(self.openFiles)):
                	print(k)
			FNWP, fileExtension = splitext(str(self.openFiles[k]))
			path, fileName=split(str(self.openFiles[k]))
			
			newfile=self.saveFolder.replace(' ','\\ ') + '/' + fileName.replace(' ','\\ ')
                        runstring='convert -resize ' +newRes +' '+self.openFiles[k].replace(' ','\\ ') + ' ' + newfile.replace('.JPG','_new.JPG')
                        print(runstring)
			
			self.ui.ProcessDisplay.append('processing file ' + fileName +'\n')
			system(str(runstring))	
			self.ui.ProcessDisplay.append('done!')	
                        
		#read self.openFiles
		#check if any files are selected, else display error message 
		#loop over open files and convert, 
		#use self.ui.comboBox.cuttentText() to set resolution 
		print('test')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = PictureResize()
    #myapp.show()
    sys.exit(app.exec_())
