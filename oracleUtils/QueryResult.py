from OracleDbColumn import OracleDbColumn
class QueryResult:
    def __init__(self):
        self._oracleDbColumns = []
        self._oracleDbRows = []
    
    def addColumns(self, OracleDbColumn):
        self._oracleDbColumns.append(OracleDbColumn)

    def getColumns(self):
        return self._oracleDbColumns

    def addRow(self, row = {}):
        self._oracleDbRows.append(row)

    def getRows(self):
        return self._oracleDbRows
