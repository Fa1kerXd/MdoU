import sys
import webbrowser
import os
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QScrollArea, QFrame,
    QComboBox, QMessageBox, QDialog, QFormLayout, QStatusBar,
    QProgressBar, QFileDialog
)
from PySide6.QtCore import Qt, QThread, Signal, QSize
from PySide6.QtGui import QPixmap, QIcon
import requests
from typing import List, Optional
from dataclasses import dataclass

from OsuAPIClient import OsuAPIClient
from SearchThread import SearchThread
from DownloadThread import DownloadThread


class MainWindow(QMainWindow):
    # Janela Principal do aplicativo
    def __init__(self):
        self.client: Optional[OsuAPIClient] = None

