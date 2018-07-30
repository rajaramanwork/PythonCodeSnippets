from OracleDbColumn import OracleDbColumn
class QueryResult:
    def __init__(self):
        self._oracleDbColumns = []
    
    def addColumns(self, OracleDbColumn):
        self._oracleDbColumns.append(OracleDbColumn)

    def getColumns(self):
        return self._oracleDbColumns

