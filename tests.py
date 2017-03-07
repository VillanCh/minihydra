#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Test for Hydra
  Created: 03/06/17
"""

import unittest
from minihydra import MiniHydra
from minihydra.core.modmanager import ModManager

from g3ar.utils.print_utils import print_bar


########################################################################
class MiniHydraTester(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_build_hydra(self):
        """"""
        print_bar('MiniHydra test start')
        
        hydra = MiniHydra(target='http://127.0.0.1:5000/auth', mod='testmod',
                          dict_file=None, 
                          session='default', do_continue=True,
                          debug=True)
        hydra.start()
        
    #----------------------------------------------------------------------
    def test_mod_manager(self):
        """"""
        print_bar('ModManager Test')
        
        print ModManager.get_mod_list()
        print ModManager.get_mod('testmod')
    
    #----------------------------------------------------------------------
    def test_mod(self):
        """"""
        testmod = ModManager.get_mod('testmod')('https://asdfasd')
        print testmod.guess('asdfa')
        
    
    

if __name__ == '__main__':
    unittest.main()