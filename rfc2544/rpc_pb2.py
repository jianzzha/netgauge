# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc.proto',
  package='trafficgen',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\trpc.proto\x12\ntrafficgen\"\x1b\n\x19IsTrafficgenRunningParams\"\x19\n\x17IsResultAvailableParams\"\x11\n\x0fGetResultParams\"\x16\n\x14StopTrafficgenParams\"\x12\n\x10GetMacListParams\"0\n\x11TrafficgenRunning\x12\x1b\n\x13isTrafficgenRunning\x18\x01 \x01(\x08\",\n\x0fResultAvailable\x12\x19\n\x11isResultAvailable\x18\x01 \x01(\x08\"\x1a\n\x07Success\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1a\n\x07MacList\x12\x0f\n\x07macList\x18\x01 \x01(\t\"\xd9\x01\n\tPortStats\x12\x11\n\ttx_l1_bps\x18\x01 \x01(\x02\x12\x11\n\ttx_l2_bps\x18\x02 \x01(\x02\x12\x0e\n\x06tx_pps\x18\x03 \x01(\x02\x12\x11\n\trx_l1_bps\x18\x04 \x01(\x02\x12\x11\n\trx_l2_bps\x18\x05 \x01(\x02\x12\x0e\n\x06rx_pps\x18\x06 \x01(\x02\x12\x1a\n\x12rx_latency_minimum\x18\x07 \x01(\x02\x12\x1a\n\x12rx_latency_maximum\x18\x08 \x01(\x02\x12\x1a\n\x12rx_latency_average\x18\t \x01(\x02\x12\x0c\n\x04port\x18\n \x01(\t\".\n\x06Result\x12$\n\x05stats\x18\x01 \x03(\x0b\x32\x15.trafficgen.PortStats\"\xec\x01\n\x12\x42inarySearchParams\x12\x16\n\x0esearch_runtime\x18\x01 \x01(\x05\x12\x1a\n\x12validation_runtime\x18\x02 \x01(\x05\x12\x11\n\tnum_flows\x18\x03 \x01(\x05\x12\x14\n\x0c\x64\x65vice_pairs\x18\x04 \x01(\t\x12\x12\n\nframe_size\x18\x05 \x01(\x05\x12\x14\n\x0cmax_loss_pct\x18\x06 \x01(\x02\x12\x15\n\rsniff_runtime\x18\x07 \x01(\x05\x12\n\n\x02l3\x18\x08 \x01(\x08\x12\x10\n\x08\x64st_macs\x18\t \x01(\t\x12\x1a\n\x12search_granularity\x18\n \x01(\x02\x32\xd0\x03\n\nTrafficgen\x12[\n\x13isTrafficgenRunning\x12%.trafficgen.IsTrafficgenRunningParams\x1a\x1d.trafficgen.TrafficgenRunning\x12U\n\x11isResultAvailable\x12#.trafficgen.IsResultAvailableParams\x1a\x1b.trafficgen.ResultAvailable\x12<\n\tgetResult\x12\x1b.trafficgen.GetResultParams\x1a\x12.trafficgen.Result\x12\x46\n\x0fstartTrafficgen\x12\x1e.trafficgen.BinarySearchParams\x1a\x13.trafficgen.Success\x12G\n\x0estopTrafficgen\x12 .trafficgen.StopTrafficgenParams\x1a\x13.trafficgen.Success\x12?\n\ngetMacList\x12\x1c.trafficgen.GetMacListParams\x1a\x13.trafficgen.MacListb\x06proto3'
)




_ISTRAFFICGENRUNNINGPARAMS = _descriptor.Descriptor(
  name='IsTrafficgenRunningParams',
  full_name='trafficgen.IsTrafficgenRunningParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=52,
)


_ISRESULTAVAILABLEPARAMS = _descriptor.Descriptor(
  name='IsResultAvailableParams',
  full_name='trafficgen.IsResultAvailableParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=79,
)


_GETRESULTPARAMS = _descriptor.Descriptor(
  name='GetResultParams',
  full_name='trafficgen.GetResultParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=98,
)


_STOPTRAFFICGENPARAMS = _descriptor.Descriptor(
  name='StopTrafficgenParams',
  full_name='trafficgen.StopTrafficgenParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=122,
)


_GETMACLISTPARAMS = _descriptor.Descriptor(
  name='GetMacListParams',
  full_name='trafficgen.GetMacListParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=142,
)


_TRAFFICGENRUNNING = _descriptor.Descriptor(
  name='TrafficgenRunning',
  full_name='trafficgen.TrafficgenRunning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isTrafficgenRunning', full_name='trafficgen.TrafficgenRunning.isTrafficgenRunning', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=192,
)


_RESULTAVAILABLE = _descriptor.Descriptor(
  name='ResultAvailable',
  full_name='trafficgen.ResultAvailable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isResultAvailable', full_name='trafficgen.ResultAvailable.isResultAvailable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=238,
)


_SUCCESS = _descriptor.Descriptor(
  name='Success',
  full_name='trafficgen.Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='trafficgen.Success.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=266,
)


_MACLIST = _descriptor.Descriptor(
  name='MacList',
  full_name='trafficgen.MacList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='macList', full_name='trafficgen.MacList.macList', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=294,
)


_PORTSTATS = _descriptor.Descriptor(
  name='PortStats',
  full_name='trafficgen.PortStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_l1_bps', full_name='trafficgen.PortStats.tx_l1_bps', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_l2_bps', full_name='trafficgen.PortStats.tx_l2_bps', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_pps', full_name='trafficgen.PortStats.tx_pps', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_l1_bps', full_name='trafficgen.PortStats.rx_l1_bps', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_l2_bps', full_name='trafficgen.PortStats.rx_l2_bps', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_pps', full_name='trafficgen.PortStats.rx_pps', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_latency_minimum', full_name='trafficgen.PortStats.rx_latency_minimum', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_latency_maximum', full_name='trafficgen.PortStats.rx_latency_maximum', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_latency_average', full_name='trafficgen.PortStats.rx_latency_average', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='trafficgen.PortStats.port', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=514,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='trafficgen.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stats', full_name='trafficgen.Result.stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=562,
)


_BINARYSEARCHPARAMS = _descriptor.Descriptor(
  name='BinarySearchParams',
  full_name='trafficgen.BinarySearchParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='search_runtime', full_name='trafficgen.BinarySearchParams.search_runtime', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validation_runtime', full_name='trafficgen.BinarySearchParams.validation_runtime', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_flows', full_name='trafficgen.BinarySearchParams.num_flows', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_pairs', full_name='trafficgen.BinarySearchParams.device_pairs', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_size', full_name='trafficgen.BinarySearchParams.frame_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_loss_pct', full_name='trafficgen.BinarySearchParams.max_loss_pct', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sniff_runtime', full_name='trafficgen.BinarySearchParams.sniff_runtime', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='l3', full_name='trafficgen.BinarySearchParams.l3', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dst_macs', full_name='trafficgen.BinarySearchParams.dst_macs', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search_granularity', full_name='trafficgen.BinarySearchParams.search_granularity', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=565,
  serialized_end=801,
)

_RESULT.fields_by_name['stats'].message_type = _PORTSTATS
DESCRIPTOR.message_types_by_name['IsTrafficgenRunningParams'] = _ISTRAFFICGENRUNNINGPARAMS
DESCRIPTOR.message_types_by_name['IsResultAvailableParams'] = _ISRESULTAVAILABLEPARAMS
DESCRIPTOR.message_types_by_name['GetResultParams'] = _GETRESULTPARAMS
DESCRIPTOR.message_types_by_name['StopTrafficgenParams'] = _STOPTRAFFICGENPARAMS
DESCRIPTOR.message_types_by_name['GetMacListParams'] = _GETMACLISTPARAMS
DESCRIPTOR.message_types_by_name['TrafficgenRunning'] = _TRAFFICGENRUNNING
DESCRIPTOR.message_types_by_name['ResultAvailable'] = _RESULTAVAILABLE
DESCRIPTOR.message_types_by_name['Success'] = _SUCCESS
DESCRIPTOR.message_types_by_name['MacList'] = _MACLIST
DESCRIPTOR.message_types_by_name['PortStats'] = _PORTSTATS
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['BinarySearchParams'] = _BINARYSEARCHPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IsTrafficgenRunningParams = _reflection.GeneratedProtocolMessageType('IsTrafficgenRunningParams', (_message.Message,), {
  'DESCRIPTOR' : _ISTRAFFICGENRUNNINGPARAMS,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.IsTrafficgenRunningParams)
  })
_sym_db.RegisterMessage(IsTrafficgenRunningParams)

IsResultAvailableParams = _reflection.GeneratedProtocolMessageType('IsResultAvailableParams', (_message.Message,), {
  'DESCRIPTOR' : _ISRESULTAVAILABLEPARAMS,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.IsResultAvailableParams)
  })
_sym_db.RegisterMessage(IsResultAvailableParams)

GetResultParams = _reflection.GeneratedProtocolMessageType('GetResultParams', (_message.Message,), {
  'DESCRIPTOR' : _GETRESULTPARAMS,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.GetResultParams)
  })
_sym_db.RegisterMessage(GetResultParams)

StopTrafficgenParams = _reflection.GeneratedProtocolMessageType('StopTrafficgenParams', (_message.Message,), {
  'DESCRIPTOR' : _STOPTRAFFICGENPARAMS,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.StopTrafficgenParams)
  })
_sym_db.RegisterMessage(StopTrafficgenParams)

GetMacListParams = _reflection.GeneratedProtocolMessageType('GetMacListParams', (_message.Message,), {
  'DESCRIPTOR' : _GETMACLISTPARAMS,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.GetMacListParams)
  })
_sym_db.RegisterMessage(GetMacListParams)

TrafficgenRunning = _reflection.GeneratedProtocolMessageType('TrafficgenRunning', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICGENRUNNING,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.TrafficgenRunning)
  })
_sym_db.RegisterMessage(TrafficgenRunning)

ResultAvailable = _reflection.GeneratedProtocolMessageType('ResultAvailable', (_message.Message,), {
  'DESCRIPTOR' : _RESULTAVAILABLE,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.ResultAvailable)
  })
_sym_db.RegisterMessage(ResultAvailable)

Success = _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESS,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.Success)
  })
_sym_db.RegisterMessage(Success)

MacList = _reflection.GeneratedProtocolMessageType('MacList', (_message.Message,), {
  'DESCRIPTOR' : _MACLIST,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.MacList)
  })
_sym_db.RegisterMessage(MacList)

PortStats = _reflection.GeneratedProtocolMessageType('PortStats', (_message.Message,), {
  'DESCRIPTOR' : _PORTSTATS,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.PortStats)
  })
_sym_db.RegisterMessage(PortStats)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.Result)
  })
_sym_db.RegisterMessage(Result)

BinarySearchParams = _reflection.GeneratedProtocolMessageType('BinarySearchParams', (_message.Message,), {
  'DESCRIPTOR' : _BINARYSEARCHPARAMS,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:trafficgen.BinarySearchParams)
  })
_sym_db.RegisterMessage(BinarySearchParams)



_TRAFFICGEN = _descriptor.ServiceDescriptor(
  name='Trafficgen',
  full_name='trafficgen.Trafficgen',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=804,
  serialized_end=1268,
  methods=[
  _descriptor.MethodDescriptor(
    name='isTrafficgenRunning',
    full_name='trafficgen.Trafficgen.isTrafficgenRunning',
    index=0,
    containing_service=None,
    input_type=_ISTRAFFICGENRUNNINGPARAMS,
    output_type=_TRAFFICGENRUNNING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='isResultAvailable',
    full_name='trafficgen.Trafficgen.isResultAvailable',
    index=1,
    containing_service=None,
    input_type=_ISRESULTAVAILABLEPARAMS,
    output_type=_RESULTAVAILABLE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getResult',
    full_name='trafficgen.Trafficgen.getResult',
    index=2,
    containing_service=None,
    input_type=_GETRESULTPARAMS,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='startTrafficgen',
    full_name='trafficgen.Trafficgen.startTrafficgen',
    index=3,
    containing_service=None,
    input_type=_BINARYSEARCHPARAMS,
    output_type=_SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stopTrafficgen',
    full_name='trafficgen.Trafficgen.stopTrafficgen',
    index=4,
    containing_service=None,
    input_type=_STOPTRAFFICGENPARAMS,
    output_type=_SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getMacList',
    full_name='trafficgen.Trafficgen.getMacList',
    index=5,
    containing_service=None,
    input_type=_GETMACLISTPARAMS,
    output_type=_MACLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRAFFICGEN)

DESCRIPTOR.services_by_name['Trafficgen'] = _TRAFFICGEN

# @@protoc_insertion_point(module_scope)