import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTimeEdit, QMessageBox, QListWidget, QListWidgetItem, QInputDialog
from PyQt5.QtCore import QTimer, QTime, Qt


class ReminderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reminders")
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_reminders)
        
        self.layout = QVBoxLayout()
        
        self.reminder_label = QLabel("Set Reminder:")
        self.layout.addWidget(self.reminder_label)
        
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        self.layout.addWidget(self.time_edit)
        
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_reminder)
        self.layout.addWidget(self.add_button)
        
        self.reminder_list = QListWidget()
        self.layout.addWidget(self.reminder_list)
        
        self.setLayout(self.layout)
        
        self.load_reminders()
        self.start_timer()
    
    def add_reminder(self):
        reminder_time = self.time_edit.time()
        reminder_text, ok = QInputDialog.getText(self, "New Reminder", "Reminder Text:")
        if ok:
            reminder_item = QListWidgetItem(f"{reminder_time.toString('HH:mm')} - {reminder_text}")
            self.reminder_list.addItem(reminder_item)
            self.save_reminders()
    
    def start_timer(self):
        self.timer.start(60000)
        self.check_reminders()
    
    def check_reminders(self):
        current_time = QTime.currentTime()
        current_time_string = current_time.toString("HH:mm")
        for index in range(self.reminder_list.count()):
            item_text = self.reminder_list.item(index).text()
            reminder_time_str = item_text.split("-")[0].strip()
            if current_time_string == reminder_time_str:
                reminder_text = item_text.split("-")[1].strip()
                QMessageBox.information(self, "Reminder", reminder_text)
    
    def load_reminders(self):
        try:
            with open("reminders.txt", "r") as file:
                for line in file:
                    item = QListWidgetItem(line.strip())
                    self.reminder_list.addItem(item)
        except FileNotFoundError:
            pass
    
    def save_reminders(self):
        with open("reminders.txt", "w") as file:
            for index in range(self.reminder_list.count()):
                file.write(self.reminder_list.item(index).text() + "\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    reminder_app = ReminderApp()
    reminder_app.show()
    sys.exit(app.exec_())