class OracleColumnType:
    def __init__(self, name, datatype, bytesize, internalsize, precision, scale, nullable ):
        self.name = name
        self.type = str(datatype)[18:-2]
        self.byte_size = bytesize
        self.internal_size = internalsize
        self.precision = precision
        self.scale = scale
        self.nullable = (lambda: 'N', lambda: 'Y')[nullable == 0]()


