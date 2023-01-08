"""PySide6 Multimedia player example"""

import sys
from PySide6.QtCore import QStandardPaths, Qt, Slot, QThread, QObject, Signal
from PySide6.QtGui import QAction, QIcon, QKeySequence, QScreen
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
    QMainWindow, QSlider, QStyle, QToolBar, QWidget, QPushButton, QVBoxLayout, QHBoxLayout)
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget

import os
from model import runMLAgent
# Step 1: Create a worker class
class Worker(QObject):
    finished = Signal()
    # progress = pyqtSignal(int)
    def __init__(self, logsText, mainWidget):
        super().__init__()
        self.logsText = logsText
        self.mainWidget = mainWidget

    def run(self):
        print("thread 1")
        isSus = runMLAgent()
        if(isSus):
            self.logsText.append("Suspicious activity detected notifying user\n")
        self.mainWidget.send_request()
        self.finished.emit()
class PlayerWidget(QWidget):

    def __init__(self, logsText, mainWidget):
        super().__init__()
        self.thread = QThread()
        self.mainWidget = mainWidget
        playerLayout = QVBoxLayout()
        playBackLayout = QHBoxLayout()
        self.player = QMediaPlayer()
        self.playButton = QPushButton("Run WatchDog")
        self.playButton.clicked.connect(self.handlePlay)
        self.stopButton = QPushButton("Stop WatchDog")
        self.stopButton.clicked.connect(self.player.stop)
        self.videoWidget = QVideoWidget()
        self.player.setSource(os.path.abspath("theft.mp4"))
        self.player.setVideoOutput(self.videoWidget)
        self.logsText = logsText
        playerLayout.addWidget(self.videoWidget)
        playBackLayout.addWidget(self.playButton)
        playBackLayout.addWidget(self.stopButton)
        playerLayout.addLayout(playBackLayout)
        self.setLayout(playerLayout)
    
    def handlePlay(self):
        
        #TODO: Run model.py
        #TODO: send post request to server 
        #TODO: add the log
        self.player.play()
        self.logsText.append("Watchdog video and AI started\n")
        self.worker = Worker(self.logsText, self.mainWidget)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

        
        
    def handleStop(self):
        self.player.stop()
        self.logsText.append("Watchdog video and AI stopped\n")
        
        
        
        
    
        
        

