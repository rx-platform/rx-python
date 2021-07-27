
class RxBufferWriter:

    def __init__(self, buffer) :
        if buffer == None :
            self.buffer = bytearray()
        else :
            self.buffer = buffer

    def writeUInt8(self, val) :
        self.buffer+=  val.to_bytes(1,'little')   

    def writeUInt16(self, val) :
        self.buffer+=  val.to_bytes(2,'little')   
    
    def writeUInt32(self, val) :
        self.buffer+=  val.to_bytes(4,'little') 

    
    def writeString(self, val) :
        if val == None :
            self.buffer+=  val.to_bytes(-1,'little') 

        else :
            length = len(val)
            self.writeUInt32(length)
            
            if length>0 :
                self.buffer+=val.encode()
     
    def getBuffer(self) : 
        return self.buffer