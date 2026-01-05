from pathlib import Path
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, 
    QDialog, QFormLayout,
    QFileDialog
)





class ConfigDialog(QDialog):
    """Diálogo para configurar credenciais da API"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configurar API do osu!")
        self.setModal(True)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        info_label = QLabel(
            "Para usar este aplicativo, você precisa de credenciais OAuth do osu!\n\n"
            "1. Acesse: https://osu.ppy.sh/home/account/edit\n"
            "2. Vá até a seção 'OAuth'\n"
            "3. Clique em 'New OAuth Application'\n"
            "4. Preencha os dados (callback: http://localhost)\n"
            "5. Copie o Client ID e Client Secret"
        )
        info_label.setWordWrap(True)
        layout.addWidget(info_label)
        
        form_layout = QFormLayout()
        
        self.client_id_input = QLineEdit()
        self.client_id_input.setPlaceholderText("Ex: 12345")
        
        self.client_secret_input = QLineEdit()
        self.client_secret_input.setPlaceholderText("Seu Client Secret")
        self.client_secret_input.setEchoMode(QLineEdit.Password)
        
        form_layout.addRow("Client ID:", self.client_id_input)
        form_layout.addRow("Client Secret:", self.client_secret_input)
        
        layout.addLayout(form_layout)
        
        # Campo para escolher pasta de download
        download_layout = QHBoxLayout()
        self.download_path_input = QLineEdit()
        default_path = str(Path.home() / "Downloads" / "osu_beatmaps")
        self.download_path_input.setText(default_path)
        
        browse_btn = QPushButton("Escolher...")
        browse_btn.clicked.connect(self.browse_folder)
        
        download_layout.addWidget(QLabel("Pasta de Download:"))
        download_layout.addWidget(self.download_path_input)
        download_layout.addWidget(browse_btn)
        
        layout.addLayout(download_layout)
        
        buttons_layout = QHBoxLayout()
        
        ok_btn = QPushButton("Conectar")
        ok_btn.clicked.connect(self.accept)
        
        cancel_btn = QPushButton("Cancelar")
        cancel_btn.clicked.connect(self.reject)
        
        buttons_layout.addWidget(ok_btn)
        buttons_layout.addWidget(cancel_btn)
        
        layout.addLayout(buttons_layout)
    
    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Escolher Pasta de Download")
        if folder:
            self.download_path_input.setText(folder)
    
    def get_credentials(self):
        return (
            self.client_id_input.text(),
            self.client_secret_input.text(),
            self.download_path_input.text()
        )