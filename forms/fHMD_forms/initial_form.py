# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class initial_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2): 
		initial_obj = None
		
		#----------------Если файл initial.pkl существует, получаем данные из него для вывода в форму---------------#

		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
			input = open(initial_path_file, 'rb')
			initial_obj = pickle.load(input)
			input.close()
			
			geometry_visible = True
			surfaceConformation_visible = True
			initialPoints_visible = True
			motionControl_visible = True
			polyMF_visible = True
			
		else:
			geometry_visible = False
			surfaceConformation_visible = False
			initialPoints_visible = False
			motionControl_visible = False
			polyMF_visible = False
		
		#-----------------------Формируем внешний вид формы для файла initial.pkl----------------------#	
		
		main_lbl = QtGui.QLabel()
		
		#######################################Список названий параметров###############################	
		
		g_key = QtGui.QLabel("geometry")
		
		#######################################Список описаний параметров###############################	

		g_lbl = QtGui.QLabel()
		
		#####################Список элементов управления для значений параметров########################	
				
		g_edit = QtGui.QSpinBox()
		g_edit.setRange(1, 1000)
		g_hbox = QtGui.QHBoxLayout()
		g_hbox.setContentsMargins(0, 2, 0, 0)
		g_hbox.addWidget(g_edit)
		g_hbox.setAlignment(QtCore.Qt.AlignCenter)
		g_cell_widget = QtGui.QWidget()
		g_cell_widget.setLayout(g_hbox)
		if initial_obj != None:
			g_edit.setValue(initial_obj['g'])
		
		g_edit.setFixedSize(70, 22) 

		############################################Таблица параметров##################################
		
		initial_table = QtGui.QTableWidget()
		initial_table.setFixedSize(610, 60)
		initial_table.setRowCount(1)
		initial_table.setColumnCount(3)
		
		initial_table.horizontalHeader().resizeSection(0, 155)
		initial_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
		column_1 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(0, column_1)
		initial_table.horizontalHeader().setStyleSheet("color: steelblue")

		initial_table.horizontalHeader().resizeSection(1, 360)
		initial_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
		column_2 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(1, column_2)
		
		initial_table.horizontalHeader().resizeSection(2, 75)
		initial_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
		column_3 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(2, column_3)	
		
		initial_table.setCellWidget(0,0, g_key)
		initial_table.setCellWidget(0,1, g_lbl)
		initial_table.setCellWidget(0,2, g_cell_widget)
		
        # -----------------------------Кнопка сохранения--------------------------#

		initial_btnSave = QtGui.QPushButton()
		initial_btnSave.setFixedSize(80, 25)

		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(initial_btnSave)
		
		# ----------------------Определяем параметры интерфейса окна--------------#
		
		if int_lng == 'Russian':
			
			main_lbl.setText("Начальные данные")
			
			column_1.setText("Параметр")
			column_2.setText("Описание")
			column_3.setText("Значение")
			
			g_lbl.setText("Количество используемых геометрий")
			
			initial_btnSave.setText("Записать")
			
		elif int_lng == 'English':
			
			main_lbl.setText("Initial data")
			
			column_1.setText("Parameter")
			column_2.setText("Description")
			column_3.setText("Value")
			
			g_lbl.setText("Number of used geometries")
			
			initial_btnSave.setText("Write")
			
        # -------------------------Групповой элемент формы---------------------------#

		initial_grid = QtGui.QGridLayout()
		initial_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.addWidget(initial_table, 1, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.setRowStretch(3, 6)

		initial_group = QtGui.QGroupBox()
		initial_group.setLayout(initial_grid)
		
		return initial_group, initial_btnSave, geometry_visible, surfaceConformation_visible, initialPoints_visible, motionControl_visible, polyMF_visible, g_edit
	
