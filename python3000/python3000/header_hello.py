class header_hello():
    """description of class"""

    def __init__(self, MessageType, Reserved, MessageSize, ProtocolVersion, ReceiveBufferSize, SendBufferSize, MaxMessageSize, MaxChunkCount):

       self.type         =  MessageType
       self.res          =  Reserved
       self.size         =  MessageSize
       self.protocol     =  ProtocolVersion
       self.rec_buffer   =  ReceiveBufferSize
       self.send_buffer  =  SendBufferSize
       self.max_msg      =  MaxMessageSize
       self.max_chunk    =  MaxChunkCount


        


