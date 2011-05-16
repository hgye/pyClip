#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom import minidom

class Command:
    """
    command
    every instance is a cli command
    """
    def __init__(xmlfile):
        fd = open(xmlfile)
        self.dom = minidom.parse(fd)
        close()

    def packMsg():
        
    
