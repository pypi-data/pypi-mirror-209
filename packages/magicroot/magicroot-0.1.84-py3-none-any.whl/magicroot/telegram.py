
import requests

class Bot:
    
    def __init__(self, token) -> None:
        self.token = token

    def updates(self):
        url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        return requests.get(url).json()
    
    def send_message(self, chat_id, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={message}"
        return requests.get(url).json()
    

