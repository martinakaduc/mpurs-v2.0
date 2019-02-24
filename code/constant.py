DATA_DIR = '../data/'
DIEMCHUAN_OFFICAL = DATA_DIR + "diemchuanOfficial.xlsx"
# SCHOOLS_NAME = ['NK', 'NQ', 'PL', 'PR']
SCHOOLS_NAME = ['NK', 'NQ', 'PL', 'PR']
DIEM_THI_TN = {}
SO_DIEM_TONG_KET = {}
for NAME in SCHOOLS_NAME:
    DIEM_THI_TN[NAME] = DATA_DIR + 'diem_tn_%s.xls' % NAME
    SO_DIEM_TONG_KET[NAME] = DATA_DIR + 'so_diem_tong_ket_khoi_khoi_12_%s.xls' % NAME

MODEL_DIR = '../models/'

SUBJECT_NAME = ['toan', 'ly', 'hoa', 'sinh', 'van', 'su', 'dia', 'ngoaingu', 'gdcd']
SUBJECT_NAME_TK_VI = ['Toán', 'Lí','Hóa', 'Sinh', 'Văn','Sử','Địa', 'Ng.ngữ','GDCD']
SUBJECT_NAME_TN_VI = ['Toán', 'Vật lí', 'Hóa học', 'Sinh học', 'Ngữ văn', 'Lịch sử', 'Địa lý', 'Ngoại ngữ', 'GDCD']

WEB_DIR = '../web/'
MAINPAGE_HTML = WEB_DIR + 'mainPage.html'
