import asyncio
from OpcUa.RxBufferWriter import *
from OpcUa.RxBufferReader import *
from OpcUa.OpcUaMessages import *
from Error.error import *

def CorrectPacketSize(data) :

    data[4:8]=len(data).to_bytes(4,'little') 

class OpcUaTransport:
    def __init__(self , ip, port, endpoint) :

       self.ip= ip
       self.port=port
       self.endpoint=endpoint
       self.reader=None
       self.writer=None
       self.SequenceNum=1
       self.RequestId=1
       self.ReceiveSize=0
       self.SendSize=0;

    async def InternalSendPacket(self, data) :

       CorrectPacketSize(data)
       self.writer.write(data)
       await self.writer.drain()

    async def InternalReceivePacket(self) :

        # read header first
        recData = await self.reader.read(8)

        recHead = OpcUaHeader()
        if recHead.deserialize(recData) :
            recData = bytes()
            leftToRead=recHead.MessageSize - 8

            while leftToRead > len(recData) :
               recData +=  await self.reader.read(65536)

            return recHead , bytearray(recData)
        else :
            return None , None


    async def connect(self) :
       try:
           self.reader, self.writer = await asyncio.open_connection(self.ip, self.port)
       except:
           error('Connection error')
           return False
       # create hello message
       toSend=bytearray()
       toSend+='HELF'.encode()
       buffWriter = RxBufferWriter(toSend)
       buffWriter.writeUInt32(0) #write dummy size, just make space

       msg = OpcUaHelloMessage(self.endpoint)
       msg.serialize(buffWriter)

       await self.InternalSendPacket(toSend)
       
       header, data = await self.InternalReceivePacket()

       if header!=None and header.MessageType=='ACK' :
           msg = OpcUaACKMessage()
           bufferReader=RxBufferReader(data);
           msg.deserialize(bufferReader);

           self.ReceiveSize=msg.ReceiveBufferSize
           self.SendSize = msg.SendBufferSize

           return True

       else : 
           error('Ack error')
           return False

    async def sendReceive(self, data) :
        
        # ovde fali provera da li je paket veci od SendSize pa deljenje
        # za sada je i ovo dosta

        toSend=bytearray()
        toSend+='MSGF'.encode()
        buffWriter = RxBufferWriter(toSend)
        buffWriter.writeUInt32(0) #write dummy size, just make space


        # ovo mozda upakovati u serialize(self.SequenceNum, self.RequestId)
        #chanel id
        buffWriter.writeUInt32(0)
        #token id
        buffWriter.writeUInt32(0)
        # sequence number
        buffWriter.writeUInt32(self.SequenceNum)
        #handle rollover
        self.SequenceNum = self.SequenceNum + 1
        # request number
        buffWriter.writeUInt32(self.RequestId)
        #handle rollover
        self.RequestId = self.RequestId + 1

        #now add the message:
        toSend+=data

        CorrectPacketSize(toSend)

        self.writer.write(toSend)
        await self.writer.drain()

        header, data = await self.InternalReceivePacket()

        if header!=None and header.MessageType=='MSG' :
           msg = OpcUaTransportMessage()
           bufferReader=RxBufferReader(data)
           msg.deserialize(bufferReader)

           #provera sequenceid i request id varijabli

           return bufferReader.getRestData()








       

       
    