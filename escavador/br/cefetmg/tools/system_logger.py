import logging


def configure_scraper_logger(debug_file: str, error_file: str):
    try:
        logger = logging.getLogger('scraper')
        logger.setLevel(logging.DEBUG)
        # Info and debug log file handler
        info_handler = logging.FileHandler(debug_file)
        info_handler.setLevel(logging.DEBUG)

        # Error log file handler
        error_handler = logging.FileHandler(error_file)
        error_handler.setLevel(logging.ERROR)

        # Add handlers to br.tools
        logger.addHandler(info_handler)
        logger.addHandler(error_handler)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Set formatter for each handler
        info_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)

    except Exception as e:
        logging.error(f'Unexpected error while configuring the logger: {e}')


