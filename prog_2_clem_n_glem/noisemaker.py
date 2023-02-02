from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QLineEdit, 
                             QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("goobertron")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.UI()

    def UI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        #Create our widgets
        title_label = QLabel("Goober")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Brush Script MT", 30))

        description = "Use the Noise Background generator to make cool new backgrounds."
        description_label = QLabel(description)
        title_label.setFont(QFont("Courier New", 20))

        search_layout = QHBoxLayout()
        self.search_field = QLineEdit()
        search_button = QPushButton("Generate")
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(search_button)
        
        results_text = QTextEdit("      ")
        
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addLayout(search_layout)
        layout.addWidget(results_text)

def main(): 
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec()) 

if __name__ == "__main__":
    main()