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
import types

from g3ar import DictParser, DictParserMixer
from g3ar import ThreadPool
from g3ar.utils.thread_utils import start_new_thread

from .core.modmanager import ModManager
from .core.base import ModBase
from .core.exceptions import ImportModError, NoModExisted, UnknownException, NoTarget, NoMod, DictsError
from .core import conf
from .core import mod_maker

#
# DEFINE PATHS
#
MINIHYDRA_ROOT = os.path.dirname(__file__)
DEFAULT_DICT_DIR = os.path.join(MINIHYDRA_ROOT, 'dicts/')
DEFAULT_DICT_PATH = os.path.join(MINIHYDRA_ROOT, 'dicts/default_pd.txt')

#
# DEFINE CONST
#
DEFAULT_SESSION = conf.DEFAULT_SESSION
DO_CONTINUE = conf.DO_CONTINUE
THREAD_MAX = conf.THREAD_MAX
DEBUG = conf.DEBUG
SUCCESS_FILE = conf.SUCCESS_FILE



########################################################################
class MiniHydra(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, target=None, mod=None, one_result=False, dict_file=None, session=DEFAULT_SESSION,
                 do_continue=DO_CONTINUE, thread_max=THREAD_MAX, 
                 result_callback=None, debug=DEBUG,
                 success_file=SUCCESS_FILE):
        """Constructor"""
        #
        # set target
        #
        self._target = target
        
        #
        # set dict
        #
        self.set_dict_file(dict_file, session, do_continue)
        
        #
        # current mod
        #
        self._one_result = one_result
        self.set_mod(mod)

        
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
        
        
        self._final_queue = Queue.Queue()
        
    #----------------------------------------------------------------------
    def set_dict_file(self, dict_file, session=DEFAULT_SESSION, 
                      do_continue=DO_CONTINUE):
        """"""
        if isinstance(dict_file, tuple([list, tuple])):
            _dicts = []
            for _dict_single in dict_file:
                _ret = os.path.exists(_dict_single)
                if _ret:
                    _dicts.append(_dict_single)
                else:
                    _dict_single_ex = os.path.join(DEFAULT_DICT_DIR, _dict_single)
                    if os.path.exists(_dict_single_ex):
                        _dicts.append(_dict_single_ex)
                    else:
                        raise NoSuchDict('[x] No "{orig}" and No {aft} File!'.format(
                            orig = _dict_single,
                            aft = _dict_single_ex,
                        ))
            self._dict_parser = DictParserMixer(_dicts, do_continue)
        elif isinstance(dict_file, types.StringTypes) or dict_file == None:
            if not dict_file:
                dict_file = DEFAULT_DICT_PATH
            self._dict_parser = DictParser(dict_file, session, do_continue)
        else:
            raise DictsError()
    
    #----------------------------------------------------------------------
    def start(self, async=False):
        """"""
        if self._target:
            pass
        else:
            raise NoTarget()
        
        if hasattr(self, '_mod') and self._mod:
            pass
        else:
            raise NoMod()
        
        #
        # pre attack and check it!
        #
        modinstance = self._mod(self._target)
        finish_it = modinstance.finished
        if finish_it:
            self._final_queue.put(modinstance.get_predata())
            self._result_pool.put(modinstance.get_predata())
        else:
            start_new_thread(self._start, name='minihydra-dispatcher', args=tuple([modinstance]))
        
        resultgen = self.result_gen()
        
        #
        # async / sync ?
        #
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
    def _start(self, modinstance):
        """"""
        #modinstance = self._mod(self._target)
        
        for i in self._dict_parser:
            while self._pool.get_task_queue().qsize() >= 50:
                pass
            finish_it = modinstance.finished
            if finish_it:
                while self._pool.get_task_queue().qsize() >= 1:
                    pass
                break
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
            self._final_queue.put(result)
            with open(self._success_file, 'ab+') as fp:
                    fp.write("{payload}\n".format(payload=result))
        
        return result

    #----------------------------------------------------------------------
    def result_gen(self):
        """"""
        try:
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
        except KeyboardInterrupt as e:
            raise e
        
    #----------------------------------------------------------------------
    def set_mod(self, mod):
        """"""
        #
        # mod is the name of mod
        #
        if isinstance(mod, types.StringTypes):
            self._mod_name = mod
            self._mod = ModManager.get_mod(self._mod_name)
            try:
                if not issubclass(self._mod, ModBase):
                    raise ImportModError('[x] not a right ModBase instanct!')
                elif not self._mod:
                    raise NoModExisted()
            except:
                raise ImportModError('[x] No such mod in mods or unexpected modname')
        elif callable(mod):
            self._mod = mod_maker.make_mod(mod, self._one_result)
        elif issubclass(mod, ModBase):
            self._mod = mod            
            
        
    
    @property
    def pool(self):
        """"""
        return self._pool
    
    #----------------------------------------------------------------------
    def percent(self):
        """"""
        return self._dict_parser.get_current_pos() / self._dict_parser.get_total_size()

    #----------------------------------------------------------------------
    def stop(self):
        """"""
        self.save()
        self._dict_parser.close()
        self._pool.stop()
    
    #----------------------------------------------------------------------
    def get_current_pos(self):
        """"""
        return self._dict_parser.get_current_pos()
    
    #----------------------------------------------------------------------
    def get_total_size(self):
        """"""
        return self._dict_parser.get_total_size()
    
    #----------------------------------------------------------------------
    def get_final_queue(self):
        """"""
        self._final_queue
        
        

if __name__ == '__main__':
    unittest.main()