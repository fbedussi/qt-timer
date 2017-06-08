#!/usr/bin/python

import sys
import threading

from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Timer')
        cWidget = QtGui.QWidget(self)

        vBox = QtGui.QVBoxLayout()
        vBox.setSpacing(2)

        # startLabel = QtGui.QLabel('Start time', cWidget)
        # vBox.addWidget(startLabel)

        # self.inputNumber = QtGui.QSpinBox(cWidget)
        # vBox.addWidget(self.inputNumber)

        timeLabel = QtGui.QLabel('Time', cWidget)
        vBox.addWidget(timeLabel)
        self.clockDisplay = QtGui.QLabel('0:00', cWidget)
        self.clockDisplay.setFont(QtGui.QFont('SansSerif', 20))
        vBox.addWidget(self.clockDisplay)

        buttonContainer = QtGui.QHBoxLayout()
        buttonContainer.setSpacing(10)
        vBox.addLayout(buttonContainer)

        self.startBtn = QtGui.QPushButton('Start', cWidget)
        self.startBtn.clicked.connect(self.start)
        buttonContainer.addWidget(self.startBtn)

        self.stopBtn = QtGui.QPushButton('Stop', cWidget)
        self.stopBtn.clicked.connect(self.stop)
        buttonContainer.addWidget(self.stopBtn)

        self.resetBtn = QtGui.QPushButton('Reset', cWidget)
        self.resetBtn.clicked.connect(self.reset)
        buttonContainer.addWidget(self.resetBtn)

        cWidget.setLayout(vBox)
        self.setCentralWidget(cWidget)

        self.s = 0
        self.m = 0
        self.clock = None
        self.mode = 'chrono'

    def reset(self, checked):
        self.stop(self)
        self.s = 0
        self.m = 0
        #self.inputNumber.setValue(0)
        self.clockDisplay.setText('0:00')

    def updateClock(self):
            self.s += 1
            if self.s == 60:
                self.m += 1
                self.s = 0

            txt = str(self.m) + ':' + str(self.s).zfill(2)
            self.clockDisplay.setText(txt)
            self.clock = threading.Timer(1, self.updateClock)
            self.clock.start()

    def start(self, checked):
        print('start')
        # self. = self.inputNumber.value()
        # if self.m > 

        self.clock = threading.Timer(1, self.updateClock)
        self.clock.start()
    
    def stop(self, checked):
        print('stop')

        self.clock.cancel()
        


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
