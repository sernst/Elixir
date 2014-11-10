# MessageNodeAttribute.py
# (C)2014
# Scott Ernst

from __future__ import print_function, absolute_import, unicode_literals, division

try:
    # noinspection PyUnresolvedReferences,PyUnresolvedReferences
    from maya import OpenMaya
except Exception:
    maya = None

from elixir.nodes.attrs.NodeAttribute import NodeAttribute

#___________________________________________________________________________________________________ MessageNodeAttribute
class MessageNodeAttribute(NodeAttribute):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, shortFlag, longFlag, **kwargs):
        """Creates a new instance of MessageNodeAttribute."""
        NodeAttribute.__init__(
            self,
            shortFlag,
            longFlag,
            **kwargs)

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _createAttributeFn
    def _createAttributeFn(self):
        return OpenMaya.MFnMessageAttribute()

#___________________________________________________________________________________________________ _createAttribute
    def _createAttribute(self, attrFn):
        return attrFn.create(self._longFlag, self._shortFlag)
