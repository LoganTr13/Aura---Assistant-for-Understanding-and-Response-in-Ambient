from core.recognizer import Recognizer
from core.interpreter import Interpreter
from datetime import datetime
import os
import logging

def setup_log():
    log_filename = datetime.now().strftime("system_log_%Y-%m-%d_%H-%M-%S.log")
    log_path = f"./logs/{log_filename}"
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
                logging.StreamHandler(),
                logging.FileHandler(log_path, encoding="utf-8",mode="w")
            ]
    )

def main():
    setup_log()
    logger = logging.getLogger(__name__)
    microphone = Recognizer()
    performer = Interpreter()

    performer.setup()
    while True:
        logger.info("System running, wait for input of microphone...")
        sentence = microphone.start()
        if not sentence:
            continue
        command = performer.understand(sentence)
        if not command:
            continue
        print(command)

if __name__ == "__main__":
    main()