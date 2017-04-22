#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Make a mod interface
  Created: 03/14/17
"""

import unittest
from .template import TemplateMod

####################################################################################
####################################################################################
####################################################################################
#
# Make mod instance 
# 1. parse function
# 2. check param
#
####################################################################################
####################################################################################
####################################################################################

#----------------------------------------------------------------------
def make_mod(target_func, one_result=False):
    """"""
    assert callable(target_func)
    
    class CustomMod(TemplateMod):
        #----------------------------------------------------------------------
        def __init__(self, target):
            """"""
            TemplateMod.__init__(self, target, 
                                 attack_func=target_func, 
                                only_one_result=one_result)
    
    return CustomMod
            
        

if __name__ == '__main__':
    unittest.main()