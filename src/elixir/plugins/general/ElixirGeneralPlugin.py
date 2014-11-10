# ElixirGeneralPlugin.py
# (C)2014
# Scott Ernst

from __future__ import print_function, absolute_import, unicode_literals, division

from pyaid.ModuleUtils import ModuleUtils

from elixir.plugins.general.commands import InsideMeshCommand

try:
    # noinspection PyUnresolvedReferences,PyUnresolvedReferences
    from maya import OpenMayaMPx
except Exception:
    maya = None

#___________________________________________________________________________________________________ PLUGIN_VERSION
PLUGIN_VERSION = (1, 0, 0, 0)

#___________________________________________________________________________________________________ initializePlugin
def initializePlugin(plugin):
    """ Initialize the script plug-in """

    pluginMFn = OpenMayaMPx.MFnPlugin(plugin)

    ModuleUtils.reloadModule(InsideMeshCommand)
    InsideMeshCommand.InsideMeshCommand.register(pluginMFn)

#___________________________________________________________________________________________________ uninitializePlugin
def uninitializePlugin(plugin):
    """ Un-initialize the script plug-in """

    pluginMFn = OpenMayaMPx.MFnPlugin(plugin)
    InsideMeshCommand.InsideMeshCommand.deregister(pluginMFn)

