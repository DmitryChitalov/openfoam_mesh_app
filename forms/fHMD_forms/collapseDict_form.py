# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class collapseDict_class():
    def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2):
        collapseDict_obj = None

		#----------------Если файл collapseDict.pkl существует, получаем данные из него для вывода в форму---------------#

        collapseDict_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'collapseDict.pkl'
        if os.path.exists(collapseDict_path_file):

            input = open(collapseDict_path_file, 'rb')
            collapseDict_obj = pickle.load(input)
            input.close()

		#---------------Формируем внешний вид формы для файла collapseDict.pkl-------------#

        prs_grid = QtGui.QGridLayout()
        prs_frame = QtGui.QFrame()
        prs_frame.setLayout(prs_grid)

        cMQ_lbl = QtGui.QLabel()
        if int_lng == 'Russian':
            cMQ_lbl.setText("Контроль качества сетки")
        elif int_lng == 'English':
            cMQ_lbl.setText("Сontrol mesh quality")
        cMQ_edit = QtGui.QComboBox()
        cMQ_edit.setFixedSize(140, 25)
        cMQ_list = ['on', 'off']
        cMQ_edit.addItems(cMQ_list)
        cMQ_val_hbox = QtGui.QHBoxLayout()
        cMQ_val_hbox.setContentsMargins(0, 0, 0, 0)
        cMQ_val_hbox.addWidget(cMQ_lbl)
        cMQ_val_hbox.addWidget(cMQ_edit)
        prs_grid.addLayout(cMQ_val_hbox, 0, 0, alignment=QtCore.Qt.AlignCenter)
		
        if collapseDict_obj != None:
            cMQ_edit_mas = cMQ_edit.count()
            for t in range(cMQ_edit_mas):
                if cMQ_edit.itemText(t) == collapseDict_obj['cMQ']:
                    cMQ_edit.setCurrentIndex(t)

        #collapseEdgesCoeffs - table
        cEC_lbl = QtGui.QLabel('collapseEdgesCoeffs')
        cEC_table = QtGui.QTableWidget()
        cEC_table.setFixedSize(662, 95)
        cEC_table.setRowCount(2)
        cEC_table.setColumnCount(4)
        cEC_table.verticalHeader().hide()

        cEC_table.horizontalHeader().resizeSection(0, 60)
        cEC_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
        column_1 = QtGui.QTableWidgetItem()
        cEC_table.setHorizontalHeaderItem(0, column_1)
        cEC_table.horizontalHeader().setStyleSheet("color: steelblue")

        cEC_table.horizontalHeader().resizeSection(1, 150)
        cEC_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
        column_2 = QtGui.QTableWidgetItem()
        cEC_table.setHorizontalHeaderItem(1, column_2)
        cEC_table.horizontalHeader().setStyleSheet("color: steelblue")

        cEC_table.horizontalHeader().resizeSection(2, 350)
        cEC_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
        column_3 = QtGui.QTableWidgetItem()
        cEC_table.setHorizontalHeaderItem(2, column_3)
        cEC_table.horizontalHeader().setStyleSheet("color: steelblue")

        cEC_table.horizontalHeader().resizeSection(3, 100)
        cEC_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
        column_4 = QtGui.QTableWidgetItem()
        cEC_table.setHorizontalHeaderItem(3, column_4)
        cEC_table.horizontalHeader().setStyleSheet("color: steelblue")

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

        cEC_checks_list = []
        cEC_values_list = []
        cEC_val_pr_list = []
        cEC_val_def_list = []

		#minimumEdgeLength#
        mEL_chck = QtGui.QCheckBox()
        mEL_chck_hbox = QtGui.QHBoxLayout()
        mEL_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mEL_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mEL_chck_hbox.addWidget(mEL_chck)
        mEL_chck_cell_widget = QtGui.QWidget()
        mEL_chck_cell_widget.setLayout(mEL_chck_hbox)
        cEC_table.setCellWidget(0, 0, mEL_chck_cell_widget)

        mEL_val_pr = QtGui.QLabel()
        mEL_val_pr.setText('minimumEdgeLength')
        mEL_val_pr.setEnabled(False)
        cEC_table.setCellWidget(0, 1, mEL_val_pr)
        mEL_val_def = QtGui.QLabel()
        cEC_table.setCellWidget(0, 2, mEL_val_def)
        mEL_val_def.setEnabled(False)
        mEL_edit = QtGui.QLineEdit()
        mEL_edit.setEnabled(False)
        mEL_edit.setFixedSize(50, 25)
        mEL_val_hbox = QtGui.QHBoxLayout()
        mEL_val_hbox.setContentsMargins(0, 0, 0, 0)
        mEL_val_hbox.addWidget(mEL_edit)
        mEL_val_cell_widget = QtGui.QWidget()
        mEL_val_cell_widget.setLayout(mEL_val_hbox)
        cEC_table.setCellWidget(0, 3, mEL_val_cell_widget)
        if int_lng == 'Russian':
            mEL_val_def.setText("Края, более короткие, чем это абсолютное значение, будут объединены")
        elif int_lng == 'English':
            mEL_val_def.setText("Edges shorter than this absolute value will be merged")
        if collapseDict_obj != None:
            mEL_chck.setChecked(collapseDict_obj['mEL_chck'])
            if collapseDict_obj['mEL_chck'] == True:
                mEL_val_pr.setEnabled(True)
                mEL_val_def.setEnabled(True)
                mEL_edit.setEnabled(True)
                mEL_edit.setText(collapseDict_obj['mEL'])

       	cEC_checks_list.append(mEL_chck)
        cEC_values_list.append(mEL_edit)
        cEC_val_pr_list.append(mEL_val_pr)
        cEC_val_def_list.append(mEL_val_def)


       	#maximumMergeAngle#
        mMA_chck = QtGui.QCheckBox()
        mMA_chck_hbox = QtGui.QHBoxLayout()
        mMA_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mMA_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mMA_chck_hbox.addWidget(mMA_chck)
        mMA_chck_cell_widget = QtGui.QWidget()
        mMA_chck_cell_widget.setLayout(mMA_chck_hbox)
        cEC_table.setCellWidget(1, 0, mMA_chck_cell_widget)

        mMA_val_pr = QtGui.QLabel()
        mMA_val_pr.setText('maximumMergeAngle')
        mMA_val_pr.setEnabled(False)
        cEC_table.setCellWidget(1, 1, mMA_val_pr)
        mMA_val_def = QtGui.QLabel()
        mMA_val_def.setEnabled(False)
        cEC_table.setCellWidget(1, 2, mMA_val_def)
        mMA_edit = QtGui.QLineEdit()
        mMA_edit.setFixedSize(50, 25)
        mMA_edit.setEnabled(False)
        mMA_val_hbox = QtGui.QHBoxLayout()
        mMA_val_hbox.setContentsMargins(0, 0, 0, 0)
        mMA_val_hbox.addWidget(mMA_edit)
        mMA_val_cell_widget = QtGui.QWidget()
        mMA_val_cell_widget.setLayout(mMA_val_hbox)
        cEC_table.setCellWidget(1, 3, mMA_val_cell_widget)
        if int_lng == 'Russian':
            mMA_val_def.setText("Максимальный угол между ребрами, разделяющими точку")
        elif int_lng == 'English':
            mMA_val_def.setText("The maximum angle between two edges that share a point")

        if collapseDict_obj != None:
            mMA_chck.setChecked(collapseDict_obj['mMA_chck'])
            if collapseDict_obj['mMA_chck'] == True:
                mMA_val_pr.setEnabled(True)
                mMA_val_def.setEnabled(True)
                mMA_edit.setEnabled(True)
                mMA_edit.setText(collapseDict_obj['mMA'])

       	cEC_checks_list.append(mMA_chck)
        cEC_values_list.append(mMA_edit)
        cEC_val_pr_list.append(mMA_val_pr)
        cEC_val_def_list.append(mMA_val_def)

        prs_grid.addWidget(cEC_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
        prs_grid.addWidget(cEC_table, 2, 0, alignment=QtCore.Qt.AlignCenter)

        #collapseFacesCoeffs - table
        cFC_lbl = QtGui.QLabel('collapseFacesCoeffs')
        cFC_table = QtGui.QTableWidget()
        cFC_table.setFixedSize(662, 200)
        cFC_table.setRowCount(5)
        cFC_table.setColumnCount(4)
        cFC_table.verticalHeader().hide()

        cFC_table.horizontalHeader().resizeSection(0, 60)
        cFC_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
        column_1 = QtGui.QTableWidgetItem()
        cFC_table.setHorizontalHeaderItem(0, column_1)
        cFC_table.horizontalHeader().setStyleSheet("color: steelblue")

        cFC_table.horizontalHeader().resizeSection(1, 150)
        cFC_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
        column_2 = QtGui.QTableWidgetItem()
        cFC_table.setHorizontalHeaderItem(1, column_2)
        cFC_table.horizontalHeader().setStyleSheet("color: steelblue")

        cFC_table.horizontalHeader().resizeSection(2, 350)
        cFC_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
        column_3 = QtGui.QTableWidgetItem()
        cFC_table.setHorizontalHeaderItem(2, column_3)
        cFC_table.horizontalHeader().setStyleSheet("color: steelblue")

        cFC_table.horizontalHeader().resizeSection(3, 100)
        cFC_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
        column_4 = QtGui.QTableWidgetItem()
        cFC_table.setHorizontalHeaderItem(3, column_4)
        cFC_table.horizontalHeader().setStyleSheet("color: steelblue")

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

        #initialFaceLengthFactor#
        iFLF_chck = QtGui.QCheckBox()
        iFLF_chck_hbox = QtGui.QHBoxLayout()
        iFLF_chck_hbox.setContentsMargins(0, 0, 0, 0)
        iFLF_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        iFLF_chck_hbox.addWidget(iFLF_chck)
        iFLF_chck_cell_widget = QtGui.QWidget()
        iFLF_chck_cell_widget.setLayout(iFLF_chck_hbox)
        cFC_table.setCellWidget(0, 0, iFLF_chck_cell_widget)

        iFLF_val_pr = QtGui.QLabel()
        iFLF_val_pr.setText('initialFaceLengthFactor')
        iFLF_val_pr.setEnabled(False)
        cFC_table.setCellWidget(0, 1, iFLF_val_pr)
        iFLF_val_def = QtGui.QLabel()
        iFLF_val_def.setEnabled(False)
        cFC_table.setCellWidget(0, 2, iFLF_val_def)
        iFLF_edit = QtGui.QDoubleSpinBox()
        iFLF_edit.setFixedSize(50, 25)
        iFLF_edit.setEnabled(False)
        iFLF_val_hbox = QtGui.QHBoxLayout()
        iFLF_val_hbox.setContentsMargins(0, 0, 0, 0)
        iFLF_val_hbox.addWidget(iFLF_edit)
        iFLF_val_cell_widget = QtGui.QWidget()
        iFLF_val_cell_widget.setLayout(iFLF_val_hbox)
        cFC_table.setCellWidget(0, 3, iFLF_val_cell_widget)
        if int_lng == 'Russian':
            iFLF_val_def.setText("Начальный коэффициент длины поверхности")
        elif int_lng == 'English':
            iFLF_val_def.setText("The initial face length factor")
        if collapseDict_obj != None:
            iFLF_chck.setChecked(collapseDict_obj['iFLF_chck'])
            if collapseDict_obj['iFLF_chck'] == True:
                iFLF_val_pr.setEnabled(True)
                iFLF_val_def.setEnabled(True)
                iFLF_edit.setEnabled(True)
                iFLF_edit.setValue(collapseDict_obj['iFLF'])

       	cEC_checks_list.append(iFLF_chck)
        cEC_values_list.append(iFLF_edit)
        cEC_val_pr_list.append(iFLF_val_pr)
        cEC_val_def_list.append(iFLF_val_def)

        #maxCollapseFaceToPointSideLengthCoeff#
        mCFTPSLC_chck = QtGui.QCheckBox()
        mCFTPSLC_chck_hbox = QtGui.QHBoxLayout()
        mCFTPSLC_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mCFTPSLC_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mCFTPSLC_chck_hbox.addWidget(mCFTPSLC_chck)
        mCFTPSLC_chck_cell_widget = QtGui.QWidget()
        mCFTPSLC_chck_cell_widget.setLayout(mCFTPSLC_chck_hbox)
        cFC_table.setCellWidget(1, 0, mCFTPSLC_chck_cell_widget)

        mCFTPSLC_val_pr = QtGui.QLabel()
        mCFTPSLC_val_pr.setEnabled(False)
        mCFTPSLC_val_pr.setText('maxCollapseFaceToPointSideLengthCoeff')
        cFC_table.setCellWidget(1, 1, mCFTPSLC_val_pr)
        mCFTPSLC_val_def = QtGui.QLabel()
        mCFTPSLC_val_def.setEnabled(False)
        cFC_table.setCellWidget(1, 2, mCFTPSLC_val_def)
        mCFTPSLC_edit = QtGui.QDoubleSpinBox()
        mCFTPSLC_edit.setEnabled(False)
        mCFTPSLC_edit.setFixedSize(50, 25)
        mCFTPSLC_val_hbox = QtGui.QHBoxLayout()
        mCFTPSLC_val_hbox.setContentsMargins(0, 0, 0, 0)
        mCFTPSLC_val_hbox.addWidget(mCFTPSLC_edit)
        mCFTPSLC_val_cell_widget = QtGui.QWidget()
        mCFTPSLC_val_cell_widget.setLayout(mCFTPSLC_val_hbox)
        cFC_table.setCellWidget(1, 3, mCFTPSLC_val_cell_widget)
        if int_lng == 'Russian':
            mCFTPSLC_val_def.setText("Коэффициент сворачивания поверхности к краю")
        elif int_lng == 'English':
            mCFTPSLC_val_def.setText("Coefficient of surface-to-edge folding")

        if collapseDict_obj != None:
            mCFTPSLC_chck.setChecked(collapseDict_obj['mCFTPSLC_chck'])
            if collapseDict_obj['mCFTPSLC_chck'] == True:
                mCFTPSLC_val_pr.setEnabled(True)
                mCFTPSLC_val_def.setEnabled(True)
                mCFTPSLC_edit.setEnabled(True)
                mCFTPSLC_edit.setValue(collapseDict_obj['mCFTPSLC'])

        cEC_checks_list.append(mCFTPSLC_chck)
        cEC_values_list.append(mCFTPSLC_edit)
        cEC_val_pr_list.append(mCFTPSLC_val_pr)
        cEC_val_def_list.append(mCFTPSLC_val_def)

        #allowEarlyCollapseToPoint#
        aECTP_chck = QtGui.QCheckBox()
        aECTP_chck_hbox = QtGui.QHBoxLayout()
        aECTP_chck_hbox.setContentsMargins(0, 0, 0, 0)
        aECTP_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        aECTP_chck_hbox.addWidget(aECTP_chck)
        aECTP_chck_cell_widget = QtGui.QWidget()
        aECTP_chck_cell_widget.setLayout(aECTP_chck_hbox)
        cFC_table.setCellWidget(2, 0, aECTP_chck_cell_widget)

        aECTP_val_pr = QtGui.QLabel()
        aECTP_val_pr.setEnabled(False)
        aECTP_val_pr.setText('allowEarlyCollapseToPoint')
        cFC_table.setCellWidget(2, 1, aECTP_val_pr)
        aECTP_val_def = QtGui.QLabel()
        aECTP_val_def.setEnabled(False)
        cFC_table.setCellWidget(2, 2, aECTP_val_def)
        aECTP_edit = QtGui.QComboBox()
        aECTP_edit.setEnabled(False)
        aECTP_edit.setFixedSize(80, 25)
        aECTP_list = ['on', 'off']
        aECTP_edit.addItems(aECTP_list)
        aECTP_val_hbox = QtGui.QHBoxLayout()
        aECTP_val_hbox.setContentsMargins(0, 0, 0, 0)
        aECTP_val_hbox.addWidget(aECTP_edit)
        aECTP_val_cell_widget = QtGui.QWidget()
        aECTP_val_cell_widget.setLayout(aECTP_val_hbox)
        cFC_table.setCellWidget(2, 3, aECTP_val_cell_widget)
        if int_lng == 'Russian':
            aECTP_val_def.setText("Разрешить ранний коллапс ребер до точки")
        elif int_lng == 'English':
            aECTP_val_def.setText("Allow early collapse of edges to a point")
        if collapseDict_obj != None:
            aECTP_chck.setChecked(collapseDict_obj['aECTP_chck'])
            if collapseDict_obj['aECTP_chck'] == True:
                aECTP_val_pr.setEnabled(True)
                aECTP_val_def.setEnabled(True)
                aECTP_edit.setEnabled(True)
                aECTP_edit_mas = aECTP_edit.count()
                for t in range(aECTP_edit_mas):
                    if aECTP_edit.itemText(t) == collapseDict_obj['aECTP']:
                        aECTP_edit.setCurrentIndex(t)

        cEC_checks_list.append(aECTP_chck)
        cEC_values_list.append(aECTP_edit)
        cEC_val_pr_list.append(aECTP_val_pr)
        cEC_val_def_list.append(aECTP_val_def)


        #allowEarlyCollapseCoeff#
        aECC_chck = QtGui.QCheckBox()
        aECC_chck_hbox = QtGui.QHBoxLayout()
        aECC_chck_hbox.setContentsMargins(0, 0, 0, 0)
        aECC_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        aECC_chck_hbox.addWidget(aECC_chck)
        aECC_chck_cell_widget = QtGui.QWidget()
        aECC_chck_cell_widget.setLayout(aECC_chck_hbox)
        cFC_table.setCellWidget(3, 0, aECC_chck_cell_widget)

        aECC_val_pr = QtGui.QLabel()
        aECC_val_pr.setEnabled(False)
        aECC_val_pr.setText('allowEarlyCollapseCoeff')
        cFC_table.setCellWidget(3, 1, aECC_val_pr)
        aECC_val_def = QtGui.QLabel()
        aECC_val_def.setEnabled(False)
        cFC_table.setCellWidget(3, 2, aECC_val_def)
        aECC_edit = QtGui.QDoubleSpinBox()
        aECC_edit.setEnabled(False)
        aECC_edit.setFixedSize(50, 25)
        aECC_val_hbox = QtGui.QHBoxLayout()
        aECC_val_hbox.setContentsMargins(0, 0, 0, 0)
        aECC_val_hbox.addWidget(aECC_edit)
        aECC_val_cell_widget = QtGui.QWidget()
        aECC_val_cell_widget.setLayout(aECC_val_hbox)
        cFC_table.setCellWidget(3, 3, aECC_val_cell_widget)
        if int_lng == 'Russian':
            aECC_val_def.setText("Фракция до преумножения maxCollapseFaceToPointSideLengthCoeff")
        elif int_lng == 'English':
            aECC_val_def.setText("Fraction to premultiply maxCollapseFaceToPointSideLengthCoeff")

        if collapseDict_obj != None:
            aECC_chck.setChecked(collapseDict_obj['aECC_chck'])
            if collapseDict_obj['aECC_chck'] == True:
                aECC_val_pr.setEnabled(True)
                aECC_val_def.setEnabled(True)
                aECC_edit.setEnabled(True)
                aECC_edit.setValue(collapseDict_obj['aECC'])

        cEC_checks_list.append(aECC_chck)
        cEC_values_list.append(aECC_edit)
        cEC_val_pr_list.append(aECC_val_pr)
        cEC_val_def_list.append(aECC_val_def)

        #guardFraction#
        gF_chck = QtGui.QCheckBox()
        gF_chck_hbox = QtGui.QHBoxLayout()
        gF_chck_hbox.setContentsMargins(0, 0, 0, 0)
        gF_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        gF_chck_hbox.addWidget(gF_chck)
        gF_chck_cell_widget = QtGui.QWidget()
        gF_chck_cell_widget.setLayout(gF_chck_hbox)
        cFC_table.setCellWidget(4, 0, gF_chck_cell_widget)

        gF_val_pr = QtGui.QLabel()
        gF_val_pr.setEnabled(False)
        gF_val_pr.setText('guardFraction')
        cFC_table.setCellWidget(4, 1, gF_val_pr)
        gF_val_def = QtGui.QLabel()
        gF_val_def.setEnabled(False)
        cFC_table.setCellWidget(4, 2, gF_val_def)
        gF_edit = QtGui.QDoubleSpinBox()
        gF_edit.setEnabled(False)
        gF_edit.setFixedSize(50, 25)
        gF_val_hbox = QtGui.QHBoxLayout()
        gF_val_hbox.setContentsMargins(0, 0, 0, 0)
        gF_val_hbox.addWidget(gF_edit)
        gF_val_cell_widget = QtGui.QWidget()
        gF_val_cell_widget.setLayout(gF_val_hbox)
        cFC_table.setCellWidget(4, 3, gF_val_cell_widget)
        if int_lng == 'Russian':
            gF_val_def.setText("Величина защитной фракции")
        elif int_lng == 'English':
            gF_val_def.setText("Guard fraction value")

        if collapseDict_obj != None:
            gF_chck.setChecked(collapseDict_obj['gF_chck'])
            if collapseDict_obj['gF_chck'] == True:
                gF_val_pr.setEnabled(True)
                gF_val_def.setEnabled(True)
                gF_edit.setEnabled(True)
                gF_edit.setValue(collapseDict_obj['gF'])

        cEC_checks_list.append(gF_chck)
        cEC_values_list.append(gF_edit)
        cEC_val_pr_list.append(gF_val_pr)
        cEC_val_def_list.append(gF_val_def)

        prs_grid.addWidget(cFC_lbl, 3, 0, alignment=QtCore.Qt.AlignCenter)
        prs_grid.addWidget(cFC_table, 4, 0, alignment=QtCore.Qt.AlignCenter)


        #controlMeshQualityCoeffs - table
        cMQC_lbl = QtGui.QLabel('controlMeshQualityCoeffs')
        cMQC_table = QtGui.QTableWidget()
        cMQC_table.setFixedSize(662, 210)
        cMQC_table.setRowCount(6)
        cMQC_table.setColumnCount(4)
        cMQC_table.verticalHeader().hide()

        cMQC_table.horizontalHeader().resizeSection(0, 60)
        cMQC_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
        column_1 = QtGui.QTableWidgetItem()
        cMQC_table.setHorizontalHeaderItem(0, column_1)
        cMQC_table.horizontalHeader().setStyleSheet("color: steelblue")

        cMQC_table.horizontalHeader().resizeSection(1, 150)
        cMQC_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
        column_2 = QtGui.QTableWidgetItem()
        cMQC_table.setHorizontalHeaderItem(1, column_2)
        cMQC_table.horizontalHeader().setStyleSheet("color: steelblue")

        cMQC_table.horizontalHeader().resizeSection(2, 350)
        cMQC_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
        column_3 = QtGui.QTableWidgetItem()
        cMQC_table.setHorizontalHeaderItem(2, column_3)
        cMQC_table.horizontalHeader().setStyleSheet("color: steelblue")

        cMQC_table.horizontalHeader().resizeSection(3, 100)
        cMQC_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
        column_4 = QtGui.QTableWidgetItem()
        cMQC_table.setHorizontalHeaderItem(3, column_4)
        cMQC_table.horizontalHeader().setStyleSheet("color: steelblue")

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

        #include#
        i_chck = QtGui.QCheckBox()
        i_chck_hbox = QtGui.QHBoxLayout()
        i_chck_hbox.setContentsMargins(0, 0, 0, 0)
        i_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        i_chck_hbox.addWidget(i_chck)
        i_chck_cell_widget = QtGui.QWidget()
        i_chck_cell_widget.setLayout(i_chck_hbox)
        cMQC_table.setCellWidget(0, 0, i_chck_cell_widget)

        i_val_pr = QtGui.QLabel()
        i_val_pr.setEnabled(False)
        i_val_pr.setText('include')
        cMQC_table.setCellWidget(0, 1, i_val_pr)
        i_val_def = QtGui.QLabel()
        i_val_def.setEnabled(False)
        cMQC_table.setCellWidget(0, 2, i_val_def)
        i_edit = QtGui.QComboBox()
        i_edit.setEnabled(False)
        i_edit.setFixedSize(140, 25)
        i_list = ['meshQualityDict']
        i_edit.addItems(i_list)
        i_val_hbox = QtGui.QHBoxLayout()
        i_val_hbox.setContentsMargins(0, 0, 0, 0)
        i_val_hbox.addWidget(i_edit)
        i_val_cell_widget = QtGui.QWidget()
        i_val_cell_widget.setLayout(i_val_hbox)
        cMQC_table.setCellWidget(0, 3, i_val_cell_widget)
        if int_lng == 'Russian':
            i_val_def.setText("Название словаря с коэффициентами качества сетки")
        elif int_lng == 'English':
            i_val_def.setText("Name of the dictionary that has the mesh quality coefficients")
        if collapseDict_obj != None:
            i_chck.setChecked(collapseDict_obj['i_chck'])
            if collapseDict_obj['i_chck'] == True:
                i_val_pr.setEnabled(True)
                i_val_def.setEnabled(True)
                i_edit.setEnabled(True)
                i_edit_mas = i_edit.count()
                for t in range(i_edit_mas):
                    if i_edit.itemText(t) == collapseDict_obj['i']:
                        i_edit.setCurrentIndex(t)

        cEC_checks_list.append(i_chck)
        cEC_values_list.append(i_edit)
        cEC_val_pr_list.append(i_val_pr)
        cEC_val_def_list.append(i_val_def)

        #edgeReductionFactor#
        eRF_chck = QtGui.QCheckBox()
        eRF_chck_hbox = QtGui.QHBoxLayout()
        eRF_chck_hbox.setContentsMargins(0, 0, 0, 0)
        eRF_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        eRF_chck_hbox.addWidget(eRF_chck)
        eRF_chck_cell_widget = QtGui.QWidget()
        eRF_chck_cell_widget.setLayout(eRF_chck_hbox)
        cMQC_table.setCellWidget(1, 0, eRF_chck_cell_widget)

        eRF_val_pr = QtGui.QLabel()
        eRF_val_pr.setEnabled(False)
        eRF_val_pr.setText('edgeReductionFactor')
        cMQC_table.setCellWidget(1, 1, eRF_val_pr)
        eRF_val_def = QtGui.QLabel()
        eRF_val_def.setEnabled(False)
        cMQC_table.setCellWidget(1, 2, eRF_val_def)
        eRF_edit = QtGui.QDoubleSpinBox()
        eRF_edit.setEnabled(False)
        eRF_edit.setFixedSize(50, 25)
        eRF_val_hbox = QtGui.QHBoxLayout()
        eRF_val_hbox.setContentsMargins(0, 0, 0, 0)
        eRF_val_hbox.addWidget(eRF_edit)
        eRF_val_cell_widget = QtGui.QWidget()
        eRF_val_cell_widget.setLayout(eRF_val_hbox)
        cMQC_table.setCellWidget(1, 3, eRF_val_cell_widget)
        if int_lng == 'Russian':
            eRF_val_def.setText("Количество, на которое minimumEdgeLength будет уменьшено для каждого края")
        elif int_lng == 'English':
            eRF_val_def.setText("The amount that minimumEdgeLength will be reduced by for each edge")

        if collapseDict_obj != None:
            eRF_chck.setChecked(collapseDict_obj['aECC_chck'])
            if collapseDict_obj['aECC_chck'] == True:
                eRF_val_pr.setEnabled(True)
                eRF_val_def.setEnabled(True)
                eRF_edit.setEnabled(True)
                eRF_edit.setValue(collapseDict_obj['eRF'])

        cEC_checks_list.append(eRF_chck)
        cEC_values_list.append(eRF_edit)
        cEC_val_pr_list.append(eRF_val_pr)
        cEC_val_def_list.append(eRF_val_def)

        #faceReductionFactor#
        fRF_chck = QtGui.QCheckBox()
        fRF_chck_hbox = QtGui.QHBoxLayout()
        fRF_chck_hbox.setContentsMargins(0, 0, 0, 0)
        fRF_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        fRF_chck_hbox.addWidget(fRF_chck)
        fRF_chck_cell_widget = QtGui.QWidget()
        fRF_chck_cell_widget.setLayout(fRF_chck_hbox)
        cMQC_table.setCellWidget(2, 0, fRF_chck_cell_widget)

        fRF_val_pr = QtGui.QLabel()
        fRF_val_pr.setEnabled(False)
        fRF_val_pr.setText('faceReductionFactor')
        cMQC_table.setCellWidget(2, 1, fRF_val_pr)
        fRF_val_def = QtGui.QLabel()
        fRF_val_def.setEnabled(False)
        cMQC_table.setCellWidget(2, 2, fRF_val_def)
        fRF_edit = QtGui.QDoubleSpinBox()
        fRF_edit.setEnabled(False)
        fRF_edit.setFixedSize(50, 25)
        fRF_val_hbox = QtGui.QHBoxLayout()
        fRF_val_hbox.setContentsMargins(0, 0, 0, 0)
        fRF_val_hbox.addWidget(fRF_edit)
        fRF_val_cell_widget = QtGui.QWidget()
        fRF_val_cell_widget.setLayout(fRF_val_hbox)
        cMQC_table.setCellWidget(2, 3, fRF_val_cell_widget)
        if int_lng == 'Russian':
            fRF_val_def.setText("Количество, на которое initialFaceLengthFactor будет уменьшено для каждого края")
        elif int_lng == 'English':
            fRF_val_def.setText("The amount that initialFaceLengthFactor will be reduced by for each edge")

        if collapseDict_obj != None:
            fRF_chck.setChecked(collapseDict_obj['fRF_chck'])
            if collapseDict_obj['fRF_chck'] == True:
                fRF_val_pr.setEnabled(True)
                fRF_val_def.setEnabled(True)
                fRF_edit.setEnabled(True)
                fRF_edit.setValue(collapseDict_obj['fRF'])

        cEC_checks_list.append(fRF_chck)
        cEC_values_list.append(fRF_edit)
        cEC_val_pr_list.append(fRF_val_pr)
        cEC_val_def_list.append(fRF_val_def)

        #maximumSmoothingIterations#
        mSI_chck = QtGui.QCheckBox()
        mSI_chck_hbox = QtGui.QHBoxLayout()
        mSI_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mSI_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mSI_chck_hbox.addWidget(mSI_chck)
        mSI_chck_cell_widget = QtGui.QWidget()
        mSI_chck_cell_widget.setLayout(mSI_chck_hbox)
        cMQC_table.setCellWidget(3, 0, mSI_chck_cell_widget)

        mSI_val_pr = QtGui.QLabel()
        mSI_val_pr.setEnabled(False)
        mSI_val_pr.setText('maximumSmoothingIterations')
        cMQC_table.setCellWidget(3, 1, mSI_val_pr)
        mSI_val_def = QtGui.QLabel()
        mSI_val_def.setEnabled(False)
        cMQC_table.setCellWidget(3, 2, mSI_val_def)
        mSI_edit = QtGui.QSpinBox()
        mSI_edit.setEnabled(False)
        mSI_edit.setFixedSize(50, 25)
        mSI_val_hbox = QtGui.QHBoxLayout()
        mSI_val_hbox.setContentsMargins(0, 0, 0, 0)
        mSI_val_hbox.addWidget(mSI_edit)
        mSI_val_cell_widget = QtGui.QWidget()
        mSI_val_cell_widget.setLayout(mSI_val_hbox)
        cMQC_table.setCellWidget(3, 3, mSI_val_cell_widget)
        if int_lng == 'Russian':
            mSI_val_def.setText("Максимальное количество сглаживающих итераций для уменьшающих факторов")
        elif int_lng == 'English':
            mSI_val_def.setText("Maximum number of smoothing iterations for the reductionFactors")

        if collapseDict_obj != None:
            mSI_chck.setChecked(collapseDict_obj['mSI_chck'])
            if collapseDict_obj['mSI_chck'] == True:
                mSI_val_pr.setEnabled(True)
                mSI_val_def.setEnabled(True)
                mSI_edit.setEnabled(True)
                mSI_edit.setValue(collapseDict_obj['mSI'])

        cEC_checks_list.append(mSI_chck)
        cEC_values_list.append(mSI_edit)
        cEC_val_pr_list.append(mSI_val_pr)
        cEC_val_def_list.append(mSI_val_def)

        #maximumIterations#
        mI_chck = QtGui.QCheckBox()
        mI_chck_hbox = QtGui.QHBoxLayout()
        mI_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mI_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mI_chck_hbox.addWidget(mI_chck)
        mI_chck_cell_widget = QtGui.QWidget()
        mI_chck_cell_widget.setLayout(mI_chck_hbox)
        cMQC_table.setCellWidget(4, 0, mI_chck_cell_widget)

        mI_val_pr = QtGui.QLabel()
        mI_val_pr.setEnabled(False)
        mI_val_pr.setText('maximumIterations')
        cMQC_table.setCellWidget(4, 1, mI_val_pr)
        mI_val_def = QtGui.QLabel()
        mI_val_def.setEnabled(False)
        cMQC_table.setCellWidget(4, 2, mI_val_def)
        mI_edit = QtGui.QSpinBox()
        mI_edit.setEnabled(False)
        mI_edit.setFixedSize(50, 25)
        mI_val_hbox = QtGui.QHBoxLayout()
        mI_val_hbox.setContentsMargins(0, 0, 0, 0)
        mI_val_hbox.addWidget(mI_edit)
        mI_val_cell_widget = QtGui.QWidget()
        mI_val_cell_widget.setLayout(mI_val_hbox)
        cMQC_table.setCellWidget(4, 3, mI_val_cell_widget)
        if int_lng == 'Russian':
            mI_val_def.setText("Максимальное количество внешних итераций - проверка качества сетки")
        elif int_lng == 'English':
            mI_val_def.setText("Maximum number of outer iterations is mesh quality checking is enabled")

        if collapseDict_obj != None:
            mI_chck.setChecked(collapseDict_obj['mI_chck'])
            if collapseDict_obj['mI_chck'] == True:
                mI_val_pr.setEnabled(True)
                mI_val_def.setEnabled(True)
                mI_edit.setEnabled(True)
                mI_edit.setValue(collapseDict_obj['mI'])

        cEC_checks_list.append(mI_chck)
        cEC_values_list.append(mI_edit)
        cEC_val_pr_list.append(mI_val_pr)
        cEC_val_def_list.append(mI_val_def)


        #maxPointErrorCount#
        mPEC_chck = QtGui.QCheckBox()
        mPEC_chck_hbox = QtGui.QHBoxLayout()
        mPEC_chck_hbox.setContentsMargins(0, 0, 0, 0)
        mPEC_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
        mPEC_chck_hbox.addWidget(mPEC_chck)
        mPEC_chck_cell_widget = QtGui.QWidget()
        mPEC_chck_cell_widget.setLayout(mPEC_chck_hbox)
        cMQC_table.setCellWidget(5, 0, mPEC_chck_cell_widget)

        mPEC_val_pr = QtGui.QLabel()
        mPEC_val_pr.setEnabled(False)
        mPEC_val_pr.setText('maxPointErrorCount')
        cMQC_table.setCellWidget(5, 1, mPEC_val_pr)
        mPEC_val_def = QtGui.QLabel()
        mPEC_val_def.setEnabled(False)
        cMQC_table.setCellWidget(5, 2, mPEC_val_def)
        mPEC_edit = QtGui.QSpinBox()
        mPEC_edit.setEnabled(False)
        mPEC_edit.setFixedSize(50, 25)
        mPEC_val_hbox = QtGui.QHBoxLayout()
        mPEC_val_hbox.setContentsMargins(0, 0, 0, 0)
        mPEC_val_hbox.addWidget(mPEC_edit)
        mPEC_val_cell_widget = QtGui.QWidget()
        mPEC_val_cell_widget.setLayout(mPEC_val_hbox)
        cMQC_table.setCellWidget(5, 3, mPEC_val_cell_widget)
        if int_lng == 'Russian':
            mPEC_val_def.setText("Максимальное количество удалений итераций")
        elif int_lng == 'English':
            mPEC_val_def.setText("Maximum number of iterations deletion ")

        if collapseDict_obj != None:
            mPEC_chck.setChecked(collapseDict_obj['mPEC_chck'])
            if collapseDict_obj['mI_chck'] == True:
                mPEC_val_pr.setEnabled(True)
                mPEC_val_def.setEnabled(True)
                mPEC_edit.setEnabled(True)
                mPEC_edit.setValue(collapseDict_obj['mPEC'])

        cEC_checks_list.append(mPEC_chck)
        cEC_values_list.append(mPEC_edit)
        cEC_val_pr_list.append(mPEC_val_pr)
        cEC_val_def_list.append(mPEC_val_def)


        prs_grid.addWidget(cMQC_lbl, 5, 0, alignment=QtCore.Qt.AlignCenter)
        prs_grid.addWidget(cMQC_table, 6, 0, alignment=QtCore.Qt.AlignCenter)

		# -------------------------Кнопка сохранения --------------------------#

        collapseDict_btnSave = QtGui.QPushButton()
        collapseDict_btnSave.setFixedSize(80, 25)
        buttons_hbox = QtGui.QHBoxLayout()
        buttons_hbox.addWidget(collapseDict_btnSave)
        if int_lng == 'Russian':
            collapseDict_btnSave.setText("Записать")
        elif int_lng == 'English':
            collapseDict_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

        collapseDict_grid = QtGui.QGridLayout()
        collapseDict_grid.addWidget(prs_frame, 0, 0, alignment=QtCore.Qt.AlignCenter)
        collapseDict_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        collapseDict_grid.setRowStretch(3, 6)
        collapseDict_group = QtGui.QGroupBox()
        collapseDict_group.setLayout(collapseDict_grid)
        return collapseDict_group, collapseDict_btnSave, cMQ_edit, cEC_checks_list, \
        cEC_values_list, cEC_val_pr_list, cEC_val_def_list

