import loadData
import pickle
import constant
from sklearn.ensemble import RandomForestRegressor
import numpy as np

regressorModel = {}

for subject in constant.SUBJECT_NAME:
    regressorModel[subject] = RandomForestRegressor(max_depth=50, random_state=0)
    regressorModel[subject].fit([[x] for x in loadData.X_train[subject]], loadData.y_train[subject])
    pickle.dump(regressorModel[subject], open(constant.MODEL_DIR+subject+'.sav', 'wb'))

print("All models were completely trained!")

def calRMSE(clf, testData, testLabel):
    sumError = 0
    for x in testData:
        sumError += (clf.predict([[x]]) - testLabel[testData.index(x)])**2
    return np.sqrt(sumError/len(testData))

for subject in constant.SUBJECT_NAME:
    rmse = calRMSE(regressorModel[subject], loadData.X_test[subject], loadData.y_test[subject])
    print("Model %s RMSE: %f" % (subject, rmse))
