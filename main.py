from core.recognizer import Recognizer
from core.interpreter import Interpreter
from datetime import datetime
import os
import logging

def setup_log():
    log_filename = datetime.now().strftime("system_log_%Y-%m-%d_%H-%M-%S.log")
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
                logging.StreamHandler(),
                logging.FileHandler(log_filename, encoding="utf-8",mode="w")
            ]
    )

def main():
    setup_log()
    logger = logging.getLogger(__name__)
    microphone = Recognizer()
    interpretador = Interpreter()
    while True:
        logger.info("System running, wait for input of microphone...")
        sentence = microphone.start()
        

if __name__ == "__main__":
    main()