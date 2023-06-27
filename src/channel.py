

import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()["items"][0]
        print(channel)
        self.__channel_id = channel_id
        self.title = channel["snippet"]["title"]
        self.url = "https://www.youtube.com/channel/" + channel_id
        self.view_count = channel["statistics"]["viewCount"]

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        dict_to_print = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @staticmethod
    def get_service():
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            data = {
                "channel_id": self.channel_id
            }
            json.dump(self.__dict__, file, indent=2, ensure_ascii=False)


