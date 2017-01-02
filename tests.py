#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Test For minihydra
  Created: 2017/1/2
"""

import unittest

from function_test.test_basic_api import BasicAPITest

if __name__ == '__main__':
    basic_api = unittest.TestLoader().loadTestsFromTestCase(BasicAPITest)
    unittest.TextTestRunner(verbosity=2).run(basic_api)