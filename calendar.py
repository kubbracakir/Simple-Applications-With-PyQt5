import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate


class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar")
        self.layout = QVBoxLayout()
        
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.show_date)
        self.layout.addWidget(self.calendar)
        
        self.date_label = QLabel()
        self.layout.addWidget(self.date_label)
        
        self.setLayout(self.layout)
        
        
        self.show_date(self.calendar.selectedDate())
    
    def show_date(self, date):
        selected_date_str = date.toString("dd.MM.yyyy")
        self.date_label.setText(f"Selected Date: {selected_date_str}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calendar_app = CalendarApp()
    calendar_app.show()
    sys.exit(app.exec_())