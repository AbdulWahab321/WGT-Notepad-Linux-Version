from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import components
import os
import sys
 

WHITE =     QColor(255, 255, 255)
BLACK =     QColor(0, 0, 0)
RED =       QColor(255, 0, 0)
PRIMARY =   QColor(53, 53, 53)
SECONDARY = QColor(35, 35, 35)
TERTIARY =  QColor(42, 130, 218)


class MainWindow(QMainWindow):

	def __init__(self,app, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		_translate = QCoreApplication.translate
		self.dark_palette = QPalette()

		self.app = app
		
		self.app.setPalette(self.dark_palette)
		self.dirpath = os.getcwd()
		self.treeWidget = False
		icon = QIcon()
		icon.addFile(u"./notepad.ico", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)

		self.setGeometry(100, 100, 600, 400)
		self.lastbg = "white"
		self.lastclr = "black"

		self.layout = QHBoxLayout()
  

			
        
		self.editor = QPlainTextEdit(self)
		self.showMaximized()
		self.editor.setFont(QFont('Consolas', 12))
		self.editor.textChanged.connect(self.valueChanged)

		self.font_size = QSpinBox()
		self.font_size.setValue(12)
		self.font_size.valueChanged.connect(self.change_font_size)
		settings_toolbar = QToolBar("Settings")

		self.addToolBar(settings_toolbar)
		self.font_box = QFontComboBox(settings_toolbar)
		self.font_box.setCurrentFont(QFont("Consolas"))
		self.font_box.currentFontChanged.connect(self.changeFont)
		settings_toolbar.addWidget(QLabel(settings_toolbar,text="Font: "))
		settings_toolbar.addWidget(self.font_box)
		settings_toolbar.addWidget(QLabel(settings_toolbar,text="  Font Size: "))

		self.path = None
		self.item1 = None
		self.layout.addWidget(self.editor)


		container = QWidget()

	
		container.setLayout(self.layout)


		self.setCentralWidget(container)


		self.status = QStatusBar()


		self.setStatusBar(self.status)


		file_menu = self.menuBar().addMenu("&File")


		open_file_action = QAction("Open file", self)


		open_file_action.setStatusTip("Open file")


		open_file_action.triggered.connect(self.file_open)
  
		open_dir_action = QAction("Open Directory", self)


		open_dir_action.setStatusTip("Open Directory")


		open_dir_action.triggered.connect(self.open_dir)  
		
		new_file_action = QAction("New file", self)


		new_file_action.setStatusTip("Create New file")


		new_file_action.triggered.connect(self.new_file)


		file_menu.addAction(new_file_action)

		new_window_action = QAction("New Window", self)


		new_window_action.setStatusTip("Open a new WG Notepad Window")


		new_window_action.triggered.connect(self.new_window)


		file_menu.addAction(new_window_action)  
  
		file_menu.addAction(open_dir_action)
		file_menu.addAction(open_file_action)
  		
	
		save_file_action = QAction("Save", self)
		save_file_action.setStatusTip("Save current page")
		save_file_action.triggered.connect(self.file_save)
		save_file_action.setShortcut("ctrl+s")
		file_menu.addAction(save_file_action)

	
		saveas_file_action = QAction("Save As", self)
		saveas_file_action.setStatusTip("Save current page to specified file")
		saveas_file_action.triggered.connect(self.file_saveas)
		file_menu.addAction(saveas_file_action)


		print_action = QAction("Print", self)
		print_action.setStatusTip("Print current page")
		print_action.triggered.connect(self.file_print)
		file_menu.addAction(print_action)




		edit_menu = self.menuBar().addMenu("&Edit")


		customize_action = QAction("Background Colour", self)
		customize_action.setStatusTip("Change the background colour of the program")
		customize_action.triggered.connect(self.background_change)
		customize = self.menuBar().addMenu("&Customize")
		customize.addAction(customize_action)
  
		customize_color_action = QAction("Editor Font Colour", self)
		customize_color_action.setStatusTip("change the color of the input text")
		customize_color_action.triggered.connect(self.color_change)
		customize.addAction(customize_color_action)

		customize_pg_color_action = QAction("Program's Font Colour", self)
		customize_pg_color_action.setStatusTip("change the color of the program text")
		customize_pg_color_action.triggered.connect(self.pg_color_change)
		customize.addAction(customize_pg_color_action)

		default_color_action = QAction("Reset to Defaults", self)
		default_color_action.setStatusTip("change to the default settings")
		default_color_action.triggered.connect(self.default_color)
		customize.addAction(default_color_action)

		style_menu = self.menuBar().addMenu("&Style")

		if sys.platform.lower() == "win32" or sys.platform.lower() == "win64":
			style_windowsvista = QAction("Windows Vista Style", self)
			style_windowsvista.setStatusTip("Change to Windows Vista Style")
			style_windowsvista.triggered.connect(lambda:self.app.setStyle("windowsvista"))        
        
			style_fusion = QAction("Fusion Style", self)
			style_fusion.setStatusTip("Change to Fusion Style")
			style_fusion.triggered.connect(lambda:self.app.setStyle("Fusion"))

			style_windows = QAction("Windows Style", self)
			style_windows.setStatusTip("Change to Windows Style")
			style_windows.triggered.connect(lambda:self.app.setStyle("Windows"))   
   
			style_menu.addAction(style_windowsvista)
			style_menu.addAction(style_fusion)
			style_menu.addAction(style_windows)

			
		elif sys.platform.lower() == "linux" or  sys.platform.lower() == "linux2":
			style_breeze = QAction("Adwaita Dark Style", self)
			style_breeze.setStatusTip("Change to Adwaita Style")
			style_breeze.triggered.connect(lambda:self.setAdwaitaDark())        

			style_oxygen = QAction("Adwaita Style", self)
			style_oxygen.setStatusTip("Change to Adwaita  Style")
			style_oxygen.triggered.connect(lambda:self.setStyleApp("Adwaita"))
        
			#style_qtCurve = QAction("Bb10Dark Style", self)
			#style_qtCurve.setStatusTip("Change to Bb10Dark Style")
			#style_qtCurve.triggered.connect(lambda:self.app.setStyle("bb10dark"))

			#style_bb10bright = QAction("Bb10bright Style", self)
			#style_bb10bright.setStatusTip("Change to Bb10bright Style")
			#style_bb10bright.triggered.connect(lambda:self.app.setStyle("bb10bright"))   
   
			style_cleanlooks = QAction("Cleanlooks Style",self)
			style_cleanlooks.setStatusTip("Change to Cleanlooks Style")
			style_cleanlooks.triggered.connect(lambda:self.setStyleApp("cleanlooks"))        

			style_gtk2 = QAction("Gtk2 Style", self)
			style_gtk2.setStatusTip("Change to Gtk2 Style")
			style_gtk2.triggered.connect(lambda:self.setStyleApp("Adwaita"))
        
			style_cde = QAction("Cde Style", self)
			style_cde.setStatusTip("Change to Cde Style")
			style_cde.triggered.connect(lambda:self.setStyleApp("cde"))
   
			style_motif = QAction("Motif Style", self)
			style_motif.setStatusTip("Change to Motif Style")
			style_motif.triggered.connect(lambda:self.setStyleApp("motif"))
        
			style_plastique = QAction("Plastique Style", self)
			style_plastique.setStatusTip("Change to Plastique Style")
			style_plastique.triggered.connect(lambda:self.setStyleApp("plastique"))
        
			style_fusion = QAction("Fusion Style", self)
			style_fusion.setStatusTip("Change to Fusion Style")
			style_fusion.triggered.connect(lambda:self.setStyleApp("Fusion"))

			style_windows = QAction("Windows Style", self)
			style_windows.setStatusTip("Change to Windows Style")
			style_windows.triggered.connect(lambda:self.setStyleApp("Windows"))   
   
			style_menu.addAction(style_breeze)
			style_menu.addAction(style_oxygen)
 
			style_menu.addAction(style_cleanlooks)
			style_menu.addAction(style_gtk2)
			style_menu.addAction(style_cde)
			style_menu.addAction(style_motif)
			style_menu.addAction(style_plastique)
			style_menu.addAction(style_fusion)
			style_menu.addAction(style_windows)		
		elif "mac" in sys.platform.lower():
			style_macintosh = QAction("Macintosh Style", self)
			style_macintosh.setStatusTip("Change to Macintosh Style")
			style_macintosh.triggered.connect(lambda:self.app.setStyle("macintosh"))
      
			style_fusion = QAction("Fusion Style", self)
			style_fusion.setStatusTip("Change to Fusion Style")
			style_fusion.triggered.connect(lambda:self.app.setStyle("Fusion"))

			style_windows = QAction("Windows Style", self)
			style_windows.setStatusTip("Change to Windows Style")
			style_windows.triggered.connect(lambda:self.app.setStyle("Windows"))   
   
			style_menu.addAction(style_macintosh)
			style_menu.addAction(style_fusion)
			style_menu.addAction(style_windows)
		else:
			self.dialog_information(f"Sorry!\nThe Styles Menu is Unavailable for the os:{sys.platform}")
			
  
		undo_action = QAction("Undo", self)

		undo_action.setStatusTip("Undo last change")


		undo_action.triggered.connect(self.editor.undo)



		edit_menu.addAction(undo_action)


		redo_action = QAction("Redo", self)
		redo_action.setStatusTip("Redo last change")

		redo_action.triggered.connect(self.editor.redo)

		edit_menu.addAction(redo_action)


		cut_action = QAction("Cut", self)
		cut_action.setStatusTip("Cut selected text")


		cut_action.triggered.connect(self.editor.cut)

		edit_menu.addAction(cut_action)


		copy_action = QAction("Copy", self)
		copy_action.setStatusTip("Copy selected text")


		copy_action.triggered.connect(self.editor.copy)

		edit_menu.addAction(copy_action)
		
		paste_action = QAction("Paste", self)
		paste_action.setStatusTip("Paste from clipboard")


		paste_action.triggered.connect(self.editor.paste)

		edit_menu.addAction(paste_action)

		select_action = QAction("Select all", self)
		select_action.setStatusTip("Select all text")


		select_action.triggered.connect(self.editor.selectAll)


		edit_menu.addAction(select_action)



		wrap_action = QAction("Wrap text to window", self)
		wrap_action.setStatusTip("Check to wrap text to window")


		wrap_action.setCheckable(True)


		wrap_action.setChecked(True)


		wrap_action.triggered.connect(self.edit_toggle_wrap)



	
		edit_menu.addAction(wrap_action)
		settings_toolbar.addWidget(self.font_size)

		settings_toolbar.addWidget(QPushButton(settings_toolbar,text="Reset to defaults",clicked = lambda:self.change_settings_to_default()))

		new_file_action.setShortcut("ctrl+n")
		new_window_action.setShortcut("ctrl+shift+n")
		open_file_action.setShortcut("ctrl+o")
		open_dir_action.setShortcut("ctrl+d")
		saveas_file_action.setShortcut("ctrl+shift+s")

		self.update_title()

		self.show()
	def setStyleApp(self,style):
		self.app.setStyle(style)
		self.font_size.setStyleSheet("color:black;")
	def setAdwaitaDark(self):
		self.app.setStyle("Adwaita-Dark")
		self.font_size.setStyleSheet("color:white;")	
	def change_file(self):
		item_var = self.treeWidget.currentItem()
		index_var = self.treeWidget.selectedIndexes()
		file = item_var.text(0)
		
		full_path = os.path.join(self.dirpath,file)
		if os.path.isfile(full_path):
			self.file_open(full_path)
			self.path = full_path
			self.update_title()
		else:
			components.alert("Opening Directory inside a directory is not Supported Sorry!",title="MSFEx3521")
	
	def new_window(s,d):
		if __file__.endswith(".exe"):
			os.system(f'"{__file__}"')
		else:
			os.system(f'py "{__file__}"')
	def valueChanged(self):
		if self.path:
			if open(self.path).read()!=self.editor.toPlainText():
				self.setWindowTitle("%s - W&G Notepad" %(f"{os.path.basename(self.path)}*"
													if self.path else "Untitled"))
			else:
				self.setWindowTitle("%s - W&G Notepad" %(os.path.basename(self.path)
													if self.path else "Untitled"))
	def changeFont(self):
		self.editor.setFont(QFont(self.font_box.currentFont().family(),self.font_size.value()))
	def FileDialog(directory='', forOpen=True, fmt='', isFolder=False):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseCustomDirectoryIcons
		dialog = QFileDialog(caption="Open Folder")
		dialog.setOptions(options)
		dialog.setFilter(dialog.filter() | QDir.Hidden)
		# ARE WE TALKING ABOUT FILES OR FOLDERS
		if isFolder:
		    dialog.setFileMode(QFileDialog.DirectoryOnly)
		else:
		    dialog.setFileMode(QFileDialog.AnyFile)
		# OPENING OR SAVING:
		dialog.setAcceptMode(QFileDialog.AcceptOpen) if forOpen else dialog.setAcceptMode(QFileDialog.AcceptSave)
		# SET FORMAT, IF SPECIFIED
		if fmt != '' and isFolder is False:
		    dialog.setDefaultSuffix(fmt)
		    dialog.setNameFilters([f'{fmt} (*.{fmt})'])
		# SET THE STARTING DIRECTORY
		if directory != '':
		    dialog.setDirectory(str(directory))
		else:
		    dialog.setDirectory(str(os.path.dirname(__file__)))
		if dialog.exec_() == QDialog.Accepted:
		    path = dialog.selectedFiles()[0]  # returns a list
		    return path
		else:
		    return ''	
	def open_dir(self):
		ttext = self.editor.toPlainText()
		if ttext.strip()!="":
			if self.path and os.path.exists(self.path):
				if open(self.path).read()!=ttext:
					alrt = components.alert("Your Changes are not saved!\nDo you want to save it?",components.Styles.Buttons.YES_NO|components.Styles.Icons.ICON_WARNING,"Unsaved Changes Warning")
					if alrt == "yes":
						self.file_save()

		path = self.FileDialog(isFolder=True)
		if path!='':
      
			self.dirpath = path
                               
			if self.treeWidget:
				self.layout.removeWidget(self.treeWidget)
			self.treeWidget = QTreeWidget(self)
			self.treeWidget.setMaximumWidth(250)
			self.layout.removeWidget(self.editor)
			self.treeWidget.setObjectName("treeWidget")
			self.treeWidget.headerItem().setText(0,self.dirpath)
			self.treeWidget.currentItemChanged.connect(self.change_file)
			__sortingEnabled = self.treeWidget.isSortingEnabled()
			self.treeWidget.setSortingEnabled(False)	
			for i in os.listdir(self.dirpath):
				__sortingEnabled = self.treeWidget.isSortingEnabled()
				self.treeWidget.setSortingEnabled(False)
				self.item1 = QTreeWidgetItem(self.treeWidget)
				self.item1.setText(0,i)
				self.treeWidget.setSortingEnabled(__sortingEnabled)
			self.layout.addWidget(self.treeWidget)
			self.layout.addWidget(self.editor)
			
   
	def change_settings_to_default(self):
		self.font_box.setCurrentFont(QFont("Consolas"))
		self.font_size.setValue(12)
		self.editor.setFont(QFont("Consolas",12))
	def closeEvent(self,event):
		if self.path:
			if open(self.path).read()!=self.editor.toPlainText():
				alrt = components.alert("Your Changes are not saved!\nDo you want to save it?",components.Styles.Buttons.YES_NO_CANCEL|components.Styles.Icons.ICON_WARNING,"Unsaved Changes Warning")
				if alrt == "yes":
					self.file_save()     

		else:
			alrt = components.alert("Your Changes are not saved!\nDo you want to save it?",components.Styles.Buttons.YES_NO_CANCEL|components.Styles.Icons.ICON_WARNING,"Unsaved Changes Warning")
			if alrt == "yes":
				self.file_save()
			if alrt == "cancel":
				event.ignore()
			else:
				event.accept()
	def change_font_size(self):
		self.editor.setFont(QFont(self.font_box.currentFont().family(),self.font_size.value()))
	def darkmode(self):
		global app 
		self.setStyleSheet(f"background-color: black;color:white")
		self.editor.setStyleSheet(f"color: white;background-color:black")
		self.menuBar().setStyleSheet("background-color:black;color:white")
  
		self.dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
		self.dark_palette.setColor(QPalette.WindowText, Qt.white)
		self.dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
		self.dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
		self.dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
		self.dark_palette.setColor(QPalette.ToolTipText, Qt.white)
		self.dark_palette.setColor(QPalette.Text, Qt.white)
		self.dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
		self.dark_palette.setColor(QPalette.ButtonText, Qt.white)
		self.dark_palette.setColor(QPalette.BrightText, Qt.red)
		self.dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
		self.dark_palette.setColor(QPalette.Highlight, Qt.white)
		self.dark_palette.setColor(QPalette.HighlightedText, Qt.black)
		self.dark_palette.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
		self.dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
		self.dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
		self.dark_palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
		self.dark_palette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
		app.setPalette(window.dark_palette)
	def lightmode(self):
		self.setStyleSheet(f"background-color: white;color:black")
		self.editor.setStyleSheet(f"color: black;background-color:white")
		self.menuBar().setStyleSheet("background-color:white;color:black")
	def background_change(self):
		cd = QColorDialog(self)

		if cd.Accepted:
			clr = cd.getColor().name()
			self.dark_palette.setColor(QPalette.Window,QColor(clr))
			self.lastbg = clr
			self.app.setPalette(self.dark_palette)
	def color_change(self):
		cd = QColorDialog(self)

		if cd.Accepted:
			clr = cd.getColor().name()
			self.editor.setStyleSheet(f"color: {clr};")
	def new_file(self):
		ttext = self.editor.toPlainText()
		if ttext.strip()!="":
			if open(self.path).read()!=ttext:
				alrt = components.alert("Your Changes are not saved!\nDo you want to save it?",components.Styles.Buttons.YES_NO|components.Styles.Icons.ICON_WARNING,"Unsaved Changes Warning")
				if alrt == "yes":
					self.file_save()     
		path, _ = QFileDialog.getSaveFileName(self, "Save file", "My_Text.txt","Text documents (*.txt);All files (*.*)")
		if path:

			try:
				with open(path, 'w') as f:

					f.write("")

			except Exception as e:

				self.dialog_critical(str(e))
   
			else:
				self.path = path
				# update the title
				self.update_title()
    
	def pg_color_change(self):
		cd = QColorDialog(self)

		if cd.Accepted:
			clr = cd.getColor().name()
			self.dark_palette.setColor(QPalette.Text,QColor(clr))
			self.dark_palette.setColor(QPalette.ButtonText|QPalette.ToolTipText,QColor(clr))
			self.lastclr = clr
			self.app.setPalette(self.dark_palette)
	def default_color(self):
		self.dark_palette.setColor(QPalette.Window,QColor("white"))
		self.dark_palette.setColor(QPalette.Text,QColor("black"))
		self.app.setPalette(self.dark_palette)
	def dialog_critical(self, s):

		# creating a QMessageBox object
		dlg = QMessageBox(self)

		# setting text to the dlg
		dlg.setText(s)

		# setting icon to it
		dlg.setIcon(QMessageBox.Critical)

		# showing it
		dlg.show()

	def file_open(self,spth = False):
		
		ttext = self.editor.toPlainText()
		if ttext.strip()!="":
			if self.path:
				if open(self.path).read()!=ttext:
					alrt = components.alert("Your Changes are not saved!\nDo you want to save it?",components.Styles.Buttons.YES_NO|components.Styles.Icons.ICON_WARNING,"Unsaved Changes Warning")
					if alrt == "yes":
						self.file_save()
		if spth!=False:
			path = spth

		else:
			path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
								"Text documents (*.txt);All files (*.*)")			
		if path:

			try:
				with open(path, 'rU') as f:
					text = f.read()
			except UnicodeDecodeError:
				alrt = components.alert("Sorry this is an unsupported type of encoding do you want to view it anyway?",components.Styles.Icons.ICON_WARNING|components.Styles.Buttons.YES_NO)
				if alrt == "yes":
					try:
						with open(path,"rb") as f:
							text = f.read()					
					except:
						try:
							import io
							with io.open(path) as f:
								text = f.read()
						except:
							try:
								import io
								with io.open(path,encoding = "utf-8") as f:
									text = f.read()				
							except:
								self.dialog_critical("Some unknown errors Occured")	
						
						
						
			except Exception as e:

				self.dialog_critical(str(e))
   
			else:
				self.path = path
				self.editor.setPlainText(text)
				self.update_title()


	def file_save(self):

		if self.path is None:

			return self.file_saveas()

		else:
			self._save_to_path(self.path)


	def file_saveas(self):

		path, _ = QFileDialog.getSaveFileName(self, "Save file", "My_Text.txt",
							"Text documents (*.txt);All files (*.*)")

		if not path:

			return

		self._save_to_path(path)


	def _save_to_path(self, path):

		text = self.editor.toPlainText()

		try:

			with open(path, 'w') as f:

				f.write(text)

		except Exception as e:

			self.dialog_critical(str(e))
			self.editor.selectAll()
			self.editor.copy()
		else:
			self.path = path
			self.update_title()

	# action called by print
	def file_print(self):
		dlg = QPrintDialog()

		if dlg.exec_():
			self.editor.print_(dlg.printer())


	def update_title(self):
		self.setWindowTitle("%s - W&G Notepad" %(os.path.basename(self.path)
												if self.path else "Untitled"))
  
	def edit_toggle_wrap(self):
		self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 )
  
if __name__ == '__main__':
        
		app = QApplication(sys.argv)
		print(QStyleFactory.keys())

		app.setApplicationName("W&G-Notepad")
		app.setOrganizationName("AbdulWahab")
		window = MainWindow(app)
		app.setApplicationVersion("1.9.4")


		app.exec_()

 