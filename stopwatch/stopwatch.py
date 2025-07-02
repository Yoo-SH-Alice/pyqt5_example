import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QTime, QStringListModel

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        # 작성한 ui를 로드
        self.ui = uic.loadUi("stopwatch\stopWatch.ui", self)

        # 타이머가 동작 중인지 여부를 확인하는 변수
        self.is_running = False
        self.time = QTime(0, 0, 0, 0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)

        # ui에 작성된 버튼 이벤트와 파이썬 내부에 함수를 연결
        self.ui.btn1.clicked.connect(self.start_stopwatch)
        self.ui.btn2.clicked.connect(self.stop_stopwatch)
        self.ui.pushButton.clicked.connect(self.reset_stopwatch) # 'pushButton' is the Reset button from UI


        self.model = QStringListModel()
        self.records = []
        self.ui.listView.setModel(self.model) # Use 'listView' from UI file

        self.reset_stopwatch()
        self.show()

    # Start버튼을 클릭했을때 실행되는 메소드
    def start_stopwatch(self):
        # is_running 타이머가 작동하지 않으면 
        if not self.is_running:
            # 타이머 시작
            self.timer.start(1)
            self.is_running = True

    # Stop버튼을 클릭했을때 실행되는 메소드
    def stop_stopwatch(self):
        # 타이머가 작동중이라면
        if self.is_running:
            # 타이머를 정지
            self.timer.stop()
            # 타이머 동작 상태를 멈춤(False) 상태로 표시
            self.is_running = False
            self.records.append(self.time.toString("mm:ss.zzz"))
            self.model.setStringList(self.records)

    # Reset버튼을 클릭했을때 실행되는 메소드
    def reset_stopwatch(self):

        # 타이머가 멈춰있어야하므로 stor을 실행
        self.timer.stop()
         # 타이머 동작 상태를 멈춤(False) 상태로 표시
        self.is_running = False
        self.time.setHMS(0, 0, 0, 0)
        # lcd에 출력되는 형식을 지정하고 시간을 출력
        self.ui.lcdNumber.display(self.time.toString("mm:ss.zzz"))
        self.records = []
        self.model.setStringList(self.records)

    def showTime(self):
        # 밀리초 만큼 더해서 값을 갱신
        self.time = self.time.addMSecs(1)
        self.time.setHMS(0, 0, 0, 0)
        # lcd에 출력되는 형식을 지정하고 시간을 출력
        self.ui.lcdNumber.display(self.time.toString("mm:ss.zzz"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StopWatch()
    sys.exit(app.exec_())
