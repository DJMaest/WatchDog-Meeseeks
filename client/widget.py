from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit,QSpacerItem, QMainWindow, QTextEdit, QSizePolicy
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QTextCursor
from player import PlayerWidget
from settings import Settings
import requests

class Widget(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("Watchdog")

        self.tab_widget = QTabWidget(self)

        widget_home = QWidget()
        home_layout = QHBoxLayout()

        player = PlayerWidget()
        

        self.logsText = QTextEdit()
        self.logsText.setReadOnly(True)
        self.logsText.append("He he\nhehe\nhehe\nhehe\nhehe\n")
        self.logsText.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.logsText.moveCursor(QTextCursor.End)
        home_layout.addWidget(self.logsText)
        home_layout.addWidget(player)
        widget_home.setLayout(home_layout)        
        settingsWidget = Settings()

        #Add tabs to widget
        self.tab_widget.addTab(widget_home,"Home")
        self.tab_widget.addTab(settingsWidget,"Settings")
        settingsWidget.saveButton.clicked.connect(self.back_tab)
        
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)

        self.setLayout(layout)

    def back_tab(self):
        cur_index = self.tab_widget.currentIndex()
        if cur_index > 0:
            self.tab_widget.setCurrentIndex(cur_index-1)
        #self.send_request()

    def send_request(self):
        url = 'http://localhost:3000/notification'
        f = open("info", "r")
        listItems = f.read().splitlines()
        mail = listItems[0]
        number = listItems[1]
        data= {
            "email": mail,
            "phoneNumber": int(number)
        }
        requests.post(url, json = data)