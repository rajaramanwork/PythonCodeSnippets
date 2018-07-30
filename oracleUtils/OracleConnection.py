import cx_Oracle
class OracleConnection :
    #class Variables
    conn = None

    #constructor  
    def __init__(self, host, port, serviceName, schemaUser, schemaPassword):
        self._host = host
        self._port = port
        self._serviceName = serviceName 
        self._schemaUser = schemaUser 
        self._schemaPassword = schemaPassword

    #class members
    def createConnection(self):
        try:
            dsnConfig = cx_Oracle.makedsn(self._host, self._port, service_name=self._serviceName) 
            self.conn = cx_Oracle.connect(user=self._schemaUser, password=self._schemaPassword, dsn=dsnConfig) 
        except Exception as e: 
            print("Exception: " + str(e))
        return self.conn 
    
    #destructor
    def __del__(self):
        self.conn.close()