import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import Qt

from qt_material import apply_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)

        loader = QUiLoader()
        self.ui = loader.load("main_ui.ui", None)


        self.setCentralWidget(self.ui)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()


    def mouseMoveEvent(self, event):
      self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
      self.dragPos = event.globalPosition().toPoint()
      event.accept()

    def mouseDoubleClickEvent(self, event):
        self.close()

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    apply_stylesheet(app, "dark_teal.xml")
    window.setFixedWidth(250)
    window.setFixedHeight(55)

    window.show()

    app.exec()


if __name__ == "__main__":
    run()