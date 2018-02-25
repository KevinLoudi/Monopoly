import sys
from PyQt5.QtWidgets import QMainWindow,QApplication


from ui_0_1 import Ui_MainWindow
from game_util import *
from objects_util import account, player



class CMonoployApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()

    def initUi(self):
        pass


def main_logic(app):
    #initialize ui info
    gb_ground_num = 32
    layout = init_layout_info()

    for i in range(gb_ground_num):
        app.ui.set_ground_info(i, layout[i].m_name)
    #main logic
    global gb_player1
    global gb_player2

    #initialize role info
    gb_accountList = []  # account list
    gb_accountList.append(account(1, 200, 200))  # player1's account
    gb_accountList.append(account(2, 200, 200))  # player2's account
    gb_player1 = player(1, 'player1', gb_accountList[0], 1, 0)  # init player # position in 0
    gb_player2 = player(2, 'player2', gb_accountList[1], 2, 0)

    turn = 0  # init turn
    the_player = gb_player1
    while True:
        # which player's turn and begin player
        if (turn % 2 == 0):  # player1's turn
            the_player = gb_player1
        else:
            the_player = gb_player2

        print("It is " + the_player.getName() + "'s turn.")

        turnnochange = False
        move = getDice()
        app.ui.set_dice(move)
        makeMove(the_player, move)




def init_layout_info():
    layoutList = []
    layoutList.append(go())
    # layoutlist[0].showPlaceInfo()
    layoutList.append(street(00, 1))
    layoutList.append(communitychess(2))
    layoutList.append(street(1, 3))
    layoutList.append(tax("Income tax", 4))
    layoutList.append(station("KING CROSS STATION","KC Station",5))
    layoutList.append(street(10, 6))
    layoutList.append(chance(7))
    layoutList.append(street(11, 8))
    layoutList.append(street(12, 9))
    layoutList.append(jail())

    layoutList.append(street(20, 11))
    layoutList.append(utility("ELECTRIC COMPANY","EC",12))
    layoutList.append(street(21, 13))
    layoutList.append(street(22, 14))
    layoutList.append(station("MARYLEBONE STATION", "M station", 15))
    layoutList.append(street(30, 16))
    layoutList.append(communitychess(17))
    layoutList.append(street(31, 18))
    layoutList.append(street(32, 19))
    layoutList.append(parking())

    layoutList.append(street(40, 21))
    layoutList.append(chance(22))
    layoutList.append(street(41, 23))
    layoutList.append(street(42, 24))
    layoutList.append(station("FENCHURCH STREET STATION","FE station",25))
    layoutList.append(street(50, 26))
    layoutList.append(street(51, 27))
    layoutList.append(utility("WATER WORKS","WW",28))
    layoutList.append(street(52, 29))
    layoutList.append(gotojail())

    layoutList.append(street(60, 31))
    layoutList.append(street(61, 32))
    layoutList.append(communitychess(33))
    layoutList.append(street(62, 34))
    layoutList.append(station("LIVERPOOL STREET STATION","LS station",35))
    layoutList.append(chance(36))
    layoutList.append(street(70, 37))
    layoutList.append(tax("Super Tax", 38))
    layoutList.append(street(71, 39))

    return layoutList

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CMonoployApp()
    main_logic(window)
    window.show()
    sys.exit(app.exec_())