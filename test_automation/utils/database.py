import psycopg2


class Database:

    def __init__(self, host_ip, database, port, database_user, password=""):
        self.host_ip = host_ip
        self.database = database
        self.database_user = database_user
        self.password = password
        self.port = port
        self.connection = psycopg2.connect(
            host=self.host_ip,
            database=self.database,
            user=self.database_user,
            password=self.password,
            port=self.port
        )

    def tear_down_connection(self):
        self.connection.close()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        print("Executing query: {}".format(query))
        cursor.execute(query)
        execute_status_message = cursor.statusmessage
        cursor.close()
        self.connection.commit()
        return execute_status_message

    def select_query(self, query):
        cursor = self.connection.cursor()
        print("Executing query: {}".format(query))
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return data
