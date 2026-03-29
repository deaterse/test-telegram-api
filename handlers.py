class Handler:
    def __init__(self, func, handle_text):
        self.__func = func
        self.__handle_text = handle_text

    def can_handle(self, text):
        if self.__handle_text is not None:
            return text == self.__handle_text
        else:
            return True

    def handle(self, chat_id):
        return self.__func(chat_id)