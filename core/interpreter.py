from core.trie import Trie
from core.preprocessor import Preprocessor
import logging
import json
import os

class Interpreter():
    def __init__(self):
        self.dict = {}
        self.logger = logging.getLogger(__name__)
        self.pre = Preprocessor()
        self.logger.debug("Preprocessor type: %s", type(self.pre))
        
    def setup(self,default_path='./data'):
        self._load_data(default_path)        

        verbs = self.dict.get('verbs', {})
        targets = self.dict.get('targets', {})

        self.trie_verbs = self._build_trie_synonyms(verbs)
        self.trie_targets = self._build_trie(targets)

    def understand(self,sentence):
        tokens = self.pre.process(sentence)
        verb_key = ''
        target_key = ''
        for token in tokens:

            verb = self.trie_verbs.search(token)
            target = self.trie_targets.search(token)

            if verb:
                verb_key = verb
            
            if target:
                target_key = target
        if not verb_key and not target_key:
            return None 
        self.logger.debug('Matched Verb = %s, Target = %s',verb_key,target_key)
        return {"verb": verb_key, "target": target_key}

    def _load_data(self,path):
        for filename in os.listdir(path):
            if filename.endswith('.json'):
                key = os.path.splitext(filename)[0]
                with open(os.path.join(path, filename), encoding='utf-8') as f:
                    self.dict[key] = json.load(f)
                    self.logger.debug('file %s loaded sucessfully.',filename)

    def _build_trie_synonyms(self, data):
        trie = Trie()
        for verb, synonyms in data.items():
            verb_lowercase = verb.lower()
            trie.insert(verb_lowercase,verb_lowercase)
            for sentence in synonyms:
                trie.insert(sentence.lower(),verb_lowercase)
        self.logger.debug('Synonyms Trie created.')
        return trie

    def _build_trie(self, data):
        trie = Trie()
        for word in data:
            trie.insert(word.lower())
        self.logger.debug('Trie created.')
        return trie