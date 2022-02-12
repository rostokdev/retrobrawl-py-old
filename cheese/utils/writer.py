class Writer:
    def __init__(self, endian: str = 'big'):
        self.endian = endian
        self.buffer = b''

    def write(self, data: bytes):
        self.buffer += data

    def write_unsigned_integer(self, integer: int, length: int = 1):
        self.buffer += integer.to_bytes(length, self.endian, signed=False)

    def write_integer(self, integer: int, length: int = 1):
        self.buffer += integer.to_bytes(length, self.endian, signed=True)

    def write_unsigned_int64(self, integer: int):
        self.write_unsigned_integer(integer, 8)

    def write_int64(self, integer: int):
        self.write_integer(integer, 8)

    def writeScID(self, idV, value):
        self.writeVint(idV)
        if idV != 0:
            self.writeVint(value)

    def write_float(self, floating: float):
        exponent = 0
        sign = 1

        if floating == 0:
            self.write_unsigned_int32(0)
        else:
            if floating < 0:
                sign = -1
                floating = -floating

            if floating >= 2 ** -1022:
                value = floating

                while value < 1:
                    exponent -= 1
                    value *= 2
                while value >= 2:
                    exponent += 1
                    value /= 2

            mantissa = floating / 2 ** exponent

            exponent += 127

            as_integer_bin = '0'
            if sign == -1:
                as_integer_bin = '1'

            as_integer_bin += bin(exponent)[2:].zfill(8)

            mantissa_bin = ''
            for x in range(24):
                bit = '0'
                if mantissa >= 1/2**x:
                    mantissa -= 1/2**x
                    bit = '1'
                mantissa_bin += bit

            mantissa_bin = mantissa_bin[1:]

            as_integer_bin += mantissa_bin
            as_integer = int(as_integer_bin, 2)

            self.write_unsigned_int32(as_integer)

    def write_unsigned_int32(self, integer: int):
        self.write_unsigned_integer(integer, 4)

    def write_int32(self, integer: int):
        self.write_integer(integer, 4)

    def write_normalized_unsigned_int16(self, integer: int):
        self.write_unsigned_int16(round(integer * 65535))

    def write_unsigned_int16(self, integer: int):
        self.write_unsigned_integer(integer, 2)

    def write_normalized_int16(self, integer: int):
        self.write_int16(round(integer * 32512))

    def write_int16(self, integer: int):
        self.write_integer(integer, 2)

    def write_unsigned_int8(self, integer: int):
        self.write_unsigned_integer(integer)

    def write_int8(self, integer: int):
        self.write_integer(integer)

    def write_bool(self, boolean: bool):
        if boolean:
            self.write_unsigned_int8(1)
        else:
            self.write_unsigned_int8(0)

    writeUInt = write_unsigned_integer
    writeInt = write_integer

    writeUInt64 = writeULongLong = write_unsigned_int64
    writeInt64 = writeLongLong = write_int64

    writeUInt32 = writeULong = write_unsigned_int32
    writeInt32 = writeLong = write_int32

    writeUInt16 = writeUShort = write_unsigned_int16
    writeInt16 = writeShort = write_int16

    writeNUInt16 = writeNUShort = write_normalized_unsigned_int16
    writeNInt16 = writeNShort = write_normalized_int16

    writeUInt8 = writeUByte = write_unsigned_int8
    writeInt8 = writeByte = write_int8

    def write_char(self, string: str):
        for char in list(string):
            self.buffer += char.encode('utf-8')

    def writeBool(self, boolean: bool):
        if boolean:
            self.writeUInt8(1)
        else:
            self.writeUInt8(0)

    def write_string(self, string: str = None):
        if string is None:
            self.write_int32(-1)
        else:
            encoded = string.encode('utf-8')
            self.write_int32(len(encoded))
            self.buffer += encoded

    def write_Vint(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f

                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)

                final += b.to_bytes(1, 'big')
                data >>= 7
        self.buffer += final

    writeChar = write_char
    writeString = write_string
    writeVint = write_Vint
    writeBoolean = writeBool
