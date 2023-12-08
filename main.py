# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from main_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedMenuItem.setCurrentIndex(1)
        self.ui.reset_all_list()
        
    def on_menu_nhap_clicked(self):
        self.ui.stackedMenuItem.setCurrentIndex(0)
        self.ui.reset_all_list()

    def on_menu_thanh_toan_clicked(self):
        self.ui.stackedMenuItem.setCurrentIndex(1)
        self.ui.reset_all_list()

    def on_menu_don_clicked(self):
        self.ui.stackedMenuItem.setCurrentIndex(2)
        self.ui.reset_all_list()

    def on_menu_thong_ke_clicked(self):
        self.ui.stackedMenuItem.setCurrentIndex(3)
        self.ui.reset_all_list()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())