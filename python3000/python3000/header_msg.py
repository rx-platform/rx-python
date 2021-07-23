class header_msg(object):
    """description of class"""

    def __init__(self, MessageType, Reserved, MessageSize, SecureChannelId, SecurityPolicyUriLength, SecurityPolicyUri,SenderCertificateLength, SenderCertificate, ReceiverCertificateThumbprintLength, ReceiverCertificateThumbprint, TokenId, SequenceNumber, RequestId, PaddingSize, Padding, ExtraPaddingSize, Signature):

        #Message Header 
        self.msg_type             = MessageType
        self.res                  = Reserved
        self.msg_size             = MessageSize 
        self.sec_channel          = SecureChannelId 
        #Security Header
        self.sec_pol_uri_len      = SecurityPolicyUriLength        
        self.sec_pol_uri          = SecurityPolicyUri               
        self.sen_cer_len          = SenderCertificateLength        
        self.sen_cer              = SenderCertificate                  
        self.rec_cer_thu_len      = ReceiverCertificateThumbprintLength 
        self.rec_cer_thu          = ReceiverCertificateThumbprint      
        self.token_id             = TokenId  
        #Sequence Header
        self.seq_num              = SequenceNumber 
        self.req_id               = RequestId                  
        #Message Footer
        self.pad_size             = PaddingSize                      
        self.pad                  = Padding                            
        self.extra_pad_s          = ExtraPaddingSize                   
        self.sign                 = Signature                         

