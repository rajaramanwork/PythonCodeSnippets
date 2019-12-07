import pytest
import logging
import logger.loggingutils as logger
import oracle.oracleutils as oracle_utils
import oracle.oracleparameter as oracle_param

def test_oraclequery():
    try:
        _oracle_utils =  oracle_utils.OracleUtils("SAMPLEDB_ADMIN", "localhost", "xe", "SAMPLEDB_ADMIN", "fighter70")
        """
        Oracle Queries without Params
        """
        columns, rows = _oracle_utils.execute("SELECT * FROM SAMPLEDB_ADMIN.CUSTOMERS")
    
        print('===================Columns===================')
        for x in range(len(columns)): 
            print(' Name :  ' + columns[x].name)
            print(' Type :  ' + str(columns[x].type))
            print(' byte_size :  ' + str(columns[x].byte_size))
            print(' internal_size :  ' + str(columns[x].internal_size))
            print(' internal_size :  ' + str(columns[x].internal_size))
            print(' precision :  ' + str(columns[x].precision))
            print(' scale :  ' + str(columns[x].scale))
            print(' nullable :  ' + str(columns[x].nullable))
        print('===================Rows===================')
        for row in rows:  
            print('--------------------ROW---------------------------' )
            print(' CUSTOMER_ID :  ' + str(row['CUSTOMER_ID']))
            print(' CUSTOMER_NAME :  ' + row['CUSTOMER_NAME'])
            print(' CITY :  ' + row['CITY'])
    except : 
        print('Something went wrong. check Log')

def test_oraclequerywithparams():
    try:
        _oracle_utils =  oracle_utils.OracleUtils("SAMPLEDB_ADMIN", "localhost", "xe", "SAMPLEDB_ADMIN", "fighter70")
        """
        Oracle Queries with Params
        """
        params = {'CITY_PARAM':'edison'}
        columns, rows = _oracle_utils.execute("SELECT * FROM SAMPLEDB_ADMIN.CUSTOMERS WHERE CITY=:CITY_PARAM", params)

        print('===================Rows===================')
        for row in rows:  
            print('--------------------ROW---------------------------' )
            print(' CUSTOMER_ID :  ' + str(row['CUSTOMER_ID']))
            print(' CUSTOMER_NAME :  ' + row['CUSTOMER_NAME'])
            print(' CITY :  ' + row['CITY'])
    except : 
        print('Something went wrong. check Log')

def test_oracleupdatequery():
    try:
        _oracle_utils =  oracle_utils.OracleUtils("SAMPLEDB_ADMIN", "localhost", "xe", "SAMPLEDB_ADMIN", "fighter70")
        sqlquery = "update SAMPLEDB_ADMIN.CUSTOMERS set COMMENTS=:COMMENTS_PARAM where CUSTOMER_ID=:CUSTOMER_ID_PARAM"
        params = {'CUSTOMER_ID':2, 'CUSTOMER_ID_PARAM':"raj test message"}
        recordsupdated = _oracle_utils.execute_nonquery(sqlquery, params, true)
        print(' recordsupdated:  ' + str(recordsupdated))
    except : 
        print('Something went wrong. check Log')

def test_oraclequerywithparams():
    try:
        _oracle_utils =  oracle_utils.OracleUtils("SAMPLEDB_ADMIN", "localhost", "xe", "SAMPLEDB_ADMIN", "fighter70")
        """
        Oracle Queries with Params
        """
        params = {'CITY_PARAM':'edison'}
        columns, rows = _oracle_utils.execute("SELECT * FROM SAMPLEDB_ADMIN.CUSTOMERS WHERE CITY=:CITY_PARAM", params)

        print('===================Rows===================')
        for row in rows:  
            print('--------------------ROW---------------------------' )
            print(' CUSTOMER_ID :  ' + str(row['CUSTOMER_ID']))
            print(' CUSTOMER_NAME :  ' + row['CUSTOMER_NAME'])
            print(' CITY :  ' + row['CITY'])
    except : 
        print('Something went wrong. check Log')

def test_oracleprocedure():
    """
        Oracle Procedure Calls with Binding
    """
    try:
        _oracle_utils =  oracle_utils.OracleUtils("SAMPLEDB_ADMIN", "localhost", "xe", "SAMPLEDB_ADMIN", "fighter70")
        params = [] #parameters are positional 
    
        #One input Parameter and Output RefCursor
        params.append(oracle_param.OracleParameter("p_city", "string", "input", "edison"))
        params.append(oracle_param.OracleParameter("p_cursor", "refcursor", "output", None))
        columns, rows = _oracle_utils.execute_proc("SAMPLEDB_ADMIN.PKG_CUSTOMERS_API.p_get_customers", params)
        print('===================Columns===================')
        if (columns != None ):
            for x in range(len(columns)): 
                print(' Name :  ' + columns[x].name)
                print(' Type :  ' + str(columns[x].type))
                print(' byte_size :  ' + str(columns[x].byte_size))
                print(' internal_size :  ' + str(columns[x].internal_size))
                print(' internal_size :  ' + str(columns[x].internal_size))
                print(' precision :  ' + str(columns[x].precision))
                print(' scale :  ' + str(columns[x].scale))
                print(' nullable :  ' + str(columns[x].nullable))
            print('===================Rows===================')
            for row in rows:  
                print('--------------------ROW---------------------------' )
                print(' CUSTOMER_ID :  ' + str(row['CUSTOMER_ID']))
                print(' CUSTOMER_NAME :  ' + row['CUSTOMER_NAME'])
                print(' CITY :  ' + row['CITY'])
    except Exception as e : 
        print('Something went wrong. check Log')
        print(str(e))

def test_oracleprocedurewithoutput():
    """
        Oracle Procedure Calls with Binding
    """
    try:
        _oracle_utils =  oracle_utils.OracleUtils("SAMPLEDB_ADMIN", "localhost", "xe", "SAMPLEDB_ADMIN", "fighter70")
        params = [] #parameters are positional 
    
        #One input Parameter and Two Output Parameters 
        params.append(oracle_param.OracleParameter("p_city", "string", "input", "edison"))
        params.append(oracle_param.OracleParameter("p_avg_salary", "int", "output", None))
        params.append(oracle_param.OracleParameter("p_highest_sal", "int", "output", None))
        columns, rows = _oracle_utils.execute_proc("SAMPLEDB_ADMIN.PKG_CUSTOMERS_API.p_get_customers_sal", params)
        for x in params:
            if (x.direction == 'output'):
                print(x.name + ':' + str(x.value))
    except Exception as e : 
        print('Something went wrong. check Log')
        print(str(e))

def test_oraclefunction():
    """
        Oracle Procedure Calls with Binding
    """
    try:
        _oracle_utils =  oracle_utils.OracleUtils("SAMPLEDB_ADMIN", "localhost", "xe", "SAMPLEDB_ADMIN", "fighter70")
        params = [] #parameters are positional 
    
        #One input Parameter and Two Output Parameters 
        params.append(oracle_param.OracleParameter("p_customer_id", "int", "input", "2"))
        params.append(oracle_param.OracleParameter("p_city_name", "string", "return", None))
        _oracle_utils.execute_func("SAMPLEDB_ADMIN.PKG_CUSTOMERS_API.fn_get_customer_code", params)
        for x in params:
            if (x.direction == 'return'):
                print(x.name + ':' + str(x.value))
    except Exception as e : 
        print('Something went wrong. check Log')
        print(str(e))
