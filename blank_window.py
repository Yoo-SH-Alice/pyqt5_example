## Ex 3-1. 창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget

# QWidget부모 클래스를 상속 받아서 MyApp이라는 클래스를 생성합니다
class MyApp(QWidget):

    # 생성자 함수 
    # 인스턴스 생성시 자동 호출됨
    # self 클래스 자기자신을 가르킴
    def __init__(self): 
        super().__init__()
        # super는 부모클래스. 부모클래스의 init함수를 추가함 
        # 자기 클래스 안에 initUI 메소드를 호출
        self.initUI()

    def initUI(self):
        #창의 이름을 설정
        self.setWindowTitle('My First Application') 
        # 윈도우 창을 띄우는 위치를 설정
        self.move(1000, 100)
        # 윈도우 사이즈를 설정
        self.resize(400, 400)
        # 창을 띄움
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp() # 창을 하나 띄운다
   sys.exit(app.exec_())