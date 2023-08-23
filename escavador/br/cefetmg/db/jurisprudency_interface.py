# This file contains the class JurisprudencyInterface, which is responsible for
# the communication with the database.



from br.cefetmg.db.postgress_interface import PostgressInterface
from br.cefetmg.db.jurisprudency_dataclass import JurisprudencyDataclass

class JurisprudencyInterface():

    def __init__(self, host, database, user, password):
        self.TABLE_NAME = "jurisprudence"
        self.db = PostgressInterface(host=host, database=database, user=user, password=password)
        self.db.connect()


    def insert_jurisprudency(self, jurisprudency):
        """
        Receives a JurisprudencyDataclass object, and inserts it into the database
        """
        query = "INSERT INTO {} (id, judgment_date, reporter_judge, publication_date, court, publication, parties, menu, decision, theme, thesis, indexing, legislation, observation, doctrine, full_body_url) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(self.TABLE_NAME,jurisprudency.id, jurisprudency.judgment_date, jurisprudency.reporter_judge, jurisprudency.publication_date, jurisprudency.court, jurisprudency.publication, jurisprudency.parties, jurisprudency.menu, jurisprudency.decision, jurisprudency.theme, jurisprudency.thesis, jurisprudency.indexing, jurisprudency.legislation, jurisprudency.observation, jurisprudency.doctrine, jurisprudency.full_body_url)
        print(query)
        self.db.execute_query(query)


    def get_jurisprudency(self, id):
        """
        Receives a jurisprudency id, and returns a JurisprudencyDataclass object
        """
        query = "SELECT * FROM {} WHERE id = '{}';".format(self.TABLE_NAME,id)
        result = self.db.execute_query(query)
        return result


    def delete_jurisprudency(self, id):
        """
        Receives a jurisprudency id, and deletes it from the database
        """
        query = "DELETE FROM {} WHERE id = '{}';".format(self.TABLE_NAME,id)
        self.db.execute_query(query)

    def mock_jurisprudency(self):
        """
        Creates a mock jurisprudency, and returns a JurisprudencyDataclass object
        """
        jurisprudency = JurisprudencyDataclass(id="1234567", judgment_date="2018-01-01", reporter_judge="Juiz", publication_date="2018-01-01", court="STF", publication="DJ", parties="Partes", menu="Ementa", decision="Decisao", theme="Tema", thesis="Tese", indexing="Indexacao", legislation="Legislacao", observation="Observacao", doctrine="Doutrina", full_body_url="http://www.stf.jus.br")
        return jurisprudency

    def close_connection(self):
        """
        Closes the connection with the database
        """
        self.db.disconnect()