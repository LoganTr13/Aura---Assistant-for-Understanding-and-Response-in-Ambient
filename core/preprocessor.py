import unicodedata
import logging

class Preprocessor:
    def __init__(self):
        self.logger = logging.setLogger(__name__)

    def normalize(self, sentence):
        sentence_lowered = sentence.lower()
        sentence_normalized = unicodedata.normalize('NFD', sentence_lowered)
        sentence_cleaned = sentence_normalized.encode('ascii', 'ignore').decode('utf-8')
        return sentence_cleaned

    def tokenize(self, sentence):
        sentence_cleaned = normalize(sentence)
        tokens = sentence_cleaned.split()
        self.logger.debug(f'tokens cleaned: {tokens}')
        return tokens