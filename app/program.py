from PySide2 import QtGui, QtCore, QtWidgets
from app.gui import Ui_MainWindow
from app.cipher_caesar import Caesar

Caesar = Caesar()

class Handler(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Handler, self).__init__()
        self.setupUi(self)
        
        self.btnEncrypt.clicked.connect(
            lambda: self.encrypt()
            )
        
        self.btnDecrypt.clicked.connect(
            lambda: self.decrypt()
            )
    
    def get_text(self):
        text = str(self.INPUT_TEXT.toPlainText())
        
        return text
    
    def get_key(self):
        return int(self.key.value())
    
    def setTextOutput(self, text):
        output = str(self.OUTPUT_TEXT.setPlainText(text))
        
        return output
    
    def encrypt(self):
        text = self.get_text()
        key = self.get_key()
        
        cipher = Caesar.encrypt(text, key)
        setText = self.setTextOutput(cipher)
    
    def decrypt(self):
        cipher = self.get_text()
        key = self.get_key()
        
        text_decrypt = Caesar.decrypt(cipher, key)
        setText = self.setTextOutput(text_decrypt)
    
        

        
        
        