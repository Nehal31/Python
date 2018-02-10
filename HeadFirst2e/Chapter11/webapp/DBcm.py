import mysql.connector

# custom class for creating specific error
class ConnectionError(Exception):
    pass

class CredentialError(Exception):
    pass

class SQLError(Exception):
    pass

class UseDatabase:
    
    def __init__(self,dbcon:dict) ->None:
       self.dbconfig = dbcon

    def __enter__(self) -> 'cursor':
        try:
            self.conn = mysql.connector.connect(**self.dbconfig)
            self.cursor = self.conn.cursor()
            return self.cursor

        #connection failed error can handle here        
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        #database login failed errors handle here
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialError(err)
        

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        # wrong query execution error handle here
        if exc_type is mysql.connector.errors.ProgrammingError :
            raise SQLError(exe_type)
        elif exc_type:
            raise exc_type(exc_value)
