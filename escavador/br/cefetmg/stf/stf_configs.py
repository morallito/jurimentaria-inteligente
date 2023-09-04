SEARCH_URL = 'https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&pesquisa_inteiro_teor=false&sinonimo=true' \
             '&plural=true&radicais=false&buscaExata=true&page=<PAGE_NUMBER>&pageSize=1&queryString=<QUERY_STRING>' \
             '&sort=_score&sortBy=desc'
SEARCH_FIELD = '<QUERY_STRING>'
PAGE_FIELD = '<PAGE_NUMBER>'

XPATH_NUMBER_OF_RESULTS="//span[@class='pages-resume ml-0']"

# Delay in seconds to wait the main page to load
HOMEPAGE_IMPLICIT_WAITING_TIME = 1
SEARCH_PAGE_IMPLICIT_WAITING_TIME = 5


