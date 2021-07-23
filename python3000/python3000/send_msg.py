import asyncio
from header_msg import header_msg

class send_msg(object):
    """description of class"""

    async def comunicate(reader, writer, msg, buffer_size, number_of_packages):
        current_package=0
        while current_package<number_of_packages:
            pom=current_package*(buffer_size-50)
            current_msg=''
            while pom<(current_package+1)*(buffer_size-50):
                   if pom>=len(msg):
                      break
                   current_msg+=msg[pom]
                   pom+=1
            length=len(msg)

            head=header_msg('MSG', 'F', 40+len(current_msg), 0, 0, '', 0, '', 0, '',0, current_package, number_of_packages, '', '', '', '')

            bafer=bytearray()

            #Message Header 
            bafer+=  head.msg_type.encode()       
            bafer+=  head.res.encode()      
            bafer+=  head.msg_size.to_bytes(4,'little')        
            bafer+=  head.sec_channel.to_bytes(4,'little') 
            #Security Header
            bafer+=  head.sec_pol_uri_len.to_bytes(4,'little') 
            bafer+=  head.sec_pol_uri.encode()  
            bafer+=  head.sen_cer_len.to_bytes(4,'little') 
            bafer+=  head.sen_cer.encode()  
            bafer+=  head.rec_cer_thu_len.to_bytes(4,'little') 
            bafer+=  head.rec_cer_thu.encode()  
            bafer+=  head.token_id.to_bytes(4,'little')   
            #Sequence Header
            bafer+=  head.seq_num.to_bytes(4,'little')  
            bafer+=  head.req_id.to_bytes(4,'little')   
            #Message Footer
            bafer+=  head.pad_size.encode()  
            bafer+=  head.pad.encode()
            bafer+=  head.extra_pad_s.encode()
            bafer+=  head.sign.encode()
            bafer+=  len(current_msg).to_bytes(4,'little')
            bafer+=  current_msg.encode()

            writer.write(bafer)
            await writer.drain()
            print('Poruka je poslata')  
            print(current_package)
            #data =await reader.read(100)
            #bufer=data.decode()
            current_package += 1