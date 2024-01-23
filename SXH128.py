class SXH128:
    def __init__(self, _buffer):
        self.SIZE = 128
        self._buffer = _buffer
    
    def block(self, _buffer):
        return [_buffer[i:i+self.SIZE] for i in range(0, len(_buffer), self.SIZE)]

    def modulate(self, _buffer: bytes):
        _new_buffer=b""
        for byte in _buffer:
            byte=byte%16
            _new_buffer+=hex(byte).replace("0x", "").encode()
        return _new_buffer

    def xor_chars(self, _buffer: bytes):
        _buffer=self.modulate(_buffer)
        result = ''
        for i in range(len(_buffer) - 1):
            xor_result = _buffer[i] ^ _buffer[i + 1]
            result += format(xor_result, '01x') 
        return result
    
    def xor_strings(self, _buffer: list[str]):
        for i in range(len(_buffer) - 1):
            xor_result = ""
            for j in range(self.SIZE):
                xor_result += hex((int(_buffer[0][j], 16) ^ int(_buffer[i + 1][j], 16)) % 16)[2:]
            _buffer[0] = xor_result
        return _buffer[0]
    
    def hash(self):
        blocks=[]
        for block in self.block(self._buffer):
            blocks.append(self.xor_chars(block.ljust(self.SIZE, b"\0")))
        result=self.xor_strings(blocks)        
        return result
        