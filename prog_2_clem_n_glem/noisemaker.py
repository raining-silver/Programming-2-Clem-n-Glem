from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("goobertron")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.UI()

    def UI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        label = QLabel("Hello World")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

def main(): 
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec()) 

if __name__ == "__main__":
    main()