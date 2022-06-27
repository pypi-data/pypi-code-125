# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/servingsite/v1/servingsite.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgithub.com/metaprov/modelaapi/services/servingsite/v1/servingsite.proto\x12\x35github.com.metaprov.modelaapi.services.servingsite.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x45github.com/metaprov/modelaapi/pkg/apis/infra/v1alpha1/generated.proto\"\x80\x02\n\x17ListServingSitesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12j\n\x06labels\x18\x02 \x03(\x0b\x32Z.github.com.metaprov.modelaapi.services.servingsite.v1.ListServingSitesRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x91\x01\n\x18ListServingSitesResponse\x12\\\n\x0cservingsites\x18\x01 \x01(\x0b\x32\x46.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.ServingSiteList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"s\n\x18\x43reateServingSiteRequest\x12W\n\x0bservingsite\x18\x01 \x01(\x0b\x32\x42.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.ServingSite\"\x1b\n\x19\x43reateServingSiteResponse\"\xa3\x01\n\x18UpdateServingSiteRequest\x12W\n\x0bservingsite\x18\x01 \x01(\x0b\x32\x42.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.ServingSite\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x1b\n\x19UpdateServingSiteResponse\"8\n\x15GetServingSiteRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x7f\n\x16GetServingSiteResponse\x12W\n\x0bservingsite\x18\x01 \x01(\x0b\x32\x42.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.ServingSite\x12\x0c\n\x04yaml\x18\x02 \x01(\t\";\n\x18\x44\x65leteServingSiteRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1b\n\x19\x44\x65leteServingSiteResponse2\x9c\t\n\x12ServingSiteService\x12\xd9\x01\n\x10ListServingSites\x12N.github.com.metaprov.modelaapi.services.servingsite.v1.ListServingSitesRequest\x1aO.github.com.metaprov.modelaapi.services.servingsite.v1.ListServingSitesResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/servingsites/{namespace}\x12\xd3\x01\n\x11\x43reateServingSite\x12O.github.com.metaprov.modelaapi.services.servingsite.v1.CreateServingSiteRequest\x1aP.github.com.metaprov.modelaapi.services.servingsite.v1.CreateServingSiteResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/servingsites:\x01*\x12\xda\x01\n\x0eGetServingSite\x12L.github.com.metaprov.modelaapi.services.servingsite.v1.GetServingSiteRequest\x1aM.github.com.metaprov.modelaapi.services.servingsite.v1.GetServingSiteResponse\"+\x82\xd3\xe4\x93\x02%\x12#/v1/servingsites/{namespace}/{name}\x12\x90\x02\n\x11UpdateServingSite\x12O.github.com.metaprov.modelaapi.services.servingsite.v1.UpdateServingSiteRequest\x1aP.github.com.metaprov.modelaapi.services.servingsite.v1.UpdateServingSiteResponse\"X\x82\xd3\xe4\x93\x02R\x1aM/v1/servingsites/{servingsite.metadata.namespace}/{servingsite.metadata.name}:\x01*\x12\xe3\x01\n\x11\x44\x65leteServingSite\x12O.github.com.metaprov.modelaapi.services.servingsite.v1.DeleteServingSiteRequest\x1aP.github.com.metaprov.modelaapi.services.servingsite.v1.DeleteServingSiteResponse\"+\x82\xd3\xe4\x93\x02%*#/v1/servingsites/{namespace}/{name}B7Z5github.com/metaprov/modelaapi/services/servingsite/v1b\x06proto3')



_LISTSERVINGSITESREQUEST = DESCRIPTOR.message_types_by_name['ListServingSitesRequest']
_LISTSERVINGSITESREQUEST_LABELSENTRY = _LISTSERVINGSITESREQUEST.nested_types_by_name['LabelsEntry']
_LISTSERVINGSITESRESPONSE = DESCRIPTOR.message_types_by_name['ListServingSitesResponse']
_CREATESERVINGSITEREQUEST = DESCRIPTOR.message_types_by_name['CreateServingSiteRequest']
_CREATESERVINGSITERESPONSE = DESCRIPTOR.message_types_by_name['CreateServingSiteResponse']
_UPDATESERVINGSITEREQUEST = DESCRIPTOR.message_types_by_name['UpdateServingSiteRequest']
_UPDATESERVINGSITERESPONSE = DESCRIPTOR.message_types_by_name['UpdateServingSiteResponse']
_GETSERVINGSITEREQUEST = DESCRIPTOR.message_types_by_name['GetServingSiteRequest']
_GETSERVINGSITERESPONSE = DESCRIPTOR.message_types_by_name['GetServingSiteResponse']
_DELETESERVINGSITEREQUEST = DESCRIPTOR.message_types_by_name['DeleteServingSiteRequest']
_DELETESERVINGSITERESPONSE = DESCRIPTOR.message_types_by_name['DeleteServingSiteResponse']
ListServingSitesRequest = _reflection.GeneratedProtocolMessageType('ListServingSitesRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTSERVINGSITESREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.ListServingSitesRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTSERVINGSITESREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.ListServingSitesRequest)
  })
_sym_db.RegisterMessage(ListServingSitesRequest)
_sym_db.RegisterMessage(ListServingSitesRequest.LabelsEntry)

ListServingSitesResponse = _reflection.GeneratedProtocolMessageType('ListServingSitesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVINGSITESRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.ListServingSitesResponse)
  })
_sym_db.RegisterMessage(ListServingSitesResponse)

CreateServingSiteRequest = _reflection.GeneratedProtocolMessageType('CreateServingSiteRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVINGSITEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.CreateServingSiteRequest)
  })
_sym_db.RegisterMessage(CreateServingSiteRequest)

CreateServingSiteResponse = _reflection.GeneratedProtocolMessageType('CreateServingSiteResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVINGSITERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.CreateServingSiteResponse)
  })
_sym_db.RegisterMessage(CreateServingSiteResponse)

UpdateServingSiteRequest = _reflection.GeneratedProtocolMessageType('UpdateServingSiteRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVINGSITEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.UpdateServingSiteRequest)
  })
_sym_db.RegisterMessage(UpdateServingSiteRequest)

UpdateServingSiteResponse = _reflection.GeneratedProtocolMessageType('UpdateServingSiteResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVINGSITERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.UpdateServingSiteResponse)
  })
_sym_db.RegisterMessage(UpdateServingSiteResponse)

GetServingSiteRequest = _reflection.GeneratedProtocolMessageType('GetServingSiteRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVINGSITEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.GetServingSiteRequest)
  })
_sym_db.RegisterMessage(GetServingSiteRequest)

GetServingSiteResponse = _reflection.GeneratedProtocolMessageType('GetServingSiteResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVINGSITERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.GetServingSiteResponse)
  })
_sym_db.RegisterMessage(GetServingSiteResponse)

DeleteServingSiteRequest = _reflection.GeneratedProtocolMessageType('DeleteServingSiteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESERVINGSITEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.DeleteServingSiteRequest)
  })
_sym_db.RegisterMessage(DeleteServingSiteRequest)

DeleteServingSiteResponse = _reflection.GeneratedProtocolMessageType('DeleteServingSiteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETESERVINGSITERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.servingsite.v1.servingsite_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.servingsite.v1.DeleteServingSiteResponse)
  })
_sym_db.RegisterMessage(DeleteServingSiteResponse)

_SERVINGSITESERVICE = DESCRIPTOR.services_by_name['ServingSiteService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/metaprov/modelaapi/services/servingsite/v1'
  _LISTSERVINGSITESREQUEST_LABELSENTRY._options = None
  _LISTSERVINGSITESREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _SERVINGSITESERVICE.methods_by_name['ListServingSites']._options = None
  _SERVINGSITESERVICE.methods_by_name['ListServingSites']._serialized_options = b'\202\323\344\223\002\036\022\034/v1/servingsites/{namespace}'
  _SERVINGSITESERVICE.methods_by_name['CreateServingSite']._options = None
  _SERVINGSITESERVICE.methods_by_name['CreateServingSite']._serialized_options = b'\202\323\344\223\002\025\"\020/v1/servingsites:\001*'
  _SERVINGSITESERVICE.methods_by_name['GetServingSite']._options = None
  _SERVINGSITESERVICE.methods_by_name['GetServingSite']._serialized_options = b'\202\323\344\223\002%\022#/v1/servingsites/{namespace}/{name}'
  _SERVINGSITESERVICE.methods_by_name['UpdateServingSite']._options = None
  _SERVINGSITESERVICE.methods_by_name['UpdateServingSite']._serialized_options = b'\202\323\344\223\002R\032M/v1/servingsites/{servingsite.metadata.namespace}/{servingsite.metadata.name}:\001*'
  _SERVINGSITESERVICE.methods_by_name['DeleteServingSite']._options = None
  _SERVINGSITESERVICE.methods_by_name['DeleteServingSite']._serialized_options = b'\202\323\344\223\002%*#/v1/servingsites/{namespace}/{name}'
  _LISTSERVINGSITESREQUEST._serialized_start=266
  _LISTSERVINGSITESREQUEST._serialized_end=522
  _LISTSERVINGSITESREQUEST_LABELSENTRY._serialized_start=477
  _LISTSERVINGSITESREQUEST_LABELSENTRY._serialized_end=522
  _LISTSERVINGSITESRESPONSE._serialized_start=525
  _LISTSERVINGSITESRESPONSE._serialized_end=670
  _CREATESERVINGSITEREQUEST._serialized_start=672
  _CREATESERVINGSITEREQUEST._serialized_end=787
  _CREATESERVINGSITERESPONSE._serialized_start=789
  _CREATESERVINGSITERESPONSE._serialized_end=816
  _UPDATESERVINGSITEREQUEST._serialized_start=819
  _UPDATESERVINGSITEREQUEST._serialized_end=982
  _UPDATESERVINGSITERESPONSE._serialized_start=984
  _UPDATESERVINGSITERESPONSE._serialized_end=1011
  _GETSERVINGSITEREQUEST._serialized_start=1013
  _GETSERVINGSITEREQUEST._serialized_end=1069
  _GETSERVINGSITERESPONSE._serialized_start=1071
  _GETSERVINGSITERESPONSE._serialized_end=1198
  _DELETESERVINGSITEREQUEST._serialized_start=1200
  _DELETESERVINGSITEREQUEST._serialized_end=1259
  _DELETESERVINGSITERESPONSE._serialized_start=1261
  _DELETESERVINGSITERESPONSE._serialized_end=1288
  _SERVINGSITESERVICE._serialized_start=1291
  _SERVINGSITESERVICE._serialized_end=2471
# @@protoc_insertion_point(module_scope)
