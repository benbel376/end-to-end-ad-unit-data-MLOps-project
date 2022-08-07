import psycopg2


class Manager():
    """
    a python class used to manage connection with posgres server 
    and the execution of sql queries
    """
    def __init__(self):
        pass
        
    def connect_to_server(self,
                        host:str = "localhost", 
                        port:int=5432, 
                        user:str = "warehouse", 
                        password:str="warehouse", 
                        dbName:str="warehouse"):
        """
        A function that allows you to connect to postgreSQL database
        Args:
            host: ip address or domain
            user: the user of the server
            password: the password to server
            dbName: the name of the server

        Returns:
            connection: connection object
            cursor: cursor object

        """
        try:
            conn = psycopg2.connect(
                                host=host,
                                port=port,
                                database=dbName,
                                user=user,
                                password=password)
            cur = conn.cursor()
            print(f"successfully connected; cursor: {cur}")
            return conn, cur
        except Exception as e:
            print(f"Error: {e}")


    def close_connection(self, connection, cursor):
        """
        closes connection with database.

        Args: 
            connection: mysql connection object
            cursor: cursor object

        Returns: None.
        """
        connection.commit()
        cursor.close()
        print("connection closed and transaction committed")

    def execute_query(self, cursor, file_sql) -> None:
        """
        A function to execute sql queries
        
        Args:
            cursor: cursor object
            file_sql: the location of the sql query file
            dbName: the name of the database

        Returns: None
        """
        sqlFile = file_sql
        fd = open(sqlFile, 'r')
        readsqlFile = fd.read()
        fd.close()
        sqlQueries = readsqlFile.split(';')
        for query in sqlQueries:
            try:
                cursor.execute(query)
                # try:
                #     rows = cursor.fetchall()    # get all selected rows, as Barmar mentioned
                #     for r in rows:
                #         print(r)
                # except Exception as e:
                #     print(f"Inner error: {e}")
                print("successfully executed")
            except Exception as e:
                print('command skipped: ', query)
                print(e)

if __name__=="__main__":
    pass
