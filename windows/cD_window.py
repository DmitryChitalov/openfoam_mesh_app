import sys, re
import os

from PyQt4 import QtCore, QtGui

import pickle

from forms.fHMD_forms.collapseDict_form import collapseDict_class
from functions.collapseDict_generation import collapseDict_generation_class


class cD_window_class(QtGui.QWidget):
	def __init__(self, parent, par, prj_path_cur, mesh_name_txt_cur, pd_2_cur):
		QtGui.QWidget.__init__(self, parent)

		global tab
		global collapseDict_group, collapseDict_btnSave, cMQ_edit, cEC_checks_list, cEC_values_list, cEC_val_pr_list, cEC_val_def_list

		global int_lng

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
		collapseDict_group, collapseDict_btnSave, cMQ_edit, cEC_checks_list, \
        cEC_values_list, cEC_val_pr_list, cEC_val_def_list = collapseDict_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2)
		tab.insertTab(0, collapseDict_group, "&collapseDict")
		for bvc in range(len(cEC_checks_list)):
			self.cEC_control_chng(cEC_checks_list, bvc)
		collapseDict_btnSave.clicked.connect(self.on_collapseDict_btnSave)

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
		scrollArea.setFixedSize(800, 580)

		cEC_grid = QtGui.QGridLayout()
		cEC_grid.addWidget(scrollArea, 0, 0, alignment=QtCore.Qt.AlignCenter)
		cEC_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		cEC_frame = QtGui.QFrame()
		cEC_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
		cEC_frame.setFrameShape(QtGui.QFrame.Panel)
		cEC_frame.setFrameShadow(QtGui.QFrame.Sunken)
		cEC_frame.setLayout(cEC_grid)

		cEC_vbox = QtGui.QVBoxLayout()
		cEC_vbox.addWidget(cEC_frame)

		# ---------------------Размещение на форме всех компонентов-------------------------#

		form = QtGui.QFormLayout()
		form.addRow(cEC_vbox)
		self.setLayout(form)

	#------------------------------Связываем элементы управления с функциями----------------------------#

	def cEC_control_chng(self, cEC_checks_list, bvc):
		cEC_checks_list[bvc].clicked.connect(lambda: self.cEC_on_change(bvc))

	#------------------------------Функции, связанные с элементами формы--------------------------------#

	def cEC_on_change(self, bvc):
		if cEC_checks_list[bvc].isChecked() == True:
			cEC_values_list[bvc].setEnabled(True)
			cEC_val_pr_list[bvc].setEnabled(True)
			cEC_val_def_list[bvc].setEnabled(True)
		else:
			cEC_values_list[bvc].setEnabled(False)
			cEC_val_pr_list[bvc].setEnabled(False)
			cEC_val_def_list[bvc].setEnabled(False)

	###---------------------Сохранение вкладки collapseDict-------------------------###

	def on_collapseDict_btnSave(self):
		if os.path.exists(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'collapseDict.pkl') == True:
			os.remove(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'collapseDict.pkl')  
		
		msg_list = []
		if cEC_checks_list[0].isChecked() == True and cEC_values_list[0].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра minimumEdgeLength"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter minimumEdgeLength"
			msg_list.append(msg)
		if cEC_checks_list[1].isChecked() == True and cEC_values_list[1].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра maximumMergeAngle"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter maximumMergeAngle"
			msg_list.append(msg)

		if msg_list != []:
			self.on_msg_error(msg_list)
		else:
			obj = {}
			obj["cMQ"] = cMQ_edit.currentText()
            # mEL
			obj["mEL_chck"] = cEC_checks_list[0].isChecked()
			if cEC_checks_list[0].isChecked() == True: 
				obj["mEL"] = cEC_values_list[0].text()
            # mMA
			obj["mMA_chck"] = cEC_checks_list[1].isChecked()
			if cEC_checks_list[1].isChecked() == True: 
				obj["mMA"] = cEC_values_list[1].text()
            # iFLF
			obj["iFLF_chck"] = cEC_checks_list[2].isChecked()
			if cEC_checks_list[2].isChecked() == True:
				obj["iFLF"] = cEC_values_list[2].value()
            # mCFTPSLC
			obj["mCFTPSLC_chck"] = cEC_checks_list[3].isChecked()
			if cEC_checks_list[3].isChecked() == True:
				obj["mCFTPSLC"] = cEC_values_list[3].value()
            # aECTP
			obj["aECTP_chck"] = cEC_checks_list[4].isChecked()
			if cEC_checks_list[4].isChecked() == True:
				obj["aECTP"] = cEC_values_list[4].currentText()
            # aECC
			obj["aECC_chck"] = cEC_checks_list[5].isChecked()
			if cEC_checks_list[5].isChecked() == True:
				obj["aECC"] = cEC_values_list[5].value()
            # gF
			obj["gF_chck"] = cEC_checks_list[6].isChecked()
			if cEC_checks_list[6].isChecked() == True:
				obj["gF"] = cEC_values_list[6].value()
            # i
			obj["i_chck"] = cEC_checks_list[7].isChecked()
			if cEC_checks_list[7].isChecked() == True:
				obj["i"] = cEC_values_list[7].currentText()
            # eRF
			obj["eRF_chck"] = cEC_checks_list[8].isChecked()
			if cEC_checks_list[8].isChecked() == True:
				obj["eRF"] = cEC_values_list[8].value()
            # fRF
			obj["fRF_chck"] = cEC_checks_list[9].isChecked()
			if cEC_checks_list[9].isChecked() == True:
				obj["fRF"] = cEC_values_list[9].value()
            # mSI
			obj["mSI_chck"] = cEC_checks_list[10].isChecked()
			if cEC_checks_list[10].isChecked() == True:
				obj["mSI"] = cEC_values_list[10].value()
            # mI
			obj["mI_chck"] = cEC_checks_list[11].isChecked()
			if cEC_checks_list[11].isChecked() == True:
				obj["mI"] = cEC_values_list[11].value()
            # mPEC
			obj["mPEC_chck"] = cEC_checks_list[12].isChecked()
			if cEC_checks_list[12].isChecked() == True:
				obj["mPEC"] = cEC_values_list[12].value()

			print(prj_path)
			
			prj_path_dir = prj_path + '/' + mesh_name_txt + '_' + pd_2

			if os.path.exists(prj_path_dir) == False:
				os.mkdir(prj_path_dir) 

			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'collapseDict.pkl', 'wb')
			pickle.dump(obj, output)
			output.close()

			if int_lng == 'Russian':
				msg = "Данные collapseDict успешно сохранены"
			elif int_lng == 'English':
				msg = "The collapseDict data was successfully saved"
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

	###---------------------Запуск сохранения файла blocksMeshDict-------------------------###

	def on_btnSave_clicked(self):
		collapseDict_generation_class.collapseDict_func(int_lng, parn, tab, prj_path, mesh_name_txt, self)
