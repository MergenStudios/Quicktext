import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader

from qt_material import apply_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("main_ui.ui", None)

        self.setCentralWidget(self.ui)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    apply_stylesheet(app, "dark_teal.xml")
    window.setGeometry(100, 100, 229, 41)

    window.show()

    app.exec()