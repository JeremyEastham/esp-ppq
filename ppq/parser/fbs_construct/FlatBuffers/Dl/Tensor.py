# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Dl

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Tensor(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Tensor()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTensor(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Tensor
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Tensor
    def Dims(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Tensor
    def DimsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # Tensor
    def DimsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def DimsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Tensor
    def DataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Tensor
    def FloatData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Tensor
    def FloatDataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # Tensor
    def FloatDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def FloatDataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Tensor
    def Int32Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Tensor
    def Int32DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Tensor
    def Int32DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def Int32DataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Tensor
    def StringData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Tensor
    def StringDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def StringDataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # Tensor
    def Int64Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Tensor
    def Int64DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # Tensor
    def Int64DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def Int64DataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # Tensor
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Tensor
    def DocString(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Tensor
    def RawData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Tensor
    def RawDataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Tensor
    def RawDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def RawDataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # Tensor
    def ExternalData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatBuffers.Dl.StringStringEntry import StringStringEntry
            obj = StringStringEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Tensor
    def ExternalDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def ExternalDataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # Tensor
    def DataLocation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Tensor
    def DoubleData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Tensor
    def DoubleDataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # Tensor
    def DoubleDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def DoubleDataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # Tensor
    def Uint64Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Tensor
    def Uint64DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # Tensor
    def Uint64DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def Uint64DataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # Tensor
    def Exponents(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Tensor
    def ExponentsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # Tensor
    def ExponentsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Tensor
    def ExponentsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

def TensorStart(builder):
    builder.StartObject(14)

def Start(builder):
    TensorStart(builder)

def TensorAddDims(builder, dims):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dims), 0)

def AddDims(builder, dims):
    TensorAddDims(builder, dims)

def TensorStartDimsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartDimsVector(builder, numElems):
    return TensorStartDimsVector(builder, numElems)

def TensorAddDataType(builder, dataType):
    builder.PrependInt32Slot(1, dataType, 0)

def AddDataType(builder, dataType):
    TensorAddDataType(builder, dataType)

def TensorAddFloatData(builder, floatData):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(floatData), 0)

def AddFloatData(builder, floatData):
    TensorAddFloatData(builder, floatData)

def TensorStartFloatDataVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartFloatDataVector(builder, numElems):
    return TensorStartFloatDataVector(builder, numElems)

def TensorAddInt32Data(builder, int32Data):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(int32Data), 0)

def AddInt32Data(builder, int32Data):
    TensorAddInt32Data(builder, int32Data)

def TensorStartInt32DataVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartInt32DataVector(builder, numElems):
    return TensorStartInt32DataVector(builder, numElems)

def TensorAddStringData(builder, stringData):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(stringData), 0)

def AddStringData(builder, stringData):
    TensorAddStringData(builder, stringData)

def TensorStartStringDataVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartStringDataVector(builder, numElems):
    return TensorStartStringDataVector(builder, numElems)

def TensorAddInt64Data(builder, int64Data):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(int64Data), 0)

def AddInt64Data(builder, int64Data):
    TensorAddInt64Data(builder, int64Data)

def TensorStartInt64DataVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartInt64DataVector(builder, numElems):
    return TensorStartInt64DataVector(builder, numElems)

def TensorAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    TensorAddName(builder, name)

def TensorAddDocString(builder, docString):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(docString), 0)

def AddDocString(builder, docString):
    TensorAddDocString(builder, docString)

def TensorAddRawData(builder, rawData):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(rawData), 0)

def AddRawData(builder, rawData):
    TensorAddRawData(builder, rawData)

def TensorStartRawDataVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartRawDataVector(builder, numElems):
    return TensorStartRawDataVector(builder, numElems)

def TensorAddExternalData(builder, externalData):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(externalData), 0)

def AddExternalData(builder, externalData):
    TensorAddExternalData(builder, externalData)

def TensorStartExternalDataVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartExternalDataVector(builder, numElems):
    return TensorStartExternalDataVector(builder, numElems)

def TensorAddDataLocation(builder, dataLocation):
    builder.PrependInt32Slot(10, dataLocation, 0)

def AddDataLocation(builder, dataLocation):
    TensorAddDataLocation(builder, dataLocation)

def TensorAddDoubleData(builder, doubleData):
    builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(doubleData), 0)

def AddDoubleData(builder, doubleData):
    TensorAddDoubleData(builder, doubleData)

def TensorStartDoubleDataVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartDoubleDataVector(builder, numElems):
    return TensorStartDoubleDataVector(builder, numElems)

def TensorAddUint64Data(builder, uint64Data):
    builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(uint64Data), 0)

def AddUint64Data(builder, uint64Data):
    TensorAddUint64Data(builder, uint64Data)

def TensorStartUint64DataVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartUint64DataVector(builder, numElems):
    return TensorStartUint64DataVector(builder, numElems)

def TensorAddExponents(builder, exponents):
    builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(exponents), 0)

def AddExponents(builder, exponents):
    TensorAddExponents(builder, exponents)

def TensorStartExponentsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartExponentsVector(builder, numElems):
    return TensorStartExponentsVector(builder, numElems)

def TensorEnd(builder):
    return builder.EndObject()

def End(builder):
    return TensorEnd(builder)

import FlatBuffers.Dl.StringStringEntry
try:
    from typing import List
except:
    pass

class TensorT(object):

    # TensorT
    def __init__(self):
        self.dims = None  # type: List[int]
        self.dataType = 0  # type: int
        self.floatData = None  # type: List[float]
        self.int32Data = None  # type: List[int]
        self.stringData = None  # type: List[str]
        self.int64Data = None  # type: List[int]
        self.name = None  # type: str
        self.docString = None  # type: str
        self.rawData = None  # type: List[int]
        self.externalData = None  # type: List[FlatBuffers.Dl.StringStringEntry.StringStringEntryT]
        self.dataLocation = 0  # type: int
        self.doubleData = None  # type: List[float]
        self.uint64Data = None  # type: List[int]
        self.exponents = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        tensor = Tensor()
        tensor.Init(buf, pos)
        return cls.InitFromObj(tensor)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, tensor):
        x = TensorT()
        x._UnPack(tensor)
        return x

    # TensorT
    def _UnPack(self, tensor):
        if tensor is None:
            return
        if not tensor.DimsIsNone():
            if np is None:
                self.dims = []
                for i in range(tensor.DimsLength()):
                    self.dims.append(tensor.Dims(i))
            else:
                self.dims = tensor.DimsAsNumpy()
        self.dataType = tensor.DataType()
        if not tensor.FloatDataIsNone():
            if np is None:
                self.floatData = []
                for i in range(tensor.FloatDataLength()):
                    self.floatData.append(tensor.FloatData(i))
            else:
                self.floatData = tensor.FloatDataAsNumpy()
        if not tensor.Int32DataIsNone():
            if np is None:
                self.int32Data = []
                for i in range(tensor.Int32DataLength()):
                    self.int32Data.append(tensor.Int32Data(i))
            else:
                self.int32Data = tensor.Int32DataAsNumpy()
        if not tensor.StringDataIsNone():
            self.stringData = []
            for i in range(tensor.StringDataLength()):
                self.stringData.append(tensor.StringData(i))
        if not tensor.Int64DataIsNone():
            if np is None:
                self.int64Data = []
                for i in range(tensor.Int64DataLength()):
                    self.int64Data.append(tensor.Int64Data(i))
            else:
                self.int64Data = tensor.Int64DataAsNumpy()
        self.name = tensor.Name()
        self.docString = tensor.DocString()
        if not tensor.RawDataIsNone():
            if np is None:
                self.rawData = []
                for i in range(tensor.RawDataLength()):
                    self.rawData.append(tensor.RawData(i))
            else:
                self.rawData = tensor.RawDataAsNumpy()
        if not tensor.ExternalDataIsNone():
            self.externalData = []
            for i in range(tensor.ExternalDataLength()):
                if tensor.ExternalData(i) is None:
                    self.externalData.append(None)
                else:
                    stringStringEntry_ = FlatBuffers.Dl.StringStringEntry.StringStringEntryT.InitFromObj(tensor.ExternalData(i))
                    self.externalData.append(stringStringEntry_)
        self.dataLocation = tensor.DataLocation()
        if not tensor.DoubleDataIsNone():
            if np is None:
                self.doubleData = []
                for i in range(tensor.DoubleDataLength()):
                    self.doubleData.append(tensor.DoubleData(i))
            else:
                self.doubleData = tensor.DoubleDataAsNumpy()
        if not tensor.Uint64DataIsNone():
            if np is None:
                self.uint64Data = []
                for i in range(tensor.Uint64DataLength()):
                    self.uint64Data.append(tensor.Uint64Data(i))
            else:
                self.uint64Data = tensor.Uint64DataAsNumpy()
        if not tensor.ExponentsIsNone():
            if np is None:
                self.exponents = []
                for i in range(tensor.ExponentsLength()):
                    self.exponents.append(tensor.Exponents(i))
            else:
                self.exponents = tensor.ExponentsAsNumpy()

    # TensorT
    def Pack(self, builder):
        if self.dims is not None:
            if np is not None and type(self.dims) is np.ndarray:
                dims = builder.CreateNumpyVector(self.dims)
            else:
                TensorStartDimsVector(builder, len(self.dims))
                for i in reversed(range(len(self.dims))):
                    builder.PrependInt64(self.dims[i])
                dims = builder.EndVector()
        if self.floatData is not None:
            if np is not None and type(self.floatData) is np.ndarray:
                floatData = builder.CreateNumpyVector(self.floatData)
            else:
                TensorStartFloatDataVector(builder, len(self.floatData))
                for i in reversed(range(len(self.floatData))):
                    builder.PrependFloat32(self.floatData[i])
                floatData = builder.EndVector()
        if self.int32Data is not None:
            if np is not None and type(self.int32Data) is np.ndarray:
                int32Data = builder.CreateNumpyVector(self.int32Data)
            else:
                TensorStartInt32DataVector(builder, len(self.int32Data))
                for i in reversed(range(len(self.int32Data))):
                    builder.PrependInt32(self.int32Data[i])
                int32Data = builder.EndVector()
        if self.stringData is not None:
            stringDatalist = []
            for i in range(len(self.stringData)):
                stringDatalist.append(builder.CreateString(self.stringData[i]))
            TensorStartStringDataVector(builder, len(self.stringData))
            for i in reversed(range(len(self.stringData))):
                builder.PrependUOffsetTRelative(stringDatalist[i])
            stringData = builder.EndVector()
        if self.int64Data is not None:
            if np is not None and type(self.int64Data) is np.ndarray:
                int64Data = builder.CreateNumpyVector(self.int64Data)
            else:
                TensorStartInt64DataVector(builder, len(self.int64Data))
                for i in reversed(range(len(self.int64Data))):
                    builder.PrependInt64(self.int64Data[i])
                int64Data = builder.EndVector()
        if self.name is not None:
            name = builder.CreateString(self.name)
        if self.docString is not None:
            docString = builder.CreateString(self.docString)
        if self.rawData is not None:
            if np is not None and type(self.rawData) is np.ndarray:
                rawData = builder.CreateNumpyVector(self.rawData)
            else:
                TensorStartRawDataVector(builder, len(self.rawData))
                for i in reversed(range(len(self.rawData))):
                    builder.PrependUint8(self.rawData[i])
                rawData = builder.EndVector()
        if self.externalData is not None:
            externalDatalist = []
            for i in range(len(self.externalData)):
                externalDatalist.append(self.externalData[i].Pack(builder))
            TensorStartExternalDataVector(builder, len(self.externalData))
            for i in reversed(range(len(self.externalData))):
                builder.PrependUOffsetTRelative(externalDatalist[i])
            externalData = builder.EndVector()
        if self.doubleData is not None:
            if np is not None and type(self.doubleData) is np.ndarray:
                doubleData = builder.CreateNumpyVector(self.doubleData)
            else:
                TensorStartDoubleDataVector(builder, len(self.doubleData))
                for i in reversed(range(len(self.doubleData))):
                    builder.PrependFloat64(self.doubleData[i])
                doubleData = builder.EndVector()
        if self.uint64Data is not None:
            if np is not None and type(self.uint64Data) is np.ndarray:
                uint64Data = builder.CreateNumpyVector(self.uint64Data)
            else:
                TensorStartUint64DataVector(builder, len(self.uint64Data))
                for i in reversed(range(len(self.uint64Data))):
                    builder.PrependUint64(self.uint64Data[i])
                uint64Data = builder.EndVector()
        if self.exponents is not None:
            if np is not None and type(self.exponents) is np.ndarray:
                exponents = builder.CreateNumpyVector(self.exponents)
            else:
                TensorStartExponentsVector(builder, len(self.exponents))
                for i in reversed(range(len(self.exponents))):
                    builder.PrependInt64(self.exponents[i])
                exponents = builder.EndVector()
        TensorStart(builder)
        if self.dims is not None:
            TensorAddDims(builder, dims)
        TensorAddDataType(builder, self.dataType)
        if self.floatData is not None:
            TensorAddFloatData(builder, floatData)
        if self.int32Data is not None:
            TensorAddInt32Data(builder, int32Data)
        if self.stringData is not None:
            TensorAddStringData(builder, stringData)
        if self.int64Data is not None:
            TensorAddInt64Data(builder, int64Data)
        if self.name is not None:
            TensorAddName(builder, name)
        if self.docString is not None:
            TensorAddDocString(builder, docString)
        if self.rawData is not None:
            TensorAddRawData(builder, rawData)
        if self.externalData is not None:
            TensorAddExternalData(builder, externalData)
        TensorAddDataLocation(builder, self.dataLocation)
        if self.doubleData is not None:
            TensorAddDoubleData(builder, doubleData)
        if self.uint64Data is not None:
            TensorAddUint64Data(builder, uint64Data)
        if self.exponents is not None:
            TensorAddExponents(builder, exponents)
        tensor = TensorEnd(builder)
        return tensor
