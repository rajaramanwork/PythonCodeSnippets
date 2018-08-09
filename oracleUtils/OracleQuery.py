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
    def executeProcedure(self, query, params=[]):
        try:
            oracleConnectionRef = OracleConnection(self._host, self._port, self._serviceName, self._schemaUser, self._schemaPassword)
            oracleConn = oracleConnectionRef.createConnection()
            if oracleConn is None :
                print("Connection failed to open..")
                return None
            else:
                cur = oracleConn.cursor()
                refCursorVar = cur.var(cx_Oracle.CURSOR)
                params.append(refCursorVar)
                cur.callproc(query, params )
                queryResult = QueryResult() 
                refCursor = refCursorVar.getvalue()
                
                #Populate Columns
                for column in refCursor.description:
                   columnDefn = OracleDbColumn(column[0], self.__getDataType(column[1]), column[2], column[4], column[5])
                   queryResult.addColumns(columnDefn)
                
                #Populate Rows
                columns = [i[0] for i in refCursor.description]
                for row in refCursor:
                    row_dict = dict()
                    for col in columns:
                        row_dict[col] = row[columns.index(col)]
                    queryResult.addRow(row_dict)
                
                return queryResult
        except Exception as e: 
            print("Exception: " + str(e))
    
    def __getDataType(self, argument):
        convArgument = str(argument)
        startIndex = convArgument.find("'")
        endIndex = convArgument.rfind("'")
        parsedDataType = convArgument[startIndex+1:endIndex]
        _dataTypeSwitcher = {
            "cx_Oracle.STRING": "STRING",
            "cx_Oracle.NUMBER": "NUMBER",
            "cx_Oracle.DATE": "DATE",
            "cx_Oracle.FIXED_CHAR": "CHAR"
        }
        return _dataTypeSwitcher.get(parsedDataType, "undefined")

