# InsideMeshCommand.py
# (C)2014
# Scott Ernst

from __future__ import print_function, absolute_import, unicode_literals, division

try:
    # noinspection PyUnresolvedReferences
    from maya import OpenMaya
except Exception:
    maya = None

from elixir.commands.ElixirCommand import ElixirCommand

#___________________________________________________________________________________________________ InsideMeshCommand
class InsideMeshCommand(ElixirCommand):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

    COMMAND_NAME = 'elixirGeneral_PointInsideMesh'

#___________________________________________________________________________________________________ __init__
    def __init__(self):
        """Creates a new instance of InsideMeshCommand."""
        ElixirCommand.__init__(self)

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _populateSyntax
    @classmethod
    def _populateSyntax(cls, syntax):
        """ Defines the argument and flag syntax for this command. """

        syntax.addFlag('-p', '-point', *[
            OpenMaya.MSyntax.kDouble,
            OpenMaya.MSyntax.kDouble,
            OpenMaya.MSyntax.kDouble ])

        syntax.addFlag('-d', '-direction', *[
            OpenMaya.MSyntax.kDouble,
            OpenMaya.MSyntax.kDouble,
            OpenMaya.MSyntax.kDouble ])

        syntax.addFlag('-m', '-mesh', OpenMaya.MSyntax.kString)

#___________________________________________________________________________________________________ _runImpl
    def _runImpl(self):
        meshPath = self.getArg('-mesh', self.STRING_TYPE, None)
        if meshPath is None:
            self.setResult(False)
            return

        mesh = OpenMaya.MFnMesh(self.getDagPathFromString(meshPath))
        if not mesh:
            self.setResult(False)
            return

        point = self.getArg('-point', self.POINT_TYPE)
        direction = self.getArg('-direction', self.FLOAT_VECTOR_TYPE)
        if direction is None:
            direction = OpenMaya.MFloatVector(0.0, 1.0, 0.0)

        fArray = OpenMaya.MFloatPointArray()
        mesh.allIntersections(
            point, direction, None, None,
            False, OpenMaya.MSpace.kWorld,
            10000, False, None, # replace none with a mesh look up accelerator if needed
            False, fArray, None, None, None, None, None)

        self.setResult(fArray.length() % 2 == 1)
