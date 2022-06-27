# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/batchpredictord/v1/batchpredictord.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_inference_dot_v1alpha1_dot_generated__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOgithub.com/metaprov/modelaapi/services/batchpredictord/v1/batchpredictord.proto\x12\x39github.com.metaprov.modelaapi.services.batchpredictord.v1\x1a\x45github.com/metaprov/modelaapi/pkg/apis/infra/v1alpha1/generated.proto\x1aIgithub.com/metaprov/modelaapi/pkg/apis/inference/v1alpha1/generated.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xa2\x06\n\x13\x42\x61tchPredictRequest\x12Y\n\nprediction\x18\x01 \x01(\x0b\x32\x45.github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1.Prediction\x12X\n\nfromBucket\x18\x02 \x01(\x0b\x32\x44.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.VirtualBucket\x12Y\n\x0e\x66romConnection\x18\x03 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Connection\x12r\n\nfromSecret\x18\x04 \x03(\x0b\x32^.github.com.metaprov.modelaapi.services.batchpredictord.v1.BatchPredictRequest.FromSecretEntry\x12Z\n\x0ctargetBucket\x18\x05 \x01(\x0b\x32\x44.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.VirtualBucket\x12W\n\x0ctoConnection\x18\x06 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Connection\x12n\n\x08toSecret\x18\x07 \x03(\x0b\x32\\.github.com.metaprov.modelaapi.services.batchpredictord.v1.BatchPredictRequest.ToSecretEntry\x1a\x31\n\x0f\x46romSecretEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a/\n\rToSecretEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"$\n\x14\x42\x61tchPredictResponse\x12\x0c\n\x04rows\x18\x01 \x01(\x05\"\x11\n\x0fShutdownRequest\"\x12\n\x10ShutdownResponse2\xe3\x02\n\x05\x42\x61tch\x12\xb1\x01\n\x0c\x42\x61tchPredict\x12N.github.com.metaprov.modelaapi.services.batchpredictord.v1.BatchPredictRequest\x1aO.github.com.metaprov.modelaapi.services.batchpredictord.v1.BatchPredictResponse\"\x00\x12\xa5\x01\n\x08Shutdown\x12J.github.com.metaprov.modelaapi.services.batchpredictord.v1.ShutdownRequest\x1aK.github.com.metaprov.modelaapi.services.batchpredictord.v1.ShutdownResponse\"\x00\x42;Z9github.com/metaprov/modelaapi/services/batchpredictord/v1b\x06proto3')



_BATCHPREDICTREQUEST = DESCRIPTOR.message_types_by_name['BatchPredictRequest']
_BATCHPREDICTREQUEST_FROMSECRETENTRY = _BATCHPREDICTREQUEST.nested_types_by_name['FromSecretEntry']
_BATCHPREDICTREQUEST_TOSECRETENTRY = _BATCHPREDICTREQUEST.nested_types_by_name['ToSecretEntry']
_BATCHPREDICTRESPONSE = DESCRIPTOR.message_types_by_name['BatchPredictResponse']
_SHUTDOWNREQUEST = DESCRIPTOR.message_types_by_name['ShutdownRequest']
_SHUTDOWNRESPONSE = DESCRIPTOR.message_types_by_name['ShutdownResponse']
BatchPredictRequest = _reflection.GeneratedProtocolMessageType('BatchPredictRequest', (_message.Message,), {

  'FromSecretEntry' : _reflection.GeneratedProtocolMessageType('FromSecretEntry', (_message.Message,), {
    'DESCRIPTOR' : _BATCHPREDICTREQUEST_FROMSECRETENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.batchpredictord.v1.batchpredictord_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.batchpredictord.v1.BatchPredictRequest.FromSecretEntry)
    })
  ,

  'ToSecretEntry' : _reflection.GeneratedProtocolMessageType('ToSecretEntry', (_message.Message,), {
    'DESCRIPTOR' : _BATCHPREDICTREQUEST_TOSECRETENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.batchpredictord.v1.batchpredictord_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.batchpredictord.v1.BatchPredictRequest.ToSecretEntry)
    })
  ,
  'DESCRIPTOR' : _BATCHPREDICTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.batchpredictord.v1.batchpredictord_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.batchpredictord.v1.BatchPredictRequest)
  })
_sym_db.RegisterMessage(BatchPredictRequest)
_sym_db.RegisterMessage(BatchPredictRequest.FromSecretEntry)
_sym_db.RegisterMessage(BatchPredictRequest.ToSecretEntry)

BatchPredictResponse = _reflection.GeneratedProtocolMessageType('BatchPredictResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHPREDICTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.batchpredictord.v1.batchpredictord_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.batchpredictord.v1.BatchPredictResponse)
  })
_sym_db.RegisterMessage(BatchPredictResponse)

ShutdownRequest = _reflection.GeneratedProtocolMessageType('ShutdownRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWNREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.batchpredictord.v1.batchpredictord_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.batchpredictord.v1.ShutdownRequest)
  })
_sym_db.RegisterMessage(ShutdownRequest)

ShutdownResponse = _reflection.GeneratedProtocolMessageType('ShutdownResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWNRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.batchpredictord.v1.batchpredictord_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.batchpredictord.v1.ShutdownResponse)
  })
_sym_db.RegisterMessage(ShutdownResponse)

_BATCH = DESCRIPTOR.services_by_name['Batch']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/metaprov/modelaapi/services/batchpredictord/v1'
  _BATCHPREDICTREQUEST_FROMSECRETENTRY._options = None
  _BATCHPREDICTREQUEST_FROMSECRETENTRY._serialized_options = b'8\001'
  _BATCHPREDICTREQUEST_TOSECRETENTRY._options = None
  _BATCHPREDICTREQUEST_TOSECRETENTRY._serialized_options = b'8\001'
  _BATCHPREDICTREQUEST._serialized_start=318
  _BATCHPREDICTREQUEST._serialized_end=1120
  _BATCHPREDICTREQUEST_FROMSECRETENTRY._serialized_start=1022
  _BATCHPREDICTREQUEST_FROMSECRETENTRY._serialized_end=1071
  _BATCHPREDICTREQUEST_TOSECRETENTRY._serialized_start=1073
  _BATCHPREDICTREQUEST_TOSECRETENTRY._serialized_end=1120
  _BATCHPREDICTRESPONSE._serialized_start=1122
  _BATCHPREDICTRESPONSE._serialized_end=1158
  _SHUTDOWNREQUEST._serialized_start=1160
  _SHUTDOWNREQUEST._serialized_end=1177
  _SHUTDOWNRESPONSE._serialized_start=1179
  _SHUTDOWNRESPONSE._serialized_end=1197
  _BATCH._serialized_start=1200
  _BATCH._serialized_end=1555
# @@protoc_insertion_point(module_scope)
