import requests, os
from PySide6.QtCore import QThread, Signal




class DownloadThread(QThread):
    """Thread para baixar beatmaps sem travar a interface"""

    progress = Signal(int)
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, beatmap_id: int, download_path: str, filename: str):
        super().__init__()
        self.beatmap_id = beatmap_id
        self.download_path = download_path
        self.filename = filename

    def run(self):
        try:
            url = f"https://osu.ppy.sh/beatmapsets/{self.beatmap_id}/download"
            
            #Faz o request com stream para mostrar progresso
            response = requests.get(url, stream=True, timeout=30, allow_redirects=True)

            #Verifica se o download foi bem-sucedido
            if response.status_code != 200:
                self.error.emit(f"Erro ao baixar: Status {response.status_code}")
                return
            
            #Pega o tamanho total do arquivo
            total_size = int(response.headers.get('content-lenght', 0))

            #Caminho completo do arquivo
            filepath = os.path.join(self.download_path, self.filename)

            #Baixa o arquivo em chunks
            downloaded = 0
            chunk_size = 8192

            with open(filepath, 'wb') as file:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        file.write(chunk)
                        downloaded += len(chunk)
                        
                        #Emite progresso
                        if total_size > 0:
                            progress_percent = int((downloaded / total_size)) * 100
                            self.progress.emit(progress_percent)
            
            self.finished.emit(filepath)

        except Exception as e:
            self.error.emit(f'Erro no download {str(e)}')
