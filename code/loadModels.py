import os
import pickle
import constant

predictMarkModel = {}

for subjectName in constant.SUBJECT_NAME:
    if not os.path.exists(constant.MODEL_DIR+subjectName+'.sav'):
        os.system('python3 trainModel.py')
        break

for subjectName in constant.SUBJECT_NAME:
    predictMarkModel[subjectName] = pickle.load(open(constant.MODEL_DIR+subjectName+'.sav', 'rb'))
