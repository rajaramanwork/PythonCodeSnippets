class OracleDbColumn:
    def __init__(self, name, dataType, size, precision, scale):
        self._name = name
        self._dataType = dataType
        self._size = 0 if size == "None" else size
        self._precision = 0 if precision == "None" else precision
        self._scale = 0 if scale == "None" else scale