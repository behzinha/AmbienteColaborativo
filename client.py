# -*- coding: utf-8 -*-
import Pyro.core

o=Pyro.core.getProxyForURI('PYRONAME://:Default.AmbienteColaborativo')

print o.boasvindas()
