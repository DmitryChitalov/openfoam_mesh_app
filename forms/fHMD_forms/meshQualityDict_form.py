# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class meshQualityDict_class():
    def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2):
        meshQualityDict_obj = None

		#----------------Если файл meshQualityDict.pkl существует, получаем данные из него для вывода в форму---------------#

        meshQualityDict_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'meshQualityDict.pkl'
        if os.path.exists(meshQualityDict_path_file):

            input = open(meshQualityDict_path_file, 'rb')
            meshQualityDict_obj = pickle.load(input)
            input.close()

		#---------------Формируем внешний вид формы для файла meshQualityDict.pkl-------------#

        prs_grid = QtGui.QGridLayout()
        prs_frame = QtGui.QFrame()
        prs_frame.setLayout(prs_grid)

        #meshQualityDict - table
        mQD_table = QtGui.QTableWidget()
        mQD_table.setFixedSize(660, 390)
        mQD_table.setRowCount(12)
        mQD_table.setColumnCount(4)
        mQD_table.verticalHeader().hide()

        mQD_table.horizontalHeader().resizeSection(0, 60)
        mQD_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
        column_1 = QtGui.QTableWidgetItem()
        mQD_table.setHorizontalHeaderItem(0, column_1)
        mQD_table.horizontalHeader().setStyleSheet("color: steelblue")

        mQD_table.horizontalHeader().resizeSection(1, 150)
        mQD_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
        column_2 = QtGui.QTableWidgetItem()
        mQD_table.setHorizontalHeaderItem(1, column_2)
        mQD_table.horizontalHeader().setStyleSheet("color: steelblue")

        mQD_table.horizontalHeader().resizeSection(2, 343)
        mQD_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
        column_3 = QtGui.QTableWidgetItem()
        mQD_table.setHorizontalHeaderItem(2, column_3)
        mQD_table.horizontalHeader().setStyleSheet("color: steelblue")

        mQD_table.horizontalHeader().resizeSection(3, 100)
        mQD_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
        column_4 = QtGui.QTableWidgetItem()
        mQD_table.setHorizontalHeaderItem(3, column_4)
        mQD_table.horizontalHeader().setStyleSheet("color: steelblue")

        if int_lng == 'Russian':
            column_1.setText("Флаг")
            column_2.setText("Параметр")
            column_3.setText("Описание")
            column_4.setText("Значение")
        elif int_lng == 'English':
            column_1.setText("Flag")
            column_2.setText("Parameter")
            column_3.setText("Definition")
            column_4.setText("Value")

        mQD_checks_list = []
        mQD_values_list = []
        mQD_val_pr_list = []
        mQD_val_def_list = []

		#maxNonOrtho#
        mNO_chck = QtGui.QCheckBox()
        mNO_chck_hbox = QtGui.QHBoxLayout()
        mNO_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mNO_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mNO_chck_hbox.addWidget(mNO_chck)
        mNO_chck_cell_widget = QtGui.QWidget()
        mNO_chck_cell_widget.setLayout(mNO_chck_hbox)
        mQD_table.setCellWidget(0, 0, mNO_chck_cell_widget)

        mNO_val_pr = QtGui.QLabel()
        mNO_val_pr.setText('maxNonOrtho')
        mNO_val_pr.setEnabled(False)
        mQD_table.setCellWidget(0, 1, mNO_val_pr)
        mNO_val_def = QtGui.QLabel()
        mNO_val_def.setEnabled(False)
        mQD_table.setCellWidget(0, 2, mNO_val_def)
        mNO_edit = QtGui.QDoubleSpinBox()
        mNO_edit.setFixedSize(50, 25)
        mNO_edit.setEnabled(False)
        mNO_val_hbox = QtGui.QHBoxLayout()
        mNO_val_hbox.setContentsMargins(0, 0, 0, 0)
        mNO_val_hbox.addWidget(mNO_edit)
        mNO_val_cell_widget = QtGui.QWidget()
        mNO_val_cell_widget.setLayout(mNO_val_hbox)
        mQD_table.setCellWidget(0, 3, mNO_val_cell_widget)
        if int_lng == 'Russian':
            mNO_val_def.setText("Величина максимальной неортогональности")
        elif int_lng == 'English':
            mNO_val_def.setText("The value of the maximum nonorthogonality")
        if meshQualityDict_obj != None:
            mNO_chck.setChecked(meshQualityDict_obj['mNO_chck'])
            if meshQualityDict_obj['mNO_chck'] == True:
                mNO_val_pr.setEnabled(True)
                mNO_val_def.setEnabled(True)
                mNO_edit.setEnabled(True)
                mNO_edit.setValue(meshQualityDict_obj['mNO'])

       	mQD_checks_list.append(mNO_chck)
        mQD_values_list.append(mNO_edit)
        mQD_val_pr_list.append(mNO_val_pr)
        mQD_val_def_list.append(mNO_val_def)

       	#maxBoundarySkewness#
        mBS_chck = QtGui.QCheckBox()
        mBS_chck_hbox = QtGui.QHBoxLayout()
        mBS_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mBS_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mBS_chck_hbox.addWidget(mBS_chck)
        mBS_chck_cell_widget = QtGui.QWidget()
        mBS_chck_cell_widget.setLayout(mBS_chck_hbox)
        mQD_table.setCellWidget(1, 0, mBS_chck_cell_widget)

        mBS_val_pr = QtGui.QLabel()
        mBS_val_pr.setText('maxBoundarySkewness')
        mBS_val_pr.setEnabled(False)
        mQD_table.setCellWidget(1, 1, mBS_val_pr)
        mBS_val_def = QtGui.QLabel()
        mBS_val_def.setEnabled(False)
        mQD_table.setCellWidget(1, 2, mBS_val_def)
        mBS_edit = QtGui.QDoubleSpinBox()
        mBS_edit.setFixedSize(50, 25)
        mBS_edit.setEnabled(False)
        mBS_val_hbox = QtGui.QHBoxLayout()
        mBS_val_hbox.setContentsMargins(0, 0, 0, 0)
        mBS_val_hbox.addWidget(mBS_edit)
        mBS_val_cell_widget = QtGui.QWidget()
        mBS_val_cell_widget.setLayout(mBS_val_hbox)
        mQD_table.setCellWidget(1, 3, mBS_val_cell_widget)
        if int_lng == 'Russian':
            mBS_val_def.setText("Максимальная кратковременная ассиметрия")
        elif int_lng == 'English':
            mBS_val_def.setText("Maximum short-term asymmetry")
        if meshQualityDict_obj != None:
            mBS_chck.setChecked(meshQualityDict_obj['mBS_chck'])
            if meshQualityDict_obj['mBS_chck'] == True:
                mBS_val_pr.setEnabled(True)
                mBS_val_def.setEnabled(True)
                mBS_edit.setEnabled(True)
                mBS_edit.setValue(meshQualityDict_obj['mBS'])

       	mQD_checks_list.append(mBS_chck)
        mQD_values_list.append(mBS_edit)
        mQD_val_pr_list.append(mBS_val_pr)
        mQD_val_def_list.append(mBS_val_def)


        #maxInternalSkewness#
        mIS_chck = QtGui.QCheckBox()
        mIS_chck_hbox = QtGui.QHBoxLayout()
        mIS_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mIS_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mIS_chck_hbox.addWidget(mIS_chck)
        mIS_chck_cell_widget = QtGui.QWidget()
        mIS_chck_cell_widget.setLayout(mIS_chck_hbox)
        mQD_table.setCellWidget(2, 0, mIS_chck_cell_widget)

        mIS_val_pr = QtGui.QLabel()
        mIS_val_pr.setText('maxInternalSkewness')
        mIS_val_pr.setEnabled(False)
        mQD_table.setCellWidget(2, 1, mIS_val_pr)
        mIS_val_def = QtGui.QLabel()
        mIS_val_def.setEnabled(False)
        mQD_table.setCellWidget(2, 2, mIS_val_def)
        mIS_edit = QtGui.QDoubleSpinBox()
        mIS_edit.setFixedSize(50, 25)
        mIS_edit.setEnabled(False)
        mIS_val_hbox = QtGui.QHBoxLayout()
        mIS_val_hbox.setContentsMargins(0, 0, 0, 0)
        mIS_val_hbox.addWidget(mIS_edit)
        mIS_val_cell_widget = QtGui.QWidget()
        mIS_val_cell_widget.setLayout(mIS_val_hbox)
        mQD_table.setCellWidget(2, 3, mIS_val_cell_widget)
        if int_lng == 'Russian':
            mIS_val_def.setText("Максимальная внутренняя ассиметрия")
        elif int_lng == 'English':
            mIS_val_def.setText("Maximum Internal Skewness")
        if meshQualityDict_obj != None:
            mIS_chck.setChecked(meshQualityDict_obj['mIS_chck'])
            if meshQualityDict_obj['mIS_chck'] == True:
                mIS_val_pr.setEnabled(True)
                mIS_val_def.setEnabled(True)
                mIS_edit.setEnabled(True)
                mIS_edit.setValue(meshQualityDict_obj['mIS'])

       	mQD_checks_list.append(mIS_chck)
        mQD_values_list.append(mIS_edit)
        mQD_val_pr_list.append(mIS_val_pr)
        mQD_val_def_list.append(mIS_val_def)


        #maxConcave#
        mC_chck = QtGui.QCheckBox()
        mC_chck_hbox = QtGui.QHBoxLayout()
        mC_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mC_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mC_chck_hbox.addWidget(mC_chck)
        mC_chck_cell_widget = QtGui.QWidget()
        mC_chck_cell_widget.setLayout(mC_chck_hbox)
        mQD_table.setCellWidget(3, 0, mC_chck_cell_widget)

        mC_val_pr = QtGui.QLabel()
        mC_val_pr.setText('maxConcave')
        mC_val_pr.setEnabled(False)
        mQD_table.setCellWidget(3, 1, mC_val_pr)
        mC_val_def = QtGui.QLabel()
        mC_val_def.setEnabled(False)
        mQD_table.setCellWidget(3, 2, mC_val_def)
        mC_edit = QtGui.QDoubleSpinBox()
        mC_edit.setFixedSize(50, 25)
        mC_edit.setEnabled(False)
        mC_val_hbox = QtGui.QHBoxLayout()
        mC_val_hbox.setContentsMargins(0, 0, 0, 0)
        mC_val_hbox.addWidget(mC_edit)
        mC_val_cell_widget = QtGui.QWidget()
        mC_val_cell_widget.setLayout(mC_val_hbox)
        mQD_table.setCellWidget(3, 3, mC_val_cell_widget)
        if int_lng == 'Russian':
            mC_val_def.setText("Максимальная вогнутость")
        elif int_lng == 'English':
            mC_val_def.setText("Maximum concaveness")
        if meshQualityDict_obj != None:
            mC_chck.setChecked(meshQualityDict_obj['mC_chck'])
            if meshQualityDict_obj['mC_chck'] == True:
                mC_val_pr.setEnabled(True)
                mC_val_def.setEnabled(True)
                mC_edit.setEnabled(True)
                mC_edit.setValue(meshQualityDict_obj['mC'])

       	mQD_checks_list.append(mC_chck)
        mQD_values_list.append(mC_edit)
        mQD_val_pr_list.append(mC_val_pr)
        mQD_val_def_list.append(mC_val_def)


        #minTetQuality#
        mTQ_chck = QtGui.QCheckBox()
        mTQ_chck_hbox = QtGui.QHBoxLayout()
        mTQ_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mTQ_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mTQ_chck_hbox.addWidget(mTQ_chck)
        mTQ_chck_cell_widget = QtGui.QWidget()
        mTQ_chck_cell_widget.setLayout(mTQ_chck_hbox)
        mQD_table.setCellWidget(4, 0, mTQ_chck_cell_widget)

        mTQ_val_pr = QtGui.QLabel()
        mTQ_val_pr.setText('minTetQuality')
        mTQ_val_pr.setEnabled(False)
        mQD_table.setCellWidget(4, 1, mTQ_val_pr)
        mTQ_val_def = QtGui.QLabel()
        mQD_table.setCellWidget(4, 2, mTQ_val_def)
        mTQ_val_def.setEnabled(False)
        mTQ_edit = QtGui.QLineEdit()
        mTQ_edit.setEnabled(False)
        mTQ_edit.setFixedSize(50, 25)
        mTQ_val_hbox = QtGui.QHBoxLayout()
        mTQ_val_hbox.setContentsMargins(0, 0, 0, 0)
        mTQ_val_hbox.addWidget(mTQ_edit)
        mTQ_val_cell_widget = QtGui.QWidget()
        mTQ_val_cell_widget.setLayout(mTQ_val_hbox)
        mQD_table.setCellWidget(4, 3, mTQ_val_cell_widget)
        if int_lng == 'Russian':
            mTQ_val_def.setText("Минимальное качество тета, образованного лицевым центром")
        elif int_lng == 'English':
            mTQ_val_def.setText("Minimum quality of the tet formed by the face-centre")
        if meshQualityDict_obj != None:
            mTQ_chck.setChecked(meshQualityDict_obj['mTQ_chck'])
            if meshQualityDict_obj['mTQ_chck'] == True:
                mTQ_val_pr.setEnabled(True)
                mTQ_val_def.setEnabled(True)
                mTQ_edit.setEnabled(True)
                mTQ_edit.setText(meshQualityDict_obj['mTQ'])

       	mQD_checks_list.append(mTQ_chck)
        mQD_values_list.append(mTQ_edit)
        mQD_val_pr_list.append(mTQ_val_pr)
        mQD_val_def_list.append(mTQ_val_def)


        #minVol#
        mV_chck = QtGui.QCheckBox()
        mV_chck_hbox = QtGui.QHBoxLayout()
        mV_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mV_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mV_chck_hbox.addWidget(mV_chck)
        mV_chck_cell_widget = QtGui.QWidget()
        mV_chck_cell_widget.setLayout(mV_chck_hbox)
        mQD_table.setCellWidget(5, 0, mV_chck_cell_widget)

        mV_val_pr = QtGui.QLabel()
        mV_val_pr.setText('minVol')
        mV_val_pr.setEnabled(False)
        mQD_table.setCellWidget(5, 1, mV_val_pr)
        mV_val_def = QtGui.QLabel()
        mQD_table.setCellWidget(5, 2, mV_val_def)
        mV_val_def.setEnabled(False)
        mV_edit = QtGui.QLineEdit()
        mV_edit.setEnabled(False)
        mV_edit.setFixedSize(50, 25)
        mV_val_hbox = QtGui.QHBoxLayout()
        mV_val_hbox.setContentsMargins(0, 0, 0, 0)
        mV_val_hbox.addWidget(mV_edit)
        mV_val_cell_widget = QtGui.QWidget()
        mV_val_cell_widget.setLayout(mV_val_hbox)
        mQD_table.setCellWidget(5, 3, mV_val_cell_widget)
        if int_lng == 'Russian':
            mV_val_def.setText("Минимальный объем пирамиды")
        elif int_lng == 'English':
            mV_val_def.setText("Minimum pyramid volume")
        if meshQualityDict_obj != None:
            mV_chck.setChecked(meshQualityDict_obj['mV_chck'])
            if meshQualityDict_obj['mV_chck'] == True:
                mV_val_pr.setEnabled(True)
                mV_val_def.setEnabled(True)
                mV_edit.setEnabled(True)
                mV_edit.setText(meshQualityDict_obj['mV'])

       	mQD_checks_list.append(mV_chck)
        mQD_values_list.append(mV_edit)
        mQD_val_pr_list.append(mV_val_pr)
        mQD_val_def_list.append(mV_val_def)


        #minArea#
        mA_chck = QtGui.QCheckBox()
        mA_chck_hbox = QtGui.QHBoxLayout()
        mA_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mA_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mA_chck_hbox.addWidget(mA_chck)
        mA_chck_cell_widget = QtGui.QWidget()
        mA_chck_cell_widget.setLayout(mA_chck_hbox)
        mQD_table.setCellWidget(6, 0, mA_chck_cell_widget)

        mA_val_pr = QtGui.QLabel()
        mA_val_pr.setText('minArea')
        mA_val_pr.setEnabled(False)
        mQD_table.setCellWidget(6, 1, mA_val_pr)
        mA_val_def = QtGui.QLabel()
        mQD_table.setCellWidget(6, 2, mA_val_def)
        mA_val_def.setEnabled(False)
        mA_edit = QtGui.QLineEdit()
        mA_edit.setEnabled(False)
        mA_edit.setFixedSize(50, 25)
        mA_val_hbox = QtGui.QHBoxLayout()
        mA_val_hbox.setContentsMargins(0, 0, 0, 0)
        mA_val_hbox.addWidget(mA_edit)
        mA_val_cell_widget = QtGui.QWidget()
        mA_val_cell_widget.setLayout(mA_val_hbox)
        mQD_table.setCellWidget(6, 3, mA_val_cell_widget)
        if int_lng == 'Russian':
            mA_val_def.setText("Минимальный площадь поверхности")
        elif int_lng == 'English':
            mA_val_def.setText("Minimum face area")
        if meshQualityDict_obj != None:
            mA_chck.setChecked(meshQualityDict_obj['mV_chck'])
            if meshQualityDict_obj['mV_chck'] == True:
                mA_val_pr.setEnabled(True)
                mA_val_def.setEnabled(True)
                mA_edit.setEnabled(True)
                mA_edit.setText(meshQualityDict_obj['mA'])

       	mQD_checks_list.append(mA_chck)
        mQD_values_list.append(mA_edit)
        mQD_val_pr_list.append(mA_val_pr)
        mQD_val_def_list.append(mA_val_def)


        #minTwist#
        mT_chck = QtGui.QCheckBox()
        mT_chck_hbox = QtGui.QHBoxLayout()
        mT_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mT_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mT_chck_hbox.addWidget(mT_chck)
        mT_chck_cell_widget = QtGui.QWidget()
        mT_chck_cell_widget.setLayout(mT_chck_hbox)
        mQD_table.setCellWidget(7, 0, mT_chck_cell_widget)

        mT_val_pr = QtGui.QLabel()
        mT_val_pr.setText('minTwist')
        mT_val_pr.setEnabled(False)
        mQD_table.setCellWidget(7, 1, mT_val_pr)
        mT_val_def = QtGui.QLabel()
        mQD_table.setCellWidget(7, 2, mT_val_def)
        mT_val_def.setEnabled(False)
        mT_edit = QtGui.QLineEdit()
        mT_edit.setEnabled(False)
        mT_edit.setFixedSize(50, 25)
        mT_val_hbox = QtGui.QHBoxLayout()
        mT_val_hbox.setContentsMargins(0, 0, 0, 0)
        mT_val_hbox.addWidget(mT_edit)
        mT_val_cell_widget = QtGui.QWidget()
        mT_val_cell_widget.setLayout(mT_val_hbox)
        mQD_table.setCellWidget(7, 3, mT_val_cell_widget)
        if int_lng == 'Russian':
            mT_val_def.setText("Минимальное скручивание поверхности")
        elif int_lng == 'English':
            mT_val_def.setText("Minimum face twist")
        if meshQualityDict_obj != None:
            mT_chck.setChecked(meshQualityDict_obj['mT_chck'])
            if meshQualityDict_obj['mT_chck'] == True:
                mT_val_pr.setEnabled(True)
                mT_val_def.setEnabled(True)
                mT_edit.setEnabled(True)
                mT_edit.setText(meshQualityDict_obj['mT'])

       	mQD_checks_list.append(mT_chck)
        mQD_values_list.append(mT_edit)
        mQD_val_pr_list.append(mT_val_pr)
        mQD_val_def_list.append(mT_val_def)


        #minDeterminant#
        mD_chck = QtGui.QCheckBox()
        mD_chck_hbox = QtGui.QHBoxLayout()
        mD_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mD_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mD_chck_hbox.addWidget(mD_chck)
        mD_chck_cell_widget = QtGui.QWidget()
        mD_chck_cell_widget.setLayout(mD_chck_hbox)
        mQD_table.setCellWidget(8, 0, mD_chck_cell_widget)

        mD_val_pr = QtGui.QLabel()
        mD_val_pr.setText('minDeterminant')
        mD_val_pr.setEnabled(False)
        mQD_table.setCellWidget(8, 1, mD_val_pr)
        mD_val_def = QtGui.QLabel()
        mQD_table.setCellWidget(8, 2, mD_val_def)
        mD_val_def.setEnabled(False)
        mD_edit = QtGui.QLineEdit()
        mD_edit.setEnabled(False)
        mD_edit.setFixedSize(50, 25)
        mD_val_hbox = QtGui.QHBoxLayout()
        mD_val_hbox.setContentsMargins(0, 0, 0, 0)
        mD_val_hbox.addWidget(mD_edit)
        mD_val_cell_widget = QtGui.QWidget()
        mD_val_cell_widget.setLayout(mD_val_hbox)
        mQD_table.setCellWidget(8, 3, mD_val_cell_widget)
        if int_lng == 'Russian':
            mD_val_def.setText("Минимальная нормированная детерминанта клетки")
        elif int_lng == 'English':
            mD_val_def.setText("Minimum normalised cell determinant")
        if meshQualityDict_obj != None:
            mD_chck.setChecked(meshQualityDict_obj['mD_chck'])
            if meshQualityDict_obj['mD_chck'] == True:
                mD_val_pr.setEnabled(True)
                mD_val_def.setEnabled(True)
                mD_edit.setEnabled(True)
                mD_edit.setText(meshQualityDict_obj['mD'])

       	mQD_checks_list.append(mD_chck)
        mQD_values_list.append(mD_edit)
        mQD_val_pr_list.append(mD_val_pr)
        mQD_val_def_list.append(mD_val_def)


        #minFaceWeight#
        mFW_chck = QtGui.QCheckBox()
        mFW_chck_hbox = QtGui.QHBoxLayout()
        mFW_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mFW_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mFW_chck_hbox.addWidget(mFW_chck)
        mFW_chck_cell_widget = QtGui.QWidget()
        mFW_chck_cell_widget.setLayout(mFW_chck_hbox)
        mQD_table.setCellWidget(9, 0, mFW_chck_cell_widget)

        mFW_val_pr = QtGui.QLabel()
        mFW_val_pr.setText('minFaceWeight')
        mFW_val_pr.setEnabled(False)
        mQD_table.setCellWidget(9, 1, mFW_val_pr)
        mFW_val_def = QtGui.QLabel()
        mQD_table.setCellWidget(9, 2, mFW_val_def)
        mFW_val_def.setEnabled(False)
        mFW_edit = QtGui.QLineEdit()
        mFW_edit.setEnabled(False)
        mFW_edit.setFixedSize(50, 25)
        mFW_val_hbox = QtGui.QHBoxLayout()
        mFW_val_hbox.setContentsMargins(0, 0, 0, 0)
        mFW_val_hbox.addWidget(mFW_edit)
        mFW_val_cell_widget = QtGui.QWidget()
        mFW_val_cell_widget.setLayout(mFW_val_hbox)
        mQD_table.setCellWidget(9, 3, mFW_val_cell_widget)
        if int_lng == 'Russian':
            mFW_val_def.setText("Минимальный вес поверхности")
        elif int_lng == 'English':
            mFW_val_def.setText("Minimum face weight")
        if meshQualityDict_obj != None:
            mFW_chck.setChecked(meshQualityDict_obj['mFW_chck'])
            if meshQualityDict_obj['mFW_chck'] == True:
                mFW_val_pr.setEnabled(True)
                mFW_val_def.setEnabled(True)
                mFW_edit.setEnabled(True)
                mFW_edit.setText(meshQualityDict_obj['mFW'])

       	mQD_checks_list.append(mFW_chck)
        mQD_values_list.append(mFW_edit)
        mQD_val_pr_list.append(mFW_val_pr)
        mQD_val_def_list.append(mFW_val_def)


        #minVolRatio#
        mVR_chck = QtGui.QCheckBox()
        mVR_chck_hbox = QtGui.QHBoxLayout()
        mVR_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mVR_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mVR_chck_hbox.addWidget(mVR_chck)
        mVR_chck_cell_widget = QtGui.QWidget()
        mVR_chck_cell_widget.setLayout(mVR_chck_hbox)
        mQD_table.setCellWidget(10, 0, mVR_chck_cell_widget)

        mVR_val_pr = QtGui.QLabel()
        mVR_val_pr.setText('minVolRatio')
        mVR_val_pr.setEnabled(False)
        mQD_table.setCellWidget(10, 1, mVR_val_pr)
        mVR_val_def = QtGui.QLabel()
        mQD_table.setCellWidget(10, 2, mVR_val_def)
        mVR_val_def.setEnabled(False)
        mVR_edit = QtGui.QLineEdit()
        mVR_edit.setEnabled(False)
        mVR_edit.setFixedSize(50, 25)
        mVR_val_hbox = QtGui.QHBoxLayout()
        mVR_val_hbox.setContentsMargins(0, 0, 0, 0)
        mVR_val_hbox.addWidget(mVR_edit)
        mVR_val_cell_widget = QtGui.QWidget()
        mVR_val_cell_widget.setLayout(mVR_val_hbox)
        mQD_table.setCellWidget(10, 3, mVR_val_cell_widget)
        if int_lng == 'Russian':
            mVR_val_def.setText("Минимальный коэффициент объема")
        elif int_lng == 'English':
            mVR_val_def.setText("Minimum volume ratio")
        if meshQualityDict_obj != None:
            mVR_chck.setChecked(meshQualityDict_obj['mVR_chck'])
            if meshQualityDict_obj['mVR_chck'] == True:
                mVR_val_pr.setEnabled(True)
                mVR_val_def.setEnabled(True)
                mVR_edit.setEnabled(True)
                mVR_edit.setText(meshQualityDict_obj['mVR'])

       	mQD_checks_list.append(mVR_chck)
        mQD_values_list.append(mVR_edit)
        mQD_val_pr_list.append(mVR_val_pr)
        mQD_val_def_list.append(mVR_val_def)


        #minTriangleTwist#
        mTT_chck = QtGui.QCheckBox()
        mTT_chck_hbox = QtGui.QHBoxLayout()
        mTT_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mTT_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mTT_chck_hbox.addWidget(mTT_chck)
        mTT_chck_cell_widget = QtGui.QWidget()
        mTT_chck_cell_widget.setLayout(mTT_chck_hbox)
        mQD_table.setCellWidget(11, 0, mTT_chck_cell_widget)

        mTT_val_pr = QtGui.QLabel()
        mTT_val_pr.setText('minTriangleTwist')
        mTT_val_pr.setEnabled(False)
        mQD_table.setCellWidget(11, 1, mTT_val_pr)
        mTT_val_def = QtGui.QLabel()
        mQD_table.setCellWidget(11, 2, mTT_val_def)
        mTT_val_def.setEnabled(False)
        mTT_edit = QtGui.QLineEdit()
        mTT_edit.setEnabled(False)
        mTT_edit.setFixedSize(50, 25)
        mTT_val_hbox = QtGui.QHBoxLayout()
        mTT_val_hbox.setContentsMargins(0, 0, 0, 0)
        mTT_val_hbox.addWidget(mTT_edit)
        mTT_val_cell_widget = QtGui.QWidget()
        mTT_val_cell_widget.setLayout(mTT_val_hbox)
        mQD_table.setCellWidget(11, 3, mTT_val_cell_widget)
        if int_lng == 'Russian':
            mTT_val_def.setText("Минимальный треугольное скручивание")
        elif int_lng == 'English':
            mTT_val_def.setText("Minimum triangle twist")
        if meshQualityDict_obj != None:
            mTT_chck.setChecked(meshQualityDict_obj['mTT_chck'])
            if meshQualityDict_obj['mTT_chck'] == True:
                mTT_val_pr.setEnabled(True)
                mTT_val_def.setEnabled(True)
                mTT_edit.setEnabled(True)
                mTT_edit.setText(meshQualityDict_obj['mTT'])

       	mQD_checks_list.append(mTT_chck)
        mQD_values_list.append(mTT_edit)
        mQD_val_pr_list.append(mTT_val_pr)
        mQD_val_def_list.append(mTT_val_def)

        prs_grid.addWidget(mQD_table, 0, 0, alignment=QtCore.Qt.AlignCenter)

		# -------------------------Кнопка сохранения --------------------------#

        meshQualityDict_btnSave = QtGui.QPushButton()
        meshQualityDict_btnSave.setFixedSize(80, 25)
        buttons_hbox = QtGui.QHBoxLayout()
        buttons_hbox.addWidget(meshQualityDict_btnSave)
        if int_lng == 'Russian':
            meshQualityDict_btnSave.setText("Записать")
        elif int_lng == 'English':
            meshQualityDict_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

        meshQualityDict_grid = QtGui.QGridLayout()
        meshQualityDict_grid.addWidget(prs_frame, 0, 0, alignment=QtCore.Qt.AlignCenter)
        meshQualityDict_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        meshQualityDict_grid.setRowStretch(3, 6)
        meshQualityDict_group = QtGui.QGroupBox()
        meshQualityDict_group.setLayout(meshQualityDict_grid)
        return meshQualityDict_group, meshQualityDict_btnSave, mQD_checks_list, \
        mQD_values_list, mQD_val_pr_list, mQD_val_def_list

