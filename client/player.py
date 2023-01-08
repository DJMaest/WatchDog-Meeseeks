"""PySide6 Multimedia player example"""

import sys
from PySide6.QtCore import QStandardPaths, Qt, Slot
from PySide6.QtGui import QAction, QIcon, QKeySequence, QScreen
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
    QMainWindow, QSlider, QStyle, QToolBar, QWidget, QPushButton, QVBoxLayout, QHBoxLayout)
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget

class PlayerWidget(QWidget):

    def __init__(self):
        super().__init__()
        playerLayout = QVBoxLayout()
        playBackLayout = QHBoxLayout()
        self.player = QMediaPlayer()
        self.playButton = QPushButton("Run WatchDog")
        self.playButton.clicked.connect(self.player.play)
        self.stopButton = QPushButton("Stop WatchDog")
        self.stopButton.clicked.connect(self.player.stop)
        self.videoWidget = QVideoWidget()
        self.player.setSource("theft.mp4")
        self.player.setVideoOutput(self.videoWidget)
        playerLayout.addWidget(self.videoWidget)
        playBackLayout.addWidget(self.playButton)
        playBackLayout.addWidget(self.stopButton)
        playerLayout.addLayout(playBackLayout)
        self.setLayout(playerLayout)
        
        
        
    
        
        

