import string

class SXH256:
    def __init__(self, buffer:bytes) -> None:
        self.alphabet = string.printable.encode()
        self.buffer=(buffer+self.alphabet)*200
        self.block=256
        self.alphabet_block = self.__block_pad__(self.alphabet)

    def __block_pad__(self, string:bytes):
        blocks=[self.buffer[i:i+self.block] for i in range(0, len(self.buffer), self.block)]
        for i in range(len(blocks)):
            blocks[i]=blocks[i].ljust(self.block, b"0")
        return blocks
    
    def xor_chars(self, block):
        result = b''
        for i in range(len(block)-1):
            result += bytes([block[i]^block[i+1]])
        return result
    
    def xor_strings(self, string_list):
        result = string_list[0]
        for s in string_list[1:]:
            result = bytes([a^b for a,b in zip(result, s)])
        return result

    def hash(self):
        for i in range(self.block//2):
            blocks=[]
            for block in self.__block_pad__(self.buffer)+self.alphabet_block:
                blocks.append(self.xor_chars(block))
            self.buffer=self.xor_chars(self.xor_strings(blocks))
        return self.buffer
    
    def hexidigest(self, hash:bytes):
        hexidigest=""
        for byte in hash:
            hexidigest+=hex(byte%16).removeprefix("0x")
        return hexidigest

if __name__=='__main__':
    hash_gen=SXH256(b"b")
    hash=hash_gen.hash()
    print(hash_gen.hexidigest(hash))