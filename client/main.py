from PySide6.QtWidgets import QApplication
from widget import Widget
import sys

app = QApplication(sys.argv)

widget = Widget()
# widget.resize(500,500)
widget.showFullScreen()

app.exec()