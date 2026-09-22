import logging


class Logger:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("bot.log"),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger(__name__)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


if __name__ == "__main__":
    logger = Logger()

    logger.info("Bot started")
    logger.warning("This is a warning")
    logger.error("Test error message")