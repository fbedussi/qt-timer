#!/usr/bin/python

import sys
import threading
import os.path as osp

path = osp.join(osp.dirname(sys.executable), 'timer-icon.ico')

from PyQt4 import QtGui

class Timer(QtGui.QMainWindow):
    """A simple timer/chronometer"""

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Timer')
        self.setWindowIcon(QtGui.QIcon(path))
        cWidget = QtGui.QWidget(self)
        self.setCentralWidget(cWidget)

        vBox = QtGui.QVBoxLayout()
        vBox.setSpacing(10)
        cWidget.setLayout(vBox)

        inputWrapper = QtGui.QHBoxLayout()
        inputWrapper.setSpacing(10)
        vBox.addLayout(inputWrapper)
        minWrapper = QtGui.QVBoxLayout()
        secWrapper = QtGui.QVBoxLayout()
        inputWrapper.addLayout(minWrapper)
        inputWrapper.addLayout(secWrapper)

        startMinLabel = QtGui.QLabel('Minutes', cWidget)
        minWrapper.addWidget(startMinLabel)
        self.startMin = QtGui.QSpinBox(cWidget)
        minWrapper.addWidget(self.startMin)

        startSecLabel = QtGui.QLabel('Seconds', cWidget)
        secWrapper.addWidget(startSecLabel)
        self.startSec = QtGui.QSpinBox(cWidget)
        secWrapper.addWidget(self.startSec)

        timeLabel = QtGui.QLabel('Time', cWidget)
        vBox.addWidget(timeLabel)
        self.clockDisplay = QtGui.QLabel('00:00', cWidget)
        self.clockDisplay.setFont(QtGui.QFont('SansSerif', 20))
        vBox.addWidget(self.clockDisplay)

        buttonContainer = QtGui.QHBoxLayout()
        buttonContainer.setSpacing(10)
        vBox.addLayout(buttonContainer)

        self.startBtn = QtGui.QPushButton('start', cWidget)
        self.startBtn.clicked.connect(self.toggle)
        buttonContainer.addWidget(self.startBtn)

        self.resetBtn = QtGui.QPushButton('reset', cWidget)
        self.resetBtn.clicked.connect(self.reset)
        buttonContainer.addWidget(self.resetBtn)

        self.s = 0
        self.clock = None
        self.mode = 'chrono'

    def reset(self):
        self.stop()
        self.s = 0
        self.mode = 'chrono'
        self.startMin.setValue(0)
        self.startSec.setValue(0)
        self.clockDisplay.setText('00:00')

    def updateClock(self):
        if self.mode == 'chrono':
            self.s += 1
        else:
            self.s -= 1

        m, s = divmod(self.s, 60)
        h, m = divmod(m, 60)
        txt = "%02d:%02d" % (m, s)
        if h > 0:
            txt = "%d:" % (h) + txt

        self.clockDisplay.setText(txt)
        self.clock = threading.Timer(1, self.updateClock)
        if self.s > 0:
            self.clock.start()

    def start(self):
        if self.startSec.value() != 0 or self.startMin.value() != 0:
            self.mode = 'timer'
            self.s = self.startMin.value() * 60 + self.startSec.value()

        print('start, mode: ', self.mode)
        self.startBtn.setText('stop')
        self.clock = threading.Timer(1, self.updateClock)
        self.clock.start()

    def stop(self):
        print('stop')
        self.startBtn.setText('start')
        if self.clock:
            self.clock.cancel()
            self.clock = None

    def toggle(self):
        if self.clock:
            self.stop()
        else:
            self.start()

app = QtGui.QApplication(sys.argv)
main = Timer()
main.show()
sys.exit(app.exec_())
