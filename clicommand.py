C#!/usr/bin/env python
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

    def handleCommand:
        """
        handle xml segment
        <Command ...>
        """
        comlist = self.dom.getElementsByTagName("Command")

        for com in comlist:
            getVersion(com)
            getName(com)
            getRetType(com)
            #getRetVal(com)

    def getVersion(dom):
        return dom.getAttribute(u'version').encode('ascii', 'ignore')

    def getName(dom):
        return dom.getAttribute(u'command_name').encode('ascii', 'ignore')
    
    def getRetType(dom):
        return dom.getAttribute(u'return_type').encode('ascii', 'ignore')

    def handleParameter:
        """
        handle xml segment
        <Paramter ...>
        """
        parlist = self.dom.getElementsByTagName("Parameter")
        for par in parlist:
            getParInOut(par)
            getParType(par)
            getParVal(par)

    def getParInOut(par):
        return par.getAttribute(u'in_or_out').encode('ascii'. 'ignore')

    def getParType(par):
        return par.getAttribute(u'data_type').encode('ascii', 'ignore')

    def getParVal(par):
        return par.getAttribute(u'vale').encode('ascii', 'ignore')

    def getvalue(key):
        key.value


    def packMsg():
        comlist[0].attributes[u"version"]
