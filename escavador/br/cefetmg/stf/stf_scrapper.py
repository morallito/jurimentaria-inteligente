#!/usr/bin/env python
import logging

from .stf_configs import SEARCH_URL, SEARCH_FIELD, HOMEPAGE_IMPLICIT_WAITING_TIME, PAGE_FIELD, \
SEARCH_PAGE_IMPLICIT_WAITING_TIME

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class stf_scrapper():

    def __init__(self):
        service = Service(executable_path='/usr/bin/chromedriver')
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-extensions'); # disabling extensions
        chrome_options.add_argument("--remote-debugging-port=9222"); # enable debug port 
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(HOMEPAGE_IMPLICIT_WAITING_TIME)


    def perform_simple_stf_search(self, query):
        """
        Performs a simple search on the STF website, and returns the results
        """
        URL = SEARCH_URL.replace(SEARCH_FIELD, query)
        print(f'Performing search at {URL}...')

        self.driver.get(URL)
        self.driver.implicitly_wait(SEARCH_PAGE_IMPLICIT_WAITING_TIME)
        return self.driver.page_source