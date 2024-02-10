import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

class VoiceAssistant:

  def __init__(self):
    logger.error("VoiceAssistant wird initialisiert")

  def run(self):
    logger.debug("Los geht es")


if __name__ == '__main__':
  va = VoiceAssistant()
  va.run()
  logger.info("VoiceAssistant gestartet")
