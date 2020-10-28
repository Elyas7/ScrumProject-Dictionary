# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class About(object):
    def __init__(self, window):
        self.window = window
    def home(self):
        self.window.hide()
        from mainpage import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
    def help(self):
        self.window.hide();
        from helppage import Help
        self.window = QtWidgets.QMainWindow()
        self.ui = Help(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QtCore.QSize(800, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("\n"
"background-color: rgb(148, 158, 145);\n"
"border: 0px solid;\n"
"color: white;\n"
"font-family: times new roman;\n"
"font-style: italic;\n"
"")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    font-family: times new roman;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(148, 158, 145);\n"
"}\n"
"")
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)
        self.btn_page_1.clicked.connect(self.home)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    font-family: times new roman;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(148, 158, 145);\n"
"}")
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    font-family: times new roman;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(148, 158, 145);\n"
"}")
        self.btn_page_3.setObjectName("btn_page_3")
        self.btn_page_3.clicked.connect(self.help)
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 601, 51))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 18px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(0, 80, 391, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 15px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(-10, 110, 311, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 15px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(-10, 140, 351, 21))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 15px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(0, 160, 291, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 15px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(0, 190, 321, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 15px;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(10, 220, 301, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 15px;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(400, 300, 301, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 15px;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(10, 20, 641, 131))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 641, 111))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 20px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 161, 51))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #FFF;\n"
"font-family: times new roman;\n"
"font-size: 20px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_Toggle.setText(_translate("MainWindow", "Dictionary"))
        self.btn_page_1.setText(_translate("MainWindow", "Home"))
        self.btn_page_2.setText(_translate("MainWindow", "About"))
        self.btn_page_3.setText(_translate("MainWindow", "Help"))
        self.label_2.setText(_translate("MainWindow", "This Dictionary is a project in software engineering class which is developed by:"))
        self.label_6.setText(_translate("MainWindow", "- Sayed Shabeer Hashimi (Shabeer.hashimi@auaf.edu.af)"))
        self.label_7.setText(_translate("MainWindow", "- Emal Ismail (emal.ismail@auaf.edu.af)"))
        self.label_8.setText(_translate("MainWindow", "- Zahra Stanikzai (zahra.stanikzai@auaf.edu.af)"))
        self.label_9.setText(_translate("MainWindow", "- Elyas Fekrat (elyas.fekrat@auaf.edu.af)"))
        self.label_10.setText(_translate("MainWindow", "- Rayhana Amiri (rayhana.amiri@auaf.edu.af)"))
        self.label_11.setText(_translate("MainWindow", "- Yousaf Sultani (yousaf.sultani@auaf.edu.af)"))
        self.label_12.setText(_translate("MainWindow", "Supervised by: Ali Rahman Shinwari"))
        self.label.setText(_translate("MainWindow", "Please insert the word you need to know the meaning and hit the search button."))
        self.label_4.setText(_translate("MainWindow", "If you faced any kind of issue, please contact us through the emails provide in "))
        self.label_5.setText(_translate("MainWindow", "the about section."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = About()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())