from OracleQuery import OracleQuery
oracleQueryRef = OracleQuery('W7PC-C4J0CX1.r1-core.r1.aig.net', '1622', 'pdborcl','ERM_ATRIUM', 'erm_atrium')
if oracleQueryRef is None :
    print("Exception: OracleQuery is null")
else:
    queryResult = oracleQueryRef.executeProcedure('PKG_TASKDRIVER_API.p_get_batch_details')
print("----------------------------------Column Info-------------------------------")
columns = queryResult.getColumns()
if columns is None :
     print("Exception: Columns is null")
else:
    for column in columns:
        print(column._name)