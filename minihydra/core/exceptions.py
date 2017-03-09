#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Define exceptions
  Created: 03/07/17
"""

import unittest

########################################################################
class ImportModError(Exception):
    """"""
    pass

########################################################################
class NoModExisted(Exception):
    """"""
    pass

########################################################################
class UnknownException(Exception):
    """"""
    pass

########################################################################
class NoTarget(Exception):
    """"""
    pass

########################################################################
class NoMod(Exception):
    """"""
    pass

########################################################################
class ModReturnError(Exception):
    """"""
    pass

########################################################################
class DictsError(Exception):
    """"""
    pass
    
    
########################################################################
class END(Exception):
    """"""
    pass
    
    
    
    
    

if __name__ == '__main__':
    unittest.main()