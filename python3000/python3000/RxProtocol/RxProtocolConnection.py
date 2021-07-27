import asyncio
from OpcUa.RxBufferWriter import *
from OpcUa.OpcUaTransport import *


class RxProtocolConnection :
    def __init__(self, transport) :
        self.transport = transport

    async def SendReceiveString(self, msg) :
        
        # write application message
        writer = RxBufferWriter(None)
        
        writer.writeUInt8(1)
        writer.writeUInt8(1)
        writer.writeUInt16(0x7fff)
        writer.writeString(msg)

        receivedData = await self.transport.sendReceive(writer.getBuffer())

        reader = RxBufferReader(receivedData)

        nodeType = reader.readUInt8()
        nodeNamespace = reader.readUInt8()
        nodeId = reader.readUInt8()

        response=reader.readString()

        return response
        