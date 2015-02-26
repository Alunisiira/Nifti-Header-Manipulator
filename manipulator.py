import sys
import string
from copy import deepcopy
from os.path import isfile
from collections import OrderedDict
import dicom
import nibabel
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow



class StartQT4(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.leftFile = 0
		self.rightFile = 0
		self.leftNifti = 0
		self.rightNifti = 0
		self.leftDict = {}
		self.rightDict = {}
		self.ui.LeftEdit.setEnabled(False)
		self.ui.RightEdit.setEnabled(False)
		self.ui.LeftSaveHeaderButton.setEnabled(False)
		self.ui.RightSaveHeaderButton.setEnabled(False)
		self.ui.CopyToRightButton.setEnabled(False)
		self.ui.CopyToLeftButton.setEnabled(False)
		self.ui.comboBoxLeftSide.setEnabled(False)
		self.ui.comboBoxRightSide.setEnabled(False)
		self.ui.actionExportPresets.setEnabled(False)
		self.presetDict = {}
		self.NIFTIV1_DICT = OrderedDict([('sizeof_hdr',''), ('data_type',''), ('db_name',''), ('extents', ''), ('session_error',''), ('regular',''), ('dim_info',''), ('dim',''), ('intent_p1',''), ('intent_p2',''), ('intent_p3',''), ('intent_code',''), ('datatype',''), ('bitpix',''), ('slice_start',''), ('pixdim',''), ('vox_offset',''), ('scl_slope',''), ('scl_inter',''), ('slice_end',''), ('slice_code',''), ('xyzt_units',''), ('cal_max',''), ('cal_min',''), ('slice_duration',''), ('toffset',''), ('glmax',''), ('glmin',''), ('descrip',''), ('aux_file',''), ('qform_code',''), ('sform_code',''), ('quatern_b',''), ('quatern_c',''), ('quatern_d',''), ('qoffset_x',''), ('qoffset_y',''), ('qoffset_z',''), ('srow_x',''), ('srow_y',''), ('srow_z',''), ('intent_name',''), ('magic','')])
	
		""" Nifti are defined as following:
		int   sizeof_hdr;    /*!< MUST be 348           */  /* int sizeof_hdr;      */
		char  data_type[10]; /*!< ++UNUSED++            */  /* char data_type[10];  */
		char  db_name[18];   /*!< ++UNUSED++            */  /* char db_name[18];    */
		int   extents;       /*!< ++UNUSED++            */  /* int extents;         */
		short session_error; /*!< ++UNUSED++            */  /* short session_error; */
		char  regular;       /*!< ++UNUSED++            */  /* char regular;        */
		char  dim_info;      /*!< MRI slice ordering.   */  /* char hkey_un0;       */

				                              /*--- was image_dimension substruct ---*/
		short dim[8];        /*!< Data array dimensions.*/  /* short dim[8];        */
		float intent_p1 ;    /*!< 1st intent parameter. */  /* short unused8;       */
				                                             /* short unused9;       */
		float intent_p2 ;    /*!< 2nd intent parameter. */  /* short unused10;      */
				                                             /* short unused11;      */
		float intent_p3 ;    /*!< 3rd intent parameter. */  /* short unused12;      */
				                                             /* short unused13;      */
		short intent_code ;  /*!< NIFTI_INTENT_* code.  */  /* short unused14;      */
		short datatype;      /*!< Defines data type!    */  /* short datatype;      */
		short bitpix;        /*!< Number bits/voxel.    */  /* short bitpix;        */
		short slice_start;   /*!< First slice index.    */  /* short dim_un0;       */
		float pixdim[8];     /*!< Grid spacings.        */  /* float pixdim[8];     */
		float vox_offset;    /*!< Offset into .nii file */  /* float vox_offset;    */
		float scl_slope ;    /*!< Data scaling: slope.  */  /* float funused1;      */
		float scl_inter ;    /*!< Data scaling: offset. */  /* float funused2;      */
		short slice_end;     /*!< Last slice index.     */  /* float funused3;      */
		char  slice_code ;   /*!< Slice timing order.   */
		char  xyzt_units ;   /*!< Units of pixdim[1..4] */
		float cal_max;       /*!< Max display intensity */  /* float cal_max;       */
		float cal_min;       /*!< Min display intensity */  /* float cal_min;       */
		float slice_duration;/*!< Time for 1 slice.     */  /* float compressed;    */
		float toffset;       /*!< Time axis shift.      */  /* float verified;      */
		int   glmax;         /*!< ++UNUSED++            */  /* int glmax;           */
		int   glmin;         /*!< ++UNUSED++            */  /* int glmin;           */

				                                 /*--- was data_history substruct ---*/
		char  descrip[80];   /*!< any text you like.    */  /* char descrip[80];    */
		char  aux_file[24];  /*!< auxiliary filename.   */  /* char aux_file[24];   */

		short qform_code ;   /*!< NIFTI_XFORM_* code.   */  /*-- all ANALYZE 7.5 ---*/
		short sform_code ;   /*!< NIFTI_XFORM_* code.   */  /*   fields below here  */
				                                             /*   are replaced       */
		float quatern_b ;    /*!< Quaternion b param.   */
		float quatern_c ;    /*!< Quaternion c param.   */
		float quatern_d ;    /*!< Quaternion d param.   */
		float qoffset_x ;    /*!< Quaternion x shift.   */
		float qoffset_y ;    /*!< Quaternion y shift.   */
		float qoffset_z ;    /*!< Quaternion z shift.   */

		float srow_x[4] ;    /*!< 1st row affine transform.   */
		float srow_y[4] ;    /*!< 2nd row affine transform.   */
		float srow_z[4] ;    /*!< 3rd row affine transform.   */

		char intent_name[16];/*!< 'name' or meaning of data.  */

		char magic[4] ;      /*!< MUST be "ni1\0" or "n+1\0". */
		"""






		#populate comboboxes
		#self.ui.comboBoxLeftSide.addItem("")
		#self.ui.comboBoxLeftSide.setItemText(1, QtGui.QApplication.translate("MainWindow", "afni", None, QtGui.QApplication.UnicodeUTF8))
		

		#method linking
		QtCore.QObject.connect(self.ui.LeftLoadHeaderButton,QtCore.SIGNAL("clicked()"), self.loadLeftFile)
		QtCore.QObject.connect(self.ui.RightLoadHeaderButton,QtCore.SIGNAL("clicked()"), self.loadRightFile)
		QtCore.QObject.connect(self.ui.LeftSaveHeaderButton,QtCore.SIGNAL("clicked()"), self.saveLeftFile)
		QtCore.QObject.connect(self.ui.RightSaveHeaderButton,QtCore.SIGNAL("clicked()"), self.saveRightFile)
		QtCore.QObject.connect(self.ui.CopyToRightButton,QtCore.SIGNAL("clicked()"), self.copyToRight)
		QtCore.QObject.connect(self.ui.CopyToLeftButton,QtCore.SIGNAL("clicked()"), self.copyToLeft)
		QtCore.QObject.connect(self.ui.comboBoxLeftSide,QtCore.SIGNAL("currentIndexChanged(QString)"), self.leftIndexChanged)
		QtCore.QObject.connect(self.ui.comboBoxRightSide,QtCore.SIGNAL("currentIndexChanged(QString)"), self.rightIndexChanged)
		QtCore.QObject.connect(self.ui.actionImportPresets,QtCore.SIGNAL("triggered(bool)"), self.importPresets)
		QtCore.QObject.connect(self.ui.actionExportPresets,QtCore.SIGNAL("triggered(bool)"), self.exportPresets)
		QtCore.QObject.connect(self.ui.actionHelp,QtCore.SIGNAL("triggered(bool)"), self.helpAbout)
		
	def buildNormNi1HeaderDict(self, s):
		cleanedHeader = self.replaceInnerCommaWithSpace(s.strip('()'))
		splittedHeader = cleanedHeader.split(',')
		csHeader = map (lambda s: s.replace("'","").strip(), splittedHeader)
		result = OrderedDict([])	
		#test if it is a Nifti 1 Header
		if not (len(csHeader) < 43  or not csHeader[0] == '348' or  not ( csHeader[42] == 'n+1' or csHeader[42] == 'ni1')):
			result = OrderedDict([('sizeof_hdr',csHeader[0]), ('data_type',csHeader[1]), ('db_name',csHeader[2]), ('extents', csHeader[3]), ('session_error',csHeader[4]), ('regular',csHeader[5]), ('dim_info',csHeader[6]), ('dim',csHeader[7]), ('intent_p1',csHeader[8]), ('intent_p2',csHeader[9]), ('intent_p3',csHeader[10]), ('intent_code',csHeader[11]), ('datatype',csHeader[12]), ('bitpix',csHeader[13]), ('slice_start',csHeader[14]), ('pixdim',csHeader[15]), ('vox_offset',csHeader[16]), ('scl_slope',csHeader[17]), ('scl_inter',csHeader[18]), ('slice_end',csHeader[19]), ('slice_code',csHeader[20]), ('xyzt_units',csHeader[21]), ('cal_max',csHeader[22]), ('cal_min',csHeader[23]), ('slice_duration',csHeader[24]), ('toffset',csHeader[25]), ('glmax',csHeader[26]), ('glmin',csHeader[27]), ('descrip',csHeader[28]), ('aux_file',csHeader[29]), ('qform_code',csHeader[30]), ('sform_code',csHeader[31]), ('quatern_b',csHeader[32]), ('quatern_c',csHeader[33]), ('quatern_d',csHeader[34]), ('qoffset_x',csHeader[35]), ('qoffset_y',csHeader[36]), ('qoffset_z',csHeader[37]), ('srow_x',csHeader[38]), ('srow_y',csHeader[39]), ('srow_z',csHeader[40]), ('intent_name',csHeader[41]), ('magic',csHeader[42])])
		return result
	

	def replaceInnerCommaWithSpace(self, s):
			leftBr = string.find(s,'[')
			rightBr = string.find(s,']')
			result = s[:leftBr]
			while leftBr is not -1:
				result += s[leftBr:rightBr+1].replace(',',' ').replace('[','').replace(']','')
				leftBr = string.find (s,'[',rightBr)
				if leftBr == -1:
					result += s[rightBr+1:]
				else:
					result += s[rightBr+1:leftBr]
				rightBr = string.find (s,']',rightBr+1)
			return result

		
	def readImage(self, path, left=True):
		if path[-3:] == 'nii':
			#nifti format
			img = nibabel.load(path)
			_dict = self.buildNormNi1HeaderDict(img.get_header().structarr.__str__())
			#if len(_dict.values()) == 0:
			#	#kein Nifti 1 format			
			if left:
				self.ui.LeftEdit.setReadOnly(False)
				self.ui.CopyToLeftButton.setEnabled(True)			
				self.leftNifti = img
				self.leftDict = _dict
			else :
				self.ui.RightEdit.setReadOnly(False)
				self.ui.CopyToRightButton.setEnabled(True)
				self.rightNifti = img
				self.rightDict =_dict
			result = ''			
			for i in _dict:
				result += i + ": " + _dict[i] + "\n"
			return result
		elif path[-3:] == 'ima' :
			#dicom format
			fds = dicom.read_file(path, stop_before_pixels=True)
			if left:
				self.ui.LeftEdit.setReadOnly(True)
				self.ui.CopyToLeftButton.setEnabled(False)
				self.ui.LeftSaveHeaderButton.setEnabled(False)
			else :
				self.ui.RightEdit.setReadOnly(True)
				self.ui.CopyToRightButton.setEnabled(False)
				self.ui.RightSaveHeaderButton.setEnabled(False)
			return fds.__str__()
		else :
			#assume readable format
			with open(path) as f:
				if left:
					self.ui.LeftEdit.setReadOnly(False)
					self.ui.CopyToLeftButton.setEnabled(True)		
				else :
					self.ui.RightEdit.setReadOnly(False)
					self.ui.CopyToRightButton.setEnabled(True)
				return f.read()


	def helpAbout(self):
		print """Version 0.1 Alpha\nAuthor Jan Zelmer\nEmail jzelmer@cbs.mpg.de\nTool for manipulating dicom and nifti header."""


	def importPresets(self):
		fd = QtGui.QFileDialog(self)
		fn = fd.getOpenFileName()
		if isfile(fn):
			fd = open(fn)
			self.presetDict.clear()
			i = 0
			for line in fd:				
				i = i + 1
				if line[0]=='#':
					continue
				keysargs = line.split()			
				if len(keysargs)==1:
					key = keysargs[0]
					arg = ""
					self.presetDict[key]= arg
				elif len(keysargs)==2:
					key = keysargs[0]
					arg = keysargs[1]
					self.presetDict[key]= arg
				else :
					print "I don't understand the following line.\n%i %s\n" %(i,line)
			fd.close()
			lib = False
			for li in xrange(0,self.ui.comboBoxLeftSide.__len__()):
				if self.ui.comboBoxLeftSide.itemText(li).__str__()=='Preset':
					lib = True
			if not lib:
				self.ui.comboBoxLeftSide.addItem("Preset")
			rib = False
			for ri in xrange(0,self.ui.comboBoxLeftSide.__len__()):
				if self.ui.comboBoxLeftSide.itemText(ri).__str__()=='Preset':
					rib = True
			if not rib:
				self.ui.comboBoxRightSide.addItem("Preset")
			self.ui.actionExportPresets.setEnabled(True)


	def exportPresets(self):
		fd = QtGui.QFileDialog(self)
		fn = fd.getSaveFileName()
		if not fn.__str__() == '':
			with open(fn,'w') as fd:
				for keys in self.presetDict:
					s = keys + "    " + self.presetDict[keys] + "\n"
					fd.write(s)
				fd.close()

		
	def loadLeftFile(self):		
		fd = QtGui.QFileDialog(self)
		leftFile = fd.getSaveFileName(options = QtGui.QFileDialog.DontConfirmOverwrite)
		if isfile(leftFile) or not leftFile.__str__() == '':
			if not self.ui.LeftEdit.isEnabled():
				self.ui.LeftEdit.setEnabled(True)
				self.ui.LeftSaveHeaderButton.setEnabled(True)
				if not self.ui.RightEdit.isReadOnly():
					self.ui.CopyToRightButton.setEnabled(True)
				self.ui.comboBoxLeftSide.setEnabled(True)			
			self.leftFile = leftFile
			if len(leftFile)>100:
				s = leftFile
				s = s[0:10] + "..." + s[-90:]
				self.ui.labelPathLeft.setText(s)
			else:
				self.ui.labelPathLeft.setText(leftFile)			
			self.ui.LeftEdit.setPlainText(self.readImage(leftFile.__str__()))
			

	def saveLeftFile(self):
		fd = open(self.leftFile,'w')
		fd.write(self.ui.LeftEdit.toPlainText())
		fd.close()

	def copyToRight(self):
		#if self.ui.LeftEdit.
		self.ui.RightEdit.setPlainText(self.ui.LeftEdit.toPlainText())

	def leftIndexChanged(self):
		print "left index changed"

	def loadRightFile(self):		
		fd = QtGui.QFileDialog(self)
		rightFile = fd.getSaveFileName(options = QtGui.QFileDialog.DontConfirmOverwrite)
		if isfile(rightFile) or not rightFile.__str__() == '':
			if not self.ui.RightEdit.isEnabled():
				self.ui.RightEdit.setEnabled(True)
				self.ui.RightSaveHeaderButton.setEnabled(True)
				if not self.ui.LeftEdit.isReadOnly():					
					self.ui.CopyToLeftButton.setEnabled(True)
				self.ui.comboBoxRightSide.setEnabled(True)
			self.rightFile = rightFile
			if len(rightFile)>100:
				s = rightFile
				s = s[0:10] + "..." + s[-90:]
				self.ui.labelPathRight.setText(s)
			else:
				self.ui.labelPathRight.setText(rightFile)			
			self.ui.RightEdit.setPlainText(self.readImage(rightFile.__str__(), left=False))

	def saveRightFile(self):
		fd = open(self.rightFile,'w')
		fd.write(self.ui.RightEdit.toPlainText())
		fd.close()

	def copyToLeft(self):
		self.ui.LeftEdit.setPlainText(self.ui.RightEdit.toPlainText())

	def rightIndexChanged(self):
		print "right index changed"

if __name__ == "__main__":	
	if len(sys.argv) > 1:
		#command line usage
		pass
	else :
		#graphical user interface usage		
		app = QtGui.QApplication(sys.argv)
		myapp = StartQT4()
		myapp.show()		
		sys.exit(app.exec_())

