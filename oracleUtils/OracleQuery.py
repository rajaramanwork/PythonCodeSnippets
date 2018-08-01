import cx_Oracle
from OracleConnection import OracleConnection
from QueryResult import QueryResult
from OracleDbColumn import OracleDbColumn
class OracleQuery :
    #class Variables

    #constructor  
    def __init__(self, host, port, serviceName, schemaUser, schemaPassword):
        self._host = host
        self._port = port
        self._serviceName = serviceName 
        self._schemaUser = schemaUser 
        self._schemaPassword = schemaPassword
    #class members
    def executeProcedure(self, query):
        try:
            oracleConnectionRef = OracleConnection(self._host, self._port, self._serviceName, self._schemaUser, self._schemaPassword)
            oracleConn = oracleConnectionRef.createConnection()
            if oracleConn is None :
                print("Connection failed to open..")
                return None
            else:
                cur = oracleConn.cursor()
                refCursorVar = cur.var(cx_Oracle.CURSOR)
                cur.callproc(query, [14032, refCursorVar] )
                queryResult = QueryResult() 
                refCursor = refCursorVar.getvalue()
                #Populate Columns
                for column in refCursor.description:
                   columnDefn = OracleDbColumn(column[0])
                   queryResult.addColumns(columnDefn)
                #Populate Rows
                for row in refCursor:
                    noOfRowIndexes = len(row)
                    dataRow = row
                return queryResult
        except Exception as e: 
            print("Exception: " + str(e))
