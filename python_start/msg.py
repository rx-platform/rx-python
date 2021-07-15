import asyncio

async def tcp_echo_client1(message):

    #Message Header 
    MessageType                         =   'MSG'
    Reserved                            =   'F'  
    MessageSize                         =   32 +len(message)
    SecureChannelId                     =   0
    #Security Header
    SecurityPolicyUriLength             =   0
    SecurityPolicyUri                   =   None
    SenderCertificateLength             =   0
    SenderCertificate                   =   None
    ReceiverCertificateThumbprintLength =   0
    ReceiverCertificateThumbprint       =   None
    TokenId                             =   0
    #Sequence Header
    SequenceNumber                      =   0
    RequestId                           =   0
    #Message Footer
    PaddingSize                         =   ''
    Padding                             =   ''
    ExtraPaddingSize                    =   ''
    Signature                           =   ''
   
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 31420)

    print(f'Send: {message!r}')
    arr=bytearray()
    arr+=MessageType.encode()
    arr+=Reserved.encode()
    arr+=MessageSize.to_bytes(4,'little')
    #
    arr+=SecureChannelId.to_bytes(4,'little')
    #arr+=SecurityPolicyUriLength.to_bytes(4,'little')
    #arr+=SecurityPolicyUri.encode()
    #arr+=SenderCertificateLength.to_bytes(4,'little')
    #arr+=SenderCertificate.encode()
    #arr+=ReceiverCertificateThumbprintLength.to_bytes(4,'little')
    #arr+=ReceiverCertificateThumbprint.encode()
    arr+=TokenId.to_bytes(4,'little')
    arr+=SequenceNumber.to_bytes(4,'little')
    arr+=RequestId.to_bytes(4,'little')
    arr+=PaddingSize.encode()
    arr+=Padding.encode()
    arr+=ExtraPaddingSize.encode()
    arr+=Signature.encode()
    #
    arr+=len(message).to_bytes(4,'little')
    arr+=message.encode()
    writer.write(arr)
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()


#asyncio.run(tcp_echo_client1('hello'))