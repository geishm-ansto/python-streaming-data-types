# automatically generated by the FlatBuffers compiler, do not modify

# namespace:

import flatbuffers


class Status(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsStatus(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Status()
        x.Init(buf, n + offset)
        return x

    # Status
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Status
    def SoftwareName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Status
    def SoftwareVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Status
    def ServiceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Status
    def HostName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Status
    def ProcessId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Status
    def UpdateInterval(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Status
    def StatusJson(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


def StatusStart(builder): builder.StartObject(7)
def StatusAddSoftwareName(builder, softwareName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(softwareName), 0)
def StatusAddSoftwareVersion(builder, softwareVersion): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(softwareVersion), 0)
def StatusAddServiceId(builder, serviceId): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(serviceId), 0)
def StatusAddHostName(builder, hostName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(hostName), 0)
def StatusAddProcessId(builder, processId): builder.PrependUint32Slot(4, processId, 0)
def StatusAddUpdateInterval(builder, updateInterval): builder.PrependUint32Slot(5, updateInterval, 0)
def StatusAddStatusJson(builder, statusJson): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(statusJson), 0)
def StatusEnd(builder): return builder.EndObject()
