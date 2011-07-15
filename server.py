# -*- coding: utf-8 -*-
import Pyro.naming
import Pyro.core
from Pyro.errors import NamingError

import principal

class ambprincipal(Pyro.core.ObjBase, principal.ambprincipal):
	pass

def main():
        Pyro.core.initServer()
        daemon = Pyro.core.Daemon()
        # locate the NS
        locator = Pyro.naming.NameServerLocator()
        print 'searching for Name Server...'
        ns = locator.getNS()
        daemon.useNameServer(ns)

        # connect a new object implementation (first unregister previous one)
        try:
            ns.unregister('AmbienteColaborativo')
        except NamingError:
            pass

        # connect new object implementation
        daemon.connect(ambprincipal(),'AmbienteColaborativo')

        # enter the server loop.
        print 'Server object "AmbienteColaborativo" no ar.'
        daemon.requestLoop()

if __name__=="__main__":
        main()
