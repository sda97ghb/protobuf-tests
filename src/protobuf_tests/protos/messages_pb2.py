# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protobuf_tests/protos/messages.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    "",
    "protobuf_tests/protos/messages.proto",
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n$protobuf_tests/protos/messages.proto"\'\n\x07\x41\x64\x64ress\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x0e\n\x06street\x18\x02 \x01(\t"\xae\x02\n\x06Person\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x16\n\tlast_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\nnick_names\x18\x03 \x03(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\x12\x1e\n\x11number_of_fingers\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12\x19\n\x11\x66\x61vourite_numbers\x18\x06 \x03(\x05\x12\x1e\n\x0c\x61\x64\x64ress_home\x18\x07 \x01(\x0b\x32\x08.Address\x12#\n\x0c\x61\x64\x64ress_work\x18\x08 \x01(\x0b\x32\x08.AddressH\x02\x88\x01\x01\x12"\n\x10\x66\x61vourite_places\x18\t \x03(\x0b\x32\x08.AddressB\x0c\n\n_last_nameB\x14\n\x12_number_of_fingersB\x0f\n\r_address_workb\x06proto3',
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR,
    "protobuf_tests.protos.messages_pb2",
    _globals,
)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_ADDRESS"]._serialized_start = 40
    _globals["_ADDRESS"]._serialized_end = 79
    _globals["_PERSON"]._serialized_start = 82
    _globals["_PERSON"]._serialized_end = 384
# @@protoc_insertion_point(module_scope)
