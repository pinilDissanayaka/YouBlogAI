import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Youtube(object):
    def __init__(self):
        self.api_key=os.getenv("GOOGLE_API_KEY")
        
    def get_channel_statistic(self, channel_id):
                
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={self.api_key}'
        
        data=requests.get(url)
        
        
        print(data.text)