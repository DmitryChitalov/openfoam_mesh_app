# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class surfaceConformation_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, surfaceConformation_visible): 
		surfaceConformation_obj = None
		
		#----------------Если файл surfaceConformation.pkl существует, получаем данные из него для вывода в форму---------------#

		if surfaceConformation_visible == True:
			surfaceConformation_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceConformation.pkl'
			if os.path.exists(surfaceConformation_path_file):
		
				input = open(surfaceConformation_path_file, 'rb')
				surfaceConformation_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла surfaceConformation.pkl на основе данных файла initial.pkl-------------#
		
		prs_grid = QtGui.QGridLayout()
		prs_frame = QtGui.QFrame()
		prs_frame.setLayout(prs_grid)
		
		#####-----------------------Первая часть параметров------------------------------#####
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Параметры управления конформацией поверхностей")
		elif int_lng == 'English':
			main_lbl.setText("Parameters of surface conformation")
			
		#locationInMesh#
		lIM_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			lIM_lbl.setText("Вектор координат плоскости (locationInMesh):")
		elif int_lng == 'English':
			lIM_lbl.setText("The coordinate vector of the plane (locationInMesh):")
			
		lIM_edit_x = QtGui.QLineEdit()
		lIM_edit_x.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, lIM_edit_x))
		lIM_edit_x.setFixedSize(80, 25)
		lIM_edit_y = QtGui.QLineEdit()
		lIM_edit_y.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, lIM_edit_y))
		lIM_edit_y.setFixedSize(80, 25)
		lIM_edit_z = QtGui.QLineEdit()
		lIM_edit_z.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, lIM_edit_z))
		lIM_edit_z.setFixedSize(80, 25)
		if surfaceConformation_obj != None:
			lIM_edit_x.setText(surfaceConformation_obj['sC_start_prs']['lIM'][0])
			lIM_edit_y.setText(surfaceConformation_obj['sC_start_prs']['lIM'][1])
			lIM_edit_z.setText(surfaceConformation_obj['sC_start_prs']['lIM'][2])
		
		#featurePointControls
		fPC_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			fPC_lbl.setText("Функции управления точками")
		elif int_lng == 'English':
			fPC_lbl.setText("Feature point controls")
		
		#specialiseFeaturePoints
		sFP_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			sFP_lbl.setText("Cпециализировать функции:")
		elif int_lng == 'English':
			sFP_lbl.setText("Specialise feature points:")
			
		sFP_edit = QtGui.QComboBox()
		sFP_edit.addItems(['on', 'off'])
		sFP_edit.setFixedSize(80, 25)	
		if surfaceConformation_obj != None:
			sFP_edit_mas = sFP_edit.count()  
			for t in range(sFP_edit_mas):
				if sFP_edit.itemText(t) == surfaceConformation_obj['sC_start_prs']['sFP']:
					sFP_edit.setCurrentIndex(t)
			
		#edgeAiming
		eA_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			eA_lbl.setText("Прицеливание ядра:")
		elif int_lng == 'English':
			eA_lbl.setText("Edge aiming:")
			
		eA_edit = QtGui.QComboBox()
		eA_edit.addItems(['on', 'off'])
		eA_edit.setFixedSize(80, 25)	
		if surfaceConformation_obj != None:
			eA_edit_mas = eA_edit.count()  
			for t in range(eA_edit_mas):
				if eA_edit.itemText(t) == surfaceConformation_obj['sC_start_prs']['eA']:
					eA_edit.setCurrentIndex(t)
		
		#guardFeaturePoints
		gFP_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			gFP_lbl.setText("Защитные функции:")
		elif int_lng == 'English':
			gFP_lbl.setText("Guard feature points:")
			
		gFP_edit = QtGui.QComboBox()
		gFP_edit.addItems(['on', 'off'])
		gFP_edit.setFixedSize(80, 25)	
		if surfaceConformation_obj != None:
			gFP_edit_mas = gFP_edit.count()  
			for t in range(gFP_edit_mas):
				if gFP_edit.itemText(t) == surfaceConformation_obj['sC_start_prs']['gFP']:
					gFP_edit.setCurrentIndex(t)
		
		#snapFeaturePoints
		snapFP_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			snapFP_lbl.setText("Оснастка:")
		elif int_lng == 'English':
			snapFP_lbl.setText("Snap feature points:")
			
		snapFP_edit = QtGui.QComboBox()
		snapFP_edit.addItems(['on', 'off'])
		snapFP_edit.setFixedSize(80, 25)	
		if surfaceConformation_obj != None:
			snapFP_edit_mas = snapFP_edit.count()  
			for t in range(snapFP_edit_mas):
				if snapFP_edit.itemText(t) == surfaceConformation_obj['sC_start_prs']['snapFP']:
					snapFP_edit.setCurrentIndex(t)
					
		#circulateEdges
		cE_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			cE_lbl.setText("Циркулярные ребра:")
		elif int_lng == 'English':
			cE_lbl.setText("Сirculate edges:")
			
		cE_edit = QtGui.QComboBox()
		cE_edit.addItems(['on', 'off'])
		cE_edit.setFixedSize(80, 25)	
		if surfaceConformation_obj != None:
			cE_edit_mas = cE_edit.count()  
			for t in range(cE_edit_mas):
				if cE_edit.itemText(t) == surfaceConformation_obj['sC_start_prs']['cE']:
					cE_edit.setCurrentIndex(t)
				
		sC_start_prs_grid = QtGui.QGridLayout()
		sC_start_prs_grid.addWidget(lIM_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(lIM_edit_x, 0, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(lIM_edit_y, 0, 2, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(lIM_edit_z, 0, 3, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(fPC_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(sFP_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(sFP_edit, 2, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(eA_lbl, 3, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(eA_edit, 3, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(gFP_lbl, 4, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(gFP_edit, 4, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(snapFP_lbl, 5, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(snapFP_edit, 5, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(cE_lbl, 6, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(cE_edit, 6, 1, alignment=QtCore.Qt.AlignCenter)
		
		
		prs_grid.addLayout(sC_start_prs_grid, 0, 0, alignment=QtCore.Qt.AlignCenter)
		
		tri_distirbTri_list = []
		tri_distirbTri_geometry_list = []
		tri_distirbTri_name_list = []
		other_geometry_list = []
		other_geometry_list_geom = []
		
		#####-----------------------Вторая часть параметров-geometryToConformTo------------------------------#####
		
		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):

			input = open(initial_path_file, 'rb')
			initial_obj = pickle.load(input)
			input.close()
				
		geometry_2_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
		if os.path.exists(geometry_2_path_file):

			input = open(geometry_2_path_file, 'rb')
			geometry_2_obj = pickle.load(input)
			input.close()
				
			i = 1			
			for el in geometry_2_obj:
				if el['geometry_' + str(i)] == 'Tri-surface' or el['geometry_' + str(i)] == 'Три-поверхность' \
				or el['geometry_' + str(i)] == 'Closed tri-surface' or el['geometry_' + str(i)] == 'Закрытая три-поверхность' \
				or el['geometry_' + str(i)] == 'Distributed tri-surface' \
				or el['geometry_' + str(i)] == 'Распределенная три-поверхность':
					tri_distirbTri_list.append(True)
					tri_distirbTri_geometry_list.append(el['file'])
					tri_distirbTri_name_list.append(el['name'])

					other_geometry_list.append(False)

				elif el['geometry_' + str(i)] == 'Base shape' or el['geometry_' + str(i)] == 'Базовая фигура':
					tri_distirbTri_name_list.append(el['shape'])
					other_geometry_list.append(True)
				i = i + 1
			
			geometry_list = []
			featureMethod_list = []
			includedAngle_list = []

			if True in tri_distirbTri_list:
			
				sC_gTCT_lbl = QtGui.QLabel()	
				sC_gTCT_lbl.setVisible(False)
				if int_lng == 'Russian':
					sC_gTCT_lbl.setText("Список конформаций поверхностей:")
				elif int_lng == 'English':
					sC_gTCT_lbl.setText("List of surfaces conformations:")
				sC_gTCT_lbl.setVisible(True)

				sC_gTCT_table = QtGui.QTableWidget()

				sC_gTCT_table.setRowCount(len(geometry_2_obj))
				#geometry_2_obj
				sC_gTCT_table.setColumnCount(3)

				sC_gTCT_table.horizontalHeader().resizeSection(0, 150)
				sC_gTCT_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
				column_1 = QtGui.QTableWidgetItem()
				sC_gTCT_table.setHorizontalHeaderItem(0, column_1)
				sC_gTCT_table.horizontalHeader().setStyleSheet("color: steelblue")

				sC_gTCT_table.horizontalHeader().resizeSection(1, 200)
				sC_gTCT_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
				column_2 = QtGui.QTableWidgetItem()
				sC_gTCT_table.setHorizontalHeaderItem(1, column_2)
				sC_gTCT_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				sC_gTCT_table.horizontalHeader().resizeSection(2, 290)
				sC_gTCT_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
				column_3 = QtGui.QTableWidgetItem()
				sC_gTCT_table.setHorizontalHeaderItem(2, column_3)
				sC_gTCT_table.horizontalHeader().setStyleSheet("color: steelblue")

				if int_lng == 'Russian':
					column_1.setText("Три-поверхность")
					column_2.setText("Метод определения")
					column_3.setText("Угол")
				elif int_lng == 'English':
					column_1.setText("Tri-surface")
					column_2.setText("Method of determination")
					column_3.setText("Included angle")

				nof = 1
				q = 0
				height = 60
				
				while nof <= len(geometry_2_obj):
					sC_gTCT_table.setFixedSize(660, height)

					#geometry#
					gTCT_geometry_edit = QtGui.QComboBox()
					gTCT_geometry_edit.setFixedSize(110, 25)
					gTCT_geometry_edit.addItems(tri_distirbTri_name_list)
					gTCT_geometry_hbox = QtGui.QHBoxLayout()
					gTCT_geometry_hbox.setContentsMargins(0, 0, 0, 0)
					gTCT_geometry_hbox.addWidget(gTCT_geometry_edit)
					gTCT_geometry_cell_widget = QtGui.QWidget()
					gTCT_geometry_cell_widget.setLayout(gTCT_geometry_hbox)
					if surfaceConformation_obj != None:
						g_geometry_edit_mas = gTCT_geometry_edit.count()  
						for t in range(g_geometry_edit_mas):
							if gTCT_geometry_edit.itemText(t) == surfaceConformation_obj['sC_conf_prs'][q]['g']:
								gTCT_geometry_edit.setCurrentIndex(t)
								
					#featureMethod#
					gTCT_featureMethod_edit = QtGui.QComboBox()
					gTCT_featureMethod_edit.setFixedSize(180, 25)
					gTCT_featureMethod_list = ['extendedFeatureEdgeMesh', 'extractFeatures', 'none']
					gTCT_featureMethod_edit.addItems(gTCT_featureMethod_list)
					gTCT_featureMethod_hbox = QtGui.QHBoxLayout()
					gTCT_featureMethod_hbox.setContentsMargins(0, 0, 0, 0)
					gTCT_featureMethod_hbox.addWidget(gTCT_featureMethod_edit)
					gTCT_featureMethod_cell_widget = QtGui.QWidget()
					gTCT_featureMethod_cell_widget.setLayout(gTCT_featureMethod_hbox)
					if surfaceConformation_obj != None:
						fM_geometry_edit_mas = gTCT_featureMethod_edit.count()  
						for t in range(fM_geometry_edit_mas):
							if gTCT_featureMethod_edit.itemText(t) == surfaceConformation_obj['sC_conf_prs'][q]['fM']:
								gTCT_featureMethod_edit.setCurrentIndex(t)
					
					#includedAngle#
					gTCT_includedAngle_edit = QtGui.QSpinBox()
					gTCT_includedAngle_edit.setRange(0, 1000)
					gTCT_includedAngle_edit.setFixedSize(140, 25)
					gTCT_includedAngle_hbox = QtGui.QHBoxLayout()
					gTCT_includedAngle_hbox.setContentsMargins(0, 0, 0, 0)
					gTCT_includedAngle_hbox.addWidget(gTCT_includedAngle_edit)
					gTCT_includedAngle_cell_widget = QtGui.QWidget()
					gTCT_includedAngle_cell_widget.setLayout(gTCT_includedAngle_hbox)
					if surfaceConformation_obj != None:
						gTCT_includedAngle_edit.setValue(surfaceConformation_obj['sC_conf_prs'][q]['iA'])
									
					geometry_list.append(gTCT_geometry_edit)
					featureMethod_list.append(gTCT_featureMethod_edit)
					includedAngle_list.append(gTCT_includedAngle_edit)

					sC_gTCT_table.setCellWidget(q, 0, gTCT_geometry_cell_widget)
					sC_gTCT_table.setCellWidget(q, 1, gTCT_featureMethod_cell_widget)
					sC_gTCT_table.setCellWidget(q, 2, gTCT_includedAngle_cell_widget)
					
					nof = nof + 1
					q = q + 1
					height = height + 30
	
				prs_grid.addWidget(sC_gTCT_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
				prs_grid.addWidget(sC_gTCT_table, 2, 0, alignment=QtCore.Qt.AlignCenter)

		# -------------------------Кнопка сохранения --------------------------#

		surfaceConformation_btnSave = QtGui.QPushButton()
		surfaceConformation_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(surfaceConformation_btnSave)
		if int_lng == 'Russian':
			surfaceConformation_btnSave.setText("Записать")
		elif int_lng == 'English':
			surfaceConformation_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

		surfaceConformation_grid = QtGui.QGridLayout()
		surfaceConformation_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		surfaceConformation_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		surfaceConformation_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		surfaceConformation_grid.setRowStretch(3, 6)
		surfaceConformation_group = QtGui.QGroupBox()
		surfaceConformation_group.setLayout(surfaceConformation_grid)
		return surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, includedAngle_list

