# __init__.py
# (C)2014
# Scott Ernst

from __future__ import print_function, absolute_import, unicode_literals, division

from pyaid.debug.Logger import Logger

from nimble import cmds

#___________________________________________________________________________________________________ loadGeneralPlugin
def loadGeneralPlugin():
    """ Loads the elixir general plugin. Must be called within Maya. """

    try:
        if cmds.pluginInfo('ElixirGeneralPlugin', loaded=True):
            return True
    except Exception:
        pass

    try:
        from elixir.plugins.general import ElixirGeneralPlugin
        cmds.loadPlugin(ElixirGeneralPlugin.__file__)
        return True
    except Exception as err:
        print(Logger.createErrorMessage('ERROR: Failed to load Elixir General Plugin', err))
        return False

#___________________________________________________________________________________________________ unloadGeneralPlugin
def unloadGeneralPlugin(force =False):
    try:
        #from elixir.plugins.general import ElixirGeneralPlugin
        results = cmds.unloadPlugin('ElixirGeneralPlugin', force=force)
        if not results:
            print('ERROR: Failed to unload the Elixir General Plugin')
            return False
        return True
    except Exception as err:
        print(Logger.createErrorMessage('ERROR: Failed to unload the Elixir General Plugin', err))
        return False
