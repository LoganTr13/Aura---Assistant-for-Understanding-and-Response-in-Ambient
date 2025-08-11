import speech_recognition as sr 

class Recognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.source = sr.Microphone()
    
    def start(self):
        with self.source as src:
            self.recognizer.adjust_for_ambient_noise(src, duration=0.5)
            return self._capture_command(src)
        
    def _capture_command(self, src):
        while True:
            words = self._listening(src)
            if not words:
                continue
            if self._call_command(words.split()):
                return words
                
    def _call_command(self, words):
        return "aura" in words

    def _listening(self, src):
        rec = self.recognizer
        try: 
            audio = rec.listen(src, timeout=3, phrase_time_limit=7)
            return rec.recognize_google(audio, language='pt-BR').lower()
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except Exception as e:
            print("Me desculpe, durante o aguardo ocorreu o seguinte erro: " + e)
            return None