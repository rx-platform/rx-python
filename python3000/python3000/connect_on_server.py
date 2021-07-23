import asyncio
from header_hello import header_hello
from deserialization import deserialization
from deserialization import function_for_deserialization
from error import error
from buffer_cut import buffer_cut
class connect_on_server(object):
    """description of class"""
   

    async def connect(ip, port, msg_length):

        msg='hello'
        length=len(msg)

        head=header_hello('HEL', 'F', 32+length, 0, 65536, 65536, 0, 0)
        recieved=deserialization('','',0,0,0,0,0,0)

        reader, writer = await asyncio.open_connection(ip, port)

        bafer=bytearray()

        bafer+=  head.type.encode()       
        bafer+=  head.res.encode()      
        bafer+=  head.size.to_bytes(4,'little')        
        bafer+=  head.protocol.to_bytes(4,'little')     
        bafer+=  head.rec_buffer.to_bytes(4,'little')   
        bafer+=  head.send_buffer.to_bytes(4,'little')  
        bafer+=  head.max_msg.to_bytes(4,'little')      
        bafer+=  head.max_chunk.to_bytes(4,'little')    
        bafer+=  length.to_bytes(4,'little')
        bafer+=  msg.encode()

     
        writer.write(bafer)
        await writer.drain()
        
        data = await reader.read(100)
        recieved=function_for_deserialization(recieved,data)
      
        number_of_packages=await buffer_cut.break_in_pieces(recieved.Send_Buffer_Size, msg_length)
        

        if recieved.Message_Type=='ACK':
            print('Konekcija je uspesna')  
        else:
            error('Ack error')
        return reader, writer, number_of_packages, head.send_buffer


