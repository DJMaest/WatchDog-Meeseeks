from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit,QSpacerItem, QMainWindow, QTextEdit, QSizePolicy
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtDesigner import QDesignerFormWindowCursorInterface
from PySide6.QtGui import QTextCursor
from player import PlayerWidget
from settings import Settings

class Widget(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("Watchdog")

        tab_widget = QTabWidget(self)

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
        tab_widget.addTab(widget_home,"Home")
        tab_widget.addTab(settingsWidget,"Settings")
        
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)
