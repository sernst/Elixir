# NodeComputeHandles.py
# (C)2014
# Scott Ernst

from __future__ import print_function, absolute_import, unicode_literals, division

from pyaid.dict.DictUtils import DictUtils

#___________________________________________________________________________________________________ NodeComputeHandles
class NodeComputeHandles(object):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, nodeComputeData, inputType =False):
        """Creates a new instance of NodeComputeHandles."""
        self._nodeComputeData = nodeComputeData
        self._inputType       = inputType
        self._handles         = {}

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ clean
    def clean(self, name):
        if self._inputType:
            return

        if name in self._handles:
            self._handles[name].setClean()

#___________________________________________________________________________________________________ cleanAll
    def cleanAll(self):
        """Doc..."""
        for name,value in DictUtils.iter(self._handles):
            value.setClean()

#===================================================================================================
#                                                                               I N T R I N S I C

#___________________________________________________________________________________________________ __getattr__
    def __getattr__(self, item):
        if item.startswith('_'):
            raise AttributeError

        if item not in self._handles:
            attr = getattr(self._nodeComputeData.node, item)
            if not attr:
                raise AttributeError
            self._handles[item] = self._nodeComputeData.dataBlock.inputValue(attr) \
                if self._inputType else \
                self._nodeComputeData.dataBlock.outputValue(attr)

        return self._handles[item]

#___________________________________________________________________________________________________ __repr__
    def __repr__(self):
        return self.__str__()

#___________________________________________________________________________________________________ __str__
    def __str__(self):
        return '<%s>' % self.__class__.__name__

