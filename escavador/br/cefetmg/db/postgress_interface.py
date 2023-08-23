# /usr/bin/python3.6


import psycopg2

class PostgressInterface:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        
        self.connection = None
        self.cursor = None
    
    def connect(self):
        #Checks if the connection is already established, if not, it connects
        if self.connection is None:
            self.connection = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            self.cursor = self.connection.cursor()
    
    def disconnect(self):
        #Checks if the connection is established, if so, it disconnects
        if self.connection is not None:
            self.cursor.close()
            self.connection.close()
            self.connection = None
            self.cursor = None

    def test_connection(self):
        #Test the database connection, return true if it is connected, false otherwise
        if self.connection is not None: 
            return True
        else:
            return False

    def execute_query(self, query):
        #Execute a query on the database
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print(e)
            self.connection.rollback()
            raise e
