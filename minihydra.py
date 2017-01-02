#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Blasting passwd
  Created: 2017/1/2
"""

import unittest

from g3ar import DictParser
from g3ar import ThreadPool

from script_driver import ScriptManager

########################################################################
class MiniHydra(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, script_name, path=None, \
                 username_dict=None, password_dict=None):
        """Constructor"""
        assert isinstance(script_name, (unicode, str)), '[!] Error Script Name'
        
        self._func = ScriptManager.get(script_name, path)
        
        assert callable(_func), '[!] Function Error! Invalid Function!?'
        
        self._username_gen = None
        self._password_gen = None
        
    #----------------------------------------------------------------------
    def _init_config(self):
        """"""
        self.
        
    #----------------------------------------------------------------------
    def set_username_generator(self, username_gen):
        """"""
        pass
    
    #----------------------------------------------------------------------
    def set_password_generator(self, password_gen):
        """"""
        pass
        
        
    
    

if __name__ == '__main__':
    unittest.main()