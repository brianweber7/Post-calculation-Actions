'''
Created by: Brian Weber
Project: 1601 DOF Dynamic Lowering Analysis
Date Created: 1/8/2015

Description: This script is to be used to perform post-calculation 
actions in Orcaflex after a statics or dynamics simulation has finished
running.
'''


import os
import re
import numpy as np


def Execute(info):
	# Set line variables in the model, i.e. nameOfVariable = info.model['objectName']
	LowerSling_1 = info.model['LowerSling-1']
	LowerSling_2 = info.model['LowerSling-2']
	LowerSling_3 = info.model['LowerSling-3']
	LowerSling_4 = info.model['LowerSling-4']
	UpperSling_1 = info.model['UpperSling-1']
	UpperSling_2 = info.model['UpperSling-2']
	CraneWire = info.model['Crane Wire']

	# Set plate variables in the model
	Plate_1 = info.model['Plate-1']
	Plate_2 = info.model['Plate-2']
	Plate_3 = info.model['Plate-3']
	Plate_4 = info.model['Plate-4']
	Plate_5 = info.model['Plate-5']
	Plate_6 = info.model['Plate-6']
	Plate_7 = info.model['Plate-7']
	Plate_8 = info.model['Plate-8']
	Plate_9 = info.model['Plate-9']
	Plate_10 = info.model['Plate-10']

	#### Specify results desired ####
	## Line tension results ##
	# Example ---->  nameOfVariable.RangeGraph('variableName', period, objectExtra)
	# Example ---->  nameOfVariable.TimeHistory('variableName', period, objectExtra)
	LowerSling_1_Tension = LowerSling_1.RangeGraph('Effective Tension', 1)
	LowerSling_2_Tension = LowerSling_2.RangeGraph('Effective Tension', 1)
	LowerSling_3_Tension = LowerSling_3.RangeGraph('Effective Tension', 1)
	LowerSling_4_Tension = LowerSling_4.RangeGraph('Effective Tension', 1)
	UpperSling_1_Tension = UpperSling_1.RangeGraph('Effective Tension', 1)
	UpperSling_2_Tension = UpperSling_2.RangeGraph('Effective Tension', 1)
	CraneWire_Tension = CraneWire.RangeGraph('Effective Tension', 1, objectExtra=OrcFxAPI.oeEndA)
	# Maximum tensions
	LowerSling_1_MaxTension = max(LowerSling_1_Tension.Max)
	LowerSling_2_MaxTension = max(LowerSling_2_Tension.Max)
	LowerSling_3_MaxTension = max(LowerSling_3_Tension.Max)
	LowerSling_4_MaxTension = max(LowerSling_4_Tension.Max)
	UpperSling_1_MaxTension = max(UpperSling_1_Tension.Max)
	UpperSling_2_MaxTension = max(UpperSling_2_Tension.Max)
	CraneWire_Tension_Max = max(CraneWire_Tension.Max)
	# Minimum tensions
	LowerSling_1_MinTension = min(LowerSling_1_Tension.Min)
	LowerSling_2_MinTension = min(LowerSling_2_Tension.Min)
	LowerSling_3_MinTension = min(LowerSling_3_Tension.Min)
	LowerSling_4_MinTension = min(LowerSling_4_Tension.Min)
	UpperSling_1_MinTension = min(UpperSling_1_Tension.Min)
	UpperSling_2_MinTension = min(UpperSling_2_Tension.Min)
	CraneWire_Tension_Min = min(CraneWire_Tension.Min)

	## Spreader bar load calculation ##
	LowerSling_1_angle = LowerSling_1.TimeHistory('End Force Declination', 1, objectExtra=OrcFxAPI.oeEndB)
	LowerSling_2_angle = LowerSling_2.TimeHistory('End Force Declination', 1, objectExtra=OrcFxAPI.oeEndB)
	LowerSling_3_angle = LowerSling_3.TimeHistory('End Force Declination', 1, objectExtra=OrcFxAPI.oeEndB)
	LowerSling_4_angle = LowerSling_4.TimeHistory('End Force Declination', 1, objectExtra=OrcFxAPI.oeEndB)
	LowerSling_1_Tension_SB = LowerSling_1.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeEndB)
	LowerSling_2_Tension_SB = LowerSling_2.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeEndB)
	LowerSling_3_Tension_SB = LowerSling_3.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeEndB)
	LowerSling_4_Tension_SB = LowerSling_4.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeEndB)

	SpreadBar_Tension = LowerSling_1_Tension_SB * np.sin(np.radians(180 - LowerSling_1_angle)) + \
	LowerSling_2_Tension_SB * np.sin(np.radians(90 - LowerSling_2_angle)) + \
	LowerSling_3_Tension_SB * np.sin(np.radians(90 - LowerSling_3_angle)) + \
	LowerSling_4_Tension_SB * np.sin(np.radians(90 - LowerSling_4_angle))

	SpreadBar_MaxTension = max(SpreadBar_Tension)
	SpreadBar_MinTension = min(SpreadBar_Tension)

	## Plate slamming results ##
	Plate_1_SF = Plate_1.TimeHistory('Slam Force', 1)
	Plate_2_SF = Plate_2.TimeHistory('Slam Force', 1)
	Plate_3_SF = Plate_3.TimeHistory('Slam Force', 1)
	Plate_4_SF = Plate_4.TimeHistory('Slam Force', 1)
	Plate_5_SF = Plate_5.TimeHistory('Slam Force', 1)
	Plate_6_SF = Plate_6.TimeHistory('Slam Force', 1)
	Plate_7_SF = Plate_7.TimeHistory('Slam Force', 1)
	Plate_8_SF = Plate_8.TimeHistory('Slam Force', 1)
	Plate_9_SF = Plate_9.TimeHistory('Slam Force', 1)
	Plate_10_SF = Plate_10.TimeHistory('Slam Force', 1)
	# Maximum slamming forces
	Plate_1_MaxSF = max(Plate_1_SF)
	Plate_2_MaxSF = max(Plate_2_SF)
	Plate_3_MaxSF = max(Plate_3_SF)
	Plate_4_MaxSF = max(Plate_4_SF)
	Plate_5_MaxSF = max(Plate_5_SF)
	Plate_6_MaxSF = max(Plate_6_SF)
	Plate_7_MaxSF = max(Plate_7_SF)
	Plate_8_MaxSF = max(Plate_8_SF)
	Plate_9_MaxSF = max(Plate_9_SF)
	Plate_10_MaxSF = max(Plate_10_SF)

	#### Output results to a text file ####
	outputFileName = os.path.splitext(info.modelFileName)[0] + '.txt'
	with open(outputFileName, 'w') as f:
		f.write('MaxLS-1, MaxLS-2, MaxLS-3, MaxLS-4, MaxSB, MaxUS-1, MaxUS-2, MaxCW, MinLS-1, MinLS-2, MinLS-3, MinLS-4, MinSB, MinUS-1, MinUS-2, MinCW\n')
		f.write('{:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}\n'\
			.format(LowerSling_1_MaxTension, LowerSling_2_MaxTension, LowerSling_3_MaxTension, LowerSling_4_MaxTension, SpreadBar_MaxTension, UpperSling_1_MaxTension, \
			UpperSling_2_MaxTension, CraneWire_Tension_Max, LowerSling_1_MinTension, LowerSling_2_MinTension, LowerSling_3_MinTension, LowerSling_4_MinTension, \
			SpreadBar_MinTension, UpperSling_1_MinTension, UpperSling_2_MinTension, CraneWire_Tension_Min
			))
		f.write('SF-Plate-1, SF-Plate-2, SF-Plate-3, SF-Plate-4, SF-Plate-5, SF-Plate-6, SF-Plate-7, SF-Plate-8, SF-Plate-9, SF-Plate-10\n')
		f.write('{:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f}'.format(Plate_1_MaxSF, Plate_2_MaxSF, Plate_3_MaxSF, \
			Plate_4_MaxSF, Plate_5_MaxSF, Plate_6_MaxSF, Plate_7_MaxSF, Plate_8_MaxSF, Plate_9_MaxSF, Plate_10_MaxSF))







