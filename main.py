from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randrange


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton: QPushButton
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randrange(10, 200)
        y = randrange(10, 200)
        qp.drawEllipse(x, x, y, y)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
