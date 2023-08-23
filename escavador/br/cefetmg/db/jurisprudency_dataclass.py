# Abstract class to represent a jurisprudency dataclass

import json
class JurisprudencyDataclass():

    def __init__(self, id, judgment_date, reporter_judge, publication_date, court, publication, parties, menu, decision, theme, thesis, indexing, legislation, observation, doctrine, full_body_url):
        self.id = id
        self.judgment_date = judgment_date
        self.reporter_judge = reporter_judge
        self.publication_date = publication_date
        self.court = court
        self.publication = publication
        self.parties = parties
        self.menu = menu
        self.decision = decision
        self.theme = theme
        self.thesis = thesis
        self.indexing = indexing
        self.legislation = legislation
        self.observation = observation
        self.doctrine = doctrine
        self.full_body_url = full_body_url
    
    def __str__(self):
        # Returns a JSON string with the jurisprudency data
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4)