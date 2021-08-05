
class RxBufferReader :
    def __init__(self, buff) :
        self.nextRead = 0;
        self.buffer = buff;

    def EOF(self) :
        return self.nextRead >= buffer.length;

    def readUInt8(self) :
        ret = int.from_bytes([self.buffer[self.nextRead]], 'little')
        self.nextRead += 1;
        return ret;
    
    def readUInt16(self) :
        ret = int.from_bytes([self.buffer[self.nextRead], self.buffer[self.nextRead+1]], 'little')
        self.nextRead += 2;
        return ret;
    
    def readUInt32(self) :
        ret = int.from_bytes([self.buffer[self.nextRead], self.buffer[self.nextRead+1], self.buffer[self.nextRead+2], self.buffer[self.nextRead+3]], 'little')
        self.nextRead += 4;
        return ret;

    def readString(self) :
        sz = self.readUInt32();
        if sz < 0 :
            return None
        elif sz == 0 :
            return ''
        else :
            ret = self.buffer[self.nextRead:self.nextRead+sz-1].decode()
            self.nextRead += sz;
            return ret;
    
    def getRestData(self) :
        return self.buffer[self.nextRead:len(self.buffer)]
