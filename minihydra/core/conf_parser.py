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
MODLIST_RAW = CONF.get('mod_list', 'mod_list')
_l = MODLIST_RAW.split(',')
MODLIST = map(lambda x: str(x.strip()), _l)


assert isinstance(MODLIST, list), '[x] Error in parse configfile: {}'.format(CONFIG_FILENAME)

if __name__ == '__main__':
    unittest.main()