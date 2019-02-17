import numpy as np
from loadData import *
from loadModels import *

def round_quarter(x):
    return np.round(x*4)/4
def round_fifth(x):
    return np.round(x*4)/5

def predictMark(markDict):
    markPredictedDict = {}
    for subjectName in constant.SUBJECT_NAME:
        markPredictedDict[subjectName] = predictMarkModel[subjectName].predict(markDict[subjectName])
        if subjectName == 'toan' or subjectName == 'ngoaingu':
            markPredictedDict[subjectName] = round_fifth(markPredictedDict[subjectName]).tolist()[0]
        else:
            markPredictedDict[subjectName] = round_quarter(markPredictedDict[subjectName]).tolist()[0]
    return markPredictedDict

def calculateSubjectCombinationMark(markDict):
    calculatedMarkDict = {}
    calculatedMarkDict['A00'] = markDict['toan'] + markDict['ly'] + markDict['hoa']
    calculatedMarkDict['A01'] = markDict['toan'] + markDict['ly'] + markDict['ngoaingu']
    calculatedMarkDict['A02'] = markDict['toan'] + markDict['ly'] + markDict['sinh']
    calculatedMarkDict['B00'] = markDict['toan'] + markDict['hoa'] + markDict['sinh']
    calculatedMarkDict['C00'] = markDict['van'] + markDict['su'] + markDict['dia']
    calculatedMarkDict['D01'] = markDict['toan'] + markDict['van'] + markDict['ngoaingu']
    calculatedMarkDict['D07'] = markDict['toan'] + markDict['hoa'] + markDict['ngoaingu']
    calculatedMarkDict['D09'] = markDict['toan'] + markDict['su'] + markDict['ngoaingu']
    for key in calculatedMarkDict.keys():
        calculatedMarkDict[key] = round_quarter(calculatedMarkDict[key])
    return calculatedMarkDict

def findUniversities(subjectCombinationMark):
    universitiesList = []
    for column in range(diemchuanOfficialSheet.ncols):
        for row in range(diemchuanOfficialSheet.nrows):
            if row >= 1 and column == 2:
                for key in subjectCombinationMark.keys():
                    if diemchuanOfficialSheet.cell_value(row, column) == key and subjectCombinationMark[key] >= diemchuanOfficialSheet.cell_value(row, column+1):
                        universitiesList.append("Trường " + diemchuanOfficialSheet.cell_value(row,column-2) + " - Ngành " + diemchuanOfficialSheet.cell_value(row,column-1) + " - Khối " + str(key))
    return universitiesList
