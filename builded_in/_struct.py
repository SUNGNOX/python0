import struct
s = b'\x04\x02'
struct.unpack('>H', s)
int('010000000010', base=2)
struct.unpack('<H', s)
int('001000000100', base=2)
