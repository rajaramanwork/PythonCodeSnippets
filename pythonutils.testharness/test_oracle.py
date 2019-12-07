import pytest
import logging
import logger.loggingutils as logger
import oracle.oracleutils as oracle_utils
import oracle.oracleparameter as oracle_param

def test_oraclequerywithparams():
    try:
        _oracle_utils =  oracle_utils.OracleUtils("SAMPLEDB_ADMIN", "localhost", "xe", "SAMPLEDB_ADMIN", "fighter70")
        """
        Oracle Queries without Params
        """
        columns, rows = _oracle_utils.execute("SELECT * FROM SAMPLEDB_ADMIN.CUSTOMERS")
        """
        Oracle Queries with Params
        """
        #params = {'isActive':'Y'}
        #columns, rows = _oracle_utils.execute("SELECT * FROM AWP.LU_APPLICATION WHERE IS_APPLICATION_ACTIVE=:isActive", params)
    
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
            print(' APPLICATION_CODE :  ' + str(row['CUSTOMER_ID']))
            print(' APPLICATION_CODE :  ' + row['CUSTOMER_NAME'])
            print(' APPLICATION_SHORT_DESC :  ' + row['CITY'])
    except : 
        print('Something went wrong. check Log')
