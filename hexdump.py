import sys
import struct
import os.path

LINE_WIDTH = 16
InputBinFile = ''

class BinParser:
    def __init__(self, binFile):
        self.binaryFile = binFile
        self.binaryFileSz = os.path.getsize(binFile)
        self.addrOffset = 0
    def HexDump(self):
        binHandle = open(self.binaryFile, 'rb')
        byteCnt = 0
        LineBuffer = ''
        charBuffer = ''
        while byteCnt < self.binaryFileSz:
            if byteCnt % LINE_WIDTH == 0:
                charBuffer = ''
                LineBuffer += '{0:08x}:'.format((byteCnt + self.addrOffset))
            if byteCnt % 2 == 0:
                LineBuffer += ' '
            byte = binHandle.read(1)
            val = struct.unpack('B', byte)[0]
            if val < 32 or val > 126:
                charBuffer += '.'
            else:
                charBuffer += chr(val)
            LineBuffer += '{0:02x}'.format(val)
            if byteCnt % LINE_WIDTH == LINE_WIDTH - 1:
                LineBuffer += '  |'
                LineBuffer += charBuffer
                LineBuffer += '|\n'
            byteCnt += 1
        print LineBuffer
def Usage():
    print """python hexdump.py binfile"""
def ValidateCmdLineArgs():
    if not os.path.isfile(sys.argv[1]):
        print 'File {0} does not exist'.format(InputBinFile)
        Usage()
        sys.exit(1)

#******************************************************************************
ValidateCmdLineArgs()
binParser = BinParser(sys.argv[1])
binParser.HexDump()
