import webbrowser
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel,QFrame,
    QProgressBar
)
from PySide6.QtCore import Qt
from typing import Optional
from OsuAPIClient import BeatmapSet
from DownloadThread import DownloadThread
from styles import BeatmapCardStyle

class BeatmapCard(QFrame):
    """Card que exibe informações de um beatmap"""

    def __init__(self, beatmap: (BeatmapSet), download_callback, parent=None):
        super().__init__(parent)
        self.beatmap = beatmap
        self.download_callback = download_callback
        self.download_thread = Optional[DownloadThread] = None 
        self.setup_ui()

    def setup_ui(self):
        self.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.setLineWidth(2)
        self.setMinimumHeight(140)
        self.setMaximumHeight(140)
        self.setStyleSheet(BeatmapCardStyle.beatmapcard)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        #Placeholder para imagem
        img_label = QLabel("🎵")     
        img_label.setFixedSize(100, 100)
        img_label.setAlignment(Qt.AlignCenter) 
        img_label.setStyleSheet(BeatmapCardStyle.beatmapcard_img_label)  
        layout.addWidget(img_label)

        #Informações
        info_layout = QVBoxLayout()
        
        title_label = QLabel(f"<b>{self.beatmap.title}</b>")
        title_label.setStyleSheet("font-size: 14px; color: #fff;")
        title_label.setWordWrap(True)

        artist_label = QLabel(F"Por: {self.beatmap.artist}")
        artist_label.setStyleSheet("font-size: 12px; color: #aaa;")

        creator_label = QLabel(f"Mapper: {self.beatmap.creator}")
        creator_label.setStyleSheet("font-size: 11px; color: #888;")
        
        stats_label = QLabel(
            f"▶ {self.beatmap.play_count:,} plays | "
            f"❤ {self.beatmap.favourite_count} favs | "
            f"🎼 {self.beatmap.beatmaps_count} diffs"
        )

        stats_label.setStyleSheet("font-size: 10px; color: #666;")

        info_layout.addWidget(title_label)
        info_layout.addWidget(artist_label)
        info_layout.addWidget(creator_label)
        info_layout.addWidget(stats_label)
        info_layout.addStretch()

        layout.addLayout(info_layout, 1)

        #Botões e progresso
        buttons_layout = QVBoxLayout()

        open_btn = QPushButton("Abrir no site")
        open_btn.setFixedSize(120, 30)
        open_btn.clicked.connect(self.open_in_browser)
        open_btn.setStyleSheet(BeatmapCardStyle.open_btn_style)

        self.download_btn = QPushButton("📥 Baixar")
        self.download_btn.setFixedSize(120, 30)
        self.download_btn.clicked.connect(self.start_download)
        self.download_btn.setStyleSheet(BeatmapCardStyle.start_download_btn_style)

        #Barra de progresso (inicialmente oculta)
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedSize(120,30)
        self.progress_bar.setVisible(False)
        self.progress_bar.setStyleSheet(BeatmapCardStyle.progress_bar_style)

        buttons_layout.addWidget(open_btn)
        buttons_layout.addWidget(self.download_btn)
        buttons_layout.addWidget(self.progress_bar)
        buttons_layout.addStretch()

        layout.addLayout(buttons_layout)

    def open_in_browser(self):
        url = f"https://osu.ppy.sh/beatmapsets/{self.beatmap.id}"
        webbrowser.open(url)

    def start_download(self):
        self.download_callback(self.beatmap, self)

    def update_progress(self, progress: int):
        self.progress_bar.setValue(progress)

    def show_downloading(self):
        self.download_btn.setEnabled(False)
        self.download_btn.setText("Baixando...")
        self.progress_bar.setValue(0)
    

    def reset_button(self, success: bool = False):
        self.download_btn.setEnabled(True)
        if success:
            self.download_btn.setText("✅ Concluído")
            self.download_btn.setStyleSheet(BeatmapCardStyle.reset_btn_style)
        else:
            self.download_btn.setText("📥 Baixar")
        self.progress_bar.setVisible(True)

        