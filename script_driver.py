#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Script Driver (Basic class from basic Script Manager)
  Created: 2017/1/2
"""

import unittest
from types import ModuleType
import os 
import re

from g3ar.utils import inspect_utils
from g3ar.utils import import_utils

_ABS_DIRNAME = os.path.dirname(__file__)

_MINIHYDRASCRIPTS_DIR = 'minihydrascripts'
_ABS_MINIHYDRASCRIPTS_DIR = os.path.join(_ABS_DIRNAME, _MINIHYDRASCRIPTS_DIR)

USERNAME = 'username'
PASSWORD = 'password'


########################################################################
class Script(object):
    """A script obj is from a script module.
    
    The script module is user modifying. A script module should only one function
    which contains at least 2 params: username and password.
    
    Attributes:
        mod: :module: the module handler of script module"""

    #----------------------------------------------------------------------
    def __init__(self, mod):
        """Constructor
        
        Params:
            mod: :module: the module where some scripts exsit"""
        assert isinstance(mod, ModuleType), '[!] The [mod] is not a module obj!'
        
        self._mod = mod
        self._targets_funcion = self._find_target_function()
    
    #----------------------------------------------------------------------
    def get_function(self):
        """"""
        return self._targets_funcion
    
    #----------------------------------------------------------------------
    @property    
    def functions(self):
        """"""
        return self._targets_funcion
    
    #----------------------------------------------------------------------
    @property
    def func(self):
        """"""
        return self._targets_funcion
        
    
    #----------------------------------------------------------------------
    def _find_target_function(self):
        """"""
        target_funcs = None
        
        funcs = inspect_utils.get_functions(self._mod)
        for i in funcs:
            params = inspect_utils.get_args_dict(i)['args']
            args_tables = params['args_table']
            _ks = args_tables.keys()
            keys = []
            for j in _ks:
                keys.append(j.lower())
            del _ks
            
            if USERNAME in keys and PASSWORD in keys:
                target_funcs = i
                break
        
        return target_funcs
    
    

########################################################################
class ScriptManager(object):
    """Manager Scripts"""

    #----------------------------------------------------------------------
    def __new__(cls, *vargs, **kwargs):
        """"""
        cls._instance = None
        if cls._instance:
            pass
        else:
            origin = super(ScriptManager, cls)
            cls._instance = origin.__new__(cls, *vargs, **kwargs)
        return cls._instance

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
    
    #----------------------------------------------------------------------
    @classmethod
    def get_script(self, script_name, path=None):
        """"""
        path = path if path else _ABS_MINIHYDRASCRIPTS_DIR
        mod = None
        
        try:
            mod = import_utils.import_by_path(path, script_name)
        except ImportError:
            pass
        
        if not mod:
            try:
                mod = import_utils.import_by_path(os.path.abspath('.'), \
                                                  script_name)
            except ImportError:
                pass
        
        sp = None    
        if mod:
            sp = Script(mod)
        else:
            pass
        
        return sp
    
    #----------------------------------------------------------------------
    @classmethod    
    def get_target_func(self, script_name, path=None):
        """"""
        script = self.get_script(script_name, path)
        if not script:
            return None
        else:
            return script.func
    
    #----------------------------------------------------------------------
    @classmethod
    def get(self, script_name, path=None):
        """"""
        return self.get_target_func(script_name, path)
    
    #----------------------------------------------------------------------
    @classmethod
    def search(self, keyword_or_regex):
        """"""
        result = []
        gen = os.walk(_ABS_MINIHYDRASCRIPTS_DIR)
        scripts = gen.next()[2]
        for i in scripts:
            if i.startswith('_'):
                continue
            elif i.startswith('.pyc'):
                continue
            else:
                if re.findall(keyword_or_regex, i):
                    result.append(i[:-3])
                    continue
        return result
                
                
                    
                    
if __name__ == '__main__':
    unittest.main()