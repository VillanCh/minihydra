#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: MiniHydra Console
  Created: 03/07/17
"""

import unittest
import Queue

from cmd2 import Cmd, options, make_option
from minihydra import MiniHydra
from minihydra.minihydra import DEFAULT_SESSION
from progressive.bar import Bar
from time import sleep
from g3ar.utils.thread_utils import start_new_thread

banner = '''
 __  __ _       _ _   _           _
|  \/  (_)_ __ (_| | | |_   _  __| |_ __ __ _
| |\/| | | '_ \| | |_| | | | |/ _` | '__/ _` |
| |  | | | | | | |  _  | |_| | (_| | | | (_| |
|_|  |_|_|_| |_|_|_| |_|\__, |\__,_|_|  \__,_|
                        |___/                   -by v1ll4n
                        
'''

info = '''
Author: v1ll4n
Home: http://minihydra.villanch.top

Brute Password or more?
Read the BIG DICTIONARY with stream?
Work with g3ar.ThreadPool.
Less cost and run faster.

Happy hunting!
'''


########################################################################
class MiniHydraCli(Cmd):
    """"""
    prompt = 'MiniHydra> '
    intro = banner + info

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        Cmd.__init__(self, use_ipython=True)
        
    #----------------------------------------------------------------------
    def do_progress(self, args):
        """show progressbar"""
        if self.hydra_running():
            pass
        else:
            print('[x] MiniHydra is not running!')
            return 
        
        try:
            bar = Bar(max_value=self._hydra.get_total_size())
            bar.cursor.clear_lines(2)
            bar.cursor.save()
            while True:
                sleep(0.1)
                bar.cursor.restore()
                bar.draw(value=self._hydra.get_current_pos())
            
        except KeyboardInterrupt:
            pass
    
    #----------------------------------------------------------------------
    @options(option_list=[make_option('-t', '--target', dest='target', help='What you want to attack!'),
                          make_option('-m', '--mod', dest='mod', help='How to attack?'),
                          make_option('-d', '--dict', dest='dict_file', default=None, help='What dict you want to use, if you want to select ' + 
                                      'more dicts, split by \',\''),
                          make_option('-c', '--continue', dest='do_continue', action='store_false', default=True, help='Continue Last Session?'),
                          make_option('-s', '--session', dest='session', default=DEFAULT_SESSION, help='Session name'),
                          make_option('-n', '--thread_max', dest='thread_max', default=50, type=int, help='Thread Max'),
                          ])
    def do_start(self, arg, opts=None):
        """start a hydra instance""" 
        target = opts.target
        mod = opts.mod
        dict_file = opts.dict_file
        if ',' in dict_file:
            dict_file = dict_file.split(',')
        else:
            pass
        
        thread_max = opts.thread_max
        session = opts.session
        do_contine = opts.do_continue
        
        if hasattr(self, '_hydra'):
            print('[x] A Hydra is running! Please stop it first!')
            return 
        
        if not mod or not target:
            print('[x] Error! target and mod have to be set!')
            return 
        
        self._hydra = MiniHydra(target=target, mod=mod, dict_file=dict_file, 
                               session=session, 
                               do_continue=do_contine, 
                               thread_max=thread_max)
        
        self._result_gem = self._hydra.start(async=True)
        self._result_queue = Queue.Queue()
        
        start_new_thread(self._collect_result, daemon=True)
    
    #----------------------------------------------------------------------
    def do_watch(self, args):
        """show the result and block the screen"""
        try:
            while True:
                try:
                    _ret = self._result_queue.get_nowait()
                    print(_ret)
                except Queue.Empty:
                    sleep(0.1)
        except KeyboardInterrupt:
            return 
        

    #----------------------------------------------------------------------
    def hydra_running(self):
        """"""
        if hasattr(self, '_hydra'):
            return True
        else:
            return False
    
    #----------------------------------------------------------------------
    def do_stop(self, args):
        """Stop the hydra"""
        self._hydra.stop()
    
    #----------------------------------------------------------------------
    def _collect_result(self):
        """"""
        for i in self._result_gem:
            self._result_queue.put(i)
        
        

if __name__ == '__main__':
    MiniHydraCli().cmdloop()