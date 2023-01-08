from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit,QSpacerItem, QMainWindow, QTextEdit, QSizePolicy
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QTextCursor
from player import PlayerWidget



class Settings(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("Watchdog")


        widget_settings = QWidget()
        label_email = QLabel("Email:")
        self.line_edit_email = QLineEdit(self)
        label_phone = QLabel("Phone:")
        self.line_edit_phone = QLineEdit(self)
        form_container = QVBoxLayout()
        email_layout = QHBoxLayout()

        email_layout.addWidget(label_email)
        email_layout.addWidget(self.line_edit_email)
        phone_layout = QHBoxLayout()
        phone_layout.addWidget(label_phone)
        phone_layout.addWidget(self.line_edit_phone)
        form_container.addLayout(email_layout)
        form_container.addLayout(phone_layout)
        self.saveButton = QPushButton("Save")
        self.saveButton.clicked.connect(self.save_clicked)
        form_container.addWidget(self.saveButton)
        widget_settings.setLayout(form_container)
        
        self.setLayout(form_container)


    def save_clicked(self):
        mail = self.line_edit_email.text()
        number = self.line_edit_phone.text()
        self.line_edit_email.clear()
        self.line_edit_phone.clear()
        with open('info', 'w') as f:
            f.write(mail)
            f.write('\n')
            f.write(number)
        