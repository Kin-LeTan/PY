from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
import csv, copy
class CheckOut(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.item_quantity_input_M2_array = {}
        self.cart_quantity_input_M2_array = {}
        self.total = 0

        layout = QtWidgets.QVBoxLayout(self)

        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.page2)
        self.scrollArea_5.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 735, 557))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.layout_list_M2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.layout_list_M2.setObjectName("layout_list_M2")
        #
        #
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_38.addWidget(self.scrollArea_5)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page2)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(300, 0))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 308, 557))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.layout_carts_M2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.layout_carts_M2.setObjectName("layout_carts_M2")
        # 
        # 
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_38.addWidget(self.scrollArea_2)
        self.verticalLayout_33.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem9)
        self.total_M2 = QtWidgets.QLabel(self.page2)
        self.total_M2.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.total_M2.setFont(font)
        self.total_M2.setObjectName("total_M2")
        self.horizontalLayout_18.addWidget(self.total_M2)
        self.verticalLayout_33.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem10)

        self.cart_btn_cancelAll_M2 = QtWidgets.QPushButton("HỦY TẤT CẢ")
        self.cart_btn_cancelAll_M2.setObjectName("cart_btn_cancelAll_M2")
        self.cart_btn_cancelAll_M2.clicked.connect(lambda: self.cancel_carts_M2())


        self.horizontalLayout_39.addWidget(self.cart_btn_cancelAll_M2)

        self.btn_checkOut_M2 = QtWidgets.QPushButton("TÍNH TIỀN")
        self.btn_checkOut_M2.setMinimumSize(QtCore.QSize(200, 44))
        self.btn_checkOut_M2.setObjectName("btn_checkOut_M2")
        self.btn_checkOut_M2.clicked.connect(self.check_out)

        self.horizontalLayout_39.addWidget(self.btn_checkOut_M2)
        self.verticalLayout_33.addLayout(self.horizontalLayout_39)
        
        layout.addWidget(self.page2)
    
    def show_item_M2(self, id, img, name, price, quantity):
        self.item_M2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.item_M2.setMinimumSize(QtCore.QSize(0, 0))
        self.item_M2.setMaximumSize(QtCore.QSize(16777215, 130))
        self.item_M2.setObjectName("item_M2")

        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.item_M2)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.item_image_M2 = QtWidgets.QLabel(self.item_M2)
        self.item_image_M2.setMinimumSize(QtCore.QSize(100, 100))
        self.item_image_M2.setMaximumSize(QtCore.QSize(100, 100))
        self.item_image_M2.setStyleSheet("image: url(:/newPrefix/images/Products/"+img+");")
        self.item_image_M2.setText("")
        self.item_image_M2.setObjectName("item_image_M2")
        self.horizontalLayout_32.addWidget(self.item_image_M2)
        self.widget_20 = QtWidgets.QWidget(self.item_M2)
        self.widget_20.setObjectName("widget_20")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.widget_20)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.item_name_M2 = QtWidgets.QLabel("Tên kho: "+name)
        self.item_name_M2.setObjectName("item_name_M2")
        self.verticalLayout_27.addWidget(self.item_name_M2)
        self.item_id_M2 = QtWidgets.QLabel("Mã id: "+str(id))
        self.item_id_M2.setObjectName("item_id_M2")
        self.verticalLayout_27.addWidget(self.item_id_M2)
        self.item_price_M2 = QtWidgets.QLabel("Giá: {:,.0f} VND".format(int(price)))#giá
        self.item_price_M2.setObjectName("item_price_M2")
        self.verticalLayout_27.addWidget(self.item_price_M2)
        self.item_quantity_RM_M2 = QtWidgets.QLabel("Số lượng còn: "+str(quantity))#Số lượng
        self.item_quantity_RM_M2.setObjectName("item_quantity_RM_M2")
        self.verticalLayout_27.addWidget(self.item_quantity_RM_M2)
        self.horizontalLayout_32.addWidget(self.widget_20)
        spacerItem6 = QtWidgets.QSpacerItem(448, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem6)
        self.widget_21 = QtWidgets.QWidget(self.item_M2)
        self.widget_21.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_21.setObjectName("widget_21")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.widget_21)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.item_label_M2 = QtWidgets.QLabel("Nhập số lượng cần thanh toán:")
        self.item_label_M2.setObjectName("item_label_M2")
        self.horizontalLayout_33.addWidget(self.item_label_M2)

        self.item_quantity_input_M2 = QtWidgets.QSpinBox(self.widget_21)
        self.item_quantity_input_M2.setObjectName("item_quantity_input_M2")
        if(int(quantity) > 0):
            rangeQuantity = 1
        else:
            rangeQuantity = 0
        self.item_quantity_input_M2.setRange(rangeQuantity, int(quantity))

        self.item_quantity_input_M2_array[int(id)] = self.item_quantity_input_M2

        self.horizontalLayout_33.addWidget(self.item_quantity_input_M2)
        self.verticalLayout_28.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")

        self.item_btn_add_M2 = QtWidgets.QPushButton("THÊM >>")
        self.item_btn_add_M2.setObjectName("item_btn_add_M2")
        self.item_btn_add_M2.clicked.connect(lambda: self.transfer_quantity_M2(0, str(id), int(self.item_quantity_input_M2_array[int(id)].value())))

        self.horizontalLayout_34.addWidget(self.item_btn_add_M2)
        self.verticalLayout_28.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_32.addWidget(self.widget_21)
        self.layout_list_M2.addWidget(self.item_M2)

    def show_cart_M2(self, id, img, name, price, quantity):
        self.cart = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.cart.setMinimumSize(QtCore.QSize(0, 0))
        self.cart.setMaximumSize(QtCore.QSize(16777215, 230))
        self.cart.setObjectName("cart")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.cart)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.cart_image_M2 = QtWidgets.QLabel(self.cart)
        self.cart_image_M2.setMinimumSize(QtCore.QSize(100, 100))
        self.cart_image_M2.setMaximumSize(QtCore.QSize(100, 100))
        self.cart_image_M2.setStyleSheet("image: url(:/newPrefix/images/Products/"+img+");")
        self.cart_image_M2.setText("")
        self.cart_image_M2.setObjectName("cart_image_M2")
        self.horizontalLayout_37.addWidget(self.cart_image_M2)
        self.widget_22 = QtWidgets.QWidget(self.cart)
        self.widget_22.setObjectName("widget_22")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.widget_22)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.cart_name_M2 = QtWidgets.QLabel("Tên kho: "+name)
        self.cart_name_M2.setObjectName("cart_name_M2")
        self.verticalLayout_30.addWidget(self.cart_name_M2)
        self.cart_id_M2 = QtWidgets.QLabel("Mã id: "+str(id))
        self.cart_id_M2.setObjectName("cart_id_M2")
        self.verticalLayout_30.addWidget(self.cart_id_M2)
        self.cart_price_M2 = QtWidgets.QLabel("Giá: {:,.0f} VND".format(int(price)))
        self.cart_price_M2.setObjectName("cart_price_M2")
        self.verticalLayout_30.addWidget(self.cart_price_M2)
        self.cart_quantity_M2 = QtWidgets.QLabel("Số lượng: "+str(quantity))
        self.cart_quantity_M2.setObjectName("cart_quantity_M2")
        self.verticalLayout_30.addWidget(self.cart_quantity_M2)
        self.horizontalLayout_37.addWidget(self.widget_22)
        self.verticalLayout_29.addLayout(self.horizontalLayout_37)
        self.widget_23 = QtWidgets.QWidget(self.cart)
        self.widget_23.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_23.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_23.setObjectName("widget_23")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.widget_23)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.item_label_M1_4 = QtWidgets.QLabel("Nhập số lượng: ")
        self.item_label_M1_4.setObjectName("item_label_M1_4")

        self.horizontalLayout_35.addWidget(self.item_label_M1_4)
        self.cart_quantity_input_M2 = QtWidgets.QSpinBox(self.widget_23)
        self.cart_quantity_input_M2.setObjectName("cart_quantity_input_M2")
        self.cart_quantity_input_M2.setRange(1, int(quantity))
        self.cart_quantity_input_M2_array[int(id)] = self.cart_quantity_input_M2

        self.horizontalLayout_35.addWidget(self.cart_quantity_input_M2)
        self.verticalLayout_32.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")

        self.cart_btn_remove_M2 = QtWidgets.QPushButton("<< TRỪ")
        self.cart_btn_remove_M2.setObjectName("cart_btn_remove_M2")
        self.horizontalLayout_36.addWidget(self.cart_btn_remove_M2)
        self.cart_btn_remove_M2.clicked.connect(lambda: self.transfer_quantity_M2(1, str(id), int(self.cart_quantity_input_M2_array[int(id)].value())))

        self.cart_btn_cancel_M2 = QtWidgets.QPushButton("HỦY")
        self.cart_btn_cancel_M2.setObjectName("cart_btn_cancel_M2")
        self.cart_btn_cancel_M2.clicked.connect(lambda: self.transfer_quantity_M2(1, str(id), int(quantity)))
        self.horizontalLayout_36.addWidget(self.cart_btn_cancel_M2)

        self.verticalLayout_32.addLayout(self.horizontalLayout_36)
        self.verticalLayout_29.addWidget(self.widget_23)
        self.layout_carts_M2.addWidget(self.cart)

    #Từ trang thanh toán
    def show_list_M2(self):
        self.clear_layout(self.layout_list_M2)

        with open('csv/kho.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            sorted_rows = sorted(csv_reader, key=lambda x: int(x['id']))

            for row in sorted_rows:
                self.show_item_M2(row['id'], row['anh'], row['ten'], row['gia'], row['so_luong'])

        self.end_item_M2()
    def show_carts_M2(self):
        self.clear_layout(self.layout_carts_M2)

        with open('csv/gio.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            sorted_rows = sorted(csv_reader, key=lambda x: int(x['id']))

            for row in sorted_rows:
                self.show_cart_M2(row['id'], row['anh'], row['ten'], row['gia'], row['so_luong'])

        self.end_cart_M2()
    def transfer_quantity_M2(self, type, id, quantity):
        if type == 0:
            csv_1 = 'csv/kho.csv'
            csv_2 = 'csv/gio.csv'
        else:
            csv_1 = 'csv/gio.csv'
            csv_2 = 'csv/kho.csv'
        if quantity > 0:
            data_1 = []
            with open(csv_1, 'r', encoding='utf-8') as file1:
                reader1 = csv.DictReader(file1)
                data_1 = list(reader1)

            data_2 = []
            with open(csv_2, 'r', encoding='utf-8') as file2:
                reader2 = csv.DictReader(file2)
                data_2 = list(reader2)

            row_test = None

            for row1 in data_1:
                if row1['id'] == id:
                    row1['so_luong'] = int(row1['so_luong']) - quantity

                    row_test = copy.copy(row1)

            exist_id = False
            for row2 in data_2:
                if row2['id'] == id:
                    exist_id = True
                    break
            
            if exist_id:
                for row2 in data_2:
                    if row2['id'] == id:
                        row2['so_luong'] = int(row2['so_luong']) + quantity
            else:
                row_test['so_luong'] = quantity
                data_2.append(row_test)

            new_data1 = []
            for row3 in data_1:
                if type == 1:
                    if int(row3['so_luong']) > 0:
                        new_data1.append(row3)
                else:
                    new_data1.append(row3)
                        
            with open(csv_1, 'w', newline='', encoding='utf-8') as file1:
                writer1 = csv.DictWriter(file1, fieldnames=reader1.fieldnames)
                writer1.writeheader()
                writer1.writerows(new_data1)

            with open(csv_2, 'w', newline='', encoding='utf-8') as file2:
                writer2 = csv.DictWriter(file2, fieldnames=reader2.fieldnames)
                writer2.writeheader()
                writer2.writerows(data_2)
        self.show_carts_M2()
        self.show_list_M2()
        self.show_total_M2()
    def cancel_carts_M2(self):
        with open('csv/gio.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        for row in data:
            self.transfer_quantity_M2(1, row['id'], int(row['so_luong']))      
    def end_item_M2(self):
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_list_M2.addItem(spacerItem7)
    def end_cart_M2(self):
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_carts_M2.addItem(spacerItem8)
    def show_total_M2(self):
        total = 0
        with open('csv/gio.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        for row in data:
            total = total + (int(row['gia']) * int(row['so_luong']))
        self.total = total
        self.total_M2.setText("TỔNG TIỀN: {:,.0f} VND".format(int(self.total)))
    def check_out(self):
        with open("csv/gio.csv", "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua hàng tiêu đề cột
            row_count = sum(1 for row in reader)
            if row_count != 0:
                max_id_don = -1
                with open("csv/don.csv", "r",encoding='utf-8') as file:
                    reader_don = csv.DictReader(file)
                    for row in reader_don:
                        if int(row['id_don']) > max_id_don:
                            max_id_don = int(row['id_don'])
                max_id_don = max_id_don + 1

                max_id_ctd = -1
                with open("csv/chi_tiet_don.csv", "r",encoding='utf-8') as file:
                    reader_ctd = csv.DictReader(file)
                    for row in reader_ctd:
                        if int(row['id']) > max_id_ctd:
                            max_id_ctd = int(row['id'])

                now = datetime.now()
                time_now = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]
                data_don = [max_id_don, time_now]
                with open('csv/don.csv', 'a', newline='',encoding='utf-8') as file:
                    writer_don = csv.writer(file)
                    writer_don.writerow(data_don)


                with open("csv/gio.csv", "r",encoding='utf-8') as file:
                    reader_gio = csv.DictReader(file)
                    for row in reader_gio:
                        max_id_ctd = max_id_ctd + 1
                        data_ctd = [max_id_ctd, max_id_don, row['id'], row['ten'], row['gia'], row['so_luong'], row['anh']]
                        with open('csv/chi_tiet_don.csv', 'a', newline='',encoding='utf-8') as file:
                            writer_ctd = csv.writer(file)
                            writer_ctd.writerow(data_ctd)

                with open("csv/gio.csv", "r",encoding='utf-8') as file:
                    reader = csv.reader(file)
                    headers = next(reader)  # Đọc các tiêu đề cột

                with open("csv/gio.csv", "w", newline="",encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)
                message_box = QMessageBox()
                message_box.setWindowTitle("Thông báo")
                message_box.setText("Thanh toán thành công!!!")
                message_box.setIcon(QMessageBox.Information)
                message_box.addButton(QMessageBox.Ok)
                message_box.exec_()
            else:
                message_box = QMessageBox()
                message_box.setWindowTitle("Thông báo")
                message_box.setText("Chưa kho hàng nào trên thanh toán!!!")
                message_box.setIcon(QMessageBox.Information)
                message_box.addButton(QMessageBox.Ok)
                message_box.exec_()
        self.show_carts_M2()
        self.show_total_M2()
        self.show_list_M2()

    #Xử lý khác
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                layout.removeWidget(widget)
                widget.deleteLater()