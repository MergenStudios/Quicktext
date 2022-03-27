from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QWidget(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 60))
        self.top_bar.setStyleSheet("background-color: rgb(52, 56, 60)")
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.top_bar)
        self.frame.setMinimumSize(QtCore.QSize(80, 60))
        self.frame.setMaximumSize(QtCore.QSize(80, 60))
        self.frame.setStyleSheet("background-color:rgb(30, 34, 38);\n"
                                                       "border: 0px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2.addWidget(self.frame)
        self.header_bar = QtWidgets.QFrame(self.top_bar)
        self.header_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_bar.setObjectName("header_bar")
        self.horizontalLayout_2.addWidget(self.header_bar)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QWidget(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        
        self.header_bar.mouseMoveEvent = self.moveWindow

        #*************************************************************************************************************************************************************
        self.header_bar.mousePressEvent = self.mousePress
        #*************************************************************************************************************************************************************

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    #*************************************************************************************************************************************************************
    def mousePress(self, event):
        MainWindow.dragPos = MainWindow.pos()
        self.mouse_original_pos = MainWindow.mapToGlobal(event.pos())
    #*************************************************************************************************************************************************************

    def moveWindow(self, event):
        if MainWindow.isMaximized():
            MainWindow.showNormal()
        else:
            if event.buttons() == Qt.LeftButton:
                #******************************************************************************************************************************************************
                MainWindow_last_pos = MainWindow.dragPos + MainWindow.mapToGlobal(event.pos()) - self.mouse_original_pos
                MainWindow.move(MainWindow_last_pos)
                event.accept()
                #******************************************************************************************************************************************************


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowFlag(Qt.FramelessWindowHint)
    MainWindow.show()
    sys.exit(app.exec_())