import cx_Oracle
import oracle.oraclecolumntype as oracle_column_type
import logger.loggingutils  as logging_utils

class OracleUtils:
    def __init__(self, dbSchema, dbHost, dbServiceName, dbLogin, dbPassword ):
        self._logger = logging_utils.LoggingUtils('C:\Data\Professional\SourceCode\PythonCodeSnippets\pythonutils\logger\logging.json')
        self._logger.get_logger(__name__)
        try:
            self._dbConn = cx_Oracle.connect(dbSchema, dbPassword, dbHost + '/' + dbServiceName)
            self._cursor = self._dbConn.cursor() # If the database connection succeeded create the cursor
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))
    
    def execute(self, sql, params=None):
        try:
            if (params is None) :
                self._cursor.execute(sql)
            else :
                self._cursor.execute(sql, params)

            #Generate Columns Signature
            columns = []
            for d in self._cursor.description:
                _oracle_column_type = oracle_column_type.OracleColumnType(d[0], d[1], d[2], d[3], d[4], d[5], d[6])
                columns.append(_oracle_column_type)
            #Generate Rows
            return columns, self.map_rows_to_dict() 
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))

    def execute_nonquery(self, sql, params=None, commit=False):
        try:
            if (params is None):
                self._cursor.execute(sql)
            else:
                self._cursor.execute(sql, params)
            if (commit):
                self._dbConn.commit()
                return self._cursor.rowcount
            else:
                return 0
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
        except Exception as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))
    
    def execute_proc(self, sql:str, params:list=None):
        try:
            if (params is None) :
                self._cursor.callproc(sql)
            else :
                #configure parameters
                params_list = []
                has_ref_cursor: bool = False
                dynamicVariables = {}
                for x in params:
                    if (x.type == 'refcursor' and x.direction == 'output' ):
                        ref_cursor_var = self._cursor.var(cx_Oracle.CURSOR)
                        params_list.append(ref_cursor_var)
                        has_ref_cursor = True
                    else:
                        if ( x.direction == 'input' ) : 
                            params_list.append(x.value)
                        if ( x.direction == 'output' ) :
                            l_param_type = self.data_type_map(x.type)
                            l_param = self._cursor.var(l_param_type)
                            dynamicVariables[x.name]=l_param
                            params_list.append(l_param)
                #execute
                if (has_ref_cursor) :
                    self._cursor.callproc(sql, params_list)
                    ref_cursor = ref_cursor_var.getvalue()
                    #Generate Columns Signature
                    columns = []
                    for d in ref_cursor.description:
                        _oracle_column_type = oracle_column_type.OracleColumnType(d[0], d[1], d[2], d[3], d[4], d[5], d[6])
                    columns.append(_oracle_column_type)
                    #Generate Rows
                    return columns, self.map_rows_to_dict_rc(ref_cursor)
                else:
                    self._cursor.callproc(sql, params_list)
                    for x in params:
                        if (x.direction == 'output' ):
                            x.value = dynamicVariables[x.name].getvalue()
                    return None, None
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))
        except Exception as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))

    def execute_func(self, sql, params:list=None):
        try:
            l_return_param = None
            if (params is None) :
                l_return_param = cursor.var(cx_Oracle.STRING)
                self._cursor.callfunc(sql, l_return_param)
            else :
                dynamicVariables = {}
                params_list = []
                for x in params:
                    if ( x.direction == 'input' ) : 
                        params_list.append(x.value)
                    if ( x.direction == 'return' ) :
                        l_param_type = self.data_type_map(x.type)
                        l_return_param = self._cursor.var(l_param_type)
                self._cursor.callfunc(sql, l_return_param, params_list)
                for x in params:
                    if (x.direction == 'return' ):
                        x.value = l_return_param.getvalue()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))
        except Exception as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))
    
    def __del__(self):
        try:
            self._cursor.close()
            self._dbConn.close()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))
    
    def map_rows_to_dict(self):
        columns = [i[0] for i in self._cursor.description]  
        return [dict(zip(columns, row)) for row in self._cursor]
    
    def map_rows_to_dict_rc(self, ref_cursor):
        columns = [i[0] for i in ref_cursor.description]  
        return [dict(zip(columns, row)) for row in ref_cursor]

    def data_type_map(self, key):
        switcher={
                    'string':cx_Oracle.STRING,
                    'char':cx_Oracle.FIXED_CHAR,
                    'int':cx_Oracle.NUMBER,
                    'datetime':cx_Oracle.DATETIME
                }
        return switcher.get(key,lambda :'Invalid')