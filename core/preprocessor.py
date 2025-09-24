import unicodedata

class Preprocessor:
    def __init__(self):

    def normalize(self, sentence):
        sentence_lowered = sentence.lower()
        sentence_normalized = unicodedata.normalize("NFD", sentence_lowered)
        sentence_cleaned = sentence_normalized.encode("ascii", "ignore").decode("utf-8")
        return sentence_cleaned

    def tokenize(self, sentence):
        sentence_cleaned = normalize(sentence)
        return sentence_cleaned.split()