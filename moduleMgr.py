# -*- coding:utf-8 -*-
import os 

def my_import(name):
	mod = __import__(name)
	components = name.split('.')
	for comp in components[1:]:
		mod = getattr(mod, comp)
	return mod

def autoLoadModule( session ):
    pymodules = []
    for root, dirs, files in os.walk("module"):
        for fname in files:
            fnamesplit = fname.split('.')
            if len(fnamesplit) < 2:
                continue
            if fnamesplit[0] != '__init__' and fnamesplit[1] == 'py':
                pymodules.append('.'.join(["module", fnamesplit[0]]))

    if len(pymodules) != 0:
        for pym in pymodules:
            mod = my_import(pym)
            mod.addUrls( session.getApp() )