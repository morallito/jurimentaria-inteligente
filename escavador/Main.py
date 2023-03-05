from br.cefetmg.tools.system_logger import configure_scraper_logger
from br.cefetmg.stf.stf_scrapper import perform_simple_stf_search
import logging


configure_scraper_logger(debug_file='systemMessages.log', error_file='systemError.log')

logger = logging.getLogger('scraper')

logger.info('Starting the scrapper.')

perform_simple_stf_search('lei')
