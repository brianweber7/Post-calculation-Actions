'''
Created by: Brian Weber
Project: 1442 SCR Global Analysis
Date Created: 1/18/2016

Description: This script is to be used to perform post-calculation 
actions in Orcaflex after a statics or dynamics simulation has finished
running.
'''


import os
import re
import numpy as np


def Execute(info):
	# Set variables in the model
	riser = info.model['Line1']

	# Constant variables
	OD = 8.625 # outer diameter in inches
	wt = 0.98 # wall thickness in inches
	ID = OD - 2 * wt # inner diameter in inches
	A = (np.pi / 4) * (OD**2 - ID**2) # cross-sectional area in inches^2
	I = (np.pi / 64) * (OD**4 - ID**4) # moment of inertia in inches^4
	y = OD / 2 # location of where equivalent tension is to be calculated


	#### Specify results desired ####
	## Line tension results ##
	# Hang-off area
	WallTensionHO = riser.TimeHistory('Wall Tension', 1, objectExtra=OrcFxAPI.oeArcLength(15))
	WallTensionHO_Max = max(WallTensionHO)
	EffectiveTensionHO = riser.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeArcLength(15))
	EffectiveTensionHO_Max = max(EffectiveTensionHO)
	BendMomentHO = riser.TimeHistory('Bend Moment', 1, objectExtra=OrcFxAPI.oeArcLength(15))
	BendMomentHO_Max = max(BendMomentHO)

	# Touchdown point
	WallTensionTD = riser.TimeHistory('Wall Tension', 1, objectExtra=OrcFxAPI.oeTouchdown)
	WallTensionTD_Max = max(WallTensionTD)
	EffectiveTensionTD = riser.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeTouchdown)
	EffectiveTensionTD_Max = max(EffectiveTensionTD)
	BendMomentTD = riser.TimeHistory('Bend Moment', 1, objectExtra=OrcFxAPI.oeTouchdown)
	BendMomentTD_Max = max(BendMomentTD)

	# Bouyancy module area
	if riser.EndADeclination == 167.5:
		EffectiveTensionBS = riser.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5100))
		WallTensionBS = riser.TimeHistory('Wall Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5100))
		BendMomentBS = riser.TimeHistory('Bend Moment', 1, objectExtra=OrcFxAPI.oeArcLength(5100))
		riserAPIRP2RD_BS_Max = max(riser.TimeHistory('API RP 2RD Utilisation', 1, objectExtra=OrcFxAPI.oeArcLength(5100)))
		riserAPISTD2RD_BS_Max = max(riser.TimeHistory('API STD 2RD Method 1', 1, objectExtra=OrcFxAPI.oeArcLength(5100)))
	elif riser.EndADeclination == 170:
		EffectiveTensionBS = riser.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5250))
		WallTensionBS = riser.TimeHistory('Wall Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5250))
		BendMomentBS = riser.TimeHistory('Bend Moment', 1, objectExtra=OrcFxAPI.oeArcLength(5250))
		riserAPIRP2RD_BS_Max = max(riser.TimeHistory('API RP 2RD Utilisation', 1, objectExtra=OrcFxAPI.oeArcLength(5250)))
		riserAPISTD2RD_BS_Max = max(riser.TimeHistory('API STD 2RD Method 1', 1, objectExtra=OrcFxAPI.oeArcLength(5250)))
	elif riser.EndADeclination == 171:
		EffectiveTensionBS = riser.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5300))
		WallTensionBS = riser.TimeHistory('Wall Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5300))
		BendMomentBS = riser.TimeHistory('Bend Moment', 1, objectExtra=OrcFxAPI.oeArcLength(5300))
		riserAPIRP2RD_BS_Max = max(riser.TimeHistory('API RP 2RD Utilisation', 1, objectExtra=OrcFxAPI.oeArcLength(5300)))
		riserAPISTD2RD_BS_Max = max(riser.TimeHistory('API STD 2RD Method 1', 1, objectExtra=OrcFxAPI.oeArcLength(5300)))
	elif riser.EndADeclination == 172:
		EffectiveTensionBS = riser.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5300))
		WallTensionBS = riser.TimeHistory('Wall Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5300))
		BendMomentBS = riser.TimeHistory('Bend Moment', 1, objectExtra=OrcFxAPI.oeArcLength(5300))
		riserAPIRP2RD_BS_Max = max(riser.TimeHistory('API RP 2RD Utilisation', 1, objectExtra=OrcFxAPI.oeArcLength(5300)))
		riserAPISTD2RD_BS_Max = max(riser.TimeHistory('API STD 2RD Method 1', 1, objectExtra=OrcFxAPI.oeArcLength(5300)))
	elif riser.EndADeclination == 173:
		EffectiveTensionBS = riser.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5300))
		WallTensionBS = riser.TimeHistory('Wall Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5300))
		BendMomentBS = riser.TimeHistory('Bend Moment', 1, objectExtra=OrcFxAPI.oeArcLength(5300))
		riserAPIRP2RD_BS_Max = max(riser.TimeHistory('API RP 2RD Utilisation', 1, objectExtra=OrcFxAPI.oeArcLength(5300)))
		riserAPISTD2RD_BS_Max = max(riser.TimeHistory('API STD 2RD Method 1', 1, objectExtra=OrcFxAPI.oeArcLength(5300)))
	elif riser.EndADeclination == 174:
		EffectiveTensionBS = riser.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5350))
		WallTensionBS = riser.TimeHistory('Wall Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5350))
		BendMomentBS = riser.TimeHistory('Bend Moment', 1, objectExtra=OrcFxAPI.oeArcLength(5350))
		riserAPIRP2RD_BS_Max = max(riser.TimeHistory('API RP 2RD Utilisation', 1, objectExtra=OrcFxAPI.oeArcLength(5350)))
		riserAPISTD2RD_BS_Max = max(riser.TimeHistory('API STD 2RD Method 1', 1, objectExtra=OrcFxAPI.oeArcLength(5350)))
	elif riser.EndADeclination == 175:
		EffectiveTensionBS = riser.TimeHistory('Effective Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5400))
		WallTensionBS = riser.TimeHistory('Wall Tension', 1, objectExtra=OrcFxAPI.oeArcLength(5400))
		BendMomentBS = riser.TimeHistory('Bend Moment', 1, objectExtra=OrcFxAPI.oeArcLength(5400))
		riserAPIRP2RD_BS_Max = max(riser.TimeHistory('API RP 2RD Utilisation', 1, objectExtra=OrcFxAPI.oeArcLength(5400)))
		riserAPISTD2RD_BS_Max = max(riser.TimeHistory('API STD 2RD Method 1', 1, objectExtra=OrcFxAPI.oeArcLength(5400)))

	EffectiveTensionBS_Max = max(EffectiveTensionBS)
	WallTensionBS_Max = max(WallTensionBS)
	BendMomentBS_Max = max(BendMomentBS)

	## Calculate equivalent tensions ##
	Teq_HO = WallTensionHO + ((BendMomentHO * 12 * y) / I) * A
	Teq_HO_Max = max(Teq_HO)
	Teq_BS = WallTensionBS + ((BendMomentBS * 12 * y) / I) * A
	Teq_BS_Max = max(Teq_BS)
	Teq_TD = WallTensionTD + ((BendMomentTD * 12 * y) / I) * A
	Teq_TD_Max = max(Teq_TD)

	## Calculate unity checks ##
	# API RP 2RD
	riserAPIRP2RD_HO_Max = max(riser.TimeHistory('API RP 2RD Utilisation', 1, objectExtra=OrcFxAPI.oeArcLength(15)))
	riserAPIRP2RD_TD_Max = max(riser.TimeHistory('API RP 2RD Utilisation', 1, objectExtra=OrcFxAPI.oeTouchdown))
	# API STD 2RD Method 1
	riserAPISTD2RD_HO_Max = max(riser.TimeHistory('API STD 2RD Method 1', 1, objectExtra=OrcFxAPI.oeArcLength(15)))
	riserAPISTD2RD_TD_Max = max(riser.TimeHistory('API STD 2RD Method 1', 1, objectExtra=OrcFxAPI.oeTouchdown))


	#### Output results to a text file ####
	outputFileName = os.path.splitext(info.modelFileName)[0] + '.txt'
	with open(outputFileName, 'w') as f:
		f.write('MaxWT-HO, Max-ET-HO, Max-BM-HO, Max-EqT-HO, Max-WT-BS, Max-ET-BS, Max-BM-BS, Max-EqT-BS, Max-WT-TD, Max-ET-TD, Max-BM-TD, Max-EqT-TD, API-STD-HO, API-STD-BS-API-STD-TD, API-2RD-HO, API-2RD-BS, API-2RD-TD\n')
		f.write('{:6.2f}, {:6.2f}, {:6.2f}, {:6.2f}, {:6.2f}, {:6.2f}, {:6.2f}, {:6.2f}, {:6.2f}, {:6.2f}, {:6.2f}, {:6.2f}, {:6.3f}, {:6.3f}, {:6.3f}, {:6.3f}, {:6.3f}, {:6.3f}\n'\
			.format(WallTensionHO_Max, EffectiveTensionHO_Max, BendMomentHO_Max, Teq_HO_Max, WallTensionBS_Max, EffectiveTensionBS_Max, BendMomentBS_Max, Teq_BS_Max, WallTensionTD_Max, \
			EffectiveTensionTD_Max, BendMomentTD_Max, Teq_TD_Max, riserAPISTD2RD_HO_Max, riserAPISTD2RD_BS_Max, riserAPISTD2RD_TD_Max, riserAPIRP2RD_HO_Max, riserAPIRP2RD_BS_Max, riserAPIRP2RD_TD_Max))

