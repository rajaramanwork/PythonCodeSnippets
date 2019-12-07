import csv
import logger.loggingutils  as logging_utils

class FileUtils:
    def __init__(self):
        try:
            self._logger = logging_utils.LoggingUtils('C:\Data\Professional\SourceCode\PythonCodeSnippets\pythonutils\logger\logging.json')
            self._logger.get_logger(__name__)
        except Exception as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))

    def open(self, dbfilename, filemode, delimiter):
        self._file  = open(dbfilename, filemode, 1) #line buffered
        if ( filemode == 'r' ):
            self._file_stream = csv.reader(self._file, delimiter=delimiter)
        if ( filemode == 'w' ):
            self._file_stream = csv.writer(self._file, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_ALL)

    def read_row(self):
        for row in self._file_stream:
            yield(row)

    def write_header(self, datarow):
        self._file_stream.writerow(datarow)

    def write_row(self, datarow):
        self._file_stream.writerow(datarow)

    def __del__(self):
        try:
            self._file.close()
        except Exception as e:
            error, = e.args
            exceptionString = "Exception Code {} : , Exception Message : {}"
            self._logger.log_error(exceptionString.format(error.code, error.message))