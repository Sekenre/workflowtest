import sys
import struct

print('pointer size: {:d}'.format(struct.calcsize('P') * 8))
print(f'sys.maxsize: {sys.maxsize}')
