# -*- coding: utf-8 -*-
# -------------------------------Импорт модулей----------------------------------

from PyQt4 import QtCore, QtGui
import shutil
import sys
import re
import os
import os.path

# ---------------------------Главная форма проекта-------------------------------

class prj_window_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        global par
        par = parent
		
        global int_lng
        int_lng = par.interface_lng_val	
             
# ------------------------Функции связанные с формой-----------------------------

# .....Функция, запускаемая при нажатии кнопки выбора директории сохранения нового проекта"......

        def on_path_choose():
            global new_dir
            global project_name_dir
            folder_dir = QtGui.QFileDialog.getExistingDirectory(directory=QtCore.QDir.currentPath())
            new_dir, project_name_dir = os.path.split(folder_dir)

            project_path_name.setText(new_dir)
            project_name.setText(project_name_dir)
                
# .....Функция, запускаемая при завершении редактирования названия проекта и его директории"......

        def handleEditingFinished():
            if project_name.text() and project_path_name.text():
                save_button.setEnabled(True)
        
# ....................Функция, запускаемая при нажатии кнопки "сохранить"....................
        
        def on_save_clicked():

            full_dir = new_dir + "/" + project_name_dir

            par.full_dir = full_dir

            prj_lbl = QtGui.QLabel()
            if int_lng == 'Russian':
                prj_lbl.setText('Путь до директории проекта:')
            elif int_lng == 'English':
                prj_lbl.setText('Path to mesh file:')

            prj_lbl.setStyleSheet("border-style: none;" "font-size: 10pt;")
            prj_path_lbl = QtGui.QLineEdit()
            prj_path_lbl.setStyleSheet("background-color: white;" "font-size: 10pt;" "color: green;")
            prj_path_lbl.setFixedSize(500, 25)
            prj_path_lbl.setText(full_dir)
            prj_path_lbl.setEnabled(False)
            par.tdw_grid.addWidget(prj_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
            par.tdw_grid.addWidget(prj_path_lbl, 0, 1, alignment=QtCore.Qt.AlignCenter)

            par.msh_open.setEnabled(True)

            self.close()

# .....................Функция, запускаемая при нажатии кнопки "отмена"......................
        
        def on_cancel_clicked():
            self.close()
            self.clear_label = QtGui.QLabel()
            parent.ffw.setTitleBarWidget(self.clear_label)
        
# -------------------------------------Второй блок формы------------------------------------

        title_label = QtGui.QLabel("Укажите директорию проекта")
        tl_hbox = QtGui.QHBoxLayout()
        tl_hbox.addWidget(title_label)
        project_label = QtGui.QLabel("Название проекта:") 
        project_name = QtGui.QLineEdit()
        project_name.setEnabled(False)
        project_name.textChanged.connect(handleEditingFinished)
        project_name.setFixedSize(180, 25)
        valid = QtGui.QRegExpValidator(QtCore.QRegExp("\S*"), self)
        project_name.setValidator(valid)
        project_path_label = QtGui.QLabel("Путь:")
        project_path_name = QtGui.QLineEdit()
        project_path_name.setEnabled(False)
        project_path_name.textChanged.connect(handleEditingFinished)
        project_path_name.setFixedSize(180, 25)
        path_button = QtGui.QPushButton("...")
        path_button.clicked.connect(on_path_choose)
        path_button.setFixedSize(25, 25)
        project_grid = QtGui.QGridLayout()
        project_grid.addWidget(project_label, 0, 0)
        project_grid.addWidget(project_name, 0, 1, alignment=QtCore.Qt.AlignRight)
        project_grid.addWidget(project_path_label, 1, 0)
        project_grid.addWidget(project_path_name, 1, 1)
        project_grid.addWidget(path_button, 1, 2)
        project_frame = QtGui.QFrame()
        project_frame.setFrameShape(QtGui.QFrame.Panel)
        project_frame.setFrameShadow(QtGui.QFrame.Sunken)
        project_frame.setLayout(project_grid) 
        project_grid_vbox = QtGui.QVBoxLayout() 
        project_grid_vbox.addWidget(project_frame)

# ---------------------Кнопки сохранения и отмены и их блок-------------------------

        save_button = QtGui.QPushButton("Сохранить")
        save_button.setFixedSize(80, 25)
        save_button.clicked.connect(on_save_clicked)
        save_button.setEnabled(False)
        cancel_button = QtGui.QPushButton("Отмена")
        cancel_button.setFixedSize(80, 25)
        cancel_button.clicked.connect(on_cancel_clicked)
        buttons_hbox = QtGui.QHBoxLayout()
        buttons_hbox.addWidget(save_button)
        buttons_hbox.addWidget(cancel_button)

# -------------------------Фрейм формы---------------------------

        bound_grid = QtGui.QGridLayout()
        bound_grid.addLayout(tl_hbox, 0, 0, alignment=QtCore.Qt.AlignCenter)
        bound_grid.addLayout(project_grid_vbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        bound_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
        bound_frame = QtGui.QFrame()
        bound_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        bound_frame.setLayout(bound_grid)
        bound_vbox = QtGui.QVBoxLayout() 
        bound_vbox.addWidget(bound_frame)

# --------------------Размещение на форме всех компонентов---------

        form_1 = QtGui.QFormLayout()
        form_1.addRow(bound_vbox)
        self.setLayout(form_1)
