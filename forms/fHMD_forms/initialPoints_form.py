# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class initialPoints_class():
    def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, initialPoints_visible):
        initialPoints_obj = None

		#----------------Если файл initialPoints.pkl существует, получаем данные из него для вывода в форму---------------#

        if initialPoints_visible == True:
            initialPoints_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initialPoints.pkl'
            if os.path.exists(initialPoints_path_file):

                input = open(initialPoints_path_file, 'rb')
                initialPoints_obj = pickle.load(input)
                input.close()
				
        main_lbl = QtGui.QLabel()
        if int_lng == 'Russian':
            main_lbl.setText("Параметры начальных точек")
        elif int_lng == 'English':
            main_lbl.setText("Initial points parameters")

		#---------------Формируем внешний вид формы для файла initialPoints.pkl-------------#

        prs_grid = QtGui.QGridLayout()
        prs_frame = QtGui.QFrame()
        prs_frame.setLayout(prs_grid)

        iPM_lbl = QtGui.QLabel()
        if int_lng == 'Russian':
            iPM_lbl.setText("Метод начальных точек")
        elif int_lng == 'English':
            iPM_lbl.setText("initialPointsMethod")
        iPM_edit = QtGui.QComboBox()
        iPM_edit.setFixedSize(140, 25)
        iPM_list = ['autoDensity']
        iPM_edit.addItems(iPM_list)
        iPM_val_hbox = QtGui.QHBoxLayout()
        iPM_val_hbox.setContentsMargins(0, 0, 0, 0)
        iPM_val_hbox.addWidget(iPM_lbl)
        iPM_val_hbox.addWidget(iPM_edit)
        prs_grid.addLayout(iPM_val_hbox, 0, 0, alignment=QtCore.Qt.AlignCenter)
        if initialPoints_obj != None:
            iPM_edit_mas = iPM_edit.count()  
            for t in range(iPM_edit_mas):
                if iPM_edit.itemText(t) == initialPoints_obj['iP']:
                    iPM_edit.setCurrentIndex(t)
			

        #autoDensityCoeffs - table
        aDC_lbl = QtGui.QLabel('autoDensityCoeffs')
        aDC_table = QtGui.QTableWidget()
        aDC_table.setFixedSize(660, 180)
        aDC_table.setRowCount(5)
        aDC_table.setColumnCount(4)
        aDC_table.verticalHeader().hide()

        aDC_table.horizontalHeader().resizeSection(0, 60)
        aDC_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
        column_1 = QtGui.QTableWidgetItem()
        aDC_table.setHorizontalHeaderItem(0, column_1)
        aDC_table.horizontalHeader().setStyleSheet("color: steelblue")

        aDC_table.horizontalHeader().resizeSection(1, 200)
        aDC_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
        column_2 = QtGui.QTableWidgetItem()
        aDC_table.setHorizontalHeaderItem(1, column_2)
        aDC_table.horizontalHeader().setStyleSheet("color: steelblue")

        aDC_table.horizontalHeader().resizeSection(2, 295)
        aDC_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
        column_3 = QtGui.QTableWidgetItem()
        aDC_table.setHorizontalHeaderItem(2, column_3)
        aDC_table.horizontalHeader().setStyleSheet("color: steelblue")

        aDC_table.horizontalHeader().resizeSection(3, 100)
        aDC_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
        column_4 = QtGui.QTableWidgetItem()
        aDC_table.setHorizontalHeaderItem(3, column_4)
        aDC_table.horizontalHeader().setStyleSheet("color: steelblue")

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

        aDC_checks_list = []
        aDC_values_list = []
        aDC_val_pr_list = []
        aDC_val_def_list = []

		#minCellSizeLimit#
        mCSL_chck = QtGui.QCheckBox()
        mCSL_chck_hbox = QtGui.QHBoxLayout()
        mCSL_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mCSL_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mCSL_chck_hbox.addWidget(mCSL_chck)
        mCSL_chck_cell_widget = QtGui.QWidget()
        mCSL_chck_cell_widget.setLayout(mCSL_chck_hbox)
        aDC_table.setCellWidget(0, 0, mCSL_chck_cell_widget)

        mCSL_val_pr = QtGui.QLabel()
        mCSL_val_pr.setText('minCellSizeLimit')
        mCSL_val_pr.setEnabled(False)
        aDC_table.setCellWidget(0, 1, mCSL_val_pr)
        mCSL_val_def = QtGui.QLabel()
        aDC_table.setCellWidget(0, 2, mCSL_val_def)
        mCSL_val_def.setEnabled(False)
        mCSL_edit = QtGui.QDoubleSpinBox()
        mCSL_edit.setEnabled(False)
        mCSL_edit.setFixedSize(50, 25)
        mCSL_val_hbox = QtGui.QHBoxLayout()
        mCSL_val_hbox.setContentsMargins(0, 0, 0, 0)
        mCSL_val_hbox.addWidget(mCSL_edit)
        mCSL_val_cell_widget = QtGui.QWidget()
        mCSL_val_cell_widget.setLayout(mCSL_val_hbox)
        aDC_table.setCellWidget(0, 3, mCSL_val_cell_widget)
        if int_lng == 'Russian':
            mCSL_val_def.setText("Минимальный размер ячейки")
        elif int_lng == 'English':
            mCSL_val_def.setText("Minimum cell size limit")
        if initialPoints_obj != None:
            mCSL_chck.setChecked(initialPoints_obj['minCellSizeLimit_chck'])
            if initialPoints_obj['minCellSizeLimit_chck'] == True:
                mCSL_val_pr.setEnabled(True)
                mCSL_val_def.setEnabled(True)
                mCSL_edit.setEnabled(True)
                mCSL_edit.setValue(initialPoints_obj['minCellSizeLimit'])

       	aDC_checks_list.append(mCSL_chck)
        aDC_values_list.append(mCSL_edit)
        aDC_val_pr_list.append(mCSL_val_pr)
        aDC_val_def_list.append(mCSL_val_def)

        #minLevels#
        mL_chck = QtGui.QCheckBox()
        mL_chck_hbox = QtGui.QHBoxLayout()
        mL_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mL_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mL_chck_hbox.addWidget(mL_chck)
        mL_chck_cell_widget = QtGui.QWidget()
        mL_chck_cell_widget.setLayout(mL_chck_hbox)
        aDC_table.setCellWidget(1, 0, mL_chck_cell_widget)

        mL_val_pr = QtGui.QLabel()
        mL_val_pr.setText('minLevels')
        mL_val_pr.setEnabled(False)
        aDC_table.setCellWidget(1, 1, mL_val_pr)
        mL_val_def = QtGui.QLabel()
        aDC_table.setCellWidget(1, 2, mL_val_def)
        mL_val_def.setEnabled(False)
        mL_edit = QtGui.QDoubleSpinBox()
        mL_edit.setEnabled(False)
        mL_edit.setFixedSize(50, 25)
        mL_val_hbox = QtGui.QHBoxLayout()
        mL_val_hbox.setContentsMargins(0, 0, 0, 0)
        mL_val_hbox.addWidget(mL_edit)
        mL_val_cell_widget = QtGui.QWidget()
        mL_val_cell_widget.setLayout(mL_val_hbox)
        aDC_table.setCellWidget(1, 3, mL_val_cell_widget)
        if int_lng == 'Russian':
            mL_val_def.setText("Минимальные уровни")
        elif int_lng == 'English':
            mCSL_val_def.setText("Minimum levels")
        if initialPoints_obj != None:
            mL_chck.setChecked(initialPoints_obj['minLevels_chck'])
            if initialPoints_obj['minLevels_chck'] == True:
                mL_val_pr.setEnabled(True)
                mL_val_def.setEnabled(True)
                mL_edit.setEnabled(True)
                mL_edit.setValue(initialPoints_obj['minLevels'])

       	aDC_checks_list.append(mL_chck)
        aDC_values_list.append(mL_edit)
        aDC_val_pr_list.append(mL_val_pr)
        aDC_val_def_list.append(mL_val_def)


        #maxSizeRatio#
        mSR_chck = QtGui.QCheckBox()
        mSR_chck_hbox = QtGui.QHBoxLayout()
        mSR_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mSR_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mSR_chck_hbox.addWidget(mSR_chck)
        mSR_chck_cell_widget = QtGui.QWidget()
        mSR_chck_cell_widget.setLayout(mSR_chck_hbox)
        aDC_table.setCellWidget(2, 0, mSR_chck_cell_widget)

        mSR_val_pr = QtGui.QLabel()
        mSR_val_pr.setText('maxSizeRatio')
        mSR_val_pr.setEnabled(False)
        aDC_table.setCellWidget(2, 1, mSR_val_pr)
        mSR_val_def = QtGui.QLabel()
        aDC_table.setCellWidget(2, 2, mSR_val_def)
        mSR_val_def.setEnabled(False)
        mSR_edit = QtGui.QDoubleSpinBox()
        mSR_edit.setEnabled(False)
        mSR_edit.setFixedSize(50, 25)
        mSR_val_hbox = QtGui.QHBoxLayout()
        mSR_val_hbox.setContentsMargins(0, 0, 0, 0)
        mSR_val_hbox.addWidget(mSR_edit)
        mSR_val_cell_widget = QtGui.QWidget()
        mSR_val_cell_widget.setLayout(mSR_val_hbox)
        aDC_table.setCellWidget(2, 3, mSR_val_cell_widget)
        if int_lng == 'Russian':
            mSR_val_def.setText("Максимальный размер")
        elif int_lng == 'English':
            mSR_val_def.setText("Maximum size ratio")
        if initialPoints_obj != None:
            mSR_chck.setChecked(initialPoints_obj['maxSizeRatio_chck'])
            if initialPoints_obj['maxSizeRatio_chck'] == True:
                mSR_val_pr.setEnabled(True)
                mSR_val_def.setEnabled(True)
                mSR_edit.setEnabled(True)
                mSR_edit.setValue(initialPoints_obj['maxSizeRatio'])

       	aDC_checks_list.append(mSR_chck)
        aDC_values_list.append(mSR_edit)
        aDC_val_pr_list.append(mSR_val_pr)
        aDC_val_def_list.append(mSR_val_def)

        #sampleResolution#
        sR_chck = QtGui.QCheckBox()
        sR_chck_hbox = QtGui.QHBoxLayout()
        sR_chck_hbox.setContentsMargins(0, 0, 0, 0)
        sR_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        sR_chck_hbox.addWidget(sR_chck)
        sR_chck_cell_widget = QtGui.QWidget()
        sR_chck_cell_widget.setLayout(sR_chck_hbox)
        aDC_table.setCellWidget(3, 0, sR_chck_cell_widget)

        sR_val_pr = QtGui.QLabel()
        sR_val_pr.setText('sampleResolution')
        sR_val_pr.setEnabled(False)
        aDC_table.setCellWidget(3, 1, sR_val_pr)
        sR_val_def = QtGui.QLabel()
        aDC_table.setCellWidget(3, 2, sR_val_def)
        sR_val_def.setEnabled(False)
        sR_edit = QtGui.QDoubleSpinBox()
        sR_edit.setEnabled(False)
        sR_edit.setFixedSize(50, 25)
        sR_val_hbox = QtGui.QHBoxLayout()
        sR_val_hbox.setContentsMargins(0, 0, 0, 0)
        sR_val_hbox.addWidget(sR_edit)
        sR_val_cell_widget = QtGui.QWidget()
        sR_val_cell_widget.setLayout(sR_val_hbox)
        aDC_table.setCellWidget(3, 3, sR_val_cell_widget)
        if int_lng == 'Russian':
            sR_val_def.setText("Образец разрешения")
        elif int_lng == 'English':
            sR_val_def.setText("Sample resolution")
        if initialPoints_obj != None:
            sR_chck.setChecked(initialPoints_obj['sampleResolution_chck'])
            if initialPoints_obj['sampleResolution_chck'] == True:
                sR_val_pr.setEnabled(True)
                sR_val_def.setEnabled(True)
                sR_edit.setEnabled(True)
                sR_edit.setValue(initialPoints_obj['sampleResolution'])

       	aDC_checks_list.append(sR_chck)
        aDC_values_list.append(sR_edit)
        aDC_val_pr_list.append(sR_val_pr)
        aDC_val_def_list.append(sR_val_def)


        #surfaceSampleResolution#
        sSR_chck = QtGui.QCheckBox()
        sSR_chck_hbox = QtGui.QHBoxLayout()
        sSR_chck_hbox.setContentsMargins(0, 0, 0, 0)
        sSR_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        sSR_chck_hbox.addWidget(sSR_chck)
        sSR_chck_cell_widget = QtGui.QWidget()
        sSR_chck_cell_widget.setLayout(sSR_chck_hbox)
        aDC_table.setCellWidget(4, 0, sSR_chck_cell_widget)

        sSR_val_pr = QtGui.QLabel()
        sSR_val_pr.setText('surfaceSampleResolution')
        sSR_val_pr.setEnabled(False)
        aDC_table.setCellWidget(4, 1, sSR_val_pr)
        sSR_val_def = QtGui.QLabel()
        aDC_table.setCellWidget(4, 2, sSR_val_def)
        sSR_val_def.setEnabled(False)
        sSR_edit = QtGui.QDoubleSpinBox()
        sSR_edit.setEnabled(False)
        sSR_edit.setFixedSize(50, 25)
        sSR_val_hbox = QtGui.QHBoxLayout()
        sSR_val_hbox.setContentsMargins(0, 0, 0, 0)
        sSR_val_hbox.addWidget(sSR_edit)
        sSR_val_cell_widget = QtGui.QWidget()
        sSR_val_cell_widget.setLayout(sSR_val_hbox)
        aDC_table.setCellWidget(4, 3, sSR_val_cell_widget)
        if int_lng == 'Russian':
            sSR_val_def.setText("Разрешение поверхности")
        elif int_lng == 'English':
            sSR_val_def.setText("Surface sample resolution")
        if initialPoints_obj != None:
            sSR_chck.setChecked(initialPoints_obj['surfaceSampleResolution_chck'])
            if initialPoints_obj['surfaceSampleResolution_chck'] == True:
                sSR_val_pr.setEnabled(True)
                sSR_val_def.setEnabled(True)
                sSR_edit.setEnabled(True)
                sSR_edit.setValue(initialPoints_obj['surfaceSampleResolution'])

       	aDC_checks_list.append(sSR_chck)
        aDC_values_list.append(sSR_edit)
        aDC_val_pr_list.append(sSR_val_pr)
        aDC_val_def_list.append(sSR_val_def)

        prs_grid.addWidget(aDC_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
        prs_grid.addWidget(aDC_table, 2, 0, alignment=QtCore.Qt.AlignCenter)

		# -------------------------Кнопка сохранения --------------------------#

        initialPoints_btnSave = QtGui.QPushButton()
        initialPoints_btnSave.setFixedSize(80, 25)
        buttons_hbox = QtGui.QHBoxLayout()
        buttons_hbox.addWidget(initialPoints_btnSave)
        if int_lng == 'Russian':
            initialPoints_btnSave.setText("Записать")
        elif int_lng == 'English':
            initialPoints_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

        initialPoints_grid = QtGui.QGridLayout()
        initialPoints_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
        initialPoints_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
        initialPoints_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
        initialPoints_grid.setRowStretch(3, 6)
        initialPoints_group = QtGui.QGroupBox()
        initialPoints_group.setLayout(initialPoints_grid)
        return initialPoints_group, initialPoints_btnSave, iPM_edit, aDC_table, aDC_checks_list, \
        aDC_values_list, aDC_val_pr_list, aDC_val_def_list

