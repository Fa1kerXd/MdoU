
from typing import List, Optional
import requests
from dataclasses import dataclass



@dataclass
class BeatmapSet:
    """Representa um conjunto de beatmaps"""
    id: int
    title: str
    artist: str
    creator: str
    status: str
    preview_url: str
    cover_url: str
    play_count: int
    favourite_count: int
    bpm: float
    beatmaps_count: int








class OsuAPIClient:
    """Cliente para interagir com a API v2 do osu!"""
    
    BASE_URL = "https://osu.ppy.sh/api/v2"
    AUTH_URL = "https://osu.ppy.sh/oauth/token"
    
    def __init__(self, client_id: int, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token: Optional[str] = None
        self.session = requests.Session()
    
    def authenticate(self) -> bool:
        """Autentica usando OAuth2"""
        try:
            response = self.session.post(
                self.AUTH_URL,
                data={
                    'client_id': self.client_id,
                    'client_secret': self.client_secret,
                    'grant_type': 'client_credentials',
                    'scope': 'public'
                },
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            self.access_token = data['access_token']
            self.session.headers.update({
                'Authorization': f'Bearer {self.access_token}',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })
            return True
            
        except Exception as e:
            print(f"Erro na autenticação: {e}")
            return False
    
    def search_beatmaps(self, query: str, mode: Optional[str] = None, 
                       status: str = 'ranked') -> List[BeatmapSet]:
        """Busca beatmaps na API"""
        if not self.access_token:
            return []
        
        try:
            params = {'q': query, 's': status}
            if mode:
                params['m'] = mode
            
            response = self.session.get(
                f"{self.BASE_URL}/beatmapsets/search",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            beatmapsets = []
            
            for item in data.get('beatmapsets', []):
                beatmapset = BeatmapSet(
                    id=item['id'],
                    title=item['title'],
                    artist=item['artist'],
                    creator=item['creator'],
                    status=item['status'],
                    preview_url=item['preview_url'],
                    cover_url=item['covers']['cover'],
                    play_count=item['play_count'],
                    favourite_count=item['favourite_count'],
                    bpm=item.get('bpm', 0),
                    beatmaps_count=len(item.get('beatmaps', []))
                )
                beatmapsets.append(beatmapset)
            
            return beatmapsets
            
        except Exception as e:
            print(f"Erro ao buscar: {e}")
            return []

