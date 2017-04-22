#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: test for minihydra
  Created: 03/07/17
"""

import unittest
import random
import time

from ..core.base import ModBase


########################################################################
class Tester(ModBase):
    """"""

    #----------------------------------------------------------------------
    def attack(self, *args, **kwargs):
        """"""
        
        time.sleep(random.randint(2,4))
        if random.randint(1,6) == 4:
            #self.finish()
            return True
        else:
            return False
        
        
    
    

if __name__ == '__main__':
    unittest.main()