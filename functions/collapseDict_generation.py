# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil

class collapseDict_generation_class:
	def collapseDict_func(int_lng, parn, tab, prj_path, mesh_name_txt, cd_par):
		def collapseDict_end(int_lng, prj_path, parn):
			cD = open(prj_path + '/collapseDict', 'a')

			close_str = '// ************************************************************************* //'
			cD.write(close_str)
			cD.close()

			if int_lng == 'Russian':
				msg = "Файл collapseDict сохранен"
			elif int_lng == 'English':
				msg = "The 'collapseDict' file was saved"
			cd_par.on_msg_correct(msg)

			
			parn.cdw.setWidget(parn.outf_scroll)

			parn.msh_run.setEnabled(True)

			prj_dir = prj_path + '/collapseDict'

			outf = open(prj_dir)
			data = outf.read()
			if int_lng == 'Russian':
				parn.outf_lbl.setText("Файл " + "<font color='peru'>" + 'collapseDict' + "</font>")
			elif int_lng == 'English':
				parn.outf_lbl.setText("<font color='peru'>" + 'collapseDict' + "</font>" + " file")
			parn.outf_edit.setText(data)

			parn.cdw.setTitleBarWidget(parn.cdw_frame)

		msg_list = []

		#проверяем на заполнение collapseDict#
		collapseDict_path = prj_path + '/' + mesh_name_txt + '_foamyHexMesh' + '/' + 'collapseDict.pkl'
		if os.path.exists(collapseDict_path):
			collapseDict_vkl_arr = []

			collapseDict_input = open(collapseDict_path, 'rb')
			obj = pickle.load(collapseDict_input)
			collapseDict_input.close()

			collapseDict_vkl_arr.append('collapseDict')

		else:
			collapseDict_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'collapseDict'"
			elif int_lng == 'English':
				msg = "Fill out the 'collapseDict' form"
			msg_list.append(msg)

			collapseDict_vkl_arr.append(None)

		cd_par.on_msg_error(msg_list)

		#########################################################################
		#Формируем блоки параметров для файла collapseDict#
		if os.path.exists(collapseDict_path):
            #controlMeshQuality
			space_str = '    '
			
			cMQ_str = '\n' + '\n' + 'controlMeshQuality' + space_str + obj['cMQ'] + ';' + '\n' + '\n'
            #collapseEdgesCoeffs
            #minimumEdgeLength
			if obj['mEL_chck'] == True:
				mEL_str = space_str + 'minimumEdgeLength' + space_str + obj['mEL'] + ';' + '\n' + '\n'
			else:
				mEL_str = ''
            #maximumMergeAngle
			if obj['mMA_chck'] == True:
				mMA_str = space_str + 'maximumMergeAngle' + space_str + obj['mMA'] + ';' 
			else:
				mMA_str = ''
			cEC_str = 'collapseEdgesCoeffs' + '\n' + '{' + '\n' + mEL_str + mMA_str + '\n' + '}' + '\n' + '\n'

            #collapseFacesCoeffs
            #initialFaceLengthFactor
			if obj['iFLF_chck'] == True:
				iFLF_str = space_str + 'initialFaceLengthFactor' + space_str + str(obj['iFLF']) + ';' + '\n' + '\n'
			else:
				iFLF_str = ''
            #maxCollapseFaceToPointSideLengthCoeff
			if obj['mCFTPSLC_chck'] == True:
				mCFTPSLC_str = space_str + 'maxCollapseFaceToPointSideLengthCoeff' + space_str + str(obj['mCFTPSLC']) + ';' + '\n' + '\n'
			else:
				mCFTPSLC_str = ''
            #allowEarlyCollapseToPoint
			if obj['aECTP_chck'] == True:
				aECTP_str = space_str + 'allowEarlyCollapseToPoint' + space_str + obj['aECTP'] + ';' + '\n' + '\n'
			else:
				aECTP_str = ''
            #allowEarlyCollapseCoeff
			if obj['aECC_chck'] == True:
				aECC_str = space_str + 'allowEarlyCollapseCoeff' + space_str + str(obj['aECC']) + ';' + '\n' + '\n'
			else:
				aECC_str = ''
            #guardFraction
			if obj['gF_chck'] == True:
				gF_str = space_str + 'guardFraction' + space_str + str(obj['gF']) + ';' 
			else:
				gF_str = ''
			cFC_str = 'collapseFacesCoeffs' + '\n' + '{' + '\n' + iFLF_str + \
            mCFTPSLC_str + aECTP_str + aECC_str + gF_str + '\n' + '}' + '\n' + '\n'

            #controlMeshQualityCoeffs
            #include
			if obj['i_chck'] == True:
				gF_str = space_str + '#include' + space_str + '"' + obj['i'] + '"' + ';' + '\n' + '\n'
			else:
				gF_str = ''
            #edgeReductionFactor
			if obj['eRF_chck'] == True:
				eRF_str = space_str + 'edgeReductionFactor' + space_str + str(obj['eRF']) + ';' + '\n' + '\n'
			else:
				eRF_str = ''
            #faceReductionFactor
			if obj['fRF_chck'] == True:
				fRF_str = space_str + 'faceReductionFactor' + space_str + str(obj['fRF']) + ';' + '\n' + '\n'
			else:
				fRF_str = ''
            #maximumSmoothingIterations
			if obj['mSI_chck'] == True:
				mSI_str = space_str + 'maximumSmoothingIterations' + space_str + str(obj['mSI']) + ';' + '\n' + '\n'
			else:
				mSI_str = ''
            #maximumIterations
			if obj['mI_chck'] == True:
				mI_str = space_str + 'maximumIterations' + space_str + str(obj['mI']) + ';' + '\n' + '\n'
			else:
				mI_str = ''
            #maxPointErrorCount
			if obj['mPEC_chck'] == True:
				mPEC_str = space_str + 'maxPointErrorCount' + space_str + str(obj['mPEC']) + ';'
			else:
				mPEC_str = ''
			cMQC_str = 'controlMeshQualityCoeffs' + '\n' + '{' + '\n' + gF_str + \
            eRF_str + fRF_str + mSI_str + mI_str + mPEC_str + '\n' + '}'

			cd_str = cMQ_str + cEC_str + cFC_str + cMQC_str

		#########################################################################
		  			#Сохраняем файл при наличии различных опций#
		#########################################################################

		if not None in collapseDict_vkl_arr:

			shutil.copyfile(r'./matches/collapseDict', prj_path + r'/collapseDict')
			cD = open(prj_path + '/collapseDict', 'a')

			cD.write(cd_str + '\n' + '\n')
			cD.close()

			collapseDict_end(int_lng, prj_path, parn)

		#########################################################################
