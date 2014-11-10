# NumericNodeAttribute.py
# (C)2014
# Scott Ernst

from __future__ import print_function, absolute_import, unicode_literals, division

from elixir.nodes.attrs.NodeAttribute import NodeAttribute

try:
    # noinspection PyUnresolvedReferences,PyUnresolvedReferences
    from maya import OpenMaya
except Exception:
    maya = None

#___________________________________________________________________________________________________ NumericNodeAttribute
class NumericNodeAttribute(NodeAttribute):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(
            self, shortFlag, longFlag, defaultValue =0, numericType =OpenMaya.MFnNumericData.kFloat,
            **kwargs
    ):
        """Creates a new instance of NumericNodeAttribute."""
        NodeAttribute.__init__(
            self,
            shortFlag,
            longFlag,
            **kwargs)

        self._defaultValue = defaultValue
        self._numericType  = numericType

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _createAttributeFn
    def _createAttributeFn(self):
        return OpenMaya.MFnNumericAttribute()

#___________________________________________________________________________________________________ _createAttribute
    def _createAttribute(self, attrFn):
        return attrFn.create(
            self._longFlag, self._shortFlag, self._numericType, self._defaultValue)
