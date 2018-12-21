"""

    This class helps to manage the different data types.
    Each instance can also contain the quantity values.

"""

class Quantity:
    def __init__(self, name, dataType):
        self.name = name
        self.dataType = ''
        self.values = []
        self.bytes = 0
        self.resolveDataType(dataType)

    def resolveDataType(self, dataType):
        dataTypes = [
            # default data types
            {'typeStr': 'Char', 'dType': 'c', 'bytes': 1},
            {'typeStr': 'Short', 'dType': 'h', 'bytes': 2},
            {'typeStr': 'Int', 'dType': 'i', 'bytes': 4},
            {'typeStr': 'Long', 'dType': 'l', 'bytes': 4},
            {'typeStr': 'Float', 'dType': 'f', 'bytes': 4},
            {'typeStr': 'Double', 'dType': 'd', 'bytes': 8},

            # padding Bytes
            {'typeStr': '1 Byte', 'dType': 'c', 'bytes': 1},
            {'typeStr': '2 Bytes', 'dType': 'h', 'bytes': 2},
            {'typeStr': '4 Bytes', 'dType': 'i', 'bytes': 4},
            {'typeStr': '8 Bytes', 'dType': 'q', 'bytes': 8}
        ]
        for dT in dataTypes:
            if dT['typeStr'] == dataType:
                self.dataType = dT['dType']
                self.bytes = dT['bytes']
