#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Store Config Options
  Created: 04/15/17
"""

try:
    from . import conf_parser
    MODLIST = conf_parser.MODLIST if conf_parser.MODLIST else []
    
    DEBUG = True if conf_parser.DEBUG else False
    
    DO_CONTINUE = True if conf_parser.DO_CONTINUE else False
    
    THREAD_MAX = conf_parser.THREAD_MAX if conf_parser.THREAD_MAX else 50
    
    DEFAULT_SESSION = conf_parser.DEFAULT_SESSION if conf_parser.THREAD_MAX else 'minihydra'
    
    SUCCESS_FILE = conf_parser.SUCCESS_FILE if conf_parser.SUCCESS_FILE else 'success.txt'    
except IOError:
    MODLIST = ['ftp', 'testmod', 'telnet']
    DEBUG = False
    DO_CONTINUE = True
    THREAD_MAX = 50
    DEFAULT_SESSION = 'minihydra'
    SUCCESS_FILE = 'success.txt'

