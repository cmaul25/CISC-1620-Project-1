from PyQt6.QtWidgets import *
from gui import *
from accounts import *


class Logic(QMainWindow, Ui_MainWindow):
        def __init__(self)->None:
            '''

            '''
            super().__init__()
            self.setupUi(self)