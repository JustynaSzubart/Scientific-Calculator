# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import math # to result trigonometric functions


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 0, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.percentage_it())
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(275, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plusminus())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.result_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.sinButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.sin_it())
        self.sinButton.setGeometry(QtCore.QRect(360, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sinButton.setFont(font)
        self.sinButton.setObjectName("sinButton")
        self.cosButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.cos_it())
        self.cosButton.setGeometry(QtCore.QRect(360, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cosButton.setFont(font)
        self.cosButton.setObjectName("cosButton")
        self.tangensButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.tangens_it())
        self.tangensButton.setGeometry(QtCore.QRect(360, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.tangensButton.setFont(font)
        self.tangensButton.setObjectName("tangensButton")
        self.ctangensButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.ctangens_it())
        self.ctangensButton.setGeometry(QtCore.QRect(360, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ctangensButton.setFont(font)
        self.ctangensButton.setObjectName("ctangensButton")
        self.rootButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.root_it())
        self.rootButton.setGeometry(QtCore.QRect(360, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.rootButton.setFont(font)
        self.rootButton.setObjectName("rootButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        #Make a result - EQUAL BUTTON "="

    def result_it(self):
        screen = self.outputLabel.text()
        try:
            #Evaluate result
            answer = eval(screen)
            #Output answer to the screen
            self.output.Label.setText(str(answer))
        except:
            #Output error to the screen
            self.output.Label.setText(str("ERROR"))

        #Change from negative/positive - PLUS_MINUS BUTTON "+/-"
    def plus_minus_it(self):
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        else:
            self.outputLabel.setText(f'-{screen}')

        #Create define remove function - ARROW BUTTON "<<"
    def remove_it(self):
        #Grab what's on the screen already
        screen = self.outputLabel.text()
        #Remove last item in list/string
        screen = screen[:-1]
        #Remove output back to the screen
        self.outputLabel.setText(screen)

        #Create define decimal function - DECIMAL BUTTON "."
    def dot_it(self):
        screen = self.outputLabel.text()
        
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')
    


        #Create define click-control function - C BUTTON "C"
    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0") # delete all, change outputLabel to '0'
        else:
            #Check to see if starts with 0 and delete 0
            if self.outputLabel.text() == "0":
               self.outputLabel.setText("")
            #concatenate teh pressed button with what was there already
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}') 
            
            
        #Create define percent function - PERCENT BUTTON "%"
    def percentage_it(self):
        if screen[-1] == "%":
            pass
        else:
            percentages = screen/100
        self.outputLabel.setText(float(percentages))

        #Create define sinus function - SINUS BUTTON "sinx"
   
   def sin_it(self):
        if screen[-1] == "sinx":
            pass
        else:
            sinus = math.sin(screen)
        self.outputLabel.setText(float(sinus))
        
        #Create define cosinus function - COSINUS BUTTON "cosx"
        
    def cos_it(self):
        if screen[-1] == "cosx":
            pass
    else:
            cosinus = math.cos(screen)
        self.outputLabel.setText(float(cosinus))

        #Create define tangens function - TANGENS BUTTON "tgx"
    def tangens_it(self):
        if screen[-1] == "tgx"
            pass
    else:
            tangens = math.tan(screen)
        self.outputLabel.setText(float(tangens))
        
        #Create define cotangens function - COTANGENS BUTTON "ctgx"
    def ctangens_it(self):
        if screen[-1] == "ctgx"
            pass
    else:
            cotangens = math.cot(screen)
        self.outputLabel.setText(float(cotangens))
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scientific Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.multiplyButton.setText(_translate("MainWindow", "X"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.sinButton.setText(_translate("MainWindow", "sinx"))
        self.cosButton.setText(_translate("MainWindow", "cosx"))
        self.tangensButton.setText(_translate("MainWindow", "tgx"))
        self.ctangensButton.setText(_translate("MainWindow", "ctgx"))
        self.rootButton.setText(_translate("MainWindow", "root"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
