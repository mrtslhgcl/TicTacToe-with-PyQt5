from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

class GameBoard(QTableWidget):
    def __init__(self,win):
        super(GameBoard, self).__init__(win)
        self.turn = 'X'
        self.finish = False
        
    def mousePressEvent(self, ev):
        self.selectedItem = self.itemAt(ev.pos())
        if ev.button() == Qt.MouseButton.LeftButton:
            if self.turn == 'X':
                if (self.selectedItem.text() != 'X') and (self.selectedItem.text() != 'O'):
                    self.selectedItem.setText('X')
                    self.turn = 'O'
                    self.controlGame()
            elif self.turn == 'O':
                if (self.selectedItem.text() != 'X') and (self.selectedItem.text() != 'O'):
                    self.selectedItem.setText('O')
                    self.turn = 'X'
                    self.controlGame()
    
    def controlGame(self):
        posibility_1 = self.itemAt(1,1).text() == self.itemAt(201,1).text() == self.itemAt(401,1).text()
        posibility_2 = self.itemAt(1,1).text() == self.itemAt(201,201).text() == self.itemAt(401,401).text()
        posibility_3 = self.itemAt(1,1).text() == self.itemAt(1,201).text() == self.itemAt(1,401).text()
        posibility_4 = self.itemAt(1,201).text() == self.itemAt(201,201).text() == self.itemAt(401,201).text()
        posibility_5 = self.itemAt(1,401).text() == self.itemAt(201,401).text() == self.itemAt(401,401).text()
        posibility_6 = self.itemAt(1,401).text() == self.itemAt(201,201).text() == self.itemAt(401,1).text()
        posibility_7 = self.itemAt(201,1).text() == self.itemAt(201,201).text() == self.itemAt(201,401).text()
        posibility_8 = self.itemAt(401,1).text() == self.itemAt(401,201).text() == self.itemAt(401,401).text()
        posibility_9 = self.itemAt(1,201).text() == self.itemAt(201,201).text() == self.itemAt(401,201).text()
        gameOver = self.findItems('',Qt.MatchFlag.MatchExactly)
        
        if posibility_1 and (self.itemAt(1,1).text() != ''): 
            print(f'{self.itemAt(1,1).text()} Oyunu Kazandı.Tebrikler!')
            self.finish = True
        elif posibility_2 and (self.itemAt(1,1).text() != ''):
            print(f'{self.itemAt(1,1).text()} Oyunu Kazandı.Tebrikler!')
            self.finish = True
        elif posibility_3 and (self.itemAt(1,1).text() != ''):
            print(f'{self.itemAt(1,1).text()} Oyunu Kazandı.Tebrikler!')
            self.finish = True
        elif posibility_4 and (self.itemAt(1,201).text() != ''):
            print(f'{self.itemAt(1,201).text()} Oyunu Kazandı.Tebrikler!')
            self.finish = True
        elif posibility_5 and (self.itemAt(1,401).text() != ''):
            print(f'{self.itemAt(1,401).text()} Oyunu Kazandı.Tebrikler!')
            self.finish = True
        elif posibility_6 and (self.itemAt(1,401).text() != ''): 
            print(f'{self.itemAt(1,401).text()} Oyunu Kazandı.Tebrikler!')
            self.finish = True
        elif posibility_7 and (self.itemAt(201,1).text() != ''): 
            print(f'{self.itemAt(201,1).text()} Oyunu Kazandı.Tebrikler!')
            self.finish = True
        elif posibility_8 and (self.itemAt(401,1).text() != ''):
            print(f'{self.itemAt(401,1).text()} Oyunu Kazandı.Tebrikler!')
            self.finish = True
        elif posibility_9 and (self.itemAt(1,201).text() != ''):
            print(f'{self.itemAt(1,201).text()} Oyunu Kazandı.Tebrikler!')
            self.finish = True
        elif (posibility_1 and posibility_2 and posibility_3 and posibility_4 and posibility_5 and posibility_6 and posibility_7 and posibility_8 and posibility_9) == False and (len(gameOver) == 0):
            print('Oyun Berabere')
            self.finish = True
            
        if self.finish == True:
            self.itemAt(1,1).setText('')
            self.itemAt(201,1).setText('')
            self.itemAt(401,1).setText('')
            self.itemAt(1,201).setText('')
            self.itemAt(201,201).setText('')
            self.itemAt(401,201).setText('')
            self.itemAt(1,401).setText('')
            self.itemAt(201,401).setText('')
            self.itemAt(401,401).setText('')
            self.finish = False