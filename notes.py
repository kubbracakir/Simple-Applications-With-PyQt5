import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QFileDialog, QColorDialog, QFontDialog
from PyQt5.QtGui import QColor, QFont


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Renkli Not Defteri")
        self.layout = QVBoxLayout()
        
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)
        
        button_layout = QVBoxLayout()
        
        self.save_button = QPushButton("Kaydet")
        self.save_button.clicked.connect(self.save_file)
        button_layout.addWidget(self.save_button)
        
        self.open_button = QPushButton("Aç")
        self.open_button.clicked.connect(self.open_file)
        button_layout.addWidget(self.open_button)
        
        self.color_button = QPushButton("Metin Rengi")
        self.color_button.clicked.connect(self.set_text_color)
        button_layout.addWidget(self.color_button)
        
        self.font_button = QPushButton("Yazı Tipi")
        self.font_button.clicked.connect(self.set_font)
        button_layout.addWidget(self.font_button)
        
        self.layout.addLayout(button_layout)
        
        self.setLayout(self.layout)
    
    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Dosyayı Kaydet", "", "Metin Dosyaları (*.txt)")
        if file_path:
            text = self.text_edit.toPlainText()
            try:
                with open(file_path, "w") as file:
                    file.write(text)
                QMessageBox.information(self, "Başarı", "Dosya başarıyla kaydedildi!")
            except Exception as e:
                QMessageBox.warning(self, "Hata", f"Dosya kaydedilirken bir hata oluştu:\n{e}")
    
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Metin Dosyaları (*.txt)")
        if file_path:
            try:
                with open(file_path, "r") as file:
                    text = file.read()
                    self.text_edit.setPlainText(text)
            except Exception as e:
                QMessageBox.warning(self, "Hata", f"Dosya açılırken bir hata oluştu:\n{e}")
    
    def set_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)
    
    def set_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    notepad = Notepad()
    notepad.show()
    sys.exit(app.exec_())