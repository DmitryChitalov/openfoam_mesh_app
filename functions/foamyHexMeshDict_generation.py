# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil

class foamyHexMeshDict_generation_class:			
	def foamyHexMeshDict_func(int_lng, parn, tab, prj_path, mesh_name_txt, pd_2, fhmd_par): 
		def foamyHexMeshDict_end(int_lng, prj_path, parn):
			fHMD = open(prj_path + '/foamyHexMeshDict', 'a')

			close_str = '// ************************************************************************* //'
			fHMD.write(close_str)
			fHMD.close()

			if int_lng == 'Russian':
				msg = "Файл 'foamyHexMeshDict' сохранен"
			elif int_lng == 'English':
				msg = "The 'foamyHexMeshDict' file was saved"
			fhmd_par.on_msg_correct(msg)

			parn.cdw.setWidget(parn.outf_scroll)
			
			parn.msh_run.setEnabled(True)

			prj_dir = prj_path + '/foamyHexMeshDict'

			outf = open(prj_dir)
			data = outf.read()
			if int_lng == 'Russian':
				parn.outf_lbl.setText("Файл " + "<font color='peru'>" + 'foamyHexMeshDict' + "</font>") 
			elif int_lng == 'English':
				parn.outf_lbl.setText("<font color='peru'>" + 'foamyHexMeshDict' + "</font>" + " file") 
			parn.outf_edit.setText(data)

			parn.cdw.setTitleBarWidget(parn.cdw_frame)
			
		msg_list = []

		#проверяем на заполнение initial#
		initial_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path):
			initial_vkl_arr = []

			initial_input = open(initial_path, 'rb')
			initial_obj = pickle.load(initial_input)
			initial_input.close()

			g_v = initial_obj['g']
			
			initial_vkl_arr.append('initial')

		else:
			initial_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'initial'"
			elif int_lng == 'English':
				msg = "Fill out the 'initial' form"
			msg_list.append(msg)

			initial_vkl_arr.append(None)

		#проверяем на заполнение geometry_1#
		geometry_1_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_1.pkl'
		if os.path.exists(geometry_1_path):	
			geometry_1_vkl_arr = []

			geometry_1_input = open(geometry_1_path, 'rb')
			geometry_1_obj = pickle.load(geometry_1_input)
			geometry_1_input.close()

			geometry_1_vkl_arr.append('geometry_1')
		else:
			geometry_1_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'geometry_1'"
			elif int_lng == 'English':
				msg = "Fill out the form 'geometry_1'"
			msg_list.append(msg)
			geometry_1_vkl_arr.append(None)

		#проверяем на заполнение geometry_2#
		geometry_2_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
		if os.path.exists(geometry_2_path):	
			geometry_2_vkl_arr = []

			geometry_2_input = open(geometry_2_path, 'rb')
			geometry_2_obj = pickle.load(geometry_2_input)
			geometry_2_input.close()

			geometry_2_vkl_arr.append('geometry_2')
		else:
			geometry_2_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'geometry_2'"
			elif int_lng == 'English':
				msg = "Fill out the form 'geometry_2'"
			msg_list.append(msg)
			geometry_2_vkl_arr.append(None)
			
		#проверяем на заполнение surfaceConformation#	
		surfaceConformation_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceConformation.pkl'	
		if os.path.exists(surfaceConformation_path):	
			surfaceConformation_vkl_arr = []

			surfaceConformation_input = open(surfaceConformation_path, 'rb')
			surfaceConformation_obj = pickle.load(surfaceConformation_input)
			surfaceConformation_input.close()

			surfaceConformation_vkl_arr.append('surfaceConformation')
		else:
			surfaceConformation_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'surfaceConformation'"
			elif int_lng == 'English':
				msg = "Fill out the form 'surfaceConformation'"
			msg_list.append(msg)
			surfaceConformation_vkl_arr.append(None)
			
		#проверяем на заполнение initialPoints#	
		initialPoints_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initialPoints.pkl'	
		if os.path.exists(initialPoints_path):	
			initialPoints_vkl_arr = []

			initialPoints_input = open(initialPoints_path, 'rb')
			initialPoints_obj = pickle.load(initialPoints_input)
			initialPoints_input.close()

			initialPoints_vkl_arr.append('initialPoints')
		else:
			initialPoints_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'initialPoints'"
			elif int_lng == 'English':
				msg = "Fill out the form 'initialPoints'"
			msg_list.append(msg)
			initialPoints_vkl_arr.append(None)
			
		#проверяем на заполнение motionControl#	
		motionControl_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'motionControl.pkl'	
		if os.path.exists(motionControl_path):	
			motionControl_vkl_arr = []

			motionControl_input = open(motionControl_path, 'rb')
			motionControl_obj = pickle.load(motionControl_input)
			motionControl_input.close()

			motionControl_vkl_arr.append('motionControl')
		else:
			motionControl_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'motionControl'"
			elif int_lng == 'English':
				msg = "Fill out the form 'motionControl'"
			msg_list.append(msg)
			motionControl_vkl_arr.append(None)
			
		#проверяем на заполнение polyMeshFiltering#	
		polyMeshFiltering_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'polyMF.pkl'
		#print(os.path.exists(polyMeshFiltering_path))
		if os.path.exists(polyMeshFiltering_path):	
			polyMeshFiltering_vkl_arr = []

			polyMeshFiltering_input = open(polyMeshFiltering_path, 'rb')
			polyMeshFiltering_obj = pickle.load(polyMeshFiltering_input)
			polyMeshFiltering_input.close()

			polyMeshFiltering_vkl_arr.append('polyMeshFiltering')
		else:
			polyMeshFiltering_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'polyMeshFiltering'"
			elif int_lng == 'English':
				msg = "Fill out the form 'polyMeshFiltering'"
			msg_list.append(msg)
			polyMeshFiltering_vkl_arr.append(None)
			
		fhmd_par.on_msg_error(msg_list)	
		
		#########Формируем блоки параметров для файла foamyHexMeshDict##########
		
		###geometry###
		if os.path.exists(geometry_1_path) and os.path.exists(geometry_2_path):	

			geometry_pred_str = '\n' + '\n' + '#includeEtc "caseDicts/mesh/generation/foamyHexMeshDict"' + '\n' + '\n' + 'geometry' + '\n' + '{' + '\n'

			i = 1
			j = 0
			
			geometry_eld_str_itog = ''
			for el_dict in geometry_1_obj:
				
				tri_pred_str_1 = '    '
				tri_pred_str_2 = '        '
				tri_pred_str_3 = '            '
				tri_pred_str_4 = '                '
				tri_pred_str_5 = '                    '
				###Три-поверхность и распределенная три-поверхность###
				if el_dict['geometry_' + str(i)] == 'Три-поверхность' or el_dict['geometry_' + str(i)] == 'Tri-surface' or el_dict['geometry_' + str(i)] == 'Распределенная три-поверхность' or el_dict['geometry_' + str(i)] == 'Distributed tri-surface':
					
					tri_pred_main_name = geometry_2_obj[j]['file']
					
					tri_pred_dop_name = 'name ' + geometry_2_obj[j]['name']
					tri_type_str = 'type ' + geometry_2_obj[j]['type']
					tri_end = tri_pred_str_1 +  '}' + '\n'
					tri_itog = tri_pred_str_1 + tri_pred_main_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + tri_pred_dop_name + ';' + '\n' + tri_pred_str_2 + tri_type_str + ';' + '\n' + tri_pred_str_1 + '}' + '\n'

					geometry_eld_str_itog = geometry_eld_str_itog + tri_itog

				###Базовая фигура###
				if el_dict['geometry_' + str(i)] == 'Базовая фигура' or el_dict['geometry_' + str(i)] == 'Base shape':
					#'шестигранник'#
					if el_dict['shape_type_' + str(i)] == 'шестигранник' or el_dict['shape_type_' + str(i)] == 'box':
						box_name = geometry_2_obj[j]['shape']
						box_type = geometry_2_obj[j]['type']
						box_max_x = geometry_2_obj[j]['max'][0]
						box_max_y = geometry_2_obj[j]['max'][1]
						box_max_z = geometry_2_obj[j]['max'][2]
						box_min_x = geometry_2_obj[j]['min'][0]
						box_min_y = geometry_2_obj[j]['min'][1]
						box_min_z = geometry_2_obj[j]['min'][2]

						box_itog_1 = tri_pred_str_1 + box_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + box_type + ';' + '\n'
						box_itog_2 = tri_pred_str_2 + 'min ' + '(' + box_min_x + ' ' + box_min_y + ' ' + box_min_z + ')' + ';' + '\n'
						box_itog_3 = tri_pred_str_2 + 'max ' + '(' + box_max_x + ' ' + box_max_y + ' ' + box_max_z + ')' + ';' + '\n' + tri_pred_str_1 + '}' + '\n'

						box_itog = box_itog_1 + box_itog_2 + box_itog_3

						geometry_eld_str_itog = geometry_eld_str_itog + box_itog

					#'сфера'#	
					if el_dict['shape_type_' + str(i)] == 'сфера' or el_dict['shape_type_' + str(i)] == 'sphere':
						sphere_name = geometry_2_obj[j]['shape']
						sphere_type = geometry_2_obj[j]['type']
						sphere_centre_x = geometry_2_obj[j]['centre'][0]
						sphere_centre_y = geometry_2_obj[j]['centre'][1]
						sphere_centre_z = geometry_2_obj[j]['centre'][2]
						sphere_radius = geometry_2_obj[j]['radius']

						sphere_itog_1 = tri_pred_str_1 + sphere_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + sphere_type + ';' + '\n'
						sphere_itog_2 = tri_pred_str_2 + 'centre ' + '(' + sphere_centre_x + ' ' + sphere_centre_y + ' ' + sphere_centre_z + ')' + ';' + '\n'
						sphere_itog_3 = tri_pred_str_2 + 'radius ' + str(sphere_radius) + ';' + '\n' + tri_pred_str_1 + '}' + '\n'

						sphere_itog = sphere_itog_1 + sphere_itog_2 + sphere_itog_3

						geometry_eld_str_itog = geometry_eld_str_itog + sphere_itog

					#'цилиндр'#
					if el_dict['shape_type_' + str(i)] == 'цилиндр' or el_dict['shape_type_' + str(i)] == 'cylinder':
						cylinder_name = geometry_2_obj[j]['shape']
						cylinder_type = geometry_2_obj[j]['type']

						cylinder_point1_x = geometry_2_obj[j]['point1'][0]
						cylinder_point1_y = geometry_2_obj[j]['point1'][1]
						cylinder_point1_z = geometry_2_obj[j]['point1'][2]

						cylinder_point2_x = geometry_2_obj[j]['point2'][0]
						cylinder_point2_y = geometry_2_obj[j]['point2'][1]
						cylinder_point2_z = geometry_2_obj[j]['point2'][2]

						cylinder_radius = geometry_2_obj[j]['radius']

						cylinder_itog_1 = tri_pred_str_1 + cylinder_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + cylinder_type + ';' + '\n'
						cylinder_itog_2 = tri_pred_str_2 + 'min ' + '(' + cylinder_point1_x + ' ' + cylinder_point1_y + ' ' + cylinder_point1_z + ')' + ';' + '\n'
						cylinder_itog_3 = tri_pred_str_2 + 'min ' + '(' + cylinder_point2_x + ' ' + cylinder_point2_y + ' ' + cylinder_point2_z + ')' + ';' + '\n'
						cylinder_itog_4 = tri_pred_str_2 + 'radius ' + str(cylinder_radius) + ';' + '\n' + tri_pred_str_1 + '}' + '\n'

						cylinder_itog = cylinder_itog_1 + cylinder_itog_2 + cylinder_itog_3 + cylinder_itog_4

						geometry_eld_str_itog = geometry_eld_str_itog + cylinder_itog

					#'плоскость'#
					if el_dict['shape_type_' + str(i)] == 'плоскость' or el_dict['shape_type_' + str(i)] == 'plane':
						plane_name = geometry_2_obj[j]['shape']
						plane_type = geometry_2_obj[j]['type']
						plane_planeType = geometry_2_obj[j]['planeType']

						plane_basePoint_x = geometry_2_obj[j]['basePoint'][0]
						plane_basePoint_y = geometry_2_obj[j]['basePoint'][1]
						plane_basePoint_z = geometry_2_obj[j]['basePoint'][2]

						plane_normalVector_x = geometry_2_obj[j]['normalVector'][0]
						plane_normalVector_y = geometry_2_obj[j]['normalVector'][1]
						plane_normalVector_z = geometry_2_obj[j]['normalVector'][2]

						plane_itog_1 = tri_pred_str_1 + plane_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + plane_type + ';' + '\n'
						plane_itog_2 = tri_pred_str_2 + 'planeType' + ' ' + plane_planeType + ';' + '\n' + tri_pred_str_2 + 'pointAndNormalDict' + '\n' + tri_pred_str_2 + '{' + '\n'
						plane_itog_3 = tri_pred_str_3 + 'basePoint ' + '(' + plane_basePoint_x + ' ' + plane_basePoint_y + ' ' + plane_basePoint_z + ')' + ';' + '\n'
						plane_itog_4 = tri_pred_str_3 + 'normalVector ' + '(' + plane_normalVector_x + ' ' + plane_normalVector_y + ' ' + plane_normalVector_z + ')' + ';' + '\n'
						plane_itog_5 = tri_pred_str_2 + '}' + '\n'+ tri_pred_str_1 + '}' + '\n'

						plane_itog = plane_itog_1 + plane_itog_2 + plane_itog_3 + plane_itog_4 + plane_itog_5

						geometry_eld_str_itog = geometry_eld_str_itog + plane_itog

					#'пластина'#
					if el_dict['shape_type_' + str(i)] == 'пластина' or el_dict['shape_type_' + str(i)] == 'plate':
						plate_name = geometry_2_obj[j]['shape']
						plate_type = geometry_2_obj[j]['type']

						plate_origin_x = geometry_2_obj[j]['origin'][0]
						plate_origin_y = geometry_2_obj[j]['origin'][1]
						plate_origin_z = geometry_2_obj[j]['origin'][2]

						plate_span_x = geometry_2_obj[j]['span'][0]
						plate_span_y = geometry_2_obj[j]['span'][1]
						plate_span_z = geometry_2_obj[j]['span'][2]

						plate_itog_1 = tri_pred_str_1 + plate_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + plate_type + ';' + '\n'
						plate_itog_2 = tri_pred_str_2 + 'origin ' + '(' + plate_origin_x + ' ' + plate_origin_y + ' ' + plate_origin_z + ')' + ';' + '\n'
						plate_itog_3 = tri_pred_str_2 + 'span ' + '(' + plate_span_x + ' ' + plate_span_y + ' ' + plate_span_z + ')' + ';' + '\n' + tri_pred_str_1 + '}' + '\n'

						plate_itog = plate_itog_1 + plate_itog_2 + plate_itog_3

						geometry_eld_str_itog = geometry_eld_str_itog + plate_itog

				i = i + 1
				j = j + 1				

			geometry_post_str = '}' + '\n' + '\n'

			geometry_bl = geometry_pred_str + geometry_eld_str_itog + geometry_post_str
			
		###surfaceConformation###
		if os.path.exists(surfaceConformation_path):
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '
			
			surfaceConformation_pred_str = 'surfaceConformation' + '\n' + '{' + '\n'
			
			lIM_list = surfaceConformation_obj['sC_start_prs']['lIM']
			sFP = surfaceConformation_obj['sC_start_prs']['sFP']
			eA = surfaceConformation_obj['sC_start_prs']['eA']
			gFP = surfaceConformation_obj['sC_start_prs']['gFP']
			snapFP = surfaceConformation_obj['sC_start_prs']['snapFP']
			cE = surfaceConformation_obj['sC_start_prs']['cE']
			
			sC_itog_1 = tri_pred_str_1 + 'locationInMesh' + tri_pred_str_1 + '(' + lIM_list[0] + ' ' + lIM_list[1] + ' ' + lIM_list[2] + ')' + ';' + '\n' + '\n'
			sC_itog_2 = tri_pred_str_1 + 'featurePointControls' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'specialiseFeaturePoints' + tri_pred_str_1 + sFP + ';' + '\n'
			sC_itog_3 = tri_pred_str_2 + 'edgeAiming' + tri_pred_str_4 + ' ' + eA + ';' + '\n'
			sC_itog_4 = tri_pred_str_2 + 'guardFeaturePoints' + tri_pred_str_2 + ' ' + gFP + ';' + '\n'
			sC_itog_5 = tri_pred_str_2 + 'snapFeaturePoints' + tri_pred_str_2 + '  ' + snapFP + ';' + '\n'
			sC_itog_6 = tri_pred_str_2 + 'circulateEdges' + tri_pred_str_2 + '     ' + cE + ';' + '\n' + tri_pred_str_1 + '}'
			
			#if gTCT_v == True:
			sC_conf_prs_list = surfaceConformation_obj['sC_conf_prs']
			sC_conf_prs_pred = tri_pred_str_1 + '\n' + '\n' + tri_pred_str_1 + 'geometryToConformTo' + '\n' + tri_pred_str_1 + '{' + '\n'
			sC_conf_prs_post = tri_pred_str_1 + '}' + '\n' + '\n'
			sC_conf_prs_itog = ''
			for sC_cp in sC_conf_prs_list:

				g = sC_cp['g']
				fM = sC_cp['fM']
				iA = sC_cp['iA']

				sC_conf_prs_itog = sC_conf_prs_itog + tri_pred_str_2 + g + '\n' + tri_pred_str_2 + '{' + '\n' + tri_pred_str_3 + 'featureMethod' + tri_pred_str_1 + fM + ';' + '\n' \
				+ tri_pred_str_3 + 'includedAngle' + ' ' + str(iA) + ';' + '\n' + tri_pred_str_2 + '}' + '\n' + '\n'
			sC_itog_7 = sC_conf_prs_pred + sC_conf_prs_itog + sC_conf_prs_post
			
			surfaceConformation_itog = sC_itog_1 + sC_itog_2 + sC_itog_3 + sC_itog_4 + sC_itog_5 + sC_itog_6 + sC_itog_7
			
			surfaceConformation_post_str = '}' + '\n\n'

			surfaceConformation_bl = surfaceConformation_pred_str + surfaceConformation_itog + surfaceConformation_post_str
			
		###initialPoints###
		if os.path.exists(initialPoints_path):
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '
			
			initialPoints_pred_str = 'initialPoints' + '\n' + '{' + '\n'
			
			iP = initialPoints_obj['iP']
			mCSL_chck = initialPoints_obj['minCellSizeLimit_chck']
			mL_chck = initialPoints_obj['minLevels_chck'] 
			mSR_chck = initialPoints_obj['maxSizeRatio_chck'] 
			sR_chck = initialPoints_obj['sampleResolution_chck']  
			sSR_chck = initialPoints_obj['surfaceSampleResolution_chck']
			
			sC_itog_1 = tri_pred_str_1 + 'initialPointsMethod' + tri_pred_str_1 + iP + ';' + '\n' + '\n'
			
			aDC_pred = tri_pred_str_1 + 'autoDensityCoeffs' + '\n' + tri_pred_str_1 + '{' + '\n'
			if mCSL_chck == True:
				mCSL_bl = tri_pred_str_2 + 'minCellSizeLimit' + tri_pred_str_1 + str(initialPoints_obj['minCellSizeLimit']) + ';' + '\n'
			else:
			    mCSL_bl = ''
			if mL_chck == True:
				mL_bl = tri_pred_str_2 + 'minLevels' + tri_pred_str_1 + str(initialPoints_obj['minLevels']) + ';' + '\n'
			else:
			    mL_bl = ''
			if mSR_chck == True:
				mSR_bl = tri_pred_str_2 + 'maxSizeRatio' + tri_pred_str_1 + str(initialPoints_obj['maxSizeRatio']) + ';' + '\n'
			else:
			    mSR_bl = ''
			if sR_chck == True:
				sR_bl = tri_pred_str_2 + 'sampleResolution' + tri_pred_str_1 + str(initialPoints_obj['sampleResolution']) + ';' + '\n'
			else:
			    sR_bl = ''
			if sSR_chck == True:
				sSR_bl = tri_pred_str_2 + 'surfaceSampleResolution' + tri_pred_str_1 + str(initialPoints_obj['surfaceSampleResolution']) + ';' + '\n'
			else:
			    sSR_bl = ''
				
			aDC_middle = mCSL_bl + mL_bl + mSR_bl + sR_bl + sSR_bl
			aDC_post = tri_pred_str_1 + '}' + '\n' + '}' + '\n' + '\n'
			
			aDC_itog = aDC_pred + aDC_middle + aDC_post
			
			initialPoints_bl = initialPoints_pred_str + sC_itog_1 + aDC_itog
			
		###motionControl###
		if os.path.exists(motionControl_path):

			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '
			
			motionControl_pred_str = 'motionControl' + '\n' + '{' + '\n'
			dCS = motionControl_obj['mC_start_prs']['dCS']
			mCSC = motionControl_obj['mC_start_prs']['mCSC']
			mSI = motionControl_obj['mC_start_prs']['mSI']
			mRI = motionControl_obj['mC_start_prs']['mRI']
			oO = motionControl_obj['mC_start_prs']['oO']
			tC = motionControl_obj['mC_start_prs']['tC']
			
			sC_itog_1 = tri_pred_str_1 + 'defaultCellSize' + tri_pred_str_1 + str(dCS) + ';' + '\n' + '\n'
			sC_itog_2 = tri_pred_str_1 + 'minimumCellSizeCoeff' + tri_pred_str_1 + str(mCSC) + ';' + '\n' + '\n'
			sC_itog_3 = tri_pred_str_1 + 'maxSmoothingIterations' + tri_pred_str_1 + str(mSI) + ';' + '\n' + '\n'
			sC_itog_4 = tri_pred_str_1 + 'maxRefinementIterations' + tri_pred_str_1 + str(mRI) + ';' + '\n' + '\n'
			
			mC_sCF_prs_list = motionControl_obj['mC_sCF_prs']
			mC_sCF_prs_pred = tri_pred_str_1 + 'shapeControlFunctions' + '\n' + tri_pred_str_1 + '{'
			mC_sCF_prs_post = tri_pred_str_2 + '}' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
			mC_sCF_prs_itog = ''
			for mC_scfp in mC_sCF_prs_list:

				g = mC_scfp['g']
				t = mC_scfp['t']
				p = mC_scfp['p']
				m = mC_scfp['m']
				sCSF = mC_scfp['sCSF']
				sCSC = mC_scfp['sCSC']
				cSF = mC_scfp['cSF']
				dCSC = mC_scfp['dCSC']
				dC = mC_scfp['dC']
				
				mC_sCF_prs_itog = mC_sCF_prs_itog + '\n' + tri_pred_str_2 + g + '\n' + tri_pred_str_2 + '{' \
				+ '\n' + tri_pred_str_3 + 'type' + tri_pred_str_1 + t + ';' + '\n' \
				+ tri_pred_str_3 + 'priority' + tri_pred_str_1 + str(p) + ';' + '\n' \
				+ tri_pred_str_3 + 'mode' + tri_pred_str_1 + m + ';' + '\n' \
				+ tri_pred_str_3 + 'surfaceCellSizeFunction' + tri_pred_str_1 + sCSF + ';' + '\n' \
				+ tri_pred_str_3 + 'uniformValueCoeffs' + '\n' + tri_pred_str_3 + '{' + '\n' \
				+ tri_pred_str_4 + 'surfaceCellSizeCoeff' + tri_pred_str_1 + str(sCSC) + ';' + '\n' \
				+ tri_pred_str_3 + '}' + '\n' + '\n' \
				+ tri_pred_str_3 + 'cellSizeFunction' + tri_pred_str_1 + cSF + ';' + '\n' \
				+ tri_pred_str_3 + 'linearDistanceCoeffs' + '\n' + tri_pred_str_3 + '{' + '\n' \
				+ tri_pred_str_4 + 'distanceCellSizeCoeff' + tri_pred_str_1 + str(dCSC) + ';' + '\n' \
				+ tri_pred_str_4 + 'distanceCoeff' + tri_pred_str_1 + str(dC) + ';' + '\n' + tri_pred_str_3 + '}' + '\n' \
				

			sC_itog_5 = mC_sCF_prs_pred + mC_sCF_prs_itog + mC_sCF_prs_post
					
			sC_itog_6 = tri_pred_str_1 + 'objOutput' + tri_pred_str_1 + oO + ';' + '\n' + '\n'
			sC_itog_7 = tri_pred_str_1 + 'timeChecks' + tri_pred_str_1 + tC + ';' + '\n' + '\n'
			
			motionControl_itog = sC_itog_1 + sC_itog_2 + sC_itog_3 + sC_itog_4 + sC_itog_5 + sC_itog_6 + sC_itog_7
			
			motionControl_post_str = '}' + '\n' + '\n' + '\n'

			motionControl_bl = motionControl_pred_str + motionControl_itog + motionControl_post_str			
		
		##polyMeshFiltering
		if os.path.exists(polyMeshFiltering_path):
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '
			polyMeshFiltering_bl = 'polyMeshFiltering' + '\n' + '{'	+ '\n' \
			+ tri_pred_str_1 + 'filterEdges' + tri_pred_str_2 + ' ' + polyMeshFiltering_obj['fE'] + ';' + '\n' \
			+ tri_pred_str_1 + 'filterFaces' + tri_pred_str_2 + ' ' + polyMeshFiltering_obj['fF'] + ';' + '\n' \
			+ tri_pred_str_1 + 'writeTetDualMesh' + tri_pred_str_1 + polyMeshFiltering_obj['wTDM'] + ';' + '\n' \
			+ '}' + '\n' + '\n'
			
		meshQualityControls_bl = 'meshQualityControls' + '\n' + '{' + '\n' \
		+ tri_pred_str_1 + '#include "meshQualityDict"' + '\n' + '}' + '\n'
			
			
		#########################################################################
		  			#Сохраняем файл при наличии различных опций#
		#########################################################################
		
		if not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and not None in surfaceConformation_vkl_arr and not None in initialPoints_vkl_arr \
		and not None in motionControl_vkl_arr and not None in polyMeshFiltering_vkl_arr:
			shutil.copyfile(r'./matches/foamyHexMeshDict', prj_path + r'/foamyHexMeshDict')
			fHMD = open(prj_path + '/foamyHexMeshDict', 'a')

			fHMD.write(geometry_bl + surfaceConformation_bl + initialPoints_bl + motionControl_bl + polyMeshFiltering_bl + meshQualityControls_bl)
			fHMD.close()
			
			foamyHexMeshDict_end(int_lng, prj_path, parn)
		
						
#########################################################################################################################		
#########################################################################################################################		
#########################################################################################################################