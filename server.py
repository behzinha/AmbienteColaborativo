# -*- coding: utf-8 -*-
import Pyro.naming
import Pyro.core
from Pyro.errors import PyroError,NamingError

import principal

###### testclass Pyro object

class ambprincipal(Pyro.core.ObjBase, principal.ambprincipal):
        pass

###### main server program

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
                # 'test' is the name by which our object will be known to the outside world
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
