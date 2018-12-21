"""

    This parser can read the result files provided by CarMaker.
    The two files with the extensions .erg and .erg.info are needed.

    The parse function returns a list with all the quantities included
    in the *.erg.info file and each values.

    To do this the info file is converted to a list with all quantities and their data types.
    See Quantity.py for more details. On the other hand the *.erg file has to be read in binary mode.
    To convert each value to the corresponding data type numpy is used.


    Structure of the binary file:

    Notice: encoding is always little endian!

    First 16 bytes are always the same:

    Bytes   0 - 7   char[8]     Header
    Byte    8       u. char     Version
    Byte    9       u. char     Byte-order (0 for little endian)
    Bytes   10 - 11 u. short    Record size
    Bytes   12 - 15 char[4]     Reserved

    The quantities are following in blocks: (for example one double and one float):

    Bytes   16 - 23 double      Value of quantity one
    Bytes   24 - 27 float       Value of quantity two

    Bytes   28 - 35 double      Next value of quantity one
    Bytes   36 - 39 float       Next value of quantity two

"""

from .Quantity import Quantity
import numpy as np


class ERGPY:
    def __init__(self):
        """
        The class instance stores the parsed quantityList.
        """
        self.quantityList = []

    def getQuantityList(self, infoFilePath):
        """
        This function extracts all quantity names and their data types out of the *.erg.info file.
        :param infoFilePath:
        :return: quantityList
        """
        quList = []
        with open(infoFilePath, 'r')as infoFile:
            line = infoFile.readline()
            while line != '':
                if 'File.At.' in line:
                    name = line.split(' ', 2)[2].rstrip()
                    type = infoFile.readline().split(' ', 2)[2].rstrip()
                    quList.append(Quantity(name, type))
                line = infoFile.readline()
        return quList

    def parse(self, ergFilePath):
        """
        Parse the *.erg file.
        First the function getQuantityList is called to get the right quantity list.
        BlockSize defines how much bytes are read per cycle.
        The header bytes of the file are not needed right now.
        :param ergFilePath:
        :return: quantityList
        """
        infoFilePath = ergFilePath + '.info'
        quantityList = self.getQuantityList(infoFilePath)

        # get block size
        blockSize = sum(quantity.bytes for quantity in quantityList)

        with open(ergFilePath, 'rb') as ergFile:

            # read the first 16 bytes, as they are not needed now
            ergFile.read(16)

            # now read the rest of the file block wise
            block = ergFile.read(blockSize)
            while len(block) == blockSize:
                for q in quantityList:
                    q.values.append(np.fromstring(block[:q.bytes], q.dataType)[0])
                    block = block[q.bytes:]
                block = ergFile.read(blockSize)

        self.quantityList = quantityList
        return quantityList

    def getQuantitys(self, quantityNames):
        """
        This function returns a list including all desired quantities and their values.
        :param quantityNames:
        :return: selectedQuantities
        """
        selectedQuantities = []
        for quantityName in quantityNames:
            foundQuantities = [q for q in self.quantityList if q.name == quantityName]
            if len(foundQuantities) > 0:
                selectedQuantities.append(foundQuantities[0])
        return selectedQuantities

    def getSingleQuantityValues(self, quantityName):
        """
        Return only the value list of the desired quantity.
        If the quantity name was not found, None is returned.
        :param quantityName:
        :return: values
        """
        quantity = self.getQuantitys([quantityName])
        if len(quantity) > 0:
            return quantity[0].values
        else:
            return None

    def getJoinedSamplePoints(self, quantityNames=None):
        """
        This functions generates samplepoints out of the selected quantities.
        One samplepoint is a dict with the quantity names as key and their value at the discrete time step i as value.
        If quantityNames is None all parsed quantities are transformed to dict.
        :param quantityNames:
        :return:
        """
        selectedQuantities = []
        samplePoints = []

        if quantityNames is None:
            selectedQuantities = self.quantityList
        else:
            selectedQuantities = self.getQuantitys(quantityNames)

        for i in range(0, len(selectedQuantities[0].values), 1):
            sp = {}
            for sQ in selectedQuantities:
                sp[str(sQ.name)] = sQ.values[i]
            samplePoints.append(sp)
        return samplePoints
