# PyQt5 Qlabels
import sys  # (system)
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel  # Qlabel--> Helps to display the text and images
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt   # Used for alingment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(700,300,500,500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Times New Roman",30))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: Lightgreen;"
                            "background-color : Grey;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        #label.setAlignment(Qt.AlignTop)  # VETICALLY TOP
        #label.setAlignment(Qt.AlignBottom)  # VETICALLY BOTTOM
        #label.setAlignment(Qt.AlignVCenter)  # VETICALLY CENTER

        #label.setAlignment(Qt.AlignRight)  # HORIZONTALLY RIGHT 
        #label.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY CENTER
        #label.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT  
        
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop ) # Like this we can align combining
        
     
       

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()