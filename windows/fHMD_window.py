import sys, re
import os

from PyQt4 import QtCore, QtGui

import pickle

from forms.fHMD_forms.initial_form import initial_class
from forms.fHMD_forms.geometry_1_form import geometry_1_class
from forms.fHMD_forms.geometry_2_form import geometry_2_class
from forms.fHMD_forms.surfaceConformation_form import surfaceConformation_class
from forms.fHMD_forms.initialPoints_form import initialPoints_class
from forms.fHMD_forms.motionControl_form import motionControl_class
from forms.fHMD_forms.polyMF_form import polyMF_class
from functions.foamyHexMeshDict_generation import foamyHexMeshDict_generation_class

class fhmd_window_class(QtGui.QWidget):
	def __init__(self, parent, par, prj_path_cur, mesh_name_txt_cur, pd_2_cur):
		QtGui.QWidget.__init__(self, parent)
	
		global tab
		global initial_group, initial_btnSave, geometry_visible, surfaceConformation_visible, initialPoints_visible, motionControl_visible, polyMF_visible, g_edit
		
		global geometry_1_group, geometry_1_btnSave, geometry_type_list, base_shape_lbl_list, base_shape_type_list
		global geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list
		global surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, includedAngle_list
		global initialPoints_group, initialPoints_btnSave, iPM_edit, aDC_table, aDC_checks_list, aDC_values_list, aDC_val_pr_list, aDC_val_def_list
		global motionControl_group, motionControl_btnSave, mC_start_prs_grid, sCF_geom_edit_list, sCF_type_edit_list, sCF_priority_edit_list, sCF_mode_edit_list, sCF_surfaceCellSizeFunction_edit_list, \
		sCF_surfaceCellSizeCoeff_edit_list, sCF_cellSizeFunction_edit_list, sCF_distanceCellSizeCoeff_edit_list, sCF_distanceCoeff_edit_list
		global polyMF_group, polyMF_btnSave, pMF_prs_grid

		global geometry_1_path, geometry_2_path
		global int_lng

		global geometry_txt_old_mas

		global g_v 
		
		global parn
		parn = par
		
		int_lng = parent.int_lng_path_return()
		global prj_path, mesh_name_txt, pd_2 
		prj_path = prj_path_cur
		mesh_name_txt = mesh_name_txt_cur
		pd_2 = pd_2_cur
		
		#------------------------------Загружаем вкладки для имеющегося файла----------------------------------#
		
		#------------------------------initial----------------------------------#
		
		tab = QtGui.QTabWidget()
		initial_group, initial_btnSave, geometry_visible, surfaceConformation_visible, initialPoints_visible, motionControl_visible, polyMF_visible, g_edit = initial_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2)
		tab.insertTab(0, initial_group, "&initial")

		g_v = g_edit.value()

		initial_btnSave.clicked.connect(self.on_initial_btnSave_clicked)
			
		#-------------------------------geometry_1--------------------------------#
		
		geometry_1_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_1.pkl'
		if geometry_visible == True:
			geometry_1_group, geometry_1_btnSave, geometry_type_list, base_shape_lbl_list, base_shape_type_list = geometry_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
			tab.insertTab(1, geometry_1_group, "&geometry_1")
			geometry_1_btnSave.clicked.connect(self.on_geometry_1_btnSave_clicked)
			
			geometry_txt_old_mas = []
			base_shape_type_old_mas = []
			
			for bvc in range(len(geometry_type_list)):
				geometry_txt_old = geometry_type_list[bvc].currentText()
				geometry_txt_old_mas.append(geometry_txt_old)
				
			for bvc in range(len(base_shape_type_list)):
				base_shape_type_old = base_shape_type_list[bvc].currentText()
				base_shape_type_old_mas.append(base_shape_type_old)
				
		else:
			geometry_1_null_lbl = QtGui.QLabel()
			tab.insertTab(1, geometry_1_null_lbl, "&geometry_1")
			tab.setTabEnabled(1, False)
			
		#-------------------------------geometry_2------------------------------------#
	
		geometry_2_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
		if geometry_visible == True and os.path.exists(geometry_2_path):       
			geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list = geometry_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
			tab.insertTab(2, geometry_2_group, "&geometry_2")
			geometry_2_btnSave.clicked.connect(self.on_geometry_2_btnSave_clicked)		
		else:
			geometry_2_null_lbl = QtGui.QLabel()
			tab.insertTab(2, geometry_2_null_lbl, "&geometry_2")
			tab.setTabEnabled(2, False)
			
		#------------------------------surfaceConformation---------------------------------#

		surfaceConformation_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceConformation.pkl'  
		if surfaceConformation_visible == True:
			surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, includedAngle_list = surfaceConformation_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, surfaceConformation_visible)
			surfaceConformation_btnSave.clicked.connect(self.on_surfaceConformation_btnSave_clicked)
			tab.insertTab(3, surfaceConformation_group, "&surfaceC")
		else:
			surfaceConformation_null_lbl = QtGui.QLabel()
			tab.insertTab(3, surfaceConformation_null_lbl, "&surfaceC")
			tab.setTabEnabled(3, False)
			
		#------------------------------initialPoints---------------------------------#

		initialPoints_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initialPoints.pkl'  
		if initialPoints_visible == True:
			initialPoints_group, initialPoints_btnSave, iPM_edit, aDC_table, aDC_checks_list, aDC_values_list, aDC_val_pr_list, aDC_val_def_list = initialPoints_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, initialPoints_visible)
			initialPoints_btnSave.clicked.connect(self.on_initialPoints_btnSave_clicked)
			tab.insertTab(4, initialPoints_group, "&initialP")
		else:
			initialPoints_null_lbl = QtGui.QLabel()
			tab.insertTab(4, initialPoints_null_lbl, "&initialP")
			tab.setTabEnabled(4, False)
			
		#------------------------------motionControl---------------------------------#

		motionControl_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'motionControl.pkl'  
		if motionControl_visible == True:
			motionControl_group, motionControl_btnSave, mC_start_prs_grid, sCF_geom_edit_list, sCF_type_edit_list, sCF_priority_edit_list, sCF_mode_edit_list, sCF_surfaceCellSizeFunction_edit_list, \
			sCF_surfaceCellSizeCoeff_edit_list, sCF_cellSizeFunction_edit_list, sCF_distanceCellSizeCoeff_edit_list, sCF_distanceCoeff_edit_list = motionControl_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, motionControl_visible)
			motionControl_btnSave.clicked.connect(self.on_motionControl_btnSave_clicked)
			tab.insertTab(5, motionControl_group, "&motionC")
		else:
			motionControl_null_lbl = QtGui.QLabel()
			tab.insertTab(5, motionControl_null_lbl, "&motionC")
			tab.setTabEnabled(5, False)
			
		#------------------------------polyMeshFiltering---------------------------------#

		polyMeshFiltering_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'polyMeshFiltering.pkl'  
		if polyMF_visible == True:
			polyMF_group, polyMF_btnSave, pMF_prs_grid = polyMF_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, polyMF_visible)
			polyMF_btnSave.clicked.connect(self.on_polyMF_btnSave_clicked)
			tab.insertTab(6, polyMF_group, "&polyMF")
		else:
			polyMeshFiltering_null_lbl = QtGui.QLabel()
			tab.insertTab(6, polyMeshFiltering_null_lbl, "&polyMF")
			tab.setTabEnabled(6, False)
			
		#-------------------------Главный фрейм формы с элементами--------------------------#

		btnSave = QtGui.QPushButton("Сохранить")
		btnSave.setFixedSize(80, 25)
		btnSave.clicked.connect(self.on_btnSave_clicked)
		btnCancel = QtGui.QPushButton("Отмена")
		btnCancel.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(btnSave)
		buttons_hbox.addWidget(btnCancel)
		if int_lng == 'Russian':
			btnSave.setText("Сохранить")
			btnCancel.setText("Отмена")
		elif int_lng == 'English':	
			btnSave.setText("Save")
			btnCancel.setText("Cancel")
   
		scrollLayout = QtGui.QFormLayout()
		scrollArea = QtGui.QScrollArea()
		scrollArea.setWidgetResizable(True) 
		scrollArea.setWidget(tab)
		scrollArea.setFixedSize(760, 580)	
			
		bMD_grid = QtGui.QGridLayout()
		bMD_grid.addWidget(scrollArea, 0, 0, alignment=QtCore.Qt.AlignCenter)
		bMD_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		bMD_frame = QtGui.QFrame()
		bMD_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
		bMD_frame.setFrameShape(QtGui.QFrame.Panel)
		bMD_frame.setFrameShadow(QtGui.QFrame.Sunken)
		bMD_frame.setLayout(bMD_grid)

		fvS_vbox = QtGui.QVBoxLayout() 
		fvS_vbox.addWidget(bMD_frame)

		# ---------------------Размещение на форме всех компонентов-------------------------#

		form = QtGui.QFormLayout()
		form.addRow(fvS_vbox)
		self.setLayout(form)
		
		#---------------------Привязываем к элементам формы обработчики, если изменяем имеющийся файл сетки----------------#
		
		if geometry_visible == True and os.path.exists(geometry_1_path):	
			for bvc in range(len(geometry_type_list)):
				self.geometry_control_chng(geometry_type_list, bvc)	
				
			if os.path.exists(geometry_2_path):
				for bvc in range(len(all_tri_file_btn_list)):
					if all_tri_file_btn_list[bvc] != '':
						self.tri_file_chng(all_tri_file_btn_list, bvc)	
						
		if initialPoints_visible == True and os.path.exists(initialPoints_path):
			for bvc in range(len(aDC_checks_list)):
				self.initialPoints_control_chng(aDC_checks_list, bvc)		
			
	#------------------------------Связываем элементы управления с функциями----------------------------#
		
	def geometry_control_chng(self, geometry_type_list, bvc):
		geometry_type_list[bvc].activated.connect(lambda: self.geometry_on_change(bvc))
		
	def tri_file_chng(self, all_tri_file_btn_list, bvc):
		all_tri_file_btn_list[bvc].clicked.connect(lambda: self.tri_file_on_change(bvc))
		
	def initialPoints_control_chng(self, aDC_checks_list, bvc):
		aDC_checks_list[bvc].clicked.connect(lambda: self.initialPoints_on_change(bvc))
	
	#------------------------------Функции, связанные с элементами формы--------------------------------#
	
	def geometry_on_change(self, bvc):
		geometry_txt = geometry_type_list[bvc].currentText()
		if geometry_txt == "Базовая фигура" or geometry_txt == "Base shape":
			base_shape_lbl_list[bvc].setVisible(True)
			base_shape_type_list[bvc].setVisible(True)
		elif geometry_txt == 'Три-поверхность' or geometry_txt == 'Tri-surface' or geometry_txt == 'Распределенная три-поверхность' or geometry_txt == 'Distributed tri-surface':
			base_shape_lbl_list[bvc].setVisible(False)
			base_shape_type_list[bvc].setVisible(False)	
	
	#---
	def tri_file_on_change(self, bvc):
		tri_file_elem = all_tri_file_btn_list[bvc]
		if tri_file_elem != '':
			tri_path = QtGui.QFileDialog.getOpenFileName(directory=QtCore.QDir.currentPath())
			if tri_path:
				tri_path_begin, tri_file = os.path.split(tri_path)
				tri_name, tri_rasshir = tri_file.split('.')
				if tri_rasshir == 'stl' or tri_rasshir == 'obj':
					all_tri_file_edit_list[bvc].setText(tri_file)
				else:
					if int_lng == 'Russian':
						dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Внимание!", "Файл должен иметь расширение .stl или .obj", buttons = QtGui.QMessageBox.Ok)
					elif int_lng == 'English':
						dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Attention!", "The file must have a .stl or .obj extension", buttons = QtGui.QMessageBox.Ok)
					result = dialog.exec_()
		
	#---
	def initialPoints_on_change(self, bvc):
		aDC_chck = aDC_checks_list[bvc].isChecked()
		if aDC_chck == True:
			aDC_val_pr_list[bvc].setEnabled(True)
			aDC_val_def_list[bvc].setEnabled(True)
			aDC_values_list[bvc].setEnabled(True)
		elif aDC_chck == False:
			aDC_val_pr_list[bvc].setEnabled(False)
			aDC_val_def_list[bvc].setEnabled(False)
			aDC_values_list[bvc].setEnabled(False)
			
	###---------------------Сохранение вкладки initial-------------------------###	
						
	def on_initial_btnSave_clicked(self):
		global geometry_1_group, geometry_1_btnSave, geometry_type_list, base_shape_lbl_list, base_shape_type_list
		
		#------------------------------Получаем текущие значения полей вкладки initial--------------------------------------#

		g_v = g_edit.value()

		#-------------------------------Сохраняем файл сетки если создаем новый----------------------------------------------#
		
		if geometry_visible == False: 
			initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
			if os.path.exists(initial_path_file) == True:
				input = open(initial_path_file, 'rb')
				obj = pickle.load(input)
				input.close()
				
				g_old = obj['g']
				
			else:
				g_old = g_v
				
			obj = {"g": g_v}
			
			prj_path_dir = prj_path + '/' + mesh_name_txt + '_' + pd_2
			
			if os.path.exists(prj_path_dir) == False:
				os.mkdir(prj_path_dir) 

			output = open(initial_path_file, 'wb')

			pickle.dump(obj, output)
			output.close()
			
			if g_v != g_old or os.path.exists(geometry_1_path) == False:
				
				if os.path.exists(geometry_1_path) == True:
					os.remove(geometry_1_path)
				if os.path.exists(geometry_2_path) == True:
					os.remove(geometry_2_path)	
				
				geometry_1_group, geometry_1_btnSave, geometry_type_list, base_shape_lbl_list, base_shape_type_list = geometry_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
				geometry_1_btnSave.clicked.connect(self.on_geometry_1_btnSave_clicked)
				
				for bvc in range(len(geometry_type_list)):
					self.geometry_control_chng(geometry_type_list, bvc)	
									
				tab.setTabEnabled(1, True)
				tab.removeTab(1)
				tab.insertTab(1, geometry_1_group, "&geometry_1")

				tab.removeTab(2)
				geometry_2_null_lbl = QtGui.QLabel()
				tab.insertTab(2, geometry_2_null_lbl, "&geometry_2")
				tab.setTabEnabled(2, False)	
			
		#-------------------------------Сохраняем файл сетки если пересохраняем имеющийся------------------------------------#
			
		if geometry_visible == True: 
			initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
			
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
			
			g_old = obj['g']

			obj = {"g": g_v}
		
			output = open(initial_path_file, 'wb')

			pickle.dump(obj, output)
			output.close()
			
		#----------------------------Формируем каждую из последующих вкладок если пересохраняем имеющийся файл-------------------------#
				
			if g_v != g_old:
				
				if os.path.exists(geometry_1_path) == True: 
					os.remove(geometry_1_path)
				if os.path.exists(geometry_2_path) == True:
					os.remove(geometry_2_path)
				
				tab.removeTab(1)
				
				geometry_1_group, geometry_1_btnSave, geometry_type_list, base_shape_lbl_list, base_shape_type_list = geometry_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
				geometry_1_btnSave.clicked.connect(self.on_geometry_1_btnSave_clicked)
			
				tab.insertTab(1, geometry_1_group, "&geometry_1")
				
				for bvc in range(len(geometry_type_list)):
					self.geometry_control_chng(geometry_type_list, bvc)		
			
				tab.removeTab(2)
				geometry_2_null_lbl = QtGui.QLabel()
				tab.insertTab(2, geometry_2_null_lbl, "&geometry_2")
				tab.setTabEnabled(2, False)
				
		#----------------------------Формируем каждую из последующих вкладок если сохраняем новый файл-------------------------#

		msg_list = []

		if os.path.exists(prj_path_dir) == False:
			os.mkdir(prj_path_dir) 

		output = open(initial_path_file, 'wb')

		pickle.dump(obj, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Начальные данные успешно сохранены"
		elif int_lng == 'English':
			msg = "Initial data saved successfully"
		msg_list.append(msg)
		self.on_msg_correct(msg)
		
	###---------------------Сохранение вкладки geometry_1-------------------------###
	
	def on_geometry_1_btnSave_clicked(self):
		global geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list
		global geometry_txt_old_mas
		global base_shape_type_old_mas

		obj_list = []
		i = 1
		j = 0
		for el_m in geometry_type_list:
			if el_m.currentText() == 'Три-поверхность' or el_m.currentText() == 'Tri-surface' or el_m.currentText() == 'Распределенная три-поверхность' or el_m.currentText() == 'Distributed tri-surface':
				obj = {'geometry_' + str(i): el_m.currentText()}
			elif el_m.currentText() == 'Базовая фигура' or el_m.currentText() == 'Base shape':
				obj = {'geometry_' + str(i): el_m.currentText(), 'shape_type_' + str(i): base_shape_type_list[j].currentText()}
			obj_list.append(obj)
				
			i = i + 1
			j = j + 1
		
		print(obj_list)
		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_1.pkl', 'wb')
		pickle.dump(obj_list, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные geometry_1 успешно сохранены"
		elif int_lng == 'English':
			msg = "The geometry_1 data was successfully saved"
		self.on_msg_correct(msg)
		
		if geometry_visible == False:
			if os.path.exists(geometry_2_path) == True:
				os.remove(geometry_2_path)

			geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list = geometry_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
			geometry_2_btnSave.clicked.connect(self.on_geometry_2_btnSave_clicked)
			
			for bvc in range(len(all_tri_file_btn_list)):
				if all_tri_file_btn_list[bvc] != '':
					self.tri_file_chng(all_tri_file_btn_list, bvc)	
			
			tab.setTabEnabled(2, True)
			tab.removeTab(2)
			tab.insertTab(2, geometry_2_group, "&geometry_2")
			
		if geometry_visible == True:
			geometry_txt_new_mas = []
			base_shape_type_new_mas = []
			
			for bvc in range(len(geometry_type_list)):
				geometry_txt_new = geometry_type_list[bvc].currentText()
				geometry_txt_new_mas.append(geometry_txt_new)
				
			for bvc in range(len(base_shape_type_list)):
				base_shape_type_new = base_shape_type_list[bvc].currentText()
				base_shape_type_new_mas.append(base_shape_type_new)
							
				if os.path.exists(surfaceConformation_path) == True:
					os.remove(surfaceConformation_path)
				elif os.path.exists(initialPoints_path) == True:
					os.remove(initialPoints_path)
				elif os.path.exists(motionControl_path) == True:
					os.remove(motionControl_path)
				elif os.path.exists(polyMeshFiltering_path) == True:
					os.remove(polyMeshFiltering_path)
				geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list = geometry_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
				geometry_2_btnSave.clicked.connect(self.on_geometry_2_btnSave_clicked)
				
				for bvc in range(len(all_tri_file_btn_list)):
					if all_tri_file_btn_list[bvc] != '':
						self.tri_file_chng(all_tri_file_btn_list, bvc)	
				
				tab.setTabEnabled(2, True)
				tab.removeTab(2)
				tab.insertTab(2, geometry_2_group, "&geometry_2")
				
				tab.setTabEnabled(3, True)
				tab.removeTab(3)
				tab.insertTab(3, surfaceConformation_group, "&surfaceC")
				
				tab.setTabEnabled(4, True)
				tab.removeTab(4)
				tab.insertTab(4, initialPoints_group, "&initialP")
				
				tab.setTabEnabled(5, True)
				tab.removeTab(5)
				tab.insertTab(5, motionControl_group, "&motionC")
				
				tab.setTabEnabled(6, True)
				tab.removeTab(6)
				tab.insertTab(6, polyMeshFiltering_group, "&polyMF")
			
			geometry_txt_old_mas = geometry_txt_new_mas
			base_shape_type_old_mas = base_shape_type_new_mas
			
###---------------------Сохранение вкладки geometry_2-------------------------###		
		
	def on_geometry_2_btnSave_clicked(self):
		global surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, includedAngle_list
		global initialPoints_group, initialPoints_btnSave, iPM_edit, aDC_table, aDC_checks_list, aDC_values_list, aDC_val_pr_list, aDC_val_def_list
		global motionControl_group, motionControl_btnSave, mC_start_prs_grid, sCF_geom_edit_list, sCF_type_edit_list, sCF_priority_edit_list, sCF_mode_edit_list, sCF_surfaceCellSizeFunction_edit_list, \
		sCF_surfaceCellSizeCoeff_edit_list, sCF_cellSizeFunction_edit_list, sCF_distanceCellSizeCoeff_edit_list, sCF_distanceCoeff_edit_list
		global polyMF_group, polyMF_btnSave, pMF_prs_grid
		
		obj_list = []

		n = 1
		t = 0
		
		msg_list = []
		for el_m in all_geometry_list:	
				
			###############################################tri_table#########################################################
			if all_geometry_list_lbls[t] == 'tri_table':

				tri_table_stroka = []
				
				#file
				file_val = el_m.cellWidget(0, 0).layout().itemAt(0).widget().text()
					
				if file_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Файл' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'file' of geometry " + str(n)
					msg_list.append(msg)
				else:
					tri_table_stroka.append(file_val)
				#type
				type_val = el_m.cellWidget(0, 1).layout().itemAt(0).widget().currentText()
				tri_table_stroka.append(type_val)
				#name
				name_val = el_m.cellWidget(0, 2).layout().itemAt(0).widget().text()
				if name_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Название' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'name' of geometry " + str(n)
					msg_list.append(msg)
				else:
					tri_table_stroka.append(name_val)

				if len(tri_table_stroka) == 3:
					obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'file': file_val, 'type': type_val, 'name': name_val}
					obj_list.append(obj)
			
			###############################################distrib_tri_table##################################################
			
			if all_geometry_list_lbls[t] == 'distrib_tri_table':
				
				distrib_tri_table_stroka = []
				
				#file
				file_val = el_m.cellWidget(0, 0).layout().itemAt(0).widget().text()
				if file_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Файл' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'file' of geometry " + str(n)
					msg_list.append(msg)
				else:
					distrib_tri_table_stroka.append(file_val)
				#type
				type_val = el_m.cellWidget(0, 1).layout().itemAt(0).widget().currentText()
				distrib_tri_table_stroka.append(type_val)
				#distributionType
				distributionType_val = el_m.cellWidget(0, 2).layout().itemAt(0).widget().currentText()
				distrib_tri_table_stroka.append(distributionType_val)
				#name
				name_val = el_m.cellWidget(0, 3).layout().itemAt(0).widget().text()
				if name_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Название' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'name' of geometry " + str(n)
					msg_list.append(msg)
				else:
					distrib_tri_table_stroka.append(name_val)
					
				if len(distrib_tri_table_stroka) == 4:
					obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'file': file_val, 'type': type_val, 'distributionType': distributionType_val, 'name': name_val}
					obj_list.append(obj)
			
			###############################################box_table##################################################
			
			if all_geometry_list_lbls[t] == 'box_table':
				
				btn = el_m.rowCount()

				p = 1
				y = 0
				box_table_stroka = []
				while p <= btn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						box_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					box_table_stroka.append(type_val)
					#min
					min_val = []
					min_hbox = el_m.cellWidget(y, 2).layout()
					min_x = min_hbox.itemAt(1).widget().text()
					if min_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Мин' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'min' of geometry " + str(n)
						msg_list.append(msg)
					else:
						min_val.append(min_x)
					min_y = min_hbox.itemAt(3).widget().text()
					if min_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Мин' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'min' of geometry " + str(n)
						msg_list.append(msg)
					else:
						min_val.append(min_y)
					min_z = min_hbox.itemAt(5).widget().text()
					if min_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Мин' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'min' of geometry " + str(n)
						msg_list.append(msg)
					else:
						min_val.append(min_z)
					if len(min_val) == 3:
						box_table_stroka.append(min_val)
					
					#max
					max_val = []
					max_hbox = el_m.cellWidget(y, 3).layout()
					max_x = max_hbox.itemAt(1).widget().text()
					if max_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Макс' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'max' of geometry " + str(n)
						msg_list.append(msg)
					else:
						max_val.append(max_x)
					max_y = max_hbox.itemAt(3).widget().text()
					if max_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Макс' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'max' of geometry " + str(n)
						msg_list.append(msg)
					else:
						max_val.append(max_y)
					max_z = max_hbox.itemAt(5).widget().text()
					if max_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Макс' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'max' of geometry " + str(n)
						msg_list.append(msg)
					else:
						max_val.append(max_z)
					if len(max_val) == 3:
						box_table_stroka.append(max_val)
					
					p = p + 1
					y = y + 1
					
					if len(box_table_stroka) == 4:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'min': min_val, 'max': max_val}
						obj_list.append(obj)
			
			###############################################sphere_table##################################################
			
			if all_geometry_list_lbls[t] == 'sphere_table':
				
				stn = el_m.rowCount()

				p = 1
				y = 0
				sphere_table_stroka = []
				while p <= stn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						sphere_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					sphere_table_stroka.append(type_val)
					#centre					
					centre_val = []					
					centre_hbox = el_m.cellWidget(y, 2).layout()
					centre_x = centre_hbox.itemAt(1).widget().text()				
					if centre_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Центр' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'centre' of geometry " + str(n)
						msg_list.append(msg)
					else:
						centre_val.append(centre_x)
					centre_y = centre_hbox.itemAt(3).widget().text()	
					if centre_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Центр' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'centre' of geometry " + str(n)
						msg_list.append(msg)
					else:
						centre_val.append(centre_y)
					centre_z = centre_hbox.itemAt(5).widget().text()	
					if centre_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Центр' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'centre' of geometry " + str(n)
						msg_list.append(msg)
					else:
						centre_val.append(centre_z)
					if len(centre_val) == 3:
						sphere_table_stroka.append(centre_val)
					
					#radius
					radius_val = el_m.cellWidget(y, 3).text()
					if radius_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Радиус' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of the field 'radius' of geometry " + str(n)
						msg_list.append(msg)
					else:
						sphere_table_stroka.append(radius_val)
										
					p = p + 1
					y = y + 1
					
					if len(sphere_table_stroka) == 4:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'centre': centre_val, 'radius': radius_val}
						obj_list.append(obj)
			
			###############################################cylinder_table##################################################
			
			if all_geometry_list_lbls[t] == 'cylinder_table':
				
				ctn = el_m.rowCount()

				p = 1
				y = 0
				cylinder_table_stroka = []
				while p <= ctn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						cylinder_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					cylinder_table_stroka.append(type_val)
					#point1					
					point1_val = []					
					point1_hbox = el_m.cellWidget(y, 2).layout()
					point1_x = point1_hbox.itemAt(1).widget().text()					
					if point1_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Точка_1' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'point1' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point1_val.append(point1_x)
					point1_y = point1_hbox.itemAt(3).widget().text()	
					if point1_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Точка_1' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'point1' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point1_val.append(point1_y)
					point1_z = point1_hbox.itemAt(5).widget().text()	
					if point1_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Точка_1' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'point1' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point1_val.append(point1_z)
					if len(point1_val) == 3:
						cylinder_table_stroka.append(point1_val)
					#point2
					point2_val = []					
					point2_hbox = el_m.cellWidget(y, 3).layout()
					point2_x = point2_hbox.itemAt(1).widget().text()	
					if point2_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Точка_2' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'point2' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point2_val.append(point2_x)
					point2_y = point2_hbox.itemAt(3).widget().text()
					if point2_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Точка_2' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'point2' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point2_val.append(point2_y)
					point2_z = point2_hbox.itemAt(5).widget().text()
					if point2_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Точка_2' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'point2' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point2_val.append(point2_z)
					
					if len(point2_val) == 3:
						cylinder_table_stroka.append(point2_val)
					
					#radius
					radius_val = el_m.cellWidget(y, 4).value()
					cylinder_table_stroka.append(radius_val)
					if radius_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Радиус' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of the field 'Radius' of geometry " + str(n)
						msg_list.append(msg)
					else:
						cylinder_table_stroka.append(radius_val)
																				
					p = p + 1
					y = y + 1
					
					if len(cylinder_table_stroka) == 5:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'point1': point1_val, 'point2': point1_val, 'radius': radius_val}
						obj_list.append(obj)

			###############################################plane_table##################################################
			
			if all_geometry_list_lbls[t] == 'plane_table':
				
				ptn = el_m.rowCount()

				p = 1
				y = 0
				plane_table_stroka = []
				while p <= ptn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						plane_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					plane_table_stroka.append(type_val)
					#planeType
					planeType_val = el_m.cellWidget(y, 2).currentText()
					plane_table_stroka.append(planeType_val)
					#basePoint
					basePoint_val = []					
					basePoint_hbox = el_m.cellWidget(y, 3).layout()
					basePoint_x = basePoint_hbox.itemAt(1).widget().text()	
					if basePoint_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Базовая точка' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'basePoint' of geometry " + str(n)
						msg_list.append(msg)
					else:
						basePoint_val.append(basePoint_x)
					basePoint_y = basePoint_hbox.itemAt(3).widget().text()	
					if basePoint_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Базовая точка' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'basePoint' of geometry " + str(n)
						msg_list.append(msg)
					else:
						basePoint_val.append(basePoint_y)
					basePoint_z = basePoint_hbox.itemAt(5).widget().text()	
					if basePoint_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Базовая точка' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'basePoint' of geometry " + str(n)
						msg_list.append(msg)
					else:
						basePoint_val.append(basePoint_z)
						
					if len(basePoint_val) == 3:
						plane_table_stroka.append(basePoint_val)
					
					#normalVector					
					normalVector_val = []					
					normalVector_hbox = el_m.cellWidget(y, 4).layout()
					normalVector_x = basePoint_hbox.itemAt(1).widget().text()	
					if normalVector_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Вектор нормали' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'normalVector' of geometry " + str(n)
						msg_list.append(msg)
					else:
						normalVector_val.append(normalVector_x)
					normalVector_y = basePoint_hbox.itemAt(3).widget().text()	
					if normalVector_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Вектор нормали' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'normalVector' of geometry " + str(n)
						msg_list.append(msg)
					else:
						normalVector_val.append(normalVector_y)
					normalVector_z = basePoint_hbox.itemAt(5).widget().text()	
					if normalVector_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Вектор нормали' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'normalVector' of geometry " + str(n)
						msg_list.append(msg)
					else:
						normalVector_val.append(normalVector_z)
						
					if len(basePoint_val) == 3:
						plane_table_stroka.append(normalVector_val)
														
					p = p + 1
					y = y + 1
					
					if len(plane_table_stroka) == 5:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'planeType': planeType_val, 'basePoint': basePoint_val, 'normalVector': normalVector_val}
						obj_list.append(obj)
			
			###############################################plate_table##################################################
			
			if all_geometry_list_lbls[t] == 'plate_table':
				
				ptn = el_m.rowCount()

				p = 1
				y = 0
				plate_table_stroka = []
				while p <= ptn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						plate_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					plate_table_stroka.append(type_val)
					#origin					
					origin_val = []					
					origin_hbox = el_m.cellWidget(y, 2).layout()
					origin_x = origin_hbox.itemAt(1).widget().text()						
					if origin_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Происхождение' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'origin' of geometry " + str(n)
						msg_list.append(msg)
					else:
						origin_val.append(origin_x)
					origin_y = origin_hbox.itemAt(3).widget().text()
					if origin_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Происхождение' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'origin' of geometry " + str(n)
						msg_list.append(msg)
					else:
						origin_val.append(origin_x)
					origin_z = origin_hbox.itemAt(5).widget().text()
					if origin_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Происхождение' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'origin' of geometry " + str(n)
						msg_list.append(msg)
					else:
						origin_val.append(origin_z)
					
					if len(origin_val) == 3:
						plate_table_stroka.append(origin_val)
					#span
					span_val = []					
					span_hbox = el_m.cellWidget(y, 3).layout()
					span_x = span_hbox.itemAt(1).widget().text()		
					if span_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Пролет' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'span' of geometry " + str(n)
						msg_list.append(msg)
					else:
						span_val.append(span_x)
					
					span_y = span_hbox.itemAt(3).widget().text()
					if span_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Пролет' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'span' of geometry " + str(n)
						msg_list.append(msg)
					else:
						span_val.append(span_y)
					span_z = span_hbox.itemAt(5).widget().text()
					if span_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Пролет' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'span' of geometry " + str(n)
						msg_list.append(msg)
					else:
						span_val.append(span_z)
					
					if len(span_val) == 3:
						plate_table_stroka.append(span_val)					
					
					p = p + 1
					y = y + 1
					
					if len(plate_table_stroka) == 4:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'origin': origin_val, 'span': span_val}
						obj_list.append(obj)
				
			n = n + 1	
			t = t + 1
				
		self.on_msg_error(msg_list)	
		
		#####---------------------Итоговое сохранение geometry_2-------------------------#####
		
		if len(all_geometry_list) == len(obj_list):
			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl', 'wb')
			print(obj_list)
			pickle.dump(obj_list, output)
			output.close()	
				
			if int_lng == 'Russian':
				msg = "Данные 'geometry_2' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'geometry_2' data was successfully saved"

			self.on_msg_correct(msg)
			
			if surfaceConformation_visible == False or surfaceConformation_visible == True:
				surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, includedAngle_list = surfaceConformation_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, surfaceConformation_visible)
				surfaceConformation_btnSave.clicked.connect(self.on_surfaceConformation_btnSave_clicked)
				
				tab.setTabEnabled(3, True)
				tab.removeTab(3)
				tab.insertTab(3, surfaceConformation_group, "&surfaceC")
				
			if initialPoints_visible == False or initialPoints_visible == True:
				initialPoints_group, initialPoints_btnSave, iPM_edit, aDC_table, aDC_checks_list, aDC_values_list, aDC_val_pr_list, aDC_val_def_list = initialPoints_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, initialPoints_visible)
				initialPoints_btnSave.clicked.connect(self.on_initialPoints_btnSave_clicked)
				
				for bvc in range(len(aDC_checks_list)):
					self.initialPoints_control_chng(aDC_checks_list, bvc)
				
				tab.setTabEnabled(4, True)
				tab.removeTab(4)
				tab.insertTab(4, initialPoints_group, "&initialP")
				
			if motionControl_visible == False or motionControl_visible == True:
				motionControl_group, motionControl_btnSave, mC_start_prs_grid, sCF_geom_edit_list, sCF_type_edit_list, sCF_priority_edit_list, sCF_mode_edit_list, sCF_surfaceCellSizeFunction_edit_list, \
				sCF_surfaceCellSizeCoeff_edit_list, sCF_cellSizeFunction_edit_list, sCF_distanceCellSizeCoeff_edit_list, sCF_distanceCoeff_edit_list = motionControl_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, motionControl_visible)
				
				motionControl_btnSave.clicked.connect(self.on_motionControl_btnSave_clicked)
				
				tab.setTabEnabled(5, True)
				tab.removeTab(5)
				tab.insertTab(5, motionControl_group, "&motionC")
				
			if polyMF_visible == False or polyMF_visible == True:
				polyMF_group, polyMF_btnSave, pMF_prs_grid = polyMF_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, polyMF_visible)
				
				polyMF_btnSave.clicked.connect(self.on_polyMF_btnSave_clicked)
				
				tab.setTabEnabled(6, True)
				tab.removeTab(6)
				tab.insertTab(6, polyMF_group, "&polyMF")
				
	###---------------------Сохранение вкладки surfaceConformation-------------------------###	
	
	def on_surfaceConformation_btnSave_clicked(self):
		sC_obj = {}
		
		lIM_edit_x = sC_start_prs_grid.itemAtPosition(0,1).widget()
		lIM_edit_y = sC_start_prs_grid.itemAtPosition(0,2).widget()
		lIM_edit_z = sC_start_prs_grid.itemAtPosition(0,3).widget()
		
		msg_list = []
		lIM_list = []
		if lIM_edit_x.text() == '':
			if int_lng == 'Russian':
				msg = "Укажите параметр 'x' вектора locationInMesh"
			elif int_lng == 'English':
				msg = "Specify the 'x' parameter of vector locationInMesh"
			msg_list.append(msg)
		else:
			lIM_list.append(lIM_edit_x.text())
		if lIM_edit_y.text() == '':
			if int_lng == 'Russian':
				msg = "Укажите параметр 'y' вектора locationInMesh"
			elif int_lng == 'English':
				msg = "Specify the 'y' parameter of vector locationInMesh"
			msg_list.append(msg)
		else:
			lIM_list.append(lIM_edit_y.text())
		if lIM_edit_z.text() == '':
			if int_lng == 'Russian':
				msg = "Укажите параметр 'z' вектора locationInMesh"
			elif int_lng == 'English':
				msg = "Specify the 'z' parameter of vector locationInMesh"
			msg_list.append(msg)
		else:
			lIM_list.append(lIM_edit_z.text())
			
		self.on_msg_error(msg_list)
		
		sFP_edit = sC_start_prs_grid.itemAtPosition(2,1).widget()
		eA_edit = sC_start_prs_grid.itemAtPosition(3,1).widget()
		gFP_edit = sC_start_prs_grid.itemAtPosition(4,1).widget()
		snapFP_edit = sC_start_prs_grid.itemAtPosition(5,1).widget()
		cE_edit = sC_start_prs_grid.itemAtPosition(6,1).widget()

		obj_sC_start_prs_obj = {'lIM': lIM_list, 'sFP': sFP_edit.currentText(), 'eA': eA_edit.currentText(), 'gFP': gFP_edit.currentText(), 'snapFP': snapFP_edit.currentText(), 'cE': cE_edit.currentText()} 
		sC_obj['sC_start_prs'] = obj_sC_start_prs_obj
		
		k = 1
		i = 0
		conf_obj_list = []
		print(geometry_list)
		print(featureMethod_list)
		print(includedAngle_list)
		for el_g in range(len(geometry_list)):
			conf_obj = {'g': geometry_list[i].currentText(), 'fM': featureMethod_list[i].currentText(), 'iA': includedAngle_list[i].value()}
			conf_obj_list.append(conf_obj)
			
			k = k + 1
			i = i + 1
		
		sC_obj['sC_conf_prs'] = conf_obj_list
			
		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceConformation.pkl', 'wb')
		print(sC_obj)
		pickle.dump(sC_obj, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные 'surfaceConformation' успешно сохранены"
		elif int_lng == 'English':
			msg = "The 'surfaceConformation' data was successfully saved"

		self.on_msg_correct(msg)	
		
		
	###----------------------Сохранение вкладки initialPoints--------------------------###
	
	def on_initialPoints_btnSave_clicked(self):

		iP_obj = {}
		iP_obj['iP'] = iPM_edit.currentText()
		
		# minCellSizeLimit
		mCSL_chck = aDC_table.cellWidget(0, 0).layout().itemAt(0).widget()
		if mCSL_chck.isChecked() == True:
			mCSL_val = aDC_table.cellWidget(0, 3).layout().itemAt(0).widget()
			iP_obj['minCellSizeLimit_chck'] = True
			iP_obj['minCellSizeLimit'] = mCSL_val.value()
		else:
			iP_obj['minCellSizeLimit_chck'] = False
			
		# minLevels
		mL_chck = aDC_table.cellWidget(1, 0).layout().itemAt(0).widget()
		if mL_chck.isChecked() == True:
			mL_val = aDC_table.cellWidget(1, 3).layout().itemAt(0).widget()
			iP_obj['minLevels_chck'] = True
			iP_obj['minLevels'] = mL_val.value()
		else:
			iP_obj['minLevels_chck'] = False
			
		# maxSizeRatio
		mSR_chck = aDC_table.cellWidget(2, 0).layout().itemAt(0).widget()
		if mSR_chck.isChecked() == True:
			mSR_val = aDC_table.cellWidget(2, 3).layout().itemAt(0).widget()
			iP_obj['maxSizeRatio_chck'] = True
			iP_obj['maxSizeRatio'] = mSR_val.value()
		else:
			iP_obj['maxSizeRatio_chck'] = False
			
		# sampleResolution
		sR_chck = aDC_table.cellWidget(3, 0).layout().itemAt(0).widget()
		if sR_chck.isChecked() == True:
			sR_val = aDC_table.cellWidget(3, 3).layout().itemAt(0).widget()
			iP_obj['sampleResolution'] = sR_val.value()
			iP_obj['sampleResolution_chck'] = True
		else:
			iP_obj['sampleResolution_chck'] = False
			
		# surfaceSampleResolution
		sSR_chck = aDC_table.cellWidget(4, 0).layout().itemAt(0).widget()
		if sSR_chck.isChecked() == True:
			sSR_val = aDC_table.cellWidget(4, 3).layout().itemAt(0).widget()
			iP_obj['surfaceSampleResolution'] = sSR_val.value()
			iP_obj['surfaceSampleResolution_chck'] = True
		else:
			iP_obj['surfaceSampleResolution_chck'] = False
				
		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initialPoints.pkl', 'wb')
		print(iP_obj)
		pickle.dump(iP_obj, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные 'initialPoints' успешно сохранены"
		elif int_lng == 'English':
			msg = "The 'initialPoints' data was successfully saved"

		self.on_msg_correct(msg)
			
	###---------------------Сохранение вкладки motionControl-------------------------###		
	
	def on_motionControl_btnSave_clicked(self):
		mC_obj = {}
		
		dCS_edit = mC_start_prs_grid.itemAtPosition(0,1).widget()
		mCSC_edit = mC_start_prs_grid.itemAtPosition(1,1).widget()
		mSI_edit = mC_start_prs_grid.itemAtPosition(2,1).widget()
		mRI_edit = mC_start_prs_grid.itemAtPosition(3,1).widget()
		oO_edit = mC_start_prs_grid.itemAtPosition(4,1).widget()
		tC_edit = mC_start_prs_grid.itemAtPosition(5,1).widget()
		
		obj_mC_start_prs_obj = {'dCS': dCS_edit.value(), 'mCSC': mCSC_edit.value(), 'mSI': mSI_edit.value(), 'mRI': mRI_edit.value(), 'oO': oO_edit.currentText(), 'tC': tC_edit.currentText()}
		
		mC_obj['mC_start_prs'] = obj_mC_start_prs_obj
		
		k = 1
		i = 0
		sCF_obj_list = []
		for el_s in range(len(sCF_geom_edit_list)):
			sCF_obj = {}
			
			sCF_obj['g'] = sCF_geom_edit_list[i].currentText()
			sCF_obj['t'] = sCF_type_edit_list[i].currentText()
			sCF_obj['p'] = sCF_priority_edit_list[i].value()
			sCF_obj['m'] = sCF_mode_edit_list[i].currentText()
			sCF_obj['sCSF'] = sCF_surfaceCellSizeFunction_edit_list[i].currentText()
			sCF_obj['sCSC'] = sCF_surfaceCellSizeCoeff_edit_list[i].value()
			sCF_obj['cSF'] = sCF_cellSizeFunction_edit_list[i].currentText()
			sCF_obj['dCSC'] = sCF_distanceCellSizeCoeff_edit_list[i].value()
			sCF_obj['dC'] = sCF_distanceCoeff_edit_list[i].value()
			
			sCF_obj_list.append(sCF_obj)
			
			k = k + 1
			i = i + 1
			
		mC_obj['mC_sCF_prs'] = sCF_obj_list
		
		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'motionControl.pkl', 'wb')
		print(mC_obj)
		pickle.dump(mC_obj, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные 'motionControl' успешно сохранены"
		elif int_lng == 'English':
			msg = "The 'motionControl' data was successfully saved"

		self.on_msg_correct(msg)
		
	###---------------------Сохранение вкладки polyMF-------------------------###
	
	def on_polyMF_btnSave_clicked(self):
	
		polyMF_obj = {}

		fE_edit = pMF_prs_grid.itemAtPosition(0,1).widget()
		fF_edit = pMF_prs_grid.itemAtPosition(1,1).widget()
		wTDM_edit = pMF_prs_grid.itemAtPosition(2,1).widget()

		polyMF_obj['fE'] = fE_edit.currentText()
		polyMF_obj['fF'] = fF_edit.currentText()
		polyMF_obj['wTDM'] = wTDM_edit.currentText()

		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'polyMF.pkl', 'wb')
		print(polyMF_obj)
		pickle.dump(polyMF_obj, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные 'polyMF_obj' успешно сохранены"
		elif int_lng == 'English':
			msg = "The 'polyMF_obj' data was successfully saved"

		self.on_msg_correct(msg)

	###--------------------Функции вывода служебных сообщений-------------------------------#
			
	def on_msg_correct(self, msg):
		parn.listWidget.clear()
		parn.item = QtGui.QListWidgetItem(msg, parn.listWidget)
		color = QtGui.QColor("green")
		parn.item.setTextColor(color)
		parn.listWidget.addItem(parn.item)		
	def on_msg_error(self, msg_list):
		parn.listWidget.clear()
		for msg in msg_list:
			parn.item = QtGui.QListWidgetItem(msg, parn.listWidget)
			color = QtGui.QColor("red")
			parn.item.setTextColor(color)
			parn.listWidget.addItem(parn.item)

	###---------------------Запуск сохранения файла foamyHexMeshDict-------------------------###			
			
	def on_btnSave_clicked(self):
		foamyHexMeshDict_generation_class.foamyHexMeshDict_func(int_lng, parn, tab, prj_path, mesh_name_txt, pd_2, self)

	             
