import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from language_filtering import language_filtering
from apireader import c
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("title.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    url=""
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setupUI()
        #Textediter
        #self.urlreader.clicked.connect(self.printurl)
        self.btn_predict.clicked.connect(self.pre_start)

    def setupUI(self):
        self.datatable.setRowCount(len(c.c_comments))
        self.datatable.setColumnCount(2)


    def printurl(self):
        print(self.urlreader.toPlainText())

    def pre_start(self):
        c.n_page_token=" "
        self.url = self.urlreader.toPlainText()
        print(self.url)
        language_filtering("Korean",self.url)
        self.datatable.setRowCount(len(c.c_comments))
        self.setTableWidgetData()

    def setTableWidgetData(self):
        for i in range(0,len(c.c_comments)):
            self.datatable.setItem(i,1,QTableWidgetItem(c.c_comments[i]))
        self.datatable.resizeColumnsToContents()
        self.datatable.resizeRowsToContents()
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()