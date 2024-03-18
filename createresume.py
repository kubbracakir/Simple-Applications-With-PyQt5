import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox, QFileDialog


class ResumeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CV")
        self.layout = QVBoxLayout()
        
        self.name_label = QLabel("Name Surname:")
        self.layout.addWidget(self.name_label)
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)
        
        self.email_label = QLabel("E-mail:")
        self.layout.addWidget(self.email_label)
        self.email_input = QLineEdit()
        self.layout.addWidget(self.email_input)
        
        self.phone_label = QLabel("Telephone:")
        self.layout.addWidget(self.phone_label)
        self.phone_input = QLineEdit()
        self.layout.addWidget(self.phone_input)
        
        self.address_label = QLabel("Adress:")
        self.layout.addWidget(self.address_label)
        self.address_input = QLineEdit()
        self.layout.addWidget(self.address_input)
        
        self.skills_label = QLabel("Ability:")
        self.layout.addWidget(self.skills_label)
        self.skills_input = QTextEdit()
        self.layout.addWidget(self.skills_input)
        
        self.experience_label = QLabel("Experience:")
        self.layout.addWidget(self.experience_label)
        self.experience_input = QTextEdit()
        self.layout.addWidget(self.experience_input)
        
        button_layout = QHBoxLayout()
        
        self.save_button = QPushButton("Save CV")
        self.save_button.clicked.connect(self.save_resume)
        button_layout.addWidget(self.save_button)
        
        self.generate_button = QPushButton("Create CV")
        self.generate_button.clicked.connect(self.generate_resume)
        button_layout.addWidget(self.generate_button)
        
        self.layout.addLayout(button_layout)
        
        self.setLayout(self.layout)
    
    def generate_resume(self):
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()
        skills = self.skills_input.toPlainText()
        experience = self.experience_input.toPlainText()
        
        resume_text = f"Name Surname: {name}\n\n"
        resume_text += f"E-maşl: {email}\n"
        resume_text += f"Telephone: {phone}\n"
        resume_text += f"Adress: {address}\n\n"
        resume_text += "Ability:\n"
        resume_text += skills + "\n\n"
        resume_text += "Experience:\n"
        resume_text += experience
        
        QMessageBox.information(self, "Resume", resume_text)
    
    def save_resume(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save CV", "", "Metin Dosyaları (*.txt)")
        if file_path:
            name = self.name_input.text()
            email = self.email_input.text()
            phone = self.phone_input.text()
            address = self.address_input.text()
            skills = self.skills_input.toPlainText()
            experience = self.experience_input.toPlainText()
            
            resume_text = f"Name Surname: {name}\n\n"
            resume_text += f"E-mail: {email}\n"
            resume_text += f"Telephone: {phone}\n"
            resume_text += f"Adress: {address}\n\n"
            resume_text += "Ability:\n"
            resume_text += skills + "\n\n"
            resume_text += "Experience:\n"
            resume_text += experience
            
            with open(file_path, "w") as file:
                file.write(resume_text)
            QMessageBox.information(self, "Success", "Resume saved successfully!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    resume_app = ResumeGenerator()
    resume_app.show()
    sys.exit(app.exec_())