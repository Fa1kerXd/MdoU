from PySide6.QtCore import QThread, Signal
from .OsuAPIClient import OsuAPIClient


class SearchThread(QThread):
    """Thread para buscar beatmaps sem travar a interface"""
    finished = Signal(list)
    error = Signal(str)
    def __init__(self, client: (OsuAPIClient), query: str, mode: str, status: str):
        super().__init__()
        self.client = client
        self.query = query
        self.mode = mode if mode != "Todos" else None
        self.status = status

    
    def run(self):
        try:
            results = self.client.search_beatmaps(self.query, self.mode, self.status)
            self.finished.emit(results)
        except Exception as e:
            self.error.emit(str(e))
    