
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5 import uic

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("calc.ui", self)

        self.operands = []
        self.operation = []
        self.current_input = "0"
        self.display(self.current_input)

        # Connect number buttons
        self.ui.bnt0.clicked.connect(lambda: self.number_clicked("0"))
        self.ui.bnt1.clicked.connect(lambda: self.number_clicked("1"))
        self.ui.bnt2.clicked.connect(lambda: self.number_clicked("2"))
        self.ui.bnt3.clicked.connect(lambda: self.number_clicked("3"))
        self.ui.bnt4.clicked.connect(lambda: self.number_clicked("4"))
        self.ui.bnt5.clicked.connect(lambda: self.number_clicked("5"))
        self.ui.bnt6.clicked.connect(lambda: self.number_clicked("6"))
        self.ui.bnt7.clicked.connect(lambda: self.number_clicked("7"))
        self.ui.bnt8.clicked.connect(lambda: self.number_clicked("8"))
        self.ui.bnt9.clicked.connect(lambda: self.number_clicked("9"))

        # Connect operator buttons
        self.ui.bnt_add.clicked.connect(lambda: self.operator_clicked("+"))
        self.ui.bnt_sub.clicked.connect(lambda: self.operator_clicked("-"))
        self.ui.bnt_del.clicked.connect(lambda: self.operator_clicked("*")) # bnt_del is used as multiply
        self.ui.bnt_div.clicked.connect(lambda: self.operator_clicked("/"))

        # Connect other buttons
        self.ui.bnt_c.clicked.connect(self.clear_all)
        self.ui.bnt_ce.clicked.connect(self.clear_entry)
        self.ui.bnt_dot.clicked.connect(self.dot_clicked)
        self.ui.bnt_s.clicked.connect(self.sign_clicked)
        self.ui.bnt_result.clicked.connect(self.calculate_result)
        self.ui.bnt9_del.clicked.connect(self.del_clicked)

        self.show()

    def display(self, value):
        self.ui.lcdNumber.display(str(value))

    # 숫자를 클릭할때 해당 숫자를 인자값으로 받아 실행하는 메소드
    def number_clicked(self, number):
        #입력받은 숫자의 갯수가 5개 이상이면 경고창을 출력하고 return
        if len(self.operands) >= 5:
            QMessageBox.warning(self, "Input Error", "입력 할수있는 숫자갯수는 5개입니다")
            return
        # 0을입력했을때 
        if self.current_input == "0":
            self.current_input = number
        else:
            self.current_input += number
        self.display(self.current_input)

    # 연산자를 클릭할때 연산자 종류를 입력받아 실행하는 메소드
    def operator_clicked(self, operation):
         #입력받은 숫자의 갯수가 5개 이상이면 경고창을 출력
        if len(self.operands) >= 5:
            QMessageBox.warning(self, "Input Error", "입력 할수있는 숫자갯수는 5개입니다")
            return
        if self.current_input:
            self.operands.append(float(self.current_input))
            self.operation.append(operation)
            self.current_input = "0"

    # bnt_dot 버튼을 클릭할때 소숫점을 입역하는 메소드  
    def dot_clicked(self):
        if "." not in self.current_input:
            self.current_input += "."
        self.display(self.current_input)

    # 입력 숫자에 음수,양수 변환하는 메소드
    def sign_clicked(self):
        if self.current_input != "0":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
        self.display(self.current_input)

    # 입력값을 한자리씩 삭제하는 메소드
    def del_clicked(self):
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = "0"
        self.display(self.current_input)

    def clear_entry(self):
        self.current_input = "0"
        self.display(self.current_input)

    def clear_all(self):
        self.current_input = "0"
        self.operands = []
        self.operation = []
        self.display(self.current_input)

    # 입력한 숫자의 결과값을 출력하는 메소드
    def calculate_result(self):
        if self.current_input:
            self.operands.append(float(self.current_input))

        if len(self.operands) > 5:
            QMessageBox.warning(self, "Input Error", "입력 할수있는 숫자갯수는 5개입니다")
            self.clear_all()
            return

        # 입력받은 숫자와 연산자를 차례대로 계산하기
        result = self.operands[0]
        for i in range(len(self.operation)):
            op = self.operation[i]
            num = self.operands[i+1]
            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            elif op == "/":
                if num != 0:
                    result /= num
                else:
                    self.display("Error")
                    self.clear_all()
                    return
        
        self.display(result)
        self.current_input = str(result)
        self.operands = []
        self.operation = []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
