#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Parse config
  Created: 03/07/17
"""

import unittest
import os
import configparser
import io

MINIHYDRA_SECTION = 'minihydra_param'
MOD_LIST_SECTION = 'mod_list'

CONFIG_FILENAME = 'minihydra.conf'

CURRENT_DIR = os.path.dirname(__file__)
CONFIG_PATH = os.path.dirname(CURRENT_DIR) + '/'

_configtext = None
if not _configtext:
    with open(os.path.join(CONFIG_PATH, CONFIG_FILENAME)) as fp:
        _configtext = fp.read()
    
    CONF = configparser.RawConfigParser(allow_no_value=True)
    CONF.readfp(io.BytesIO(_configtext))

#
# Parse mod list
#
MODLIST_RAW = CONF.get(MOD_LIST_SECTION, 'mod_list')
_l = MODLIST_RAW.split(',')
MODLIST = map(lambda x: str(x.strip()), _l)

#
# Parse Param
#
#----------------------------------------------------------------------
def parse_bool(p):
    """"""
    if p.lower() == 'true' or p.lower() == 't':
        p = True
    else:
        p = False 
    
    return p

#----------------------------------------------------------------------
def debugio(p):
    """"""
    print p, type(p)
    

DEBUG = parse_bool(CONF.get(MINIHYDRA_SECTION, 'debug'))
DO_CONTINUE = parse_bool(CONF.get(MINIHYDRA_SECTION, 'do_continue'))
THREAD_MAX = int(CONF.get(MINIHYDRA_SECTION, 'thread_max'))
SUCCESS_FILE = str(CONF.get(MINIHYDRA_SECTION, 'success_file'))
DEFAULT_SESSION = str(CONF.get(MINIHYDRA_SECTION, 'default_session'))

#debugio(DEBUG)
#debugio(DO_CONTINUE)
#debugio(THREAD_MAX)
#debugio(SUCCESS_FILE)
#debugio(DEFAULT_SESSION)


assert isinstance(MODLIST, list), '[x] Error in parse configfile: {}'.format(CONFIG_FILENAME)

if __name__ == '__main__':
    unittest.main()