import xlrd
import numpy as np
import constant
from sklearn.model_selection import train_test_split

diemchuanOfficial = xlrd.open_workbook(constant.DIEMCHUAN_OFFICAL)
diemchuanOfficialSheet = diemchuanOfficial.sheet_by_index(0)

diemThiTn = {}
diemThiTnSheet = {}
diemThiTnList = {}
soDiemTongKet= {}
soDiemTongKetSheet = {}
soDiemTongKetList = {}
X = {}
y = {}

# Init X and y
for subject in constant.SUBJECT_NAME:
    X[subject] = []
    y[subject] = []

# Load excel files
for name in constant.SCHOOLS_NAME:
    soDiemTongKet[name] = xlrd.open_workbook(constant.SO_DIEM_TONG_KET[name])
    diemThiTn[name] = xlrd.open_workbook(constant.DIEM_THI_TN[name])

# Load excel sheets
for schoolName in constant.SCHOOLS_NAME:
    diemThiTnSheet[schoolName] = {}
    for sheetName in diemThiTn[schoolName].sheet_names():
        diemThiTnSheet[schoolName][sheetName] = diemThiTn[schoolName].sheet_by_name(sheetName)
        # print(diemThiTnSheet[schoolName][sheetName].cell(1, 1))

    soDiemTongKetSheet[schoolName] = {}
    for sheetName in soDiemTongKet[schoolName].sheet_names():
        soDiemTongKetSheet[schoolName][sheetName] = soDiemTongKet[schoolName].sheet_by_name(sheetName)

# Covert sheets to python lists
for schoolName in constant.SCHOOLS_NAME:
    diemThiTnList[schoolName] = {}
    for sheetName in diemThiTnSheet[schoolName]:
        diemThiTnList[schoolName][sheetName] = []
        for row in range(diemThiTnSheet[schoolName][sheetName].nrows):
            diemThiTnList[schoolName][sheetName].append([])
            for col in range(diemThiTnSheet[schoolName][sheetName].ncols):
                diemThiTnList[schoolName][sheetName][row].append(diemThiTnSheet[schoolName][sheetName].cell_value(row, col))

    soDiemTongKetList[schoolName] = {}
    for sheetName in soDiemTongKetSheet[schoolName]:
        soDiemTongKetList[schoolName][sheetName] = []
        for row in range(soDiemTongKetSheet[schoolName][sheetName].nrows):
            soDiemTongKetList[schoolName][sheetName].append([])
            for col in range(soDiemTongKetSheet[schoolName][sheetName].ncols):
                soDiemTongKetList[schoolName][sheetName][row].append(soDiemTongKetSheet[schoolName][sheetName].cell_value(row, col))
# print(diemThiTnList)

for schoolName in constant.SCHOOLS_NAME:
    for sheetName in diemThiTnList[schoolName]:
        for row in range(len(diemThiTnList[schoolName][sheetName]) - 1):
            # print("ROW: " +str(row))
            # print(soDiemTongKetList[schoolName][sheetName][row+1][1])
            studentName = diemThiTnList[schoolName][sheetName][row+1][1]
            subjectTnMark = {}
            for subject in constant.SUBJECT_NAME_TN_VI:
                subjectTnIndex = diemThiTnList[schoolName][sheetName][0].index(subject)
                subjectTnMark[subject] = diemThiTnList[schoolName][sheetName][row+1][subjectTnIndex]
            # print(subjectTnMark)
            for subject in constant.SUBJECT_NAME_TK_VI:
                studentIndex = [x[1] for x in soDiemTongKetList[schoolName][sheetName]].index(studentName)
                subjectTkIndex = soDiemTongKetList[schoolName][sheetName][0].index(subject)
                subjectMark = subjectTnMark[constant.SUBJECT_NAME_TN_VI[constant.SUBJECT_NAME_TK_VI.index(subject)]]
                if subjectMark != '':
                    index = constant.SUBJECT_NAME[constant.SUBJECT_NAME_TK_VI.index(subject)]
                    X[index].append(subjectMark)
                    y[index].append(soDiemTongKetList[schoolName][sheetName][studentIndex][subjectTkIndex])

X_train = {}
X_test = {}
y_train = {}
y_test = {}

for subject in constant.SUBJECT_NAME:
    X_train[subject], X_test[subject], y_train[subject], y_test[subject] = train_test_split(X[subject], y[subject], test_size=0.2,  random_state=42)
# print(X_test)
print("Successfully loading data!")
