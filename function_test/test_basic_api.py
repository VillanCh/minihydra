#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Test Basic api
  Created: 2017/1/2
"""

import sys
sys.path.append('..')

import unittest
from g3ar.utils.print_utils import print_bar
from script_driver import ScriptManager, Script

########################################################################
class BasicAPITest(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_build_script_manager(self):
        """Constructor"""
        print_bar()
        print_bar('ScriptManager-Test')
        print_bar()
        
        print_bar('test get functions')
        manager = ScriptManager()
        script = manager.get_script('testdemo')
        funcs = script.get_function()
        self.assertTrue(callable(funcs))
        print('Have got function')
        print(funcs('admin','password'))
        
        funcs = manager.get_target_func('testdemo')
        self.assertTrue(callable(funcs))
        
        funcs = manager.get('testdemo')
        self.assertTrue(callable(funcs))
        
        print_bar('test get functions finished!')
        print_bar()
        print_bar('test search')
        
        result = manager.search(keyword_or_regex = 'test')
        for i in result:
            print(i)
        
        print_bar('test search success!')

if __name__ == '__main__':
    unittest.main()