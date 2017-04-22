#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Manage Mod
  Created: 03/07/17
"""

import unittest
import os
import types
import importlib

from g3ar.utils.inspect_utils import get_classes

from . import conf
from .exceptions import ImportModError
from .base import ModBase


CURRENT_PATH = os.path.dirname(__file__)

########################################################################
class ModManager(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, *vargs, **kwargs):
        """Constructor"""
        
    #----------------------------------------------------------------------
    def __new__(cls, *vargs, **kwargs):
        """Build Singleton"""
        if not hasattr(cls, '_instance'):
            #
            # init instance
            #
            orig = super(ModManager, cls)
            cls._instance = orig.__new__(cls, *vargs, **kwargs)
        
        return cls._instance
    
    #----------------------------------------------------------------------
    @classmethod
    def get_mod_list(cls):
        """"""
        return conf.MODLIST
    
    #----------------------------------------------------------------------
    @classmethod
    def get_mod(cls, name):
        """get the instance of mod
        
        Params:
          name: :str: the name of mod you want."""
        if name not in cls.get_mod_list():
            return None
        
        #
        # Import mod
        #
        mod_name = '..mods.' + name
        #print mod_name
        mod = importlib.import_module(name=mod_name, package='minihydra.core')
        print mod
        if not isinstance(mod, tuple([types.ModuleType,])):
            raise ImportModError('[x] Import mod Error!')
        
        #
        # select mod instance
        #
        for i in get_classes(mod):
            #print i
            if issubclass(i, ModBase) and not (i == ModBase):
                return i
            
        return None
        
        
        
    

if __name__ == '__main__':
    unittest.main()