import sys
import os
from pathlib import Path
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QScrollArea, 
    QComboBox, QMessageBox, QDialog,QStatusBar
    
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from typing import List, Optional
from src.ConfigDialog import ConfigDialog
from src.OsuAPIClient import OsuAPIClient, BeatmapSet
from src.SearchThread import SearchThread
from src.DownloadThread import DownloadThread
from src.BeatmapCard import BeatmapCard


ROOT = Path(__file__).parent.parent
ICON = ROOT / "assets" / "icon.png"






class MainWindow(QMainWindow):
    """Janela principal do aplicativo"""
    
    def __init__(self):
        super().__init__()
        self.client: Optional[OsuAPIClient] = None
        self.search_thread: Optional[SearchThread] = None
        self.download_path: str = ""
        self.active_downloads: List[DownloadThread] = []
        self.setup_ui()
        self.show_config_dialog()
    
    def setup_ui(self):
        self.setWindowTitle("osu! Beatmap Finder & Downloader")
        self.setMinimumSize(950, 700)
        self.setWindowIcon(QIcon(str(ICON)))
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QLabel {
                color: #fff;
            }
            QLineEdit {
                background-color: #2a2a2a;
                color: #fff;
                border: 1px solid #444;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #ff66aa;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #ff88cc;
            }
            QPushButton:disabled {
                background-color: #555;
                color: #888;
            }
            QComboBox {
                background-color: #2a2a2a;
                color: #fff;
                border: 1px solid #444;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        title_label = QLabel("🎵 osu! Beatmap Finder & Downloader")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ff66aa;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Barra de busca
        search_layout = QHBoxLayout()
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Digite o nome da música, artista ou mapper...")
        self.search_input.returnPressed.connect(self.search_beatmaps)
        
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Todos", "osu", "taiko", "fruits", "mania"])
        self.mode_combo.setFixedWidth(100)
        
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Ranked", "Qualified", "Loved", "Pending"])
        self.status_combo.setFixedWidth(120)
        
        self.search_btn = QPushButton("Buscar")
        self.search_btn.setFixedWidth(100)
        self.search_btn.clicked.connect(self.search_beatmaps)
        
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.mode_combo)
        search_layout.addWidget(self.status_combo)
        search_layout.addWidget(self.search_btn)
        
        main_layout.addLayout(search_layout)
        
        # Área de resultados
        self.results_label = QLabel("Digite algo para buscar beatmaps")
        self.results_label.setAlignment(Qt.AlignCenter)
        self.results_label.setStyleSheet("font-size: 14px; color: #888; padding: 20px;")
        main_layout.addWidget(self.results_label)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)
        
        self.results_widget = QWidget()
        self.results_layout = QVBoxLayout(self.results_widget)
        self.results_layout.setAlignment(Qt.AlignTop)
        
        scroll.setWidget(self.results_widget)
        main_layout.addWidget(scroll)
        
        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Pronto")
    
    def show_config_dialog(self):
        dialog = ConfigDialog(self)
        if dialog.exec() == QDialog.Accepted:
            client_id, client_secret, download_path = dialog.get_credentials()
            
            if not client_id or not client_secret:
                QMessageBox.warning(self, "Erro", "Credenciais não podem estar vazias!")
                sys.exit()
                return
            
            # Cria pasta de download se não existir
            self.download_path = download_path
            os.makedirs(self.download_path, exist_ok=True)
            
            try:
                self.client = OsuAPIClient(int(client_id), client_secret)
                if self.client.authenticate():
                    QMessageBox.information(
                        self, 
                        "Sucesso", 
                        f"Conectado à API do osu! ✅\n\nPasta de download:\n{self.download_path}"
                    )
                    self.status_bar.showMessage(f"Conectado | Downloads: {self.download_path}")
                else:
                    QMessageBox.critical(self, "Erro", "Falha na autenticação. Verifique suas credenciais.")
                    sys.exit()
            except ValueError:
                QMessageBox.critical(self, "Erro", "Client ID deve ser um número!")
                sys.exit()
        else:
            sys.exit()
    
    def search_beatmaps(self):
        query = self.search_input.text().strip()
        if not query:
            return
        
        if not self.client:
            QMessageBox.warning(self, "Erro", "Cliente não conectado!")
            return
        
        # Limpa resultados anteriores
        for i in reversed(range(self.results_layout.count())): 
            self.results_layout.itemAt(i).widget().setParent(None)
        
        self.results_label.setText("🔍 Buscando...")
        self.results_label.show()
        self.search_btn.setEnabled(False)
        self.status_bar.showMessage(f"Buscando por '{query}'...")
        
        # Inicia busca em thread separada
        mode = self.mode_combo.currentText()
        status = self.status_combo.currentText()
        
        self.search_thread = SearchThread(self.client, query, mode, status)
        self.search_thread.finished.connect(self.display_results)
        self.search_thread.error.connect(self.display_error)
        self.search_thread.start()
    
    def display_results(self, beatmaps: List[BeatmapSet]):
        self.search_btn.setEnabled(True)
        
        if not beatmaps:
            self.results_label.setText("❌ Nenhum beatmap encontrado")
            self.status_bar.showMessage("Nenhum resultado")
            return
        
        self.results_label.hide()
        
        for beatmap in beatmaps:
            card = BeatmapCard(beatmap, self.download_beatmap)
            self.results_layout.addWidget(card)
        
        self.status_bar.showMessage(f"Encontrados {len(beatmaps)} beatmaps | Downloads: {self.download_path}")
    
    def display_error(self, error: str):
        self.search_btn.setEnabled(True)
        self.results_label.setText(f"❌ Erro: {error}")
        self.status_bar.showMessage("Erro na busca")
        QMessageBox.critical(self, "Erro", f"Erro ao buscar: {error}")
    
    def download_beatmap(self, beatmap: BeatmapSet, card: BeatmapCard):
        """Inicia o download de um beatmap"""
        # Nome do arquivo
        safe_title = "".join(c for c in f"{beatmap.artist} - {beatmap.title}" if c.isalnum() or c in (' ', '-', '_')).strip()
        filename = f"{beatmap.id} {safe_title}.osz"
        
        # Mostra interface de download
        card.show_downloading()
        
        # Cria thread de download
        download_thread = DownloadThread(beatmap.id, self.download_path, filename)
        download_thread.progress.connect(card.update_progress)
        download_thread.finished.connect(lambda path: self.download_finished(path, card))
        download_thread.error.connect(lambda err: self.download_error(err, card))
        
        self.active_downloads.append(download_thread)
        download_thread.start()
        
        self.status_bar.showMessage(f"Baixando: {safe_title}...")
    
    def download_finished(self, filepath: str, card: BeatmapCard):
        """Callback quando download termina"""
        card.reset_button(success=True)
        self.status_bar.showMessage(f"✅ Download concluído: {os.path.basename(filepath)}")
        
        # Mostra mensagem de sucesso
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Download Concluído")
        msg.setText(f"Beatmap baixado com sucesso!\n\n{os.path.basename(filepath)}")
        msg.setStandardButtons(QMessageBox.Ok)
        
        open_folder_btn = msg.addButton("Abrir Pasta", QMessageBox.ActionRole)
        open_folder_btn.clicked.connect(lambda: self.open_download_folder())
        
        msg.exec()
    
    def download_error(self, error: str, card: BeatmapCard):
        """Callback quando há erro no download"""
        card.reset_button(success=False)
        self.status_bar.showMessage(f"❌ Erro no download")
        QMessageBox.critical(self, "Erro no Download", f"Não foi possível baixar o beatmap:\n\n{error}")
    
    def open_download_folder(self):
        """Abre a pasta de downloads"""
        if sys.platform == 'win32':
            os.startfile(self.download_path)
        elif sys.platform == 'darwin':  # macOS
            os.system(f'open "{self.download_path}"')
        else:  # Linux
            os.system(f'xdg-open "{self.download_path}"')


