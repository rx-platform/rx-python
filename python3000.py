import asyncio
from OpcUa.RxBufferWriter import *
from OpcUa.OpcUaTransport import *
from RxProtocol.RxProtocolConnection import *

async def main_function() :

    transport = OpcUaTransport('127.0.0.1', 31420, 'hello')

    if await transport.connect() :
        
        connection = RxProtocolConnection(transport)

        msg='{  "header": {    "requestId": 7,    "msgType": "brwReq"  },  "body": {    "path": "/sys/host",    "filter": null  }}' 

        response = await connection.SendReceiveString(msg)

        print(response)



        
    

asyncio.run(main_function())

 