import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.layout = QVBoxLayout()
        
        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)
        self.layout.addWidget(self.result_display)
        
        button_layout = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+")
        ]
        
        for row in button_layout:
            row_layout = QHBoxLayout()
            for text in row:
                button = QPushButton(text)
                if text == "=":
                    button.clicked.connect(self.calculate)
                else:
                    button.clicked.connect(self.add_to_display)
                row_layout.addWidget(button)
            self.layout.addLayout(row_layout)
        
        clear_button = QPushButton("C")
        clear_button.clicked.connect(self.clear_display)
        self.layout.addWidget(clear_button)
        
        self.setLayout(self.layout)
    
    def add_to_display(self):
        sender = self.sender()
        self.result_display.setText(self.result_display.text() + sender.text())
        
    def calculate(self):
        try:
            result = eval(self.result_display.text())
            self.result_display.setText(str(result))
        except Exception as e:
            self.result_display.setText("Error")
        
    def clear_display(self):
        self.result_display.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())