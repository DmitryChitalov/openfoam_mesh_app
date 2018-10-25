# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil

class meshQualityDict_generation_class:
	def meshQualityDict_func(int_lng, parn, tab, prj_path, mesh_name_txt, mqd_par):

		def meshQualityDict_end(int_lng, prj_path, parn):
			mQD = open(prj_path + '/meshQualityDict', 'a')

			close_str = '// ************************************************************************* //'
			mQD.write(close_str)
			mQD.close()

			if int_lng == 'Russian':
				msg = "Файл meshQualityDict сохранен"
			elif int_lng == 'English':
				msg = "The 'meshQualityDict' file was saved"
			mqd_par.on_msg_correct(msg)

			parn.cdw.setWidget(parn.outf_scroll)

			parn.msh_run.setEnabled(True)

			prj_dir = prj_path + '/meshQualityDict'

			outf = open(prj_dir)
			data = outf.read()
			if int_lng == 'Russian':
				parn.outf_lbl.setText("Файл " + "<font color='peru'>" + 'meshQualityDict' + "</font>")
			elif int_lng == 'English':
				parn.outf_lbl.setText("<font color='peru'>" + 'meshQualityDict' + "</font>" + " file")
			parn.outf_edit.setText(data)

			parn.cdw.setTitleBarWidget(parn.cdw_frame)

		msg_list = []

		#проверяем на заполнение meshQualityDict#
		meshQualityDict_path = prj_path + '/' + mesh_name_txt + '_foamyHexMesh' + '/' + 'meshQualityDict.pkl'
		if os.path.exists(meshQualityDict_path):
			meshQualityDict_vkl_arr = []

			meshQualityDict_input = open(meshQualityDict_path, 'rb')
			obj = pickle.load(meshQualityDict_input)
			meshQualityDict_input.close()

			meshQualityDict_vkl_arr.append('meshQualityDict')

		else:
			meshQualityDict_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'meshQualityDict'"
			elif int_lng == 'English':
				msg = "Fill out the 'meshQualityDict' form"
			msg_list.append(msg)

			meshQualityDict_vkl_arr.append(None)

		mqd_par.on_msg_error(msg_list)

		#########################################################################
		#Формируем блоки параметров для файла meshQualityDict#
		if os.path.exists(meshQualityDict_path):
            #controlMeshQuality
			space_str = '    '
            #maxNonOrtho
			if obj['mNO_chck'] == True:
				mNO_str = '\n' + '\n' + 'maxNonOrtho' + space_str + str(obj['mNO']) + ';' + '\n' + '\n'
			else:
				mNO_str = ''
            #maxBoundarySkewness
			if obj['mBS_chck'] == True:
				mBS_str = 'maxBoundarySkewness' + space_str + str(obj['mBS']) + ';' + '\n' + '\n'
			else:
				mBS_str = ''
            #maxInternalSkewness
			if obj['mIS_chck'] == True:
				mIS_str = 'maxInternalSkewness' + space_str + str(obj['mIS']) + ';' + '\n' + '\n'
			else:
				mIS_str = ''
            #maxConcave
			if obj['mC_chck'] == True:
				mC_str = 'maxConcave' + space_str + str(obj['mC']) + ';' + '\n' + '\n'
			else:
				mC_str = ''
            #minTetQuality
			if obj['mTQ_chck'] == True:
				mTQ_str = 'minTetQuality' + space_str + obj['mTQ'] + ';' + '\n' + '\n'
			else:
				mTQ_str = ''
            #minVol
			if obj['mV_chck'] == True:
				mV_str = 'minVol' + space_str + obj['mV'] + ';' + '\n' + '\n'
			else:
				mV_str = ''
            #minArea
			if obj['mA_chck'] == True:
				mA_str = 'minArea' + space_str + obj['mA'] + ';' + '\n' + '\n'
			else:
				mA_str = ''
            #minTwist
			if obj['mT_chck'] == True:
				mT_str = 'minTwist' + space_str + obj['mT'] + ';' + '\n' + '\n'
			else:
				mT_str = ''
            #minDeterminant
			if obj['mD_chck'] == True:
				mD_str = 'minDeterminant' + space_str + obj['mD'] + ';' + '\n' + '\n'
			else:
				mD_str = ''
            #minFaceWeight
			if obj['mFW_chck'] == True:
				mFW_str = 'minFaceWeight' + space_str + obj['mFW'] + ';' + '\n' + '\n'
			else:
				mFW_str = ''
            #minVolRatio
			if obj['mVR_chck'] == True:
				mVR_str = 'minVolRatio' + space_str + obj['mVR'] + ';' + '\n' + '\n'
			else:
				mVR_str = ''
            #minTriangleTwist
			if obj['mTT_chck'] == True:
				mTT_str = 'minTriangleTwist' + space_str + obj['mTT'] + ';' + '\n' + '\n'
			else:
				mTT_str = ''

			mQD_str = mNO_str + mBS_str + mIS_str + mC_str + mTQ_str + mV_str + \
            mA_str + mT_str + mD_str + mFW_str + mVR_str + mTT_str

		#########################################################################
		  			#Сохраняем файл при наличии различных опций#
		#########################################################################

		if not None in meshQualityDict_vkl_arr:

			shutil.copyfile(r'./matches/meshQualityDict', prj_path + r'/meshQualityDict')
			mQD = open(prj_path + '/meshQualityDict', 'a')

			mQD.write(mQD_str + '\n' + '\n')
			mQD.close()

			meshQualityDict_end(int_lng, prj_path, parn)

		#########################################################################
