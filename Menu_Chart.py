from PyQt5 import QtCore, QtGui, QtWidgets
import csv, copy, sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
class Chart(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.item_quantity_input_M1_array = {}
        layout = QtWidgets.QVBoxLayout(self)

        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page4)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1125, 705))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.item_M4 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.item_M4.setObjectName("item_M4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.item_M4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.title_chart_M4 = QtWidgets.QLabel("Thống kê tổng giá các Sản phẩm theo ngày")
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.title_chart_M4.setFont(font)
        self.title_chart_M4.setObjectName("title_chart_M4")
        self.horizontalLayout_4.addWidget(self.title_chart_M4)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.filter_text_M4 = QtWidgets.QLabel("Lọc Sản phẩm:")
        self.filter_text_M4.setMinimumSize(QtCore.QSize(0, 0))
        self.filter_text_M4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.filter_text_M4.setObjectName("filter_text_M4")
        self.horizontalLayout_5.addWidget(self.filter_text_M4)
        self.comboBox_filter_M4 = QtWidgets.QComboBox(self.item_M4)
        self.comboBox_filter_M4.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_filter_M4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_filter_M4.setObjectName("comboBox_filter_M4")
        kho_data = []
        with open('csv/kho.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua dòng tiêu đề
            for row in reader:
                kho_id, ten, _, _, _ = row
                kho_data.append(f"{kho_id},{ten}")

        
        self.comboBox_filter_M4.addItem("Tất cả")
        for item in kho_data:
            self.comboBox_filter_M4.addItem(item)
        self.comboBox_filter_M4.currentIndexChanged.connect(self.update_chart_M4)

        self.horizontalLayout_5.addWidget(self.comboBox_filter_M4)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem18)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.widget_chart = QtWidgets.QWidget(self.item_M4)
        self.widget_chart.setMinimumSize(QtCore.QSize(0, 200))
        self.widget_chart.setObjectName("widget_chart")

        
        
        self.layout_chart = QtWidgets.QVBoxLayout(self.widget_chart)
        self.layout_chart.setObjectName("layout_chart")
        self.label_2 = QtWidgets.QLabel(self.widget_chart)
        self.label_2.setObjectName("label_2")

        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)


        self.layout_chart.addWidget(self.toolbar)
        self.layout_chart.addWidget(self.canvas)



        self.verticalLayout_8.addWidget(self.widget_chart)
        self.line_2 = QtWidgets.QFrame(self.item_M4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.verticalLayout_9.addWidget(self.item_M4)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem19)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_10.addWidget(self.scrollArea_3)

        layout.addWidget(self.page4)
    def update_chart_M4(self):

        self.df_time = pd.read_csv('csv/don.csv')
        self.df_product = pd.read_csv('csv/chi_tiet_don.csv')
        self.df_product['doanh_thu'] = self.df_product['gia'] * self.df_product['so_luong']
        self.df_merged = pd.merge(self.df_product, self.df_time, on='id_don')
        self.df_merged['thoi_gian'] = pd.to_datetime(self.df_merged['thoi_gian'])
        self.df_merged['ngay'] = self.df_merged['thoi_gian'].dt.date
        selected_kho = self.comboBox_filter_M4.currentText()

        if selected_kho == "Tất cả":
            table_doanh_thu_theo_ngay = self.df_merged.groupby('ngay')['doanh_thu'].sum()
            title = 'Tổng doanh thu theo ngày (Tất cả kho)'
        else:
            array = selected_kho.split(",")
            table_doanh_thu_theo_ngay = self.df_merged[self.df_merged['id_kho'] == int(array[0])].groupby('ngay')['doanh_thu'].sum()
            title = f'Tổng doanh thu theo ngày (Kho {selected_kho})'

        self.ax.clear()
        bars = self.ax.bar(table_doanh_thu_theo_ngay.index.astype(str), table_doanh_thu_theo_ngay.values, color='skyblue')
        self.ax.set_title(title)
        self.ax.set_xlabel('Ngày')
        self.ax.set_ylabel('Doanh thu')
        self.ax.set_xticklabels(table_doanh_thu_theo_ngay.index.astype(str), rotation=45, ha='right')
        self.ax.tick_params(axis='x', which='both', labelsize=8)
        self.ax.tick_params(axis='y', labelsize=8)
        # Hiển thị số trục y trên thanh bar
        for bar in bars:
            yval = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width() / 2, yval, '{:,.0f} VND'.format(yval), ha='center', va='bottom')

        self.canvas.draw()