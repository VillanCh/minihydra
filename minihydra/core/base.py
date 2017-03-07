#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Base classes for minihydra
  Created: 03/06/17
"""

import unittest
import abc
import traceback

########################################################################
class Base(object):
    """Base class"""

    pass

########################################################################
class ModBase(Base):
    """"""
    
    

    #----------------------------------------------------------------------
    def __init__(self, target):
        """Constructor"""
        self.target = target
        
    #----------------------------------------------------------------------
    def dict_callback(self, line):
        """"""
        return line
    
    #----------------------------------------------------------------------
    def guess(self, payloads):
        """"""
        result = {}
        result['success'] = False
        result['payload'] = payloads
        result['exception'] = None
        
        try:
            _result = self.attack(payloads)
        except Exception as e:
            _result = False
            result['exception'] = traceback.format_exc()
        
        result['success'] = _result
        
        return result
    
    #----------------------------------------------------------------------
    def attack(self, *args, **kwargs):
        """"""
        pass
    
        
        
    
    
    

if __name__ == '__main__':
    unittest.main()