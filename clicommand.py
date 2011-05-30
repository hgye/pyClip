#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from xml.dom import minidom

typedic = {'Byte':('B', 1),
           'Word':('W', 2),
           'Dword':('D', 4),
           'String':('S', 0),
           'Void':('V', 0) }

inoutdic = {'out':'O',
            'in':'I'}

class Command:
    """
    command
    every instance is a cli command
    """
    def __init__(xmlfile):
        self.xmlfile = xmlfile
        fd = open(self.xmlfile)
        self.dom = minidom.parse(fd)
        close(fd)

    def handleCommand():
        """
        handle xml segment
        <Command ...>
        """
        comlist = self.dom.getElementsByTagName("Command")

        if 1 != len(comlist):
            print "There are more than 1 <Command> Node in file %s"%(os.path.abspath(self.xmlfile) )
            return # @todo, is that OK, try.. catch, error case

        for com in comlist:
            ver = getVersion(com)
            com_name = getName(com)
            ret_type = getRetType(com)
            #getRetVal(com)

        msg_head = ''.join(['REQ   ', ver])
        msg_com  = ''.join( [chr(len(com_name)), com_name ])
        msg_ret  = ''.join([typedic[ret_type][0], typedic[ret_type][1] ])


    def getVersion(dom):
        return dom.getAttribute(u'version').encode('ascii', 'ignore')

    def getName(dom):
        return dom.getAttribute(u'command_name').encode('ascii', 'ignore')
    
    def getRetType(dom):
        return dom.getAttribute(u'return_type').encode('ascii', 'ignore')

    def handleParameters():
        """
        handle xml segment
        <Paramter ...>
        """
        parlist = self.dom.getElementsByTagName("Parameter")

        parnum = len(parlist)
        if 12 >= parnum:
            print "parameter number too much, parnum = %d"%parnum
            return # @todo, error case
        
        for par in parlist:
            handleParameter(par)

    def handleParameter(par):
        inout = inoutdic(getParInOut(par))
        par_type = getParType(par)
        par_val = getParVal(par)

        if inout == 'I':
            msg_par = ''.join([inout, typedic[par_type][0], typedic[par_type][1], par_val ])
        else inout == 'O':
            msg_par = ''.join([inout, typedic[par_type][0], typedic[par_type][1] ])


    def getParInOut(par):
        return par.getAttribute(u'in_or_out').encode('ascii'. 'ignore')

    def getParType(par):
        return par.getAttribute(u'data_type').encode('ascii', 'ignore')

    def getParVal(par):
        return par.getAttribute(u'vale').encode('ascii', 'ignore')


    def packMsg():
        handleCommand()
        handleParameters()
