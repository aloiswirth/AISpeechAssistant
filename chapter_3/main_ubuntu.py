import pyttsx3
from loguru import logger
import logging

logging.getLogger("comtypes._comobject").setLevel(logging.WARNING)


class VoiceAssistant:

    def __init__(self):
        logger.error("VoiceAssistant wird initialisiert")
        logger.debug("Initialisiere Sprachausgabes")
        self.tts = pyttsx3.init()

        # Ausgabe aller Sprachengines und Sprachpakete
        voices = self.tts.getProperty("voices")
        for voice in voices:
            logger.info(voice)

        # Set the voice by index from voices array
        self.tts.setProperty("voice", voices[0].id)
        self.tts.say("Hallo, ich bin Hedda. Initialisierung abgeschlossen.")
        self.tts.runAndWait()
        logger.debug("Sprach-Initialisierung abgeschlossen")

    def run(self):
        logger.debug("Now run() started")
        self.tts.say("Now run() started for the first time")
        self.tts.runAndWait()
        self.tts.say("Ich bin bereit. Wie kann ich Ihnen helfen?")
        self.tts.runAndWait()
        logger.debug("Los geht es")


if __name__ == "__main__":
    # sudo apt-get install libespeak1 was necessary to install espeak
    va = VoiceAssistant()
    va.run()
    logger.info("VoiceAssistant gestartet")
