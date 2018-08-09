from OracleQuery import OracleQuery
oracleQueryRef = OracleQuery('W7PC-C4J0CX1.r1-core.r1.aig.net', '1622', 'pdborcl','rwbhub', 'rwbhub')
if oracleQueryRef is None :
    print("Exception: OracleQuery is null")
else:
    queryParams = [46]
    queryResult = oracleQueryRef.executeProcedure('PKG_TEST.PR_GET_TASK_DETAILS', queryParams)
print("----------------------------------Column Info-------------------------------")
columns = queryResult.getColumns()
if columns is None :
     print("Exception: Columns is null")
else:
    #for column in columns:
    #   print(f'Name : {column._name} - DataType : {column._dataType} - Size : {column._size} Precision : {column._precision} - Scale : {column._scale} ')
    rows = queryResult.getRows()
    for row in rows:
       print(f'TASK_ID : {row["TASK_ID"]} ; TASK_NAME : {row["TASK_NAME"]}')