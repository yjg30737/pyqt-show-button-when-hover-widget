import os

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QGraphicsView, QPushButton, QGridLayout, QApplication, QFileDialog, QGraphicsScene, \
    QHBoxLayout


class ShowButtonWhenHoverWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__p = ''
        self.__scene = ''
        self.__graphicItem = ''

        addBtn = QPushButton()
        self.__delBtn = QPushButton()

        addBtn.clicked.connect(self.__add)
        self.__delBtn.clicked.connect(self.__delete)

        btns = [addBtn, self.__delBtn]

        css_file_path = os.path.join(os.path.dirname(os.path.relpath(__file__, os.getcwd())), r'style/button.css')
        css_file = open(css_file_path)
        css_code = css_file.read()
        css_file.close()

        for btn in btns:
            btn.setStyleSheet(css_code)

        addBtn.setIcon(QIcon('ico/add.png'))
        self.__delBtn.setIcon(QIcon('ico/delete.png'))

        addBtn.setToolTip('Add')
        self.__delBtn.setToolTip('Delete')

        lay = QHBoxLayout()
        lay.addWidget(addBtn)
        lay.addWidget(self.__delBtn)
        lay.setContentsMargins(2, 2, 2, 2)

        self.__btnWidget = QWidget()
        self.__btnWidget.setLayout(lay)
        self.__btnWidget.setMaximumWidth(self.__btnWidget.sizeHint().width()+4)
        self.__btnWidget.setMaximumHeight(self.__btnWidget.sizeHint().height()+4)

        self.__image_view = QGraphicsView()

        lay = QGridLayout()
        lay.addWidget(self.__image_view, 0, 0, 2, 2)
        lay.addWidget(self.__btnWidget, 1, 1, 1, 1)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)

        self.__btnWidget.setVisible(False)

        self.__btn_toggled()

    def __btn_toggled(self):
        f = isinstance(self.__p, QPixmap)
        self.__delBtn.setEnabled(f)

    def __add(self):
        filename = QFileDialog.getOpenFileName(self, 'Open image file', '', 'Image file (*.jpg *.png *.bmp)')
        if filename[0]:
            self.__filename = filename[0]
            self.__p = QPixmap(self.__filename)
            self.__set_pixmap(self.__p)
            self.__btn_toggled()

    def __delete(self):
        # todo make it back to original size after deleting the image
        if isinstance(self.__scene, QGraphicsScene):
            self.__scene.removeItem(self.__graphicItem)
            self.__btn_toggled()

    def setPixmap(self, p):
        self.__set_pixmap(p)

    def __set_pixmap(self, p):
        self.__p = p
        self.__scene = QGraphicsScene()
        self.__graphicItem = self.__scene.addPixmap(self.__p)
        self.__image_view.setScene(self.__scene)
        self.__image_view.show()

    def enterEvent(self, e):
        self.__btnWidget.setVisible(True)
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.__btnWidget.setVisible(False)
        return super().leaveEvent(e)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    cellWidget = ShowButtonWhenHoverWidget()
    cellWidget.show()
    app.exec_()
