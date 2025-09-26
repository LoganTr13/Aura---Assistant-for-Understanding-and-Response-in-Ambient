from core.trie import Trie
import logging
import json
import os

class Interpreter():
    def __init__(self):
        self.dict = {}
        self.trie_dict = {}
        self.logger = logging.getLogger(__name__)
        
    def start(self,folder='./data'):
        self._load_data(folder)
        
        verbs_data = self.dict.get('verbs')
        if not isinstance(verb_data, dict):
            self.logger.critical('Verbs.json not found or format invalid')
            return
        verbs_trie = self._build_trie_synonyms(verbs_data)
        self.trie_dict = verb_trie
        self.logger.info('Trie verbs created.')

    def _load_data(self,folder):
        for filename in os.listdir(folder):
            if filename.endswith('.json'):
                key = os.path.splitext(filename)[0]
                with open(os.path.join(folder, filename), encoding='utf-8') as f:
                    self.logger.debug(f'file {filename} loaded sucessfully.')
                    self.dict[key] = json.load(f)

    def _build_trie_synonyms(self, data):
        trie = Trie()
        for verb, synonyms in data.items():
            verb_lowercase = verb.lower()
            trie.insert(verb_lowercase,verb_lowercase)
            for sentence in synonyms:
                trie.insert(sentence.lower(),verb_lowercase)
        return trie

    def _build_trie(self, data):
        trie = Trie()
        for word in data.items():
            trie.insert(word.lower())
        return trie