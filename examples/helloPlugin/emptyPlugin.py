# emptyPlugin.py
# (C)2014
# Scott Ernst

from maya import OpenMayaMPx

#___________________________________________________________________________________________________ initializePlugin
def initializePlugin(plugin):
    """ All plugin files must have an initializePlugin function, which Maya calls when the
        loadPlugin() call is made. This function """

    # Create the plugin functional, which would be used to perform operation on the plugin such as
    # adding custom commands and nodes
    pluginMFn = OpenMayaMPx.MFnPlugin(plugin)

#___________________________________________________________________________________________________ uninitializePlugin
def uninitializePlugin(plugin):
    """ All plugins must also have an uninitializePlugin function, which Maya calls when unloading
        a plugin and is responsible for removing the custom functionality added by the plugin. """

    # Create the plugin functional, which would be used to perform operation on the plugin such as
    # removing custom commands and nodes
    pluginMFn = OpenMayaMPx.MFnPlugin(plugin)
