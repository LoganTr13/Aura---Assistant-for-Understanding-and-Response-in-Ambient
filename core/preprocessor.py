import unicodedata
import logging
import re

class Preprocessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def normalize(self, sentence):
        text = sentence.lower()
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore').decode('utf-8')
        return text

    def tokenize(self, sentence):
        tokens = re.findall(r'\w+',sentence)
        self.logger.debug(f'tokens cleaned: {tokens}')
        return tokens

    def process(self, sentence):
        text = self.normalize(sentence)
        tokens = self.tokenize(text)
        return tokens