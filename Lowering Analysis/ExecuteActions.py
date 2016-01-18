'''
Created by: Brian Weber
Date Created: 1/8/2015

Description: This script is to be used to debug post-calculation 
actions in Orcaflex after a statics or dynamics simulation has finished
running. Note that the filenames need to be passed as arguments when
the script is executed in the commandline like so:

python ExecuteActions.py SimFile1.sim SimFile2.sim
'''

import sys
import OrcFxAPI


for file in sys.argv[1:]:
	model = OrcFxAPI.Model(file)
	model.ExecutePostCalculationActions(file, OrcFxAPI.atInProcPython)
