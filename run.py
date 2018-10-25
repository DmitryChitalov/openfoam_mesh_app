#!/usr/bin/python3
# -*- coding: utf-8 -*-
###-------------------------------Импорт модулей----------------------------------###

from PyQt4 import QtCore, QtGui                                                 
import sys, os
import subprocess
import time

from functions.first_toolbar_functions import first_toolbar_functions_class
from functions.second_toolbar_functions import second_toolbar_functions_class

###-------------------------Главное окно программы-----------------------------###

class MainWindowClass(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.interface_lng_val = 'Russian'
        self.setWindowTitle("Графический интерфейс программы OpenFOAM")

        self.full_dir = ''
        self.prj_name = ''

        # ---------------------------Панель управления решением задачи МСС-----------------------------

        self.proj_open = QtGui.QAction(self)
        self.proj_open.setEnabled(True)
        proj_ico = self.style().standardIcon(QtGui.QStyle.SP_ArrowUp)
        self.proj_open.setIcon(proj_ico)
        self.proj_open.setToolTip('Открыть проект')

        self.lng_chs = QtGui.QAction(self)
        self.lng_chs.setEnabled(True)
        lng_chs_ico = self.style().standardIcon(QtGui.QStyle.SP_FileDialogDetailedView)
        self.lng_chs.setIcon(lng_chs_ico)
        self.lng_chs.setToolTip('Выбрать язык интерфейса программы')

        self.toolBar_1 = QtGui.QToolBar("MyToolBar")
        self.toolBar_1.addAction(self.proj_open)
        self.toolBar_1.addAction(self.lng_chs)

        self.proj_open.triggered.connect(lambda: first_toolbar_functions_class.on_proj_open(self))

        self.addToolBar(self.toolBar_1)
		
        ###----------------------Панель управления подготовкой расчетных сеток--------------------------###

        self.msh_open = QtGui.QAction(self)
        self.msh_open.setEnabled(False)
        msh_ico = self.style().standardIcon(QtGui.QStyle.SP_FileDialogNewFolder)
        self.msh_open.setIcon(msh_ico)
        self.msh_open.setToolTip('Открыть форму выбора расчетной сетки')

        self.msh_run = QtGui.QAction(self)
        self.msh_run.setEnabled(False)
        msh_ico = self.style().standardIcon(QtGui.QStyle.SP_ArrowRight)
        self.msh_run.setIcon(msh_ico)
        self.msh_run.setToolTip('Выполнить генерацию расчетной сетки')

        self.msh_visual = QtGui.QAction(self)
        self.msh_visual.setEnabled(False)
        msh_visual_ico = self.style().standardIcon(QtGui.QStyle.SP_MediaSeekForward)
        self.msh_visual.setIcon(msh_visual_ico)
        self.msh_visual.setToolTip('Выполнить визуализацию расчетной сетки')

        self.toolBar_2 = QtGui.QToolBar()
        self.toolBar_2.addAction(self.msh_open)
        self.toolBar_2.addAction(self.msh_run)
        self.toolBar_2.addAction(self.msh_visual)
       
        self.msh_open.triggered.connect(lambda: second_toolbar_functions_class.on_msh_open(self))
        self.msh_run.triggered.connect(lambda: second_toolbar_functions_class.on_msh_run(prj_path_val, mesh_name_txt_val, pp_dir, self, self.interface_lng_val, msh_type))
        self.msh_visual.triggered.connect(lambda: second_toolbar_functions_class.on_visual_msh_run(prj_path_val, mesh_name_txt_val, pp_dir, self, self.interface_lng_val, msh_type))
        
        self.addToolBar(self.toolBar_2)
        self.insertToolBarBreak(self.toolBar_2)

        ###--------------------Меню-------------------###

        self.menu_bar = self.menuBar()
        self.menu_bar.setNativeMenuBar(False)

        self.fhmd_open_btn = QtGui.QAction(self)
        self.fhmd_open_btn.setText('foamyHexMeshDict')

        self.mQD_open_btn = QtGui.QAction(self)
        self.mQD_open_btn.setText('meshQualityDict')

        self.cD_open_btn = QtGui.QAction(self)
        self.cD_open_btn.setText('collapseDict')
                        
        ###----------------Верхний виджет с полным путем до файла сетки----------------###

        self.tdw = QtGui.QDockWidget()
        self.tdw.setFixedSize(1400, 65)
        self.tdw.setFeatures(self.tdw.NoDockWidgetFeatures)       
        self.tdw_grid = QtGui.QGridLayout()
        self.tdw_grid.setColumnStretch(2, 1)
        self.tdw_frame = QtGui.QFrame()
        self.tdw_frame.setStyleSheet("background-color: ghostwhite;" "border-width: 0.5px;" "border-style: solid;" "border-color: silver;")
        self.tdw_frame.setLayout(self.tdw_grid)
        self.tdw.setWidget(self.tdw_frame)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.tdw)

        ###-----------------Левый виджет с формой генерации сетки--------------------###

        self.ldw = QtGui.QDockWidget()
        self.ldw.setFixedSize(840, 680)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.ldw)
        self.ldw.setFeatures(self.ldw.NoDockWidgetFeatures)
        self.ldw_grid = QtGui.QGridLayout()
        self.ldw_frame = QtGui.QFrame()
        self.ldw_frame.setFixedSize(840, 44)
        self.ldw_frame.setStyleSheet("background-color: honeydew;" "border-width: 1px;" "border-style: solid;" "border-color: dimgray;" "border-radius: 4px;")
        self.ldw_frame.setLayout(self.ldw_grid)	

        ###-----------Центральный виджет с виджетом содержимого файла сетки-----------###

        self.cdw = QtGui.QDockWidget()
        self.setCentralWidget(self.cdw)
        self.cdw.setFeatures(self.cdw.NoDockWidgetFeatures)

        self.cdw_grid = QtGui.QGridLayout()
        self.cdw_frame = QtGui.QFrame()
        self.cdw_frame.setStyleSheet("border-width: 1px;" "border-style: solid;" "border-color: dimgray;" "border-radius: 4px;" "background-color: honeydew;")
        self.cdw_frame.setLayout(self.cdw_grid)

        self.outf_lbl = QtGui.QLabel()
        self.outf_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.outf_lbl.setStyleSheet("border-style: none;" "font-size: 10pt;")
		
        self.cdw_grid.addWidget(self.outf_lbl, 0, 0)

        self.outf_edit = QtGui.QTextEdit()
        self.outf_scroll = QtGui.QScrollArea()
        self.outf_scroll.setWidgetResizable(True) 
        self.outf_scroll.setWidget(self.outf_edit)

        self.outf_scroll.setFixedSize(350, 635)
        self.cdw_frame.setFixedSize(350, 35)

        ###------------------Нижний виджет со служебными сообщениями------------------###

        self.serv_mes = QtGui.QDockWidget("Служебные сообщения")
        self.serv_mes.setFixedSize(1400, 160)
        self.serv_mes.setFeatures(self.serv_mes.NoDockWidgetFeatures)
        self.listWidget = QtGui.QListWidget()
        self.serv_mes.setWidget(self.listWidget)

    ###---------------------Функции, связанные с работой главного окна------------------------###

    # ...........................Функция клика по файлу из дерева.........................

    ###........................Функция открытия окна выбора интерфейса программы...................###         

    #.........................Функция получения языка интерфейса..........................      

    def on_lng_get(self, interface_lng):
        global interface_lng_val

        self.interface_lng_val = interface_lng

        if self.interface_lng_val == 'Russian':
            self.setWindowTitle("Генератор расчетных сеток")
            self.prj_open.setToolTip('Открыть проект')
            self.msh_run.setToolTip('Выполнить генерацию расчетной сетки')
            self.msh_visual.setToolTip('Выполнить визуализацию расчетной сетки')
            self.lng_chs.setToolTip('Выбрать язык интерфейса программы')
        elif self.interface_lng_val == 'English':
            self.setWindowTitle("Mesh generator")
            self.prj_open.setToolTip('Open project')
            self.msh_run.setToolTip('Run mesh generation')
            self.msh_visual.setToolTip('Run mesh vizualization')
            self.lng_chs.setToolTip('Select the interface language for the program')          

    #.........................Функция получения пути до директории..........................

    def on_prj_path_get(self, prj_path, mesh_name_txt):
        global prj_path_val
        global mesh_name_txt_val
        global pp_dir
        
        prj_path_val = prj_path
        mesh_name_txt_val = mesh_name_txt

        pp_dir, pp_sys = os.path.split(prj_path_val)

    #.............................Функция получения типа сетки..............................

    def on_mesh_type_get(self, pd_2):
        global msh_type
        msh_type = pd_2

###---------------------------Формирование главного окна программы-------------------------

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindowClass()
    window.setFixedSize(1400, 1000)
    window.setGeometry(200, 30, 0, 0)
    window.show()
    sys.exit(app.exec_())
       
