# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/license/v1/license.proto
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
from github.com.metaprov.modelaapi.services.common.v1 import common_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?github.com/metaprov/modelaapi/services/license/v1/license.proto\x12\x31github.com.metaprov.modelaapi.services.license.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x45github.com/metaprov/modelaapi/pkg/apis/infra/v1alpha1/generated.proto\x1a=github.com/metaprov/modelaapi/services/common/v1/common.proto\"\xf4\x01\n\x13ListLicensesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x62\n\x06labels\x18\x02 \x03(\x0b\x32R.github.com.metaprov.modelaapi.services.license.v1.ListLicensesRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x85\x01\n\x14ListLicensesResponse\x12T\n\x08licences\x18\x01 \x01(\x0b\x32\x42.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.LicenseList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x11\n\x0fLicenseResponse\"g\n\x14\x43reateLicenseRequest\x12O\n\x07license\x18\x01 \x01(\x0b\x32>.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.License\":\n\x1b\x43reateLicenseFromKeyRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06tenant\x18\x02 \x01(\t\"\x17\n\x15\x43reateLicenseResponse\"\x97\x01\n\x14UpdateLicenseRequest\x12O\n\x07license\x18\x01 \x01(\x0b\x32>.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.License\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x17\n\x15UpdateLicenseResponse\"4\n\x11GetLicenseRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"s\n\x12GetLicenseResponse\x12O\n\x07license\x18\x01 \x01(\x0b\x32>.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.License\x12\x0c\n\x04yaml\x18\x02 \x01(\t\">\n\x1bGetLicenseNamespacesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"s\n\x1cGetLicenseNamespacesResponse\x12S\n\nnamespaces\x18\x01 \x03(\x0b\x32?.github.com.metaprov.modelaapi.services.common.v1.NamespaceInfo\"7\n\x14\x44\x65leteLicenseRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x17\n\x15\x44\x65leteLicenseResponse2\xe4\t\n\x0eLicenseService\x12\xc1\x01\n\x0cListLicenses\x12\x46.github.com.metaprov.modelaapi.services.license.v1.ListLicensesRequest\x1aG.github.com.metaprov.modelaapi.services.license.v1.ListLicensesResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/licenses/{namespace}\x12\xbb\x01\n\rCreateLicense\x12G.github.com.metaprov.modelaapi.services.license.v1.CreateLicenseRequest\x1aH.github.com.metaprov.modelaapi.services.license.v1.CreateLicenseResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/licenses:\x01*\x12\xc9\x01\n\x14\x43reateLicenseFromKey\x12N.github.com.metaprov.modelaapi.services.license.v1.CreateLicenseFromKeyRequest\x1aH.github.com.metaprov.modelaapi.services.license.v1.CreateLicenseResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/licenses:\x01*\x12\xc2\x01\n\nGetLicense\x12\x44.github.com.metaprov.modelaapi.services.license.v1.GetLicenseRequest\x1a\x45.github.com.metaprov.modelaapi.services.license.v1.GetLicenseResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/licenses/{namespace}/{name}\x12\xf0\x01\n\rUpdateLicense\x12G.github.com.metaprov.modelaapi.services.license.v1.UpdateLicenseRequest\x1aH.github.com.metaprov.modelaapi.services.license.v1.UpdateLicenseResponse\"L\x82\xd3\xe4\x93\x02\x46\x1a\x41/v1/licenses/{license.metadata.namespace}/{license.metadata.name}:\x01*\x12\xcb\x01\n\rDeleteLicense\x12G.github.com.metaprov.modelaapi.services.license.v1.DeleteLicenseRequest\x1aH.github.com.metaprov.modelaapi.services.license.v1.DeleteLicenseResponse\"\'\x82\xd3\xe4\x93\x02!*\x1f/v1/licenses/{namespace}/{name}B3Z1github.com/metaprov/modelaapi/services/license/v1b\x06proto3')



_LISTLICENSESREQUEST = DESCRIPTOR.message_types_by_name['ListLicensesRequest']
_LISTLICENSESREQUEST_LABELSENTRY = _LISTLICENSESREQUEST.nested_types_by_name['LabelsEntry']
_LISTLICENSESRESPONSE = DESCRIPTOR.message_types_by_name['ListLicensesResponse']
_LICENSERESPONSE = DESCRIPTOR.message_types_by_name['LicenseResponse']
_CREATELICENSEREQUEST = DESCRIPTOR.message_types_by_name['CreateLicenseRequest']
_CREATELICENSEFROMKEYREQUEST = DESCRIPTOR.message_types_by_name['CreateLicenseFromKeyRequest']
_CREATELICENSERESPONSE = DESCRIPTOR.message_types_by_name['CreateLicenseResponse']
_UPDATELICENSEREQUEST = DESCRIPTOR.message_types_by_name['UpdateLicenseRequest']
_UPDATELICENSERESPONSE = DESCRIPTOR.message_types_by_name['UpdateLicenseResponse']
_GETLICENSEREQUEST = DESCRIPTOR.message_types_by_name['GetLicenseRequest']
_GETLICENSERESPONSE = DESCRIPTOR.message_types_by_name['GetLicenseResponse']
_GETLICENSENAMESPACESREQUEST = DESCRIPTOR.message_types_by_name['GetLicenseNamespacesRequest']
_GETLICENSENAMESPACESRESPONSE = DESCRIPTOR.message_types_by_name['GetLicenseNamespacesResponse']
_DELETELICENSEREQUEST = DESCRIPTOR.message_types_by_name['DeleteLicenseRequest']
_DELETELICENSERESPONSE = DESCRIPTOR.message_types_by_name['DeleteLicenseResponse']
ListLicensesRequest = _reflection.GeneratedProtocolMessageType('ListLicensesRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTLICENSESREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.ListLicensesRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTLICENSESREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.ListLicensesRequest)
  })
_sym_db.RegisterMessage(ListLicensesRequest)
_sym_db.RegisterMessage(ListLicensesRequest.LabelsEntry)

ListLicensesResponse = _reflection.GeneratedProtocolMessageType('ListLicensesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTLICENSESRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.ListLicensesResponse)
  })
_sym_db.RegisterMessage(ListLicensesResponse)

LicenseResponse = _reflection.GeneratedProtocolMessageType('LicenseResponse', (_message.Message,), {
  'DESCRIPTOR' : _LICENSERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.LicenseResponse)
  })
_sym_db.RegisterMessage(LicenseResponse)

CreateLicenseRequest = _reflection.GeneratedProtocolMessageType('CreateLicenseRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELICENSEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.CreateLicenseRequest)
  })
_sym_db.RegisterMessage(CreateLicenseRequest)

CreateLicenseFromKeyRequest = _reflection.GeneratedProtocolMessageType('CreateLicenseFromKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELICENSEFROMKEYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.CreateLicenseFromKeyRequest)
  })
_sym_db.RegisterMessage(CreateLicenseFromKeyRequest)

CreateLicenseResponse = _reflection.GeneratedProtocolMessageType('CreateLicenseResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATELICENSERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.CreateLicenseResponse)
  })
_sym_db.RegisterMessage(CreateLicenseResponse)

UpdateLicenseRequest = _reflection.GeneratedProtocolMessageType('UpdateLicenseRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATELICENSEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.UpdateLicenseRequest)
  })
_sym_db.RegisterMessage(UpdateLicenseRequest)

UpdateLicenseResponse = _reflection.GeneratedProtocolMessageType('UpdateLicenseResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATELICENSERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.UpdateLicenseResponse)
  })
_sym_db.RegisterMessage(UpdateLicenseResponse)

GetLicenseRequest = _reflection.GeneratedProtocolMessageType('GetLicenseRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLICENSEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.GetLicenseRequest)
  })
_sym_db.RegisterMessage(GetLicenseRequest)

GetLicenseResponse = _reflection.GeneratedProtocolMessageType('GetLicenseResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLICENSERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.GetLicenseResponse)
  })
_sym_db.RegisterMessage(GetLicenseResponse)

GetLicenseNamespacesRequest = _reflection.GeneratedProtocolMessageType('GetLicenseNamespacesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLICENSENAMESPACESREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.GetLicenseNamespacesRequest)
  })
_sym_db.RegisterMessage(GetLicenseNamespacesRequest)

GetLicenseNamespacesResponse = _reflection.GeneratedProtocolMessageType('GetLicenseNamespacesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLICENSENAMESPACESRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.GetLicenseNamespacesResponse)
  })
_sym_db.RegisterMessage(GetLicenseNamespacesResponse)

DeleteLicenseRequest = _reflection.GeneratedProtocolMessageType('DeleteLicenseRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETELICENSEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.DeleteLicenseRequest)
  })
_sym_db.RegisterMessage(DeleteLicenseRequest)

DeleteLicenseResponse = _reflection.GeneratedProtocolMessageType('DeleteLicenseResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETELICENSERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.license.v1.license_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.license.v1.DeleteLicenseResponse)
  })
_sym_db.RegisterMessage(DeleteLicenseResponse)

_LICENSESERVICE = DESCRIPTOR.services_by_name['LicenseService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/metaprov/modelaapi/services/license/v1'
  _LISTLICENSESREQUEST_LABELSENTRY._options = None
  _LISTLICENSESREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _LICENSESERVICE.methods_by_name['ListLicenses']._options = None
  _LICENSESERVICE.methods_by_name['ListLicenses']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/licenses/{namespace}'
  _LICENSESERVICE.methods_by_name['CreateLicense']._options = None
  _LICENSESERVICE.methods_by_name['CreateLicense']._serialized_options = b'\202\323\344\223\002\021\"\014/v1/licenses:\001*'
  _LICENSESERVICE.methods_by_name['CreateLicenseFromKey']._options = None
  _LICENSESERVICE.methods_by_name['CreateLicenseFromKey']._serialized_options = b'\202\323\344\223\002\021\"\014/v1/licenses:\001*'
  _LICENSESERVICE.methods_by_name['GetLicense']._options = None
  _LICENSESERVICE.methods_by_name['GetLicense']._serialized_options = b'\202\323\344\223\002!\022\037/v1/licenses/{namespace}/{name}'
  _LICENSESERVICE.methods_by_name['UpdateLicense']._options = None
  _LICENSESERVICE.methods_by_name['UpdateLicense']._serialized_options = b'\202\323\344\223\002F\032A/v1/licenses/{license.metadata.namespace}/{license.metadata.name}:\001*'
  _LICENSESERVICE.methods_by_name['DeleteLicense']._options = None
  _LICENSESERVICE.methods_by_name['DeleteLicense']._serialized_options = b'\202\323\344\223\002!*\037/v1/licenses/{namespace}/{name}'
  _LISTLICENSESREQUEST._serialized_start=317
  _LISTLICENSESREQUEST._serialized_end=561
  _LISTLICENSESREQUEST_LABELSENTRY._serialized_start=516
  _LISTLICENSESREQUEST_LABELSENTRY._serialized_end=561
  _LISTLICENSESRESPONSE._serialized_start=564
  _LISTLICENSESRESPONSE._serialized_end=697
  _LICENSERESPONSE._serialized_start=699
  _LICENSERESPONSE._serialized_end=716
  _CREATELICENSEREQUEST._serialized_start=718
  _CREATELICENSEREQUEST._serialized_end=821
  _CREATELICENSEFROMKEYREQUEST._serialized_start=823
  _CREATELICENSEFROMKEYREQUEST._serialized_end=881
  _CREATELICENSERESPONSE._serialized_start=883
  _CREATELICENSERESPONSE._serialized_end=906
  _UPDATELICENSEREQUEST._serialized_start=909
  _UPDATELICENSEREQUEST._serialized_end=1060
  _UPDATELICENSERESPONSE._serialized_start=1062
  _UPDATELICENSERESPONSE._serialized_end=1085
  _GETLICENSEREQUEST._serialized_start=1087
  _GETLICENSEREQUEST._serialized_end=1139
  _GETLICENSERESPONSE._serialized_start=1141
  _GETLICENSERESPONSE._serialized_end=1256
  _GETLICENSENAMESPACESREQUEST._serialized_start=1258
  _GETLICENSENAMESPACESREQUEST._serialized_end=1320
  _GETLICENSENAMESPACESRESPONSE._serialized_start=1322
  _GETLICENSENAMESPACESRESPONSE._serialized_end=1437
  _DELETELICENSEREQUEST._serialized_start=1439
  _DELETELICENSEREQUEST._serialized_end=1494
  _DELETELICENSERESPONSE._serialized_start=1496
  _DELETELICENSERESPONSE._serialized_end=1519
  _LICENSESERVICE._serialized_start=1522
  _LICENSESERVICE._serialized_end=2774
# @@protoc_insertion_point(module_scope)
