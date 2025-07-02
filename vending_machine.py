import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class VendingMachineApp(QWidget):
    def __init__(self):
        super().__init__()
        self.drinks = [
            {'name': '칠성사이다', 'price': 1700, 'stock': 10, 'image': 'menu1.jpg', 'button': None, 'stock_label': None},
            {'name': '코카콜라', 'price': 1700, 'stock': 10, 'image': 'menu2.jpg', 'button': None, 'stock_label': None},
            {'name': '펩시 제로', 'price': 1600, 'stock': 10, 'image': 'menu3.jpg', 'button': None, 'stock_label': None},
            {'name': '스프라이트', 'price': 1600, 'stock': 10, 'image': 'menu4.jpg', 'button': None, 'stock_label': None}
        ]
        self.total_amount = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('음료수 자동판매기')

        main_vbox = QVBoxLayout()
        drinks_hbox = QHBoxLayout()

        for i, drink in enumerate(self.drinks):
            vbox = QVBoxLayout()

            # 음료 이미지
            pixmap = QPixmap(drink['image'])
            img_label = QLabel()
            img_label.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio))
            img_label.setAlignment(Qt.AlignCenter)
            vbox.addWidget(img_label)

            # 음료 이름 및 가격
            name_label = QLabel(f"{drink['name']}\n{drink['price']}원")
            name_label.setAlignment(Qt.AlignCenter)
            vbox.addWidget(name_label)

            # 재고
            stock_label = QLabel(f"재고: {drink['stock']}개")
            stock_label.setAlignment(Qt.AlignCenter)
            self.drinks[i]['stock_label'] = stock_label
            vbox.addWidget(stock_label)

            # 선택 버튼
            button = QPushButton('선택', self)
            button.clicked.connect(lambda checked, idx=i: self.select_drink(idx))
            self.drinks[i]['button'] = button
            vbox.addWidget(button)
            
            drinks_hbox.addLayout(vbox)

        main_vbox.addLayout(drinks_hbox)

        # 총 금액 표시
        self.total_label = QLabel(f'총 금액: {self.total_amount}원')
        self.total_label.setAlignment(Qt.AlignCenter)
        font = self.total_label.font()
        font.setPointSize(16)
        self.total_label.setFont(font)
        main_vbox.addWidget(self.total_label)
        
        # 초기화 버튼
        reset_button = QPushButton('주문 초기화', self)
        reset_button.clicked.connect(self.reset_order)
        main_vbox.addWidget(reset_button)

        self.setLayout(main_vbox)
        self.setGeometry(300, 300, 700, 400)
        self.show()

    def select_drink(self, idx):
        drink = self.drinks[idx]
        if drink['stock'] > 0:
            drink['stock'] -= 1
            self.total_amount += drink['price']
            
            # 화면 업데이트
            self.update_ui(idx)

            if drink['stock'] == 0:
                drink['button'].setText('선택 불가')
                drink['button'].setDisabled(True)
        else:
            QMessageBox.warning(self, '재고 없음', '해당 음료의 재고가 모두 소진되었습니다.')

    def update_ui(self, idx):
        drink = self.drinks[idx]
        drink['stock_label'].setText(f"재고: {drink['stock']}개")
        self.total_label.setText(f'총 금액: {self.total_amount}원')

    def reset_order(self):
        self.total_amount = 0
        for i, drink in enumerate(self.drinks):
            drink['stock'] = 10
            drink['button'].setText('선택')
            drink['button'].setDisabled(False)
            self.update_ui(i)
        self.total_label.setText(f'총 금액: {self.total_amount}원')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VendingMachineApp()
    sys.exit(app.exec_())