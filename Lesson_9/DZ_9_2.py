class TextProcessor:
    def __init__(self):
        self._punktuation = '.,?*()"":“”'

    def __is_punktuation(self, marks):
        if marks in self._punktuation:
            return True
        else:
            return False

    def get_clean_string(self, text):
        for marks in text:
            if self.__is_punktuation(marks):
                text = text.replace(marks, "")
        return text


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Очищений текст: {}".format(self.__clean_string))
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_text(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


di = DataInterface()
t = ['The data that dialog takes in (such as a string entered into a input box) is normally, returned on standard "error".',
     'First, each line begins with the null command “:” which is a command that does nothing. Yes, really.']
ct = di.process_texts(t)
