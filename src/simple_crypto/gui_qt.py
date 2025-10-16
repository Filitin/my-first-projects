from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QApplication
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from pathlib import Path
from .core import encrypt, decrypt


class MainWindow(QWidget):
    def __init__(self):
        
        

        super().__init__()
        self.setWindowTitle("Simple Cryoto (Qt)")
        self.resize(740, 480)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(10)
        layout.addLayout(row)

        row.addWidget(QLabel("Key 0 - 255:"))
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("example -3")
        self.key_input.setMaxLength(3)
        self.key_input.setFixedWidth(80)
        self.key_input.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        row.addWidget(self.key_input,)

        self.btn_encrypt = QPushButton("Encrypt")
        row.addWidget(self.btn_encrypt)
        self.btn_encrypt.clicked.connect(self.on_encrypt)

        self.btn_decrypt = QPushButton("Decrypt")
        row.addWidget(self.btn_decrypt)
        self.btn_decrypt.clicked.connect(self.on_decrypt)


        row.addStretch(1)

        row2 = QHBoxLayout()
        layout.addLayout(row2)

        row2.addWidget(QLabel("File:"))
        self.file_input = QLineEdit() 
        self.file_input.setReadOnly(True)
        row2.addWidget(self.file_input)
        self.btn_browse = QPushButton("Browse")
        row2.addWidget(self.btn_browse)
        
        self.file_input.setFixedWidth(300)
        self.file_input.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.btn_browse.setFixedWidth(100)
        self.btn_browse.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        row2.addStretch(1)

        self.btn_browse.clicked.connect(self.on_browse)
        

    def on_decrypt(self):
        path = self.file_input.text().strip()
        key_txt = self.key_input.text().strip()
        if not path:
            QMessageBox.warning(self,"Error", "Please select a file and enter a key")
            return
        key = int(key_txt)
        if not (0 <= key <= 255):
            QMessageBox.warning(self,"Error", "Please enter a key")
            return
        data = Path(path).read_bytes()
        out = decrypt(data,key)

        scr = Path(path)
        suggested = scr.with_name(scr.stem + ".decrypted" + scr.suffix)
        dst_path, _ = QFileDialog.getSaveFileName(self,"Save File", str(suggested))

        

    def on_encrypt(self):
        path = self.file_input.text().strip()
        key_txt = self.key_input.text().strip()
        if not path:
            QMessageBox.warning(self,"Error", "Please select a file and enter a key")
            return
        key = int(key_txt)
        if not (0 <= key <= 255):
            QMessageBox.warning(self,"Error", "Please enter a key")
            return
        data = Path(path).read_bytes()
        out = encrypt(data,key)

        src =Path(path)
        suggested = src.with_name(src.stem + ".encrypted" + src.suffix)
        dst_path, _ = QFileDialog.getSaveFileName(self,"Save File", str(suggested))
        if not dst_path:
            return
        Path(dst_path).write_bytes(out)




    def on_browse(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if path:
            self.file_input.setText(path)





def run():
    app = QApplication([])
    win = MainWindow()
    win.show()
    return app.exec()
