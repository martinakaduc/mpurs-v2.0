from loadData import *
import pickle
import numpy as np
from constant import *
#đưa vào randomforestregressor
from sklearn.ensemble import RandomForestRegressor
regr_toan = RandomForestRegressor(max_depth=50, random_state=0)
regr_ly = RandomForestRegressor(max_depth=40, random_state=0)
regr_hoa = RandomForestRegressor(max_depth=40, random_state=0)
regr_sinh = RandomForestRegressor(max_depth=40, random_state=0)
regr_van = RandomForestRegressor(max_depth=40, random_state=0)
regr_su = RandomForestRegressor(max_depth=40, random_state=0)
regr_dia = RandomForestRegressor(max_depth=40, random_state=0)
regr_ngoaingu = RandomForestRegressor(max_depth=50, random_state=0)
regr_gdcd = RandomForestRegressor(max_depth=40, random_state=0)

regr_toan.fit(x_toan_train.reshape(-1,1), y_toan_train)
regr_ly.fit(x_ly_train.reshape(-1,1), y_ly_train)
regr_hoa.fit(x_hoa_train.reshape(-1,1), y_hoa_train)
regr_sinh.fit(x_sinh_train.reshape(-1,1), y_sinh_train)
regr_van.fit(x_van_train.reshape(-1,1), y_van_train)
regr_su.fit(x_su_train.reshape(-1,1), y_su_train)
regr_dia.fit(x_dia_train.reshape(-1,1), y_dia_train)
regr_van.fit(x_van_train.reshape(-1,1), y_van_train)
regr_ngoaingu.fit(x_ngoaingu_train.reshape(-1,1), y_ngoaingu_train)
regr_gdcd.fit(x_gdcd_train.reshape(-1,1), y_gdcd_train)

pickle.dump(regr_toan, open(MODEL_TOAN, 'wb'))
pickle.dump(regr_ly, open(MODEL_LY, 'wb'))
pickle.dump(regr_hoa, open(MODEL_HOA, 'wb'))
pickle.dump(regr_sinh, open(MODEL_SINH, 'wb'))
pickle.dump(regr_van, open(MODEL_VAN, 'wb'))
pickle.dump(regr_su, open(MODEL_SU, 'wb'))
pickle.dump(regr_dia, open(MODEL_DIA, 'wb'))
pickle.dump(regr_ngoaingu, open(MODEL_NGOAINGU, 'wb'))
pickle.dump(regr_gdcd, open(MODEL_GDCD, 'wb'))

print("All models were completely trained!")
