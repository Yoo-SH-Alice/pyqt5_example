## Ex 5-2. QLabel.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 텍스트 레이블
        label1 = QLabel('First Label', self)
        # 좌우위아래 가운데 정렬
        label1.setAlignment(Qt.AlignCenter)


        # 텍스트 레이블
        label2 = QLabel('Second Label', self)
        # 좌우위아래 가운데 정렬
        label2.setAlignment(Qt.AlignVCenter)

        # 폰트 설절을 읽어와서 사이즈를 20으로 변경
        font1 = label1.font()
        font1.setPointSize(20)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        # 굵은 폰트로 변경
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
