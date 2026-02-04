import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication

from src.dev_companion.gui.utils.window_helpers import get_offset, load_stylesheet
from src.dev_companion.gui.widgets.CentralWidget import CentralWidget
from src.dev_companion.utils.constants.config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_window()

    def __init_window(self):
        self.setWindowTitle(APP_NAME)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setCentralWidget(CentralWidget())
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setStyleSheet(load_stylesheet("test.css"))
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move(*get_offset())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()