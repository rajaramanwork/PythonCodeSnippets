import pytest
import logging
import logger.loggingutils as logger
import file.fileutils as file_utils

def test_file():
    _logger = logger.LoggingUtils("C:\Data\Professional\SourceCode\PythonCodeSnippets\pythonutils\logger\logging.json")
    _logger.get_logger(__name__)
    
    _logger.log_info("-------------FILE UTILS TEST ( START ) ---------------")

    _file_utils = file_utils.FileUtils()

    #-----------Writing csv ----------------------------

    #_file_utils.open('C:\workarea\SourceCode\python\PythonUtils\output\output.csv', "w", ',')
    #_file_utils.write_header(['name', 'category', 'salary'])
    #_file_utils.write_row(['John Smith', 'Accounting', 20000])

    #-----------Reading csv ( yield) ----------------------------
    _file_utils.open('C:\Data\Professional\SourceCode\PythonCodeSnippets\pythonutils.testharness\sourcefiles\insurancesample.csv', "r", ',')
    linenumber = 1 
    for row in _file_utils.read_row():
        print ('linenumber : ' + str(linenumber))
        print (row)
        linenumber = linenumber + 1

    _logger.log_info("-------------FILE UTILS TEST ( END ) ---------------")