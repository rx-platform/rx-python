import asyncio
from msg import tcp_echo_client1

async def tcp_echo_client(message):

    MessageType       = 'HEL'
    Reserved          = 'F'  
    MessageSize       =  32 +len(message)
    ProtocolVersion   =   0  
    ReceiveBufferSize = 65536  
    SendBufferSize    = 65536    
    MaxMessageSize    =   0  
    MaxChunkCount     =   0  
   
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 31420)

    print(f'Send: {message!r}')
    arr=bytearray()
    arr+=MessageType.encode()
    arr+=Reserved.encode()
    arr+=MessageSize.to_bytes(4,'little')
    arr+=ProtocolVersion.to_bytes(4,'little')
    arr+=ReceiveBufferSize.to_bytes(4,'little')
    arr+=SendBufferSize.to_bytes(4,'little')
    arr+=MaxMessageSize.to_bytes(4,'little')
    arr+=MaxChunkCount.to_bytes(4,'little')
    arr+=len(message).to_bytes(4,'little')
    arr+=message.encode()
    writer.write(arr)
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    #asyncio.run(tcp_echo_client1('hello'))

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client1('hello'))