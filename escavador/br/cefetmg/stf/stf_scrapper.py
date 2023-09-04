#!/usr/bin/env python
import logging

from .stf_configs import SEARCH_URL, SEARCH_FIELD, HOMEPAGE_IMPLICIT_WAITING_TIME, PAGE_FIELD, \
SEARCH_PAGE_IMPLICIT_WAITING_TIME, XPATH_NUMBER_OF_RESULTS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0"
        chrome_options.add_argument(f'--user-agent={user_agent}')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(HOMEPAGE_IMPLICIT_WAITING_TIME)

    def clean_search_query(self, query):
        """
        Clean the query, transform it into a valid url parameter
        """
        return query.replace(' ', '%20')


    def perform_simple_stf_search(self, query):
        """
        Performs a simple search on the STF website, and returns the results
        """
        query = self.clean_search_query(query)
        URL = SEARCH_URL.replace(SEARCH_FIELD, query)
        print(f'Performing search at {URL}...')

        result_number = self.get_search_result_info(query)
        print(f'Found {result_number} results.')

    def formatUrl(self, query, page):
        URL = SEARCH_URL.replace(SEARCH_FIELD, query)
        URL = URL.replace(PAGE_FIELD, page)
        return URL

    def parse_string_number_of_results(self, string_number):
        list_string = string_number.split(' ')
        result = list_string[1]
        result = result.replace('.', '')
        return int(result)

    def get_search_result_info(self, query):
        """
        Returns the number of results found by the search
        """
        search_url = self.formatUrl(query, '1') # First page
        print(f'Using base url: {search_url}.')
        self.driver.get(search_url)
        self.driver.implicitly_wait(SEARCH_PAGE_IMPLICIT_WAITING_TIME)
        result_number = self.driver.find_element(By.XPATH, XPATH_NUMBER_OF_RESULTS)
        print(self.parse_string_number_of_results(result_number.text))
        return result_number.text