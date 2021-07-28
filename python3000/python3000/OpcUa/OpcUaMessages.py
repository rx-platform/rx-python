from Error.error import *

class OpcUaHeader :
    
    def __init__(self) :
        self.MessageType = ''
        self.IsFinal = ''
        self.MessageSize = 0

    def deserialize(self, data) :

        self.MessageType=data[0:3].decode()
        self.IsFinal = data[3:4].decode()
        self.MessageSize = int.from_bytes(data[4:8], 'little')

        # check to see are messages o.k.
        if self.MessageType == 'ACK' and self.IsFinal == 'F' :
            return True
        elif self.MessageType == 'ERR' and self.IsFinal == 'F' :
            error('Response error')
            return True
        elif self.MessageType == 'MSG' and (self.IsFinal == 'F' or self.IsFinal == 'C'):
            return True
        else :
            error('Invalid message')
            return False


class OpcUaHelloMessage :
    
    def __init__(self, endpoint) :
        self.ProtocolVersion=0
        self.ReceiveBufferSize=65536
        self.SendBufferSize=65536
        self.MaxMessageSize=0
        self.MaxChunkCount=0
        self.Endpoint=endpoint

    def serialize(self, writer) :
        writer.writeUInt32(self.ProtocolVersion)
        writer.writeUInt32(self.ReceiveBufferSize)
        writer.writeUInt32(self.SendBufferSize)
        writer.writeUInt32(self.MaxMessageSize)
        writer.writeUInt32(self.MaxChunkCount)
        writer.writeString(self.Endpoint)


class OpcUaACKMessage :
    
    def __init__(self) :        
        self.ProtocolVersion=0
        self.ReceiveBufferSize=0
        self.SendBufferSize=0
        self.MaxMessageSize=0
        self.MaxChunkCount=0

    def deserialize(self, reader) :        
        self.ProtocolVersion = reader.readUInt32()
        self.ReceiveBufferSize = reader.readUInt32()
        self.SendBufferSize = reader.readUInt32()
        self.MaxMessageSize = reader.readUInt32()
        self.MaxChunkCount = reader.readUInt32()


class OpcUaTransportMessage :
    
    def __init__(self) :        
        self.ChanelId=0
        self.TokenId=0
        self.SequenceNumber=0
        self.RequestId=0

    def deserialize(self, reader) :        
        self.ChanelId = reader.readUInt32()
        self.TokenId = reader.readUInt32()
        self.SequenceNumber = reader.readUInt32()
        self.RequestId = reader.readUInt32()
