#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Test for Hydra
  Created: 03/06/17
"""

import unittest
import types

from minihydra import MiniHydra
from minihydra.core.modmanager import ModManager
from minihydra.core.mod_maker import make_mod
from minihydra.core.base import ModBase

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
                          session='default', do_continue=False,
                          debug=False)
        gen = hydra.start(async=True)
        self.assertTrue(isinstance(gen, types.GeneratorType))
        
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
        
    
    #----------------------------------------------------------------------
    def test_mixer(self):
        """"""
        gen = MiniHydra('target','testmod', dict_file=['minihydra/dicts/default_un.txt',
                                                 'minihydra/dicts/default_pd.txt'])
        gen.start(True)
        
    #----------------------------------------------------------------------
    def test_mod_maker(self):
        """"""
        def test(payload):
            print payload
            return False
        modclass = make_mod(target_func=test)
        self.assertTrue(issubclass(modclass, ModBase))

        mh = MiniHydra('target',modclass)
        mh.start(async=True)
    
    #----------------------------------------------------------------------
    def test_build_mod_auto(self):
        """"""
        def test(target, payload):
            #print 'target:{target}  -  payload:{p}'.format(target=target, p=payload)
            return False
            
        hydra = MiniHydra('target1', test, do_continue=False)
        result = hydra.start(async=True)
        
        for i in range(4):
            print result.next()
        

if __name__ == '__main__':
    unittest.main()