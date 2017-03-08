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
from .exceptions import ModReturnError

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
        result['data'] = None
        
        try:
            _result = self.attack(payloads)
            if isinstance(_result, (tuple, list,)):
                assert isinstance(_result[0], bool), '[x] Error! The first return value have to be a bool.'
                _all = _result
                _result = _all[0]
                result['data'] = _all[1:]
            elif isinstance(_result, bool):
                pass
            else:
                raise ModReturnError('[x] Error return : {}'.format(_result))
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