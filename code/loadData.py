import xlrd
import numpy as np
import constant

dataOfficial = xlrd.open_workbook(constant.DATA_OFFICAL)
dataOfficialSheet = dataOfficial.sheet_by_index(0)

diemchuanOfficial = xlrd.open_workbook(constant.DIEMCHUAN_OFFICAL)
diemchuanOfficialSheet = diemchuanOfficial.sheet_by_index(0)

# print ("So dong:")
# print (dataOfficialSheet.nrows)
# print ("\nSo cot:")
# print (dataOfficialSheet.ncols)
x_toan_train=np.zeros(dataOfficialSheet.nrows-1)#dữ liệu x, là điểm tổng kết
x_ly_train=np.zeros(dataOfficialSheet.nrows-1)
x_hoa_train=np.zeros(dataOfficialSheet.nrows-1)
x_sinh_train=np.zeros(dataOfficialSheet.nrows-1)
x_van_train=np.zeros(dataOfficialSheet.nrows-1)
x_su_train=np.zeros(dataOfficialSheet.nrows-1)
x_dia_train=np.zeros(dataOfficialSheet.nrows-1)
x_ngoaingu_train=np.zeros(dataOfficialSheet.nrows-1)
x_gdcd_train=np.zeros(dataOfficialSheet.nrows-1)

y_toan_train=np.zeros(dataOfficialSheet.nrows-1)#dữ liệu y, là điểm thi Tốt nghiệp
y_ly_train=np.zeros(dataOfficialSheet.nrows-1)
y_hoa_train=np.zeros(dataOfficialSheet.nrows-1)
y_sinh_train=np.zeros(dataOfficialSheet.nrows-1)
y_van_train=np.zeros(dataOfficialSheet.nrows-1)
y_su_train=np.zeros(dataOfficialSheet.nrows-1)
y_dia_train=np.zeros(dataOfficialSheet.nrows-1)
y_ngoaingu_train=np.zeros(dataOfficialSheet.nrows-1)
y_gdcd_train=np.zeros(dataOfficialSheet.nrows-1)

#đọc và chia dữ liệu train test cho 9 môn thi
# print ("\nCac gia tri trong cot :")
for x in range(dataOfficialSheet.ncols):
    # print ("\n")
    for rows in range(dataOfficialSheet.nrows):
        if x==0 and rows>=1:
            x_toan_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==1 and rows>=1:
            x_ly_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==2 and rows>=1:
            x_hoa_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==3 and rows>=1:
            x_sinh_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==4 and rows>=1:
            x_van_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==5 and rows>=1:
            x_su_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==6 and rows>=1:
            x_dia_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==7 and rows>=1:
            x_ngoaingu_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==8 and rows>=1:
            x_gdcd_train[rows-1]=dataOfficialSheet.cell_value(rows, x)

        if x==12 and rows>=1:
            y_toan_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==13 and rows>=1:
            y_ly_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==14 and rows>=1:
            y_hoa_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==15 and rows>=1:
            y_sinh_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==16 and rows>=1:
            y_van_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==17 and rows>=1:
            y_su_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==18 and rows>=1:
            y_dia_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==19 and rows>=1:
            y_ngoaingu_train[rows-1]=dataOfficialSheet.cell_value(rows, x)
        if x==20 and rows>=1:
            y_gdcd_train[rows-1]=dataOfficialSheet.cell_value(rows, x)

print("Successfully loading data!")
