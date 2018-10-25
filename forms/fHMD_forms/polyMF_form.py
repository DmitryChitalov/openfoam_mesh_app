# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class polyMF_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, polyMF_visible): 
		polyMF_obj = None
		
		#----------------Если файл polyMF.pkl существует, получаем данные из него для вывода в форму---------------#

		if polyMF_visible == True:
			polyMF_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'polyMF.pkl'
			if os.path.exists(polyMF_path_file):
		
				input = open(polyMF_path_file, 'rb')
				polyMF_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла polyMF.pkl на основе данных файла initial.pkl-------------#
		
		prs_grid = QtGui.QGridLayout()
		prs_frame = QtGui.QFrame()
		prs_frame.setLayout(prs_grid)
		
		#####-----------------------Первая часть параметров------------------------------#####
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Параметры фильтрации сетки")
		elif int_lng == 'English':
			main_lbl.setText("Poly mesh filtering parameters")
		
		#filterEdges
		fE_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			fE_lbl.setText("Фильтровать ребра:")
		elif int_lng == 'English':
			fE_lbl.setText("Filter edges:")
			
		fE_edit = QtGui.QComboBox()
		fE_edit.addItems(['on', 'off'])
		fE_edit.setFixedSize(80, 25)	
		if polyMF_obj != None:
			fE_edit_mas = fE_edit.count()  
			for t in range(fE_edit_mas):
				if fE_edit.itemText(t) == polyMF_obj['fE']:
					fE_edit.setCurrentIndex(t)
					
		#filterFaces
		fF_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			fF_lbl.setText("Фильтровать поверхности:")
		elif int_lng == 'English':
			fF_lbl.setText("Filter faces:")
			
		fF_edit = QtGui.QComboBox()
		fF_edit.addItems(['on', 'off'])
		fF_edit.setFixedSize(80, 25)	
		if polyMF_obj != None:
			fF_edit_mas = fF_edit.count()  
			for t in range(fF_edit_mas):
				if fF_edit.itemText(t) == polyMF_obj['fF']:
					fF_edit.setCurrentIndex(t)
					
		#writeTetDualMesh
		wTDM_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			wTDM_lbl.setText("Записывать тетраэдную двойную сетку:")
		elif int_lng == 'English':
			wTDM_lbl.setText("Write tet dual mesh:")
			
		wTDM_edit = QtGui.QComboBox()
		wTDM_edit.addItems(['false', 'true'])
		wTDM_edit.setFixedSize(80, 25)	
		if polyMF_obj != None:
			wTDM_edit_mas = wTDM_edit.count()  
			for t in range(wTDM_edit_mas):
				if wTDM_edit.itemText(t) == polyMF_obj['wTDM']:
					wTDM_edit.setCurrentIndex(t)
			
		pMF_prs_grid = QtGui.QGridLayout()
		
		pMF_prs_grid.addWidget(fE_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		pMF_prs_grid.addWidget(fE_edit, 0, 1, alignment=QtCore.Qt.AlignCenter)
		pMF_prs_grid.addWidget(fF_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
		pMF_prs_grid.addWidget(fF_edit, 1, 1, alignment=QtCore.Qt.AlignCenter)
		pMF_prs_grid.addWidget(wTDM_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)
		pMF_prs_grid.addWidget(wTDM_edit, 2, 1, alignment=QtCore.Qt.AlignCenter)
		
		prs_grid.addLayout(pMF_prs_grid, 0, 0, alignment=QtCore.Qt.AlignCenter)

		# -------------------------Кнопка сохранения --------------------------#

		polyMF_btnSave = QtGui.QPushButton()
		polyMF_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(polyMF_btnSave)
		if int_lng == 'Russian':
			polyMF_btnSave.setText("Записать")
		elif int_lng == 'English':
			polyMF_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

		polyMF_grid = QtGui.QGridLayout()
		polyMF_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		polyMF_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		polyMF_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		polyMF_grid.setRowStretch(3, 6)
		polyMF_group = QtGui.QGroupBox()
		polyMF_group.setLayout(polyMF_grid)
		return polyMF_group, polyMF_btnSave, pMF_prs_grid

