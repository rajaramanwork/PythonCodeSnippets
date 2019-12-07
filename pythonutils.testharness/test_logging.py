import pytest
import logging
import logger.loggingutils as logger

def test_logger():
    _logger = logger.LoggingUtils("C:\Data\Professional\SourceCode\PythonCodeSnippets\pythonutils\logger\logging.json")
    _logger.get_logger(__name__)
    
    _logger.log_info("Log Test:Info")
    _logger.log_debug("Log Test:Debug")