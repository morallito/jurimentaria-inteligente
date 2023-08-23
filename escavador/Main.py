#from br.cefetmg.tools.system_logger import configure_scraper_logger
#from br.cefetmg.stf.stf_scrapper import perform_simple_stf_search
import logging

# 
# configure_scraper_logger(debug_file='systemMessages.log', error_file='systemError.log')
# 
# logger = logging.getLogger('scraper')
# 
# logger.info('Starting the scrapper.')
# 
# perform_simple_stf_search('lei')

from br.cefetmg.db.postgress_interface import PostgressInterface
from br.cefetmg.credentials import DEV_POSTGRES
from br.cefetmg.db.jurisprudency_interface import JurisprudencyInterface
from br.cefetmg.db.jurisprudency_dataclass import JurisprudencyDataclass



db = PostgressInterface(host=DEV_POSTGRES['URL'], database=DEV_POSTGRES['DATABASE'], user=DEV_POSTGRES['USER'], password=DEV_POSTGRES['PASSWORD'])

db.connect()
print(db.test_connection())
db.disconnect()
print(db.test_connection())


jurisprudency_interface = JurisprudencyInterface(host=DEV_POSTGRES['URL'], database=DEV_POSTGRES['DATABASE'], user=DEV_POSTGRES['USER'], password=DEV_POSTGRES['PASSWORD'])

mock_jurisprudency = jurisprudency_interface.mock_jurisprudency()

jurisprudency_interface.insert_jurisprudency(mock_jurisprudency)

# test get_jurisprudency
print(jurisprudency_interface.get_jurisprudency(mock_jurisprudency.id))

# test delete_jurisprudency
jurisprudency_interface.delete_jurisprudency(mock_jurisprudency.id)

# test get_jurisprudency
print(jurisprudency_interface.get_jurisprudency(mock_jurisprudency.id))





