class deserialization(object):
    """description of class"""

    def __init__(self,Message_Type,Is_Final, Message_Size, Protocol_Version, Recieve_Buffer_Size, Send_Buffer_Size, Max_Message_Size, Max_Chunk_Count):   
        self.Message_Type                   =  Message_Type
        self.Is_Final                       =  Is_Final
        self.Message_Size                   =  Message_Size
        self.Protocol_Version               =  Protocol_Version
        self.Recieve_Buffer_Size            =  Recieve_Buffer_Size
        self.Send_Buffer_Size               =  Send_Buffer_Size
        self.Max_Message_Size               =  Max_Message_Size
        self.Max_Chunk_Count                =  Max_Chunk_Count

def function_for_deserialization(recieved, data):
        
        datastr=data.decode()
        recieved.Message_Type=datastr[0]+datastr[1]+datastr[2]
        recieved.Is_Final=datastr[3]
        recieved.Message_Size=int.from_bytes([data[4], data[7]], 'little')
        recieved.Protocol_Version=int.from_bytes([data[8], data[11]], 'little')
        recieved.Recieve_Buffer_Size=int.from_bytes([data[12], data[15]], 'little')
        recieved.Send_Buffer_Size=int.from_bytes([data[16], data[19]], 'little')
        recieved.Max_Message_Size=int.from_bytes([data[20], data[23]], 'little')
        recieved.Max_Chunk_Count=int.from_bytes([data[24], data[27]], 'little')
        
        
        
   
        return recieved      


