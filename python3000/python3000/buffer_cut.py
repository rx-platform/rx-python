import asyncio
from deserialization import deserialization

class buffer_cut(object):
    """description of class"""

    number_of_packages=0

    async def break_in_pieces(buffer_size, msg_size):
        number_of_packages=msg_size//65536
        
        if msg_size>65536*(number_of_packages): number_of_packages+=1

        return number_of_packages
        
