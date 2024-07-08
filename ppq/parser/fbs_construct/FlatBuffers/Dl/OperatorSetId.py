# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Dl

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class OperatorSetId(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OperatorSetId()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsOperatorSetId(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # OperatorSetId
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OperatorSetId
    def Domain(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OperatorSetId
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def OperatorSetIdStart(builder):
    builder.StartObject(2)

def Start(builder):
    OperatorSetIdStart(builder)

def OperatorSetIdAddDomain(builder, domain):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(domain), 0)

def AddDomain(builder, domain):
    OperatorSetIdAddDomain(builder, domain)

def OperatorSetIdAddVersion(builder, version):
    builder.PrependInt64Slot(1, version, 0)

def AddVersion(builder, version):
    OperatorSetIdAddVersion(builder, version)

def OperatorSetIdEnd(builder):
    return builder.EndObject()

def End(builder):
    return OperatorSetIdEnd(builder)


class OperatorSetIdT(object):

    # OperatorSetIdT
    def __init__(self):
        self.domain = None  # type: str
        self.version = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        operatorSetId = OperatorSetId()
        operatorSetId.Init(buf, pos)
        return cls.InitFromObj(operatorSetId)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, operatorSetId):
        x = OperatorSetIdT()
        x._UnPack(operatorSetId)
        return x

    # OperatorSetIdT
    def _UnPack(self, operatorSetId):
        if operatorSetId is None:
            return
        self.domain = operatorSetId.Domain()
        self.version = operatorSetId.Version()

    # OperatorSetIdT
    def Pack(self, builder):
        if self.domain is not None:
            domain = builder.CreateString(self.domain)
        OperatorSetIdStart(builder)
        if self.domain is not None:
            OperatorSetIdAddDomain(builder, domain)
        OperatorSetIdAddVersion(builder, self.version)
        operatorSetId = OperatorSetIdEnd(builder)
        return operatorSetId
