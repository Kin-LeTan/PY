import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit
import pandas as pd

# Đường dẫn tới các file csv
don_csv_path = 'csv/don.csv'
chi_tiet_don_csv_path = 'csv/chi_tiet_don.csv'

# Đọc dữ liệu từ file csv
don_df = pd.read_csv(don_csv_path)
chi_tiet_don_df = pd.read_csv(chi_tiet_don_csv_path)

# Tạo ứng dụng PyQt
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Thống kê đơn hàng')

# Tạo các thành phần giao diện
label_kho = QLabel('Chọn kho:')
combo_kho = QComboBox()
combo_kho.addItem('Tất cả')
combo_kho.addItems(map(str, chi_tiet_don_df['id_kho'].unique()))

label_ngay = QLabel('Chọn ngày:')
combo_ngay = QComboBox()
combo_ngay.addItem('Tất cả')
combo_ngay.addItems(map(str, range(1, 32)))

label_nam = QLabel('Nhập năm:')
line_edit_nam = QLineEdit()

# Tạo layout
layout = QVBoxLayout()
layout.addWidget(label_kho)
layout.addWidget(combo_kho)
layout.addWidget(label_ngay)
layout.addWidget(combo_ngay)
layout.addWidget(label_nam)
layout.addWidget(line_edit_nam)

# Xử lý sự kiện khi chọn kho và ngày
def handle_selection():
    selected_kho = combo_kho.currentText()
    selected_ngay = combo_ngay.currentText()
    nam = line_edit_nam.text()

    # Lọc dữ liệu theo các giá trị đã chọn
    filtered_don_df = don_df.copy()

    if selected_kho != 'Tất cả':
        filtered_don_df = filtered_don_df[filtered_don_df['id_don'].isin(chi_tiet_don_df[chi_tiet_don_df['id_kho'] == int(selected_kho)]['id_don'])]

    if selected_ngay != 'Tất cả':
        filtered_don_df = filtered_don_df[filtered_don_df['thoi_gian'].str.contains(f'-{selected_ngay} ')]

    if nam:
        filtered_don_df = filtered_don_df[filtered_don_df['thoi_gian'].str.contains(f'{nam}-')]

    # Tính tổng giá tiền
    total = (filtered_don_df.merge(chi_tiet_don_df, on='id_don', how='left')['gia'] * filtered_don_df.merge(chi_tiet_don_df, on='id_don', how='left')['so_luong']).sum()

    # Hiển thị kết quả
    result_label.setText(f'Tổng giá tiền: {total}')

combo_kho.currentIndexChanged.connect(handle_selection)
combo_ngay.currentIndexChanged.connect(handle_selection)
line_edit_nam.textChanged.connect(handle_selection)

# Tạo label để hiển thị kết quả
result_label = QLabel('Tổng giá tiền:')
layout.addWidget(result_label)

# Thiết lập layout cho cửa sổ
window.setLayout(layout)
window.show()

# Chạy ứng dụng PyQt
sys.exit(app.exec_())