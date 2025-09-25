from core.recognizer import Recognizer
from core.interpreter import Interpreter
import os
import logging

def setup_log():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
                logging.StreamHandler(),
                logging.FileHandler("system_log_%(asctime)s.log", encoding="utf-8")
            ]
    )

def main():
    setup_log()
    logger = logging.getLogger(__name__)
    microphone = Recognizer()
    interpretador = Interpreter()
    os.system('cls')
    while True:
        logger.info("System running, wait for input of microphone...")
        sentence = microphone.start()
        

if __name__ == "__main__":
    main()