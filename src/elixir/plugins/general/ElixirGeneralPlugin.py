# ElixirGeneralPlugin.py
# (C)2014
# Scott Ernst

from maya import OpenMayaMPx

from elixir.plugins.general.commands import InsideMeshCommand

#___________________________________________________________________________________________________ PLUGIN_VERSION
PLUGIN_VERSION = (1, 0, 0, 0)

#___________________________________________________________________________________________________ initializePlugin
def initializePlugin(plugin):
    """ Initialize the script plug-in """

    pluginMFn = OpenMayaMPx.MFnPlugin(plugin)

    reload(InsideMeshCommand)
    InsideMeshCommand.InsideMeshCommand.register(pluginMFn)

#___________________________________________________________________________________________________ uninitializePlugin
def uninitializePlugin(plugin):
    """ Un-initialize the script plug-in """

    pluginMFn = OpenMayaMPx.MFnPlugin(plugin)
    InsideMeshCommand.InsideMeshCommand.deregister(pluginMFn)

