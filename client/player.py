"""PySide6 Multimedia player example"""

import sys
from PySide6.QtCore import QStandardPaths, Qt, Slot, QUrl
from PySide6.QtGui import QAction, QIcon, QKeySequence, QScreen
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
                               QMainWindow, QSlider, QStyle, QToolBar, QWidget, QPushButton, QVBoxLayout, QHBoxLayout)
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget

import os


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
        # copy the test video into Videos directory for windows
        if sys.platform == 'win32':
            self.player.setSource(
                QUrl(QUrl("C:/Users/"+os.getenv('username') +
                          "/Videos/theft.mp4")))
        else:
            self.player.setSource(os.path.abspath("theft.mp4"))
        self.player.setVideoOutput(self.videoWidget)
        self.player.errorOccurred.connect(self._player_error)
        playerLayout.addWidget(self.videoWidget)
        playBackLayout.addWidget(self.playButton)
        playBackLayout.addWidget(self.stopButton)
        playerLayout.addLayout(playBackLayout)
        self.setLayout(playerLayout)

    def test_click(self):
        print("clicked")

    @ Slot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
