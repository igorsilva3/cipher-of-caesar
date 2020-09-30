from app.program import Handler
from PySide2.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    MainWindow = Handler()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
