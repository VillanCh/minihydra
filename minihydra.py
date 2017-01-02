#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Blasting passwd
  Created: 2017/1/2
"""

import os
import unittest
import time
import threading

from g3ar import DictParser
from g3ar import ThreadPool


from script_driver import ScriptManager

ABS_CURRENT_DIR = os.path.dirname(__file__)

DEFAULT_USERNAME_FILE = os.path.join(ABS_CURRENT_DIR, './dicts/default_un.txt')
DEFAULT_PASSWORD_FILE = os.path.join(ABS_CURRENT_DIR, './dicts/default_pd.txt')

########################################################################
class MiniHydra(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, script_name, path=None, 
                 username_dict=None, password_dict=None,
                 do_continue=False, thread_max=30,
                 ):
        """Constructor"""
        assert isinstance(script_name, (unicode, str)), '[!] Error Script Name'
        
        self._thread_max = thread_max
        self._func = ScriptManager.get(script_name, path)
        
        assert callable(self._func), '[!] Function Error! Invalid Function!?'
        
        self._username_file = username_dict if username_dict else DEFAULT_USERNAME_FILE
        self._passowrd_file = username_dict if username_dict else DEFAULT_PASSWORD_FILE
        
        self._username_parser = None
        self._password_parser = None
        
        self._init_config()
        
    #----------------------------------------------------------------------
    def _init_config(self):
        """"""
        self._pool = ThreadPool(thread_max=self._thread_max)
        self._pool.start()
        
        self._username_parser = DictParser(self._username_file)
        self._password_parser = DictParser(self._passowrd_file)
    
    #----------------------------------------------------------------------
    def gen_payloads(self):
        """"""
        #buff = 
        for usernm in self._username_parser:
            for passwd in self._password_parser:
                yield usernm, passwd
            self._password_parser.reset()
        
    #----------------------------------------------------------------------
    def _start(self):
        """"""
        ret = threading.Thread(name='dispatcher', target=self._dispatcher)
        ret.daemon = True
        ret.start()
        #params = {}
        return self._pool.get_result_generator()
    
    #----------------------------------------------------------------------
    def _dispatcher(self):
        """"""
        for username, password in self.gen_payloads():
            #print username, password
            while self._pool.get_task_queue().qsize() >= 100:
                pass
            self._pool.feed(self._func, 
                            username=username,
                            password=password)        
    
    #----------------------------------------------------------------------
    def sync_start(self):
        """"""
        for i in self._start():
            #print i
            if i['state']:
                self.process_result(i)
    
    #----------------------------------------------------------------------
    def process_result(self, all_result):
        """"""
        exec_result = all_result['result']
        flag = False
        extra = None
        if isinstance(exec_result, bool):
            flag = exec_result
        elif isinstance(exec_result, tuple):
            flag = exec_result[0]
            extra = exec_result[1:]
        #et = all_result['current_task'] if all_result.has_key('current_task') else ''
        self.print_result(flag, extra)
        
    #----------------------------------------------------------------------
    def print_result(self, flag, extra=None, taskinfo=''):
        """"""
        SUC = 'SUCCESS '
        FAI = 'FAILED! '
        if flag:
            BANNER = SUC
        else:
            BANNER = FAI
        print(BANNER + 'ExtraInfo: ' + str(extra))
            
    
    #----------------------------------------------------------------------
    def echo_to_result(self, ):
        """"""
        os.system('echo "%s | %s" >> success.txt')
        
  
        
########################################################################
class HydraTest(unittest.case.TestCase):
    """"""
    
    #----------------------------------------------------------------------
    def test_hydra(self):
        """Constructor"""
        MiniHydra(script_name='testdemo').sync_start()
                
            
            
    
    

if __name__ == '__main__':
    unittest.main()