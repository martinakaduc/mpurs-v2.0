import loadData
import pickle
import constant
from sklearn.ensemble import RandomForestRegressor

regressorModel = {}

for subject in constant.SUBJECT_NAME:
    regressorModel[subject] = RandomForestRegressor(max_depth=50, random_state=0)
    regressorModel[subject].fit([[x] for x in loadData.X[subject]], loadData.y[subject])
    pickle.dump(regressorModel[subject], open(constant.MODEL_DIR+subject+'.sav', 'wb'))

print("All models were completely trained!")
