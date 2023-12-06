from PyQt5 import QtCore, QtGui, QtWidgets
import csv, copy, sys
class Invoice(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.list_goods_items_array = {}

        layout = QtWidgets.QVBoxLayout(self)

        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scroll_order = QtWidgets.QScrollArea(self.page3)
        self.scroll_order.setWidgetResizable(True)
        self.scroll_order.setObjectName("scroll_order")
        self.scroll_orderWidgetContents = QtWidgets.QWidget()
        self.scroll_orderWidgetContents.setGeometry(QtCore.QRect(0, 0, 1255, 664))
        self.scroll_orderWidgetContents.setObjectName("scroll_orderWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scroll_orderWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.line2 = QtWidgets.QFrame(self.scroll_orderWidgetContents)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.verticalLayout_4.addWidget(self.line2)


        self.scroll_order.setWidget(self.scroll_orderWidgetContents)
        self.horizontalLayout.addWidget(self.scroll_order)
        
        layout.addWidget(self.page3)

    def show_item_M3(self, id, time, total_goods, total_price):
        self.item_M3 = QtWidgets.QWidget(self.scroll_orderWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_M3.sizePolicy().hasHeightForWidth())
        self.item_M3.setSizePolicy(sizePolicy)
        self.item_M3.setMinimumSize(QtCore.QSize(0, 200))
        self.item_M3.setMaximumSize(QtCore.QSize(1678878, 220))
        self.item_M3.setBaseSize(QtCore.QSize(0, 0))
        self.item_M3.setObjectName("item_M3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.item_M3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_id_don_M3 = QtWidgets.QLabel("ID ĐƠN: "+id)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_id_don_M3.setFont(font)
        self.label_id_don_M3.setObjectName("label_id_don_M3")
        self.verticalLayout_5.addWidget(self.label_id_don_M3)
        self.label_time_M3 = QtWidgets.QLabel("ĐÃ TẠO VÀO: "+time)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_time_M3.setFont(font)
        self.label_time_M3.setObjectName("label_time_M3")
        self.verticalLayout_5.addWidget(self.label_time_M3)
        self.label_tong_hang_M3 = QtWidgets.QLabel("TỐNG MÓN HÀNG: "+str(total_goods))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_tong_hang_M3.setFont(font)
        self.label_tong_hang_M3.setObjectName("label_tong_hang_M3")
        self.verticalLayout_5.addWidget(self.label_tong_hang_M3)
        self.label_total_price_M3 = QtWidgets.QLabel("TỔNG TIỀN: {:,.0f} VND".format(total_price))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_total_price_M3.setFont(font)
        self.label_total_price_M3.setObjectName("label_total_price_M3")
        self.verticalLayout_5.addWidget(self.label_total_price_M3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_list = QtWidgets.QLabel("NHỮNG MÓN HÀNG TRONG ĐƠN:")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_list.setFont(font)
        self.label_list.setObjectName("label_list")
        self.verticalLayout_7.addWidget(self.label_list)
        self.scroll_goods = QtWidgets.QScrollArea(self.item_M3)
        self.scroll_goods.setMinimumSize(QtCore.QSize(600, 0))
        self.scroll_goods.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scroll_goods.setWidgetResizable(True)
        self.scroll_goods.setObjectName("scroll_goods")
        self.scroll_goodsWidgetContents = QtWidgets.QWidget()
        self.scroll_goodsWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 166))
        self.scroll_goodsWidgetContents.setObjectName("scroll_goodsWidgetContents")
        self.layout_items_goods = QtWidgets.QVBoxLayout(self.scroll_goodsWidgetContents)
        self.layout_items_goods.setObjectName("layout_items_goods")
        self.list_goods_items_array[int(id)] = self.layout_items_goods

        

        self.scroll_goods.setWidget(self.scroll_goodsWidgetContents)
        self.verticalLayout_7.addWidget(self.scroll_goods)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_4.addWidget(self.item_M3)
        self.line = QtWidgets.QFrame(self.scroll_orderWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)

    def show_goods_M3(self, id_don, name, img, price, quantity, total):
        self.item_goods_M3 = QtWidgets.QWidget(self.scroll_goodsWidgetContents)
        self.item_goods_M3.setMinimumSize(QtCore.QSize(0, 83))
        self.item_goods_M3.setMaximumSize(QtCore.QSize(16777215, 83))
        self.item_goods_M3.setObjectName("item_goods_M3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.item_goods_M3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_img_M3 = QtWidgets.QLabel(self.item_goods_M3)
        self.label_img_M3.setMinimumSize(QtCore.QSize(70, 0))
        self.label_img_M3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_img_M3.setStyleSheet("image: url(images/Products/"+img+");")
        self.label_img_M3.setText("")
        self.label_img_M3.setObjectName("label_img_M3")
        self.horizontalLayout_11.addWidget(self.label_img_M3)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_name_goods_M3 = QtWidgets.QLabel("Tên kho: "+name)
        self.label_name_goods_M3.setObjectName("label_name_goods_M3")
        self.verticalLayout_25.addWidget(self.label_name_goods_M3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_gia_goods_M3 = QtWidgets.QLabel("Giá: {:,.0f} VND".format(int(price)))
        self.label_gia_goods_M3.setObjectName("label_gia_goods_M3")
        self.horizontalLayout_9.addWidget(self.label_gia_goods_M3)
        self.label_quantity_goods_M3 = QtWidgets.QLabel("Số lượng: "+quantity)
        self.label_quantity_goods_M3.setObjectName("label_quantity_goods_M3")
        self.horizontalLayout_9.addWidget(self.label_quantity_goods_M3)
        self.label_tongTien_goods_M3 = QtWidgets.QLabel("Tổng tiền: {:,.0f} VND".format(total))
        self.label_tongTien_goods_M3.setObjectName("label_tongTien_goods_M3")
        self.horizontalLayout_9.addWidget(self.label_tongTien_goods_M3)
        self.verticalLayout_25.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11.addLayout(self.verticalLayout_25)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.list_goods_items_array[int(id_don)].addWidget(self.item_goods_M3)

    def show_invoice_M3(self):
        with open('csv/don.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            sorted_rows_don = sorted(csv_reader, key=lambda x: -int(x['id']))

        with open('csv/chi_tiet_don.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            sorted_rows_ctd = sorted(csv_reader, key=lambda x: int(x['id']))

        for row_don in sorted_rows_don:
                
            data_ctd = []
            total_price = 0
            total_goods = 0
            for row_ctd in sorted_rows_ctd:
                if row_ctd['id_don'] == row_don['id']:
                    data_ctd.append(row_ctd['id_kho'])
                    total_price = total_price + (int(row_ctd['gia']) * int(row_ctd['so_luong']))
                    total_goods = total_goods + int(row_ctd['so_luong'])

            self.show_item_M3(row_don['id'], row_don['thoi_gian'], total_goods, total_price)

            for row_ctd in sorted_rows_ctd:
                if row_ctd['id_don'] == row_don['id']:
                    self.show_goods_M3(row_don['id'], row_ctd['ten'], row_ctd['anh'], row_ctd['gia'], row_ctd['so_luong'], (int(row_ctd['gia']) * int(row_ctd['so_luong'])))
            
            self.end_goods_M3(row_don['id'])
        self.end_item_M3()

    def end_item_M3(self):
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)

    def end_goods_M3(self, id):
        spacerItem13 = QtWidgets.QSpacerItem(20, 51, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.list_goods_items_array[int(id)].addItem(spacerItem13)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                layout.removeWidget(widget)
                widget.deleteLater()