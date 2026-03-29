from handlers import Handler
import time
import requests

class Bot:
    def __init__(self, token):
        self.__token = token
        self.__url =  f'https://api.telegram.org/bot{self.__token}'
        self.__last_id = 0
        self.__handlers = []

    def send_message(self, chat_id, text, keyboard = None):
        payload = {'chat_id': chat_id, 'text': text}
        if keyboard:
            payload['reply_markup'] = keyboard

        requests.post(f'{self.__url}/sendMessage', json=payload)

    def get_updates(self):
        params = {'offset': self.__last_id + 1, 'timeout': 30}
        request = requests.get(f'{self.__url}/getUpdates', params=params)

        return request.json()

    def message(self, text=None):
        def wrapper(func):
            self.add_handler(Handler(func, text))
        return wrapper

    def add_handler(self, handler):
        if handler not in self.__handlers:
            self.__handlers.append(handler)
        else:
            print('This handler is already exists.')

    def start(self):
        while True:
            updates = self.get_updates()
            if updates.get("result"):
                for update in updates["result"]:
                    self.__last_id = update["update_id"]
                    if "message" in update:
                        message = update["message"]
                        chat_id = message["chat"]["id"]
                        text = message["text"]

                        for handler in self.__handlers:
                            if handler.can_handle(text):
                                handler.handle(message)
            time.sleep(0.5)