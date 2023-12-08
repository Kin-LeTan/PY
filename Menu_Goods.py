from PyQt5 import QtCore, QtGui, QtWidgets
import csv, copy, sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
import os
import shutil
class Goods(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.item_quantity_input_M1_array = {}
        layout = QtWidgets.QVBoxLayout(self)

        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.page1)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1255, 537))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layout_list_M1 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.layout_list_M1.setObjectName("layout_list_M1")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.widget = QtWidgets.QWidget(self.page1)
        self.widget.setMinimumSize(QtCore.QSize(0, 110))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 110))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.form_image_M1 = QtWidgets.QLabel(self.widget)
        self.form_image_M1.setMinimumSize(QtCore.QSize(100, 100))
        self.form_image_M1.setMaximumSize(QtCore.QSize(100, 100))
        self.form_image_M1.setPixmap(QPixmap("images/Orthers/Empty.png").scaled(100, 100, Qt.KeepAspectRatio))
        self.form_image_M1.setText("")
        self.form_image_M1.setObjectName("form_image_M1")
        self.horizontalLayout_3.addWidget(self.form_image_M1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.form_select_img_M1 = QtWidgets.QPushButton("Chọn ảnh...")
        self.form_select_img_M1.setObjectName("form_select_img_M1")

        self.form_select_img_M1.clicked.connect(self.select_image)

        self.verticalLayout_6.addWidget(self.form_select_img_M1)
        self.label = QtWidgets.QLabel("Tên ảnh:")
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.form_name_img_M1 = QtWidgets.QLineEdit(self.widget)
        self.form_name_img_M1.setObjectName("form_name_img_M1")
        self.verticalLayout_6.addWidget(self.form_name_img_M1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(120, 0))
        self.widget_3.setObjectName("widget_3")
        self.formLayout = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel("Tên kho:")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.form_name_M1 = QtWidgets.QLineEdit(self.widget_3)
        self.form_name_M1.setObjectName("form_name_M1")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.form_name_M1)
        self.label_13 = QtWidgets.QLabel("Giá:")
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)


        validator = QIntValidator()

        self.form_price_M1 = QtWidgets.QLineEdit()
        self.form_price_M1.setObjectName("form_price_M1")
        self.form_price_M1.setValidator(validator)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.form_price_M1)
        self.label_14 = QtWidgets.QLabel("Đặt số lượng:")
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)

        self.form_quantity_M1 = QtWidgets.QLineEdit()
        self.form_quantity_M1.setObjectName("form_quantity_M1")
        self.form_quantity_M1.setValidator(validator)

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.form_quantity_M1)
        self.horizontalLayout_3.addWidget(self.widget_3)
        spacerItem5 = QtWidgets.QSpacerItem(448, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.form_btn_add_M1 = QtWidgets.QPushButton("Thêm kho")
        self.form_btn_add_M1.setMinimumSize(QtCore.QSize(0, 80))
        self.form_btn_add_M1.setObjectName("form_btn_add_M1")
        self.form_btn_add_M1.clicked.connect(self.add_item)

        self.horizontalLayout_3.addWidget(self.form_btn_add_M1)
        self.verticalLayout_3.addWidget(self.widget)

        layout.addWidget(self.page1)

        self.show_list_M1()

    def show_item_M1(self, id, img, name, price, quantity):
        self.item_M1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.item_M1.setMinimumSize(QtCore.QSize(0, 0))
        self.item_M1.setMaximumSize(QtCore.QSize(16777215, 130))
        self.item_M1.setObjectName("item_M1")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.item_M1)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.item_image_M1 = QtWidgets.QLabel(self.item_M1)
        self.item_image_M1.setMinimumSize(QtCore.QSize(100, 100))
        self.item_image_M1.setMaximumSize(QtCore.QSize(100, 100))
        self.item_image_M1.setStyleSheet("image: url(images/Products/"+img+");") # ẢNH
        self.item_image_M1.setText("")
        self.item_image_M1.setObjectName("item_image_M1")
        self.horizontalLayout_29.addWidget(self.item_image_M1)
        self.widget_16 = QtWidgets.QWidget(self.item_M1)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.item_name_M1 = QtWidgets.QLabel("Tên kho: "+name) # Tên
        self.item_name_M1.setObjectName("item_name_M1")
        self.verticalLayout_23.addWidget(self.item_name_M1)
        self.item_id_M1 = QtWidgets.QLabel("Mã id: "+str(id)) # ID
        self.item_id_M1.setObjectName("item_id_M1")
        self.verticalLayout_23.addWidget(self.item_id_M1)
        self.item_price_M1 = QtWidgets.QLabel("Giá: {:,.0f} VND".format(int(price)))# Giá
        self.item_price_M1.setObjectName("item_price_M1")
        self.verticalLayout_23.addWidget(self.item_price_M1)
        self.item_quantity_RM_M1 = QtWidgets.QLabel("Số lượng còn: "+str(quantity))# Số lượng còn lại
        self.item_quantity_RM_M1.setObjectName("item_quantity_RM_M1")
        self.verticalLayout_23.addWidget(self.item_quantity_RM_M1)
        self.horizontalLayout_29.addWidget(self.widget_16)
        spacerItem3 = QtWidgets.QSpacerItem(448, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem3)
        self.widget_17 = QtWidgets.QWidget(self.item_M1)
        self.widget_17.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.widget_17)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.item_label_M1 = QtWidgets.QLabel("Số lượng: ")
        self.item_label_M1.setObjectName("item_label_M1")
        self.horizontalLayout_30.addWidget(self.item_label_M1)

        self.item_quantity_input_M1 = QtWidgets.QSpinBox(self.widget_17)
        self.item_quantity_input_M1.setObjectName("item_quantity_input_M1")
        self.item_quantity_input_M1_array[int(id)] = self.item_quantity_input_M1

        self.horizontalLayout_30.addWidget(self.item_quantity_input_M1)
        self.verticalLayout_24.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")

        self.item_btn_add_M1 = QtWidgets.QPushButton("Thêm vào kho")
        self.item_btn_add_M1.setObjectName("item_btn_add_M1")

        self.item_btn_add_M1.clicked.connect(lambda: self.update_quantity_M1(1, str(id), self.item_quantity_input_M1_array[int(id)].value()))

        self.horizontalLayout_31.addWidget(self.item_btn_add_M1)

        self.item_btn_barring_M1 = QtWidgets.QPushButton("Giảm trừ kho")
        self.item_btn_barring_M1.setObjectName("item_btn_barring_M1")

        self.item_btn_barring_M1.clicked.connect(lambda: self.update_quantity_M1(0, str(id), self.item_quantity_input_M1_array[int(id)].value()))

        self.horizontalLayout_31.addWidget(self.item_btn_barring_M1)
        self.verticalLayout_24.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_29.addWidget(self.widget_17)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.item_btn_edit_M1 = QtWidgets.QPushButton("Sửa thông tin")
        self.item_btn_edit_M1.setObjectName("item_btn_edit_M1")
        self.verticalLayout.addWidget(self.item_btn_edit_M1)
        
        self.item_btn_delete_M1 = QtWidgets.QPushButton("Xóa kho")
        self.item_btn_delete_M1.setObjectName("item_btn_delete_M1")

        self.item_btn_delete_M1.clicked.connect(lambda: self.delete_item_M1(str(id)))

        self.verticalLayout.addWidget(self.item_btn_delete_M1)
        self.horizontalLayout_29.addLayout(self.verticalLayout)
        self.layout_list_M1.addWidget(self.item_M1)
        
    #Từ trang Kho
    def show_list_M1(self):
        self.clear_layout(self.layout_list_M1)

        with open('csv/kho.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            sorted_rows = sorted(csv_reader, key=lambda x: int(x['id']))

            for row in sorted_rows:
                self.show_item_M1(row['id'], row['anh'], row['ten'], row['gia'], row['so_luong'])

        self.end_item_M1()
    def update_quantity_M1(self, type, id, quantity):
        # Mở tệp CSV
        with open('csv/kho.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            sorted_rows = sorted(csv_reader, key=lambda x: int(x['id']))

        # Tìm hàng có ID tương ứng và cập nhật cột "so_luong"
        for row in sorted_rows:
            if row['id'] == id:
                current_quantity = int(row['so_luong'])
                if type == 0:  # Giảm số lượng
                    new_quantity = max(current_quantity - quantity, 0)
                elif type == 1:  # Tăng số lượng
                    new_quantity = current_quantity + quantity
                else:
                    raise ValueError("Invalid type. Must be 0 or 1.")
                row['so_luong'] = str(new_quantity)

        # Ghi lại dữ liệu vào tệp CSV
        fieldnames = csv_reader.fieldnames
        with open('csv/kho.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sorted_rows)
        self.show_list_M1()
    def delete_item_M1(self, id):
        rows = []
        with open('csv/kho.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                if row['id'] != id:
                    rows.append(row)

        with open('csv/kho.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        self.show_list_M1()  
    def end_item_M1(self):
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_list_M1.addItem(spacerItem4)
    def select_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.form_image_M1.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            self.selected_image_path = file_name
            self.form_name_img_M1.setText(os.path.basename(self.selected_image_path)) 
    def add_item(self):
        img = "Empty.png"
        
        name = self.form_name_M1.text()
        price = self.form_price_M1.text()
        quantity = self.form_quantity_M1.text()

        if len(name.strip()) == 0:
            name = "(Trống)"
        if len(price.strip()) == 0:
            price = 0
        if len(quantity.strip()) == 0:
            quantity = 0

        with open('csv/kho.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            sorted_rows = sorted(csv_reader, key=lambda x: int(x['id']))
            max_id = -1
        for row in sorted_rows:
            if int(row['id']) > max_id:
                max_id = int(row['id'])

        id = str(max_id + 1)

        if hasattr(self, "selected_image_path"):
            destination = os.path.join("images/Products", self.form_name_img_M1.text())
            shutil.copy2(self.selected_image_path, destination)
            img = self.form_name_img_M1.text()
        
        data = [id, name, price, quantity, img]

        with open('csv/kho.csv', 'a', newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        
        message_box = QMessageBox()
        message_box.setWindowTitle("Thông báo")
        message_box.setText("Đã thêm kho thành công!!!")
        message_box.setIcon(QMessageBox.Information)
        message_box.addButton(QMessageBox.Ok)
        message_box.exec_()
        
        self.show_list_M1()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                layout.removeWidget(widget)
                widget.deleteLater()
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                layout.removeWidget(widget)
                widget.deleteLater()
    
    
    