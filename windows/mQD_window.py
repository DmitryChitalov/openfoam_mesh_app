import sys, re
import os

from PyQt4 import QtCore, QtGui

import pickle

from forms.fHMD_forms.meshQualityDict_form import meshQualityDict_class
from functions.meshQualityDict_generation import meshQualityDict_generation_class


class mQD_window_class(QtGui.QWidget):
	def __init__(self, parent, par, prj_path_cur, mesh_name_txt_cur, pd_2_cur):
		QtGui.QWidget.__init__(self, parent)

		global tab
		global meshQualityDict_group, meshQualityDict_btnSave, mQD_checks_list, mQD_values_list, mQD_val_pr_list, mQD_val_def_list

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
		meshQualityDict_group, meshQualityDict_btnSave, mQD_checks_list, \
        mQD_values_list, mQD_val_pr_list, mQD_val_def_list = meshQualityDict_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2)
		tab.insertTab(0, meshQualityDict_group, "&meshQualityDict")

		for bvc in range(len(mQD_checks_list)):
			self.mQD_control_chng(mQD_checks_list, bvc)
		meshQualityDict_btnSave.clicked.connect(self.on_meshQualityDict_btnSave)

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

		mQD_grid = QtGui.QGridLayout()
		mQD_grid.addWidget(scrollArea, 0, 0, alignment=QtCore.Qt.AlignCenter)
		mQD_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		mQD_frame = QtGui.QFrame()
		mQD_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
		mQD_frame.setFrameShape(QtGui.QFrame.Panel)
		mQD_frame.setFrameShadow(QtGui.QFrame.Sunken)
		mQD_frame.setLayout(mQD_grid)

		mQD_vbox = QtGui.QVBoxLayout()
		mQD_vbox.addWidget(mQD_frame)

		# ---------------------Размещение на форме всех компонентов-------------------------#

		form = QtGui.QFormLayout()
		form.addRow(mQD_vbox)
		self.setLayout(form)

	#------------------------------Связываем элементы управления с функциями----------------------------#

	def mQD_control_chng(self, mQD_checks_list, bvc):
		mQD_checks_list[bvc].clicked.connect(lambda: self.mQD_on_change(bvc))

	#------------------------------Функции, связанные с элементами формы--------------------------------#

	def mQD_on_change(self, bvc):
		if mQD_checks_list[bvc].isChecked() == True:
			mQD_values_list[bvc].setEnabled(True)
			mQD_val_pr_list[bvc].setEnabled(True)
			mQD_val_def_list[bvc].setEnabled(True)
		else:
			mQD_values_list[bvc].setEnabled(False)
			mQD_val_pr_list[bvc].setEnabled(False)
			mQD_val_def_list[bvc].setEnabled(False)

	###---------------------Сохранение вкладки meshQualityDict-------------------------###

	def on_meshQualityDict_btnSave(self):
		if os.path.exists(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'meshQualityDict.pkl') == True:
			os.remove(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'meshQualityDict.pkl')  
		
		msg_list = []
		if mQD_checks_list[4].isChecked() == True and mQD_values_list[4].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра minTetQuality"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter minTetQuality"
			msg_list.append(msg)
		if mQD_checks_list[5].isChecked() == True and mQD_values_list[5].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра minVol"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter minVol"
			msg_list.append(msg)
		if mQD_checks_list[6].isChecked() == True and mQD_values_list[6].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра minArea"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter minArea"
			msg_list.append(msg)
		if mQD_checks_list[7].isChecked() == True and mQD_values_list[7].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра minTwist"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter minTwist"
			msg_list.append(msg)
		if mQD_checks_list[8].isChecked() == True and mQD_values_list[8].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра minDeterminant"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter minDeterminant"
			msg_list.append(msg)
		if mQD_checks_list[9].isChecked() == True and mQD_values_list[9].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра minFaceWeight"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter minFaceWeight"
			msg_list.append(msg)
		if mQD_checks_list[10].isChecked() == True and mQD_values_list[10].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра minVolRatio"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter minVolRatio"
			msg_list.append(msg)
		if mQD_checks_list[11].isChecked() == True and mQD_values_list[11].text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра minTriangleTwist"
			elif int_lng == 'English':
				msg = "Specify the value of the parameter minTriangleTwist"
			msg_list.append(msg)


		if msg_list != []:
			self.on_msg_error(msg_list)
		else:
			obj = {}
            # mNO
			obj["mNO_chck"] = mQD_checks_list[0].isChecked()
			if obj["mNO_chck"] == True: 
				obj["mNO"] = mQD_values_list[0].value()

            # mBS
			obj["mBS_chck"] = mQD_checks_list[1].isChecked()
			if obj["mBS_chck"] == True: 
			    obj["mBS"] = mQD_values_list[1].value()

            # mIS
			obj["mIS_chck"] = mQD_checks_list[2].isChecked()
			if obj["mIS_chck"] == True: 
				obj["mIS"] = mQD_values_list[2].value()

            # mC
			obj["mC_chck"] = mQD_checks_list[3].isChecked()
			if obj["mC_chck"] == True:  
				obj["mC"] = mQD_values_list[3].value()

            # mTQ
			obj["mTQ_chck"] = mQD_checks_list[4].isChecked()
			if obj["mTQ_chck"] == True:  
				obj["mTQ"] = mQD_values_list[4].text()

            # mV
			obj["mV_chck"] = mQD_checks_list[5].isChecked()
			if obj["mV_chck"] == True:
				obj["mV"] = mQD_values_list[5].text()

            # mA
			obj["mA_chck"] = mQD_checks_list[6].isChecked()
			if obj["mA_chck"] ==True:
				obj["mA"] = mQD_values_list[6].text()

            # mT
			obj["mT_chck"] = mQD_checks_list[7].isChecked()
			if obj["mT_chck"] == True:
				obj["mT"] = mQD_values_list[7].text()

            # mD
			obj["mD_chck"] = mQD_checks_list[8].isChecked()
			if obj["mD_chck"] == True:
				obj["mD"] = mQD_values_list[8].text()

            # mFW
			obj["mFW_chck"] = mQD_checks_list[9].isChecked()
			if obj["mFW_chck"] == True: 
				obj["mFW"] = mQD_values_list[9].text()

            # mVR
			obj["mVR_chck"] = mQD_checks_list[10].isChecked()
			if obj["mVR_chck"] == True:
				obj["mVR"] = mQD_values_list[10].text()

            # mTT
			obj["mTT_chck"] = mQD_checks_list[11].isChecked()
			if obj["mTT_chck"] == True:
				obj["mTT"] = mQD_values_list[11].text()
			
			prj_path_dir = prj_path + '/' + mesh_name_txt + '_' + pd_2

			if os.path.exists(prj_path_dir) == False:
				os.mkdir(prj_path_dir) 


			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'meshQualityDict.pkl', 'wb')
			pickle.dump(obj, output)
			output.close()

			if int_lng == 'Russian':
				msg = "Данные meshQualityDict успешно сохранены"
			elif int_lng == 'English':
				msg = "The meshQualityDict data was successfully saved"
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
		meshQualityDict_generation_class.meshQualityDict_func(int_lng, parn, tab, prj_path, mesh_name_txt, self)
