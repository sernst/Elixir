# ElixirCommand.py
# (C)2014
# Scott Ernst

import sys

from pyaid.debug.Logger import Logger

from maya import OpenMaya
from maya import OpenMayaMPx

#___________________________________________________________________________________________________ ElixirCommand
class ElixirCommand(OpenMayaMPx.MPxCommand):

#===================================================================================================
#                                                                                       C L A S S

    BOOLEAN_TYPE        = 'boolean'
    DOUBLE_TYPE         = 'double'
    FLOAT_TYPE          = 'float'
    INTEGER_TYPE        = 'integer'
    STRING_TYPE         = 'string'
    POINT_TYPE          = 'point'
    FLOAT_VECTOR_TYPE   = 'floatVector'

    COMMAND_NAME = None

#___________________________________________________________________________________________________ __init__
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)
        self.argData = None

#___________________________________________________________________________________________________ doIt
    def doIt(self, mArgs):
        """ Invoked when the command is run. """
        self.argData = OpenMaya.MArgDatabase(self.syntax(), mArgs)
        self._runImpl()

#___________________________________________________________________________________________________ hasArg
    def hasArg(self, key):
        return self.argData.isFlagSet(key)

#___________________________________________________________________________________________________ register
    @classmethod
    def register(cls, plugin, *args, **kwargs):
        cls._registerImpl(*args, **kwargs)

        # Command instance creation function
        def createCommand():
            return OpenMayaMPx.asMPxPtr(cls())

        # Syntax creation function
        def createSyntax():
            syntax = OpenMaya.MSyntax()
            cls._populateSyntax(syntax)
            return syntax

        try:
            plugin.registerCommand(cls.COMMAND_NAME, createCommand, createSyntax)
        except Exception, err:
            sys.stderr.write('Failed to register command: %s\n' % cls.COMMAND_NAME)
            raise

#___________________________________________________________________________________________________ deregister
    @classmethod
    def deregister(cls, plugin):
        try:
            plugin.deregisterCommand(cls.COMMAND_NAME)
        except:
            sys.stderr.write('Failed to unregister command: %s\n' % cls.COMMAND_NAME)
            raise

#___________________________________________________________________________________________________ getArg
    def getArg(self, key, argType, defaultValue =None):
        if not self.argData.isFlagSet(key):
            return defaultValue

        if argType == self.BOOLEAN_TYPE:
            return self.argData.flagArgumentBool(key, 0)
        elif argType == self.POINT_TYPE:
            return OpenMaya.MFloatPoint(
                self.argData.flagArgumentDouble(key, 0),
                self.argData.flagArgumentDouble(key, 1),
                self.argData.flagArgumentDouble(key, 2) )
        elif argType == self.FLOAT_VECTOR_TYPE:
            return OpenMaya.MFloatVector(
                self.argData.flagArgumentFloat(key, 0),
                self.argData.flagArgumentFloat(key, 1),
                self.argData.flagArgumentFloat(key, 2) )
        elif argType == self.DOUBLE_TYPE:
            return self.argData.flagArgumentDouble(key, 0)
        elif argType == self.INTEGER_TYPE:
            return self.argData.flagArgumentInt(key, 0)
        elif argType == self.STRING_TYPE:
            return self.argData.flagArgumentString(key, 0)

        return None

#___________________________________________________________________________________________________ createSelectionList
    def createSelectionList(self, *targets):
        """ Creates a selection list that converts the targets strings into an MSelectionList
            instance that can be used to reference the objects within the OpenMaya API.

            :param targets:
                One or more strings representing dag paths within the Maya scene.
                These will be added to the selection list and can then be referenced by MDagPath
                objects, which is how the OpenMaya API references paths.

            :return:
                :type OpenMaya.MSelectionList
                A selection list referencing the specified targets """

        selectionList = OpenMaya.MSelectionList()
        for target in targets:
            try:
                selectionList.add(target)
            except Exception, err:
                continue

        return selectionList

#___________________________________________________________________________________________________ getDagPathFromString
    def getDagPathFromString(self, path):
        """ Converts a string representation of a valid DAG path into an MDagPath instance that
            can be used to reference the associated scene object within the API

            :param path:
                :type string
                The path to convert into an MDagPath instance. The path must be a valid path
                within the Maya scene. If a partial path is supplied and represents multiple
                objects within the scene, the first one found within the scene hierarchy will
                be returned

            :return:
                :type MDagPath
                An MDagPath instance representing the path string argument if that path exists
                within the scene, otherwise None. """

        selectionList = self.createSelectionList(path)
        if not selectionList or selectionList.length() == 0:
            return None

        dagPath = OpenMaya.MDagPath()
        try:
            selectionList.getDagPath(0, dagPath)
            return dagPath
        except Exception, err:
            selection = None
            count = 0
            try:
                count = selectionList.length()
                selection = []
                selectionList.getSelectionStrings(selection)
            except Exception, err:
                pass

            print Logger.createErrorMessage([
                u'ERROR: Failed to retrieve DAG path:',
                u'PATH: ' + unicode(path),
                u'COUNT: ' + unicode(count),
                u'SELECTION: ' + unicode(selection) ], err)
            return None

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _populateSyntax
    @classmethod
    def _populateSyntax(cls, syntax):
        pass

#___________________________________________________________________________________________________ _registerImpl
    @classmethod
    def _registerImpl(cls, *args, **kwargs):
        pass

#___________________________________________________________________________________________________ _runImpl
    def _runImpl(self):
        pass


