from core.recognizer import Recognizer
from core.interpreter import Interpreter
import os

microphone = Recognizer()
interpretador = Interpreter()
os.system('cls')
while True:
    print("rodando...")
    phrase = microphone.start()
    if phrase:
        print(phrase)

