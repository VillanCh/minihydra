#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: MiniHydra main
  Created: 03/07/17
"""

import unittest
import os
import json
import Queue
import time

from g3ar import DictParser
from g3ar import ThreadPool
from g3ar.utils.thread_utils import start_new_thread

from .core.modmanager import ModManager
from .core.base import ModBase
from .core.exceptions import ImportModError, NoModExisted, UnknownException

MINIHYDRA_ROOT = os.path.dirname(__file__)

DEFAULT_SESSION = 'minihydra'
DO_CONTINUE = False
THREAD_MAX = 40

DEFAULT_DICT_PATH = os.path.join(MINIHYDRA_ROOT, 'dicts/default_pd.txt')

########################################################################
class MiniHydra(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, target, mod, dict_file, session=DEFAULT_SESSION,
                 do_continue=DO_CONTINUE, thread_max=THREAD_MAX, 
                 result_callback=None, debug=False,
                 success_file='result.success.txt'):
        """Constructor"""
        #
        # set target
        #
        self._target = target
        
        #
        # set dict
        #
        if not dict_file:
            dict_file = DEFAULT_DICT_PATH
        self._dict_parser = DictParser(dict_file, session, do_continue)
    
        #
        # current mod
        #
        self._mod_name = mod
        self._mod = ModManager.get_mod(self._mod_name)
        if not issubclass(self._mod, ModBase):
            raise ImportModError('[x] not a right ModBase instanct!')
        elif not self._mod:
            raise NoModExisted()
        
        #
        # result callback
        #
        self._result_callback = result_callback
        
        #
        # store the success paylad
        #
        self._success_file = success_file
        
        #
        # init pool
        #
        clean_mod = not debug
        self._pool = ThreadPool(thread_max=thread_max, clean_mod=clean_mod)
        self._pool.start()
        self._result_pool = self._pool.get_result_queue()
        
    
    #----------------------------------------------------------------------
    def start(self, async=False):
        """"""
        start_new_thread(self._start, name='minihydra-dispatcher')
        
        resultgen = self.result_gen()
        
        try:
            if not async:
                while True:
                    for i in resultgen:
                        print i
            else:
                #
                # async
                #
                return resultgen
        except KeyboardInterrupt:
            self.save()
            #print 'END'
        
        return resultgen
            
    #----------------------------------------------------------------------
    def _start(self):
        """"""
        modinstance = self._mod(self._target)
        
        for i in self._dict_parser:
            payloads = modinstance.dict_callback(i)
            self._pool.feed(modinstance.guess, payloads)
    
    #----------------------------------------------------------------------
    def save(self):
        """"""
        self._dict_parser.force_save()
    
    #----------------------------------------------------------------------
    def _default_result_callback(self, result):
        """"""
        if result.get('success'):
            with open(self._success_file, 'ab+') as fp:
                fp.write("{payload}\n".format(payload=result))
        
        return result

    #----------------------------------------------------------------------
    def result_gen(self):
        """"""
        while True:
            if self._result_pool.qsize() == 0:
                time.sleep(1)
                continue
            else:
                result = self._result_pool.get()
                if result.get('state'):
                    result = result.get('result')
                else:
                    continue
            
            yield self._default_result_callback(result)
        
        
        

if __name__ == '__main__':
    unittest.main()