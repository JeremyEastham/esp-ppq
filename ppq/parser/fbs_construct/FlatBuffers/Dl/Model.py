# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Dl

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Model(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Model()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsModel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Model
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Model
    def IrVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Model
    def OpsetImport(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatBuffers.Dl.OperatorSetId import OperatorSetId
            obj = OperatorSetId()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Model
    def OpsetImportLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Model
    def OpsetImportIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Model
    def ProducerName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Model
    def ProducerVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Model
    def Domain(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Model
    def ModelVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # Model
    def DocString(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Model
    def Graph(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from FlatBuffers.Dl.Graph import Graph
            obj = Graph()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Model
    def MetadataProps(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatBuffers.Dl.StringStringEntry import StringStringEntry
            obj = StringStringEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Model
    def MetadataPropsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Model
    def MetadataPropsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # Model
    def Functions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatBuffers.Dl.Function import Function
            obj = Function()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Model
    def FunctionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Model
    def FunctionsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

def ModelStart(builder):
    builder.StartObject(10)

def Start(builder):
    ModelStart(builder)

def ModelAddIrVersion(builder, irVersion):
    builder.PrependInt32Slot(0, irVersion, 0)

def AddIrVersion(builder, irVersion):
    ModelAddIrVersion(builder, irVersion)

def ModelAddOpsetImport(builder, opsetImport):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(opsetImport), 0)

def AddOpsetImport(builder, opsetImport):
    ModelAddOpsetImport(builder, opsetImport)

def ModelStartOpsetImportVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartOpsetImportVector(builder, numElems):
    return ModelStartOpsetImportVector(builder, numElems)

def ModelAddProducerName(builder, producerName):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(producerName), 0)

def AddProducerName(builder, producerName):
    ModelAddProducerName(builder, producerName)

def ModelAddProducerVersion(builder, producerVersion):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(producerVersion), 0)

def AddProducerVersion(builder, producerVersion):
    ModelAddProducerVersion(builder, producerVersion)

def ModelAddDomain(builder, domain):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(domain), 0)

def AddDomain(builder, domain):
    ModelAddDomain(builder, domain)

def ModelAddModelVersion(builder, modelVersion):
    builder.PrependInt64Slot(5, modelVersion, 0)

def AddModelVersion(builder, modelVersion):
    ModelAddModelVersion(builder, modelVersion)

def ModelAddDocString(builder, docString):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(docString), 0)

def AddDocString(builder, docString):
    ModelAddDocString(builder, docString)

def ModelAddGraph(builder, graph):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(graph), 0)

def AddGraph(builder, graph):
    ModelAddGraph(builder, graph)

def ModelAddMetadataProps(builder, metadataProps):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(metadataProps), 0)

def AddMetadataProps(builder, metadataProps):
    ModelAddMetadataProps(builder, metadataProps)

def ModelStartMetadataPropsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartMetadataPropsVector(builder, numElems):
    return ModelStartMetadataPropsVector(builder, numElems)

def ModelAddFunctions(builder, functions):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(functions), 0)

def AddFunctions(builder, functions):
    ModelAddFunctions(builder, functions)

def ModelStartFunctionsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartFunctionsVector(builder, numElems):
    return ModelStartFunctionsVector(builder, numElems)

def ModelEnd(builder):
    return builder.EndObject()

def End(builder):
    return ModelEnd(builder)

import FlatBuffers.Dl.Function
import FlatBuffers.Dl.Graph
import FlatBuffers.Dl.OperatorSetId
import FlatBuffers.Dl.StringStringEntry
try:
    from typing import List, Optional
except:
    pass

class ModelT(object):

    # ModelT
    def __init__(self):
        self.irVersion = 0  # type: int
        self.opsetImport = None  # type: List[FlatBuffers.Dl.OperatorSetId.OperatorSetIdT]
        self.producerName = None  # type: str
        self.producerVersion = None  # type: str
        self.domain = None  # type: str
        self.modelVersion = 0  # type: int
        self.docString = None  # type: str
        self.graph = None  # type: Optional[FlatBuffers.Dl.Graph.GraphT]
        self.metadataProps = None  # type: List[FlatBuffers.Dl.StringStringEntry.StringStringEntryT]
        self.functions = None  # type: List[FlatBuffers.Dl.Function.FunctionT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        model = Model()
        model.Init(buf, pos)
        return cls.InitFromObj(model)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, model):
        x = ModelT()
        x._UnPack(model)
        return x

    # ModelT
    def _UnPack(self, model):
        if model is None:
            return
        self.irVersion = model.IrVersion()
        if not model.OpsetImportIsNone():
            self.opsetImport = []
            for i in range(model.OpsetImportLength()):
                if model.OpsetImport(i) is None:
                    self.opsetImport.append(None)
                else:
                    operatorSetId_ = FlatBuffers.Dl.OperatorSetId.OperatorSetIdT.InitFromObj(model.OpsetImport(i))
                    self.opsetImport.append(operatorSetId_)
        self.producerName = model.ProducerName()
        self.producerVersion = model.ProducerVersion()
        self.domain = model.Domain()
        self.modelVersion = model.ModelVersion()
        self.docString = model.DocString()
        if model.Graph() is not None:
            self.graph = FlatBuffers.Dl.Graph.GraphT.InitFromObj(model.Graph())
        if not model.MetadataPropsIsNone():
            self.metadataProps = []
            for i in range(model.MetadataPropsLength()):
                if model.MetadataProps(i) is None:
                    self.metadataProps.append(None)
                else:
                    stringStringEntry_ = FlatBuffers.Dl.StringStringEntry.StringStringEntryT.InitFromObj(model.MetadataProps(i))
                    self.metadataProps.append(stringStringEntry_)
        if not model.FunctionsIsNone():
            self.functions = []
            for i in range(model.FunctionsLength()):
                if model.Functions(i) is None:
                    self.functions.append(None)
                else:
                    function_ = FlatBuffers.Dl.Function.FunctionT.InitFromObj(model.Functions(i))
                    self.functions.append(function_)

    # ModelT
    def Pack(self, builder):
        if self.opsetImport is not None:
            opsetImportlist = []
            for i in range(len(self.opsetImport)):
                opsetImportlist.append(self.opsetImport[i].Pack(builder))
            ModelStartOpsetImportVector(builder, len(self.opsetImport))
            for i in reversed(range(len(self.opsetImport))):
                builder.PrependUOffsetTRelative(opsetImportlist[i])
            opsetImport = builder.EndVector()
        if self.producerName is not None:
            producerName = builder.CreateString(self.producerName)
        if self.producerVersion is not None:
            producerVersion = builder.CreateString(self.producerVersion)
        if self.domain is not None:
            domain = builder.CreateString(self.domain)
        if self.docString is not None:
            docString = builder.CreateString(self.docString)
        if self.graph is not None:
            graph = self.graph.Pack(builder)
        if self.metadataProps is not None:
            metadataPropslist = []
            for i in range(len(self.metadataProps)):
                metadataPropslist.append(self.metadataProps[i].Pack(builder))
            ModelStartMetadataPropsVector(builder, len(self.metadataProps))
            for i in reversed(range(len(self.metadataProps))):
                builder.PrependUOffsetTRelative(metadataPropslist[i])
            metadataProps = builder.EndVector()
        if self.functions is not None:
            functionslist = []
            for i in range(len(self.functions)):
                functionslist.append(self.functions[i].Pack(builder))
            ModelStartFunctionsVector(builder, len(self.functions))
            for i in reversed(range(len(self.functions))):
                builder.PrependUOffsetTRelative(functionslist[i])
            functions = builder.EndVector()
        ModelStart(builder)
        ModelAddIrVersion(builder, self.irVersion)
        if self.opsetImport is not None:
            ModelAddOpsetImport(builder, opsetImport)
        if self.producerName is not None:
            ModelAddProducerName(builder, producerName)
        if self.producerVersion is not None:
            ModelAddProducerVersion(builder, producerVersion)
        if self.domain is not None:
            ModelAddDomain(builder, domain)
        ModelAddModelVersion(builder, self.modelVersion)
        if self.docString is not None:
            ModelAddDocString(builder, docString)
        if self.graph is not None:
            ModelAddGraph(builder, graph)
        if self.metadataProps is not None:
            ModelAddMetadataProps(builder, metadataProps)
        if self.functions is not None:
            ModelAddFunctions(builder, functions)
        model = ModelEnd(builder)
        return model
