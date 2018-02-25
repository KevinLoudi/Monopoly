# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_0_1.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from constant import *
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dice = QtWidgets.QLabel(self.centralwidget)
        self.dice.setGeometry(QtCore.QRect(160, 150, 81, 31))
        self.dice.setObjectName("dice")
        self.roll_dice = QtWidgets.QPushButton(self.centralwidget)
        self.roll_dice.setGeometry(QtCore.QRect(150, 190, 111, 51))
        self.roll_dice.setObjectName("roll_dice")
        self.go = QtWidgets.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(150, 260, 111, 51))
        self.go.setObjectName("go")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(320, 110, 371, 201))
        self.info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info.setObjectName("info")
        self.buy = QtWidgets.QPushButton(self.centralwidget)
        self.buy.setGeometry(QtCore.QRect(460, 340, 111, 51))
        self.buy.setObjectName("buy")
        self.skip_buy = QtWidgets.QPushButton(self.centralwidget)
        self.skip_buy.setGeometry(QtCore.QRect(590, 340, 111, 51))
        self.skip_buy.setObjectName("skip_buy")
        self.turn_token = QtWidgets.QComboBox(self.centralwidget)
        self.turn_token.setGeometry(QtCore.QRect(150, 100, 111, 21))
        self.turn_token.setObjectName("turn_token")
        self.turn_token.addItem("")
        self.turn_token.addItem("")
        self.Ground_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_1.setGeometry(QtCore.QRect(0, 0, 91, 81))
        self.Ground_1.setObjectName("Ground_1")
        self.Ground_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_2.setGeometry(QtCore.QRect(90, 0, 91, 81))
        self.Ground_2.setObjectName("Ground_2")
        self.Ground_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_3.setGeometry(QtCore.QRect(180, 0, 91, 81))
        self.Ground_3.setObjectName("Ground_3")
        self.Ground_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_4.setGeometry(QtCore.QRect(270, 0, 91, 81))
        self.Ground_4.setObjectName("Ground_4")
        self.Ground_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_5.setGeometry(QtCore.QRect(360, 0, 91, 81))
        self.Ground_5.setObjectName("Ground_5")
        self.Ground_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_6.setGeometry(QtCore.QRect(450, 0, 91, 81))
        self.Ground_6.setObjectName("Ground_6")
        self.Ground_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_7.setGeometry(QtCore.QRect(540, 0, 91, 81))
        self.Ground_7.setObjectName("Ground_7")
        self.Ground_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_8.setGeometry(QtCore.QRect(630, 0, 91, 81))
        self.Ground_8.setObjectName("Ground_8")
        self.Ground_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_9.setGeometry(QtCore.QRect(720, 0, 91, 81))
        self.Ground_9.setObjectName("Ground_9")
        self.Ground_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_10.setGeometry(QtCore.QRect(810, 0, 91, 81))
        self.Ground_10.setObjectName("Ground_10")
        self.Ground_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_11.setGeometry(QtCore.QRect(810, 80, 91, 81))
        self.Ground_11.setObjectName("Ground_11")
        self.Ground_12 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_12.setGeometry(QtCore.QRect(810, 160, 91, 81))
        self.Ground_12.setObjectName("Ground_12")
        self.Ground_13 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_13.setGeometry(QtCore.QRect(720, 160, 91, 81))
        self.Ground_13.setObjectName("Ground_13")
        self.Ground_14 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_14.setGeometry(QtCore.QRect(720, 240, 91, 81))
        self.Ground_14.setObjectName("Ground_14")
        self.Ground_15 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_15.setGeometry(QtCore.QRect(720, 320, 91, 81))
        self.Ground_15.setObjectName("Ground_15")
        self.Ground_16 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_16.setGeometry(QtCore.QRect(810, 320, 91, 81))
        self.Ground_16.setObjectName("Ground_16")
        self.Ground_17 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_17.setGeometry(QtCore.QRect(810, 400, 91, 81))
        self.Ground_17.setObjectName("Ground_17")
        self.Ground_18 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_18.setGeometry(QtCore.QRect(810, 480, 91, 81))
        self.Ground_18.setObjectName("Ground_18")
        self.Ground_19 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_19.setGeometry(QtCore.QRect(720, 480, 91, 81))
        self.Ground_19.setObjectName("Ground_19")
        self.Ground_20 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_20.setGeometry(QtCore.QRect(630, 480, 91, 81))
        self.Ground_20.setObjectName("Ground_20")
        self.Ground_21 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_21.setGeometry(QtCore.QRect(540, 480, 91, 81))
        self.Ground_21.setObjectName("Ground_21")
        self.Ground_22 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_22.setGeometry(QtCore.QRect(450, 480, 91, 81))
        self.Ground_22.setObjectName("Ground_22")
        self.Ground_23 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_23.setGeometry(QtCore.QRect(360, 480, 91, 81))
        self.Ground_23.setObjectName("Ground_23")
        self.Ground_24 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_24.setGeometry(QtCore.QRect(360, 400, 91, 81))
        self.Ground_24.setObjectName("Ground_24")
        self.Ground_25 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_25.setGeometry(QtCore.QRect(270, 400, 91, 81))
        self.Ground_25.setObjectName("Ground_25")
        self.Ground_26 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_26.setGeometry(QtCore.QRect(180, 400, 91, 81))
        self.Ground_26.setObjectName("Ground_26")
        self.Ground_27 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_27.setGeometry(QtCore.QRect(90, 400, 91, 81))
        self.Ground_27.setObjectName("Ground_27")
        self.Ground_28 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_28.setGeometry(QtCore.QRect(0, 400, 91, 81))
        self.Ground_28.setObjectName("Ground_28")
        self.Ground_29 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_29.setGeometry(QtCore.QRect(0, 320, 91, 81))
        self.Ground_29.setObjectName("Ground_29")
        self.Ground_30 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_30.setGeometry(QtCore.QRect(0, 240, 91, 81))
        self.Ground_30.setObjectName("Ground_30")
        self.Ground_31 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_31.setGeometry(QtCore.QRect(0, 160, 91, 81))
        self.Ground_31.setObjectName("Ground_31")
        self.Ground_32 = QtWidgets.QPushButton(self.centralwidget)
        self.Ground_32.setGeometry(QtCore.QRect(0, 80, 91, 81))
        self.Ground_32.setObjectName("Ground_32")
        self.copy_left = QtWidgets.QLabel(self.centralwidget)
        self.copy_left.setGeometry(QtCore.QRect(10, 490, 331, 61))
        self.copy_left.setObjectName("copy_left")
        self.time_count = QtWidgets.QTimeEdit(self.centralwidget)
        self.time_count.setGeometry(QtCore.QRect(150, 350, 221, 41))
        self.time_count.setObjectName("time_count")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.player_ix = np.array([0,1])
        self.pre_player_pos = np.array([0,0])
        self.cur_player_pos = np.array([0,0])
        self.show_player_pos()
        self.turn_token.setCurrentIndex(0)
        self.go.clicked.connect(self.on_go_clicked) #responds for go

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dice.setText(_translate("MainWindow", "Dice:[]"))
        self.roll_dice.setText(_translate("MainWindow", "Roll Dice"))
        self.go.setText(_translate("MainWindow", "Go"))
        self.info.setText(_translate("MainWindow", "Info:"))
        self.buy.setText(_translate("MainWindow", "Buy"))
        self.skip_buy.setText(_translate("MainWindow", "Skip"))
        self.turn_token.setItemText(0, _translate("MainWindow", "Player1"))
        self.turn_token.setItemText(1, _translate("MainWindow", "Player2"))
        self.Ground_1.setText(_translate("MainWindow", "Ground"))
        self.Ground_2.setText(_translate("MainWindow", "Ground"))
        self.Ground_3.setText(_translate("MainWindow", "Ground"))
        self.Ground_4.setText(_translate("MainWindow", "Ground"))
        self.Ground_5.setText(_translate("MainWindow", "Ground"))
        self.Ground_6.setText(_translate("MainWindow", "Ground"))
        self.Ground_7.setText(_translate("MainWindow", "Ground"))
        self.Ground_8.setText(_translate("MainWindow", "Ground"))
        self.Ground_9.setText(_translate("MainWindow", "Ground"))
        self.Ground_10.setText(_translate("MainWindow", "Ground"))
        self.Ground_11.setText(_translate("MainWindow", "Ground"))
        self.Ground_12.setText(_translate("MainWindow", "Ground"))
        self.Ground_13.setText(_translate("MainWindow", "Ground"))
        self.Ground_14.setText(_translate("MainWindow", "Ground"))
        self.Ground_15.setText(_translate("MainWindow", "Ground"))
        self.Ground_16.setText(_translate("MainWindow", "Ground"))
        self.Ground_17.setText(_translate("MainWindow", "Ground"))
        self.Ground_18.setText(_translate("MainWindow", "Ground"))
        self.Ground_19.setText(_translate("MainWindow", "Ground"))
        self.Ground_20.setText(_translate("MainWindow", "Ground"))
        self.Ground_21.setText(_translate("MainWindow", "Ground"))
        self.Ground_22.setText(_translate("MainWindow", "Ground"))
        self.Ground_23.setText(_translate("MainWindow", "Ground"))
        self.Ground_24.setText(_translate("MainWindow", "Ground"))
        self.Ground_25.setText(_translate("MainWindow", "Ground"))
        self.Ground_26.setText(_translate("MainWindow", "Ground"))
        self.Ground_27.setText(_translate("MainWindow", "Ground"))
        self.Ground_28.setText(_translate("MainWindow", "Ground"))
        self.Ground_29.setText(_translate("MainWindow", "Ground"))
        self.Ground_30.setText(_translate("MainWindow", "Ground"))
        self.Ground_31.setText(_translate("MainWindow", "Ground"))
        self.Ground_32.setText(_translate("MainWindow", "Ground"))
        self.copy_left.setText(_translate("MainWindow", "No right reserved, Welcome to copy and paste"))

    #player_ix: 0 (player 1), 1(player 2)
    def show_player_pos(self, player_ix = [0,1],pre_pos = [0,0],pos = [0,0]):
        ix_1 = player_ix[0]
        ix_2 = player_ix[1]

        #remove display of previous pos
        print("pre_pos 1: {0}, 2: {1}".format(pre_pos[0], pre_pos[1]))
        exec("self.Ground_{0}.setStyleSheet('background-color: {1}')".format(pre_pos[0] + 1, 'none'))
        exec("self.Ground_{0}.setStyleSheet('background-color: {1}')".format(pre_pos[1] + 1, 'none'))

        #if two player stand at the same place
        print("pos 1: {0}, pos 2: {1}".format(pos[ix_1], pos[ix_2]))
        if pos[ix_1] == pos[ix_2]:
            exec("self.Ground_{0}.setStyleSheet('background-color: {1}')".format(pos[ix_1] + 1, 'red'))
        else:
            exec("self.Ground_{0}.setStyleSheet('background-color: {1}')".format(pos[ix_1] + 1, 'yellow'))
            exec("self.Ground_{0}.setStyleSheet('background-color: {1}')".format(pos[ix_2] + 1, 'green'))

        #update info


    #action aft click go
    def on_go_clicked(self):
        import numpy.random as random
        #get dice and display
        self.latest_dice = random.randint(1, 6, 1) #+ random.randint(1, 6, 1)
        self.dice.setText("Dice: [{0}]".format(self.latest_dice))

        #calculate
        pre_player_pos = self.cur_player_pos
        cur_player = self.turn_token.currentIndex()
        print("cur_play: {0}".format(cur_player))

        if cur_player == 0:
            self.turn_token.setCurrentIndex(1)
        else:
            self.turn_token.setCurrentIndex(0)

        new_player_pos = np.array([pre_player_pos[0],pre_player_pos[1]])

        if new_player_pos[cur_player] + self.latest_dice > gbGroundNum - 1:
            new_player_pos[cur_player] = new_player_pos[cur_player] + self.latest_dice
            new_player_pos[cur_player] = new_player_pos[cur_player] - (gbGroundNum - 1)
        else:
            new_player_pos[cur_player] = new_player_pos[cur_player] + self.latest_dice

        #update player position
        print("player1 pos: {0}, player2 pos: {1}, player1 pre_pos: {2}, player2 pre_pos: {3}".format(new_player_pos[0],new_player_pos[1],pre_player_pos[0],pre_player_pos[1]))
        self.show_player_pos(self.player_ix, pre_player_pos, new_player_pos)

        #refresh data for next run
        self.cur_player_pos = new_player_pos

        #update info
        self.info.setText("Move Player 1 from {0} to {1} \n Move Player 2 from {2} to {3}".format(
            pre_player_pos[0], pre_player_pos[1],new_player_pos[0], new_player_pos[1]))


        def on_skip(self):
            pass

        def on_buy(self):
            pass