#!/usr/bin/env python
import logging

from .stf_configs import SEARCH_URL, SEARCH_FIELD, HOMEPAGE_IMPLICIT_WAITING_TIME, PAGE_FIELD

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


def log_configs_in_use():
    """
    Logs to the terminal and info file the configurations that will be used during the execution.
    """
    logger = logging.getLogger('scraper')
    logger.info(f'Running the STJ queries at: {SEARCH_URL}')
    print(f'Running the STJ queries at: {SEARCH_URL}')
    logger.info(f'URL search field to be replaced: {SEARCH_FIELD}')
    print(f'URL search field to be replaced: {SEARCH_FIELD}')


def format_url(search_key: str, page: str) -> str:
    """
    Return the URL with the search words inserted
    """
    formed_url = None
    logger = logging.getLogger('scraper')
    try:
        insertion = search_key.replace(' ', '%')
        formed_url = SEARCH_URL
        formed_url = formed_url.replace(SEARCH_FIELD, insertion)
        formed_url = formed_url.replace(PAGE_FIELD, str(page))
        logger.debug(f'URL formatted with search: {formed_url}')
    except Exception as error:
        logger.error(f'Unknown error while processing URL: {error}')
    return formed_url


def get_stf_main_pagination_size(url):
    logger = logging.getLogger('scraper')
    number_of_pages = 1
    try:
        logger.debug("Loading Chrome drive to search...")
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        chrome_drive = webdriver.Chrome(service=chrome_service)
        chrome_drive.get(url)
        chrome_drive.implicitly_wait(HOMEPAGE_IMPLICIT_WAITING_TIME)
        number_of_pages = var = \
            (chrome_drive.find_element(By.CSS_SELECTOR, "span[class='pages-resume ml-0']")).text.split(' ')[1]
        number_of_pages = int(number_of_pages.replace('.', ''))
        logger.debug(f'Search performed, pagination size is: {number_of_pages}')
    except Exception as err:
        logger.error(f'An exception occurred while using Selenium webdriver: {err}')
    return number_of_pages


def paginate_trought_results(pages_number: int, search: str):
    logger = logging.getLogger('scraper')
    logger.debug(f'Starting pagination - search: {search} - pages: {pages_number}')
    try:
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        chrome_drive = webdriver.Chrome(service=chrome_service)
    except Exception as err:
        logger.error(f'Unexpected error while creating selenium web driver {err}')
    for i in range(1, pages_number):
        logger.debug(f'Getting results for page {i}.')
        url = format_url(search, pages_number)
        chrome_drive.get(url)
        chrome_drive.implicitly_wait(HOMEPAGE_IMPLICIT_WAITING_TIME)





def perform_simple_stf_search(search_key: str) -> None:
    """
    Receives a string and return a list of objects of STJContent type that are the results of this search
    """
    log_configs_in_use()
    logger = logging.getLogger('scraper')
    logger.debug(f"Performing the simple search using: {search_key}")
    url = format_url(search_key)
    pagination_limit = get_stf_main_pagination_size(url, 1)
    paginate_trought_results(pagination_limit, search_key)
