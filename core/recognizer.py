import speech_recognition as sr 
import logging

class Recognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.source = sr.Microphone()
        self.logger = logging.setLogger(__name__)
    
    def start(self):
        with self.source as src:
            self.logger.debug("Capturing Audio...")
            self.recognizer.adjust_for_ambient_noise(src, duration=0.5)
            return self._capture_command(src)
        
    def _capture_command(self, src):
        while True:
            sentence = self._listening(src)
            self.logger.debug("Sentence Input: " + sentence)
            if not sentence:
                continue
            if self._call_command(sentence):
                return sentence
                
    def _call_command(self, sentence):
        sentence = sentence.split()
        return "aura" in sentence

    def _listening(self, src):
        rec = self.recognizer
        try: 
            audio = rec.listen(src, timeout=3, phrase_time_limit=7)
            return rec.recognize_google(audio, language='pt-BR')
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except Exception as e:
            self.logger.error("Sorry, during audio capture the following error occurred: " + e)
            return None