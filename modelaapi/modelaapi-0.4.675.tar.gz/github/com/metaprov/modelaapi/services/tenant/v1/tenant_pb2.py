# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/tenant/v1/tenant.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_training_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_inference_dot_v1alpha1_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=github.com/metaprov/modelaapi/services/tenant/v1/tenant.proto\x12\x30github.com.metaprov.modelaapi.services.tenant.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x45github.com/metaprov/modelaapi/pkg/apis/infra/v1alpha1/generated.proto\x1a\x44github.com/metaprov/modelaapi/pkg/apis/data/v1alpha1/generated.proto\x1aHgithub.com/metaprov/modelaapi/pkg/apis/training/v1alpha1/generated.proto\x1aIgithub.com/metaprov/modelaapi/pkg/apis/inference/v1alpha1/generated.proto\"\xfb\x01\n\x17ListTenantAlertsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x65\n\x06labels\x18\x02 \x03(\x0b\x32U.github.com.metaprov.modelaapi.services.tenant.v1.ListTenantAlertsRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x85\x01\n\x18ListTenantAlertsResponse\x12P\n\x06\x61lerts\x18\x01 \x01(\x0b\x32@.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.AlertList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb8\x01\n\x12ListTenantsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12`\n\x06labels\x18\x03 \x03(\x0b\x32P.github.com.metaprov.modelaapi.services.tenant.v1.ListTenantsRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x82\x01\n\x13ListTenantsResponse\x12R\n\x07tenants\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.TenantList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"d\n\x13\x43reateTenantRequest\x12M\n\x06tenant\x18\x04 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Tenant\"\x16\n\x14\x43reateTenantResponse\"\x94\x01\n\x13UpdateTenantRequest\x12M\n\x06tenant\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Tenant\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x16\n\x14UpdateTenantResponse\"3\n\x10GetTenantRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x8c\x04\n\x11GetTenantResponse\x12M\n\x06tenant\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Tenant\x12L\n\x06\x61lerts\x18\x02 \x03(\x0b\x32<.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Alert\x12O\n\x08\x64\x61tasets\x18\x03 \x03(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Dataset\x12P\n\x07studies\x18\x04 \x03(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.Study\x12O\n\x06models\x18\x05 \x03(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.Model\x12X\n\npredictors\x18\x06 \x03(\x0b\x32\x44.github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1.Predictor\x12\x0c\n\x04yaml\x18\x07 \x01(\t\"6\n\x13\x44\x65leteTenantRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x16\n\x14\x44\x65leteTenantResponse2\xa5\t\n\rTenantService\x12\xd1\x01\n\x10ListTenantAlerts\x12I.github.com.metaprov.modelaapi.services.tenant.v1.ListTenantAlertsRequest\x1aJ.github.com.metaprov.modelaapi.services.tenant.v1.ListTenantAlertsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/tenants/{namespace}:alerts\x12\xbb\x01\n\x0bListTenants\x12\x44.github.com.metaprov.modelaapi.services.tenant.v1.ListTenantsRequest\x1a\x45.github.com.metaprov.modelaapi.services.tenant.v1.ListTenantsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/tenants/{namespace}\x12\xb5\x01\n\x0c\x43reateTenant\x12\x45.github.com.metaprov.modelaapi.services.tenant.v1.CreateTenantRequest\x1a\x46.github.com.metaprov.modelaapi.services.tenant.v1.CreateTenantResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0b/v1/tenants:\x01*\x12\xbc\x01\n\tGetTenant\x12\x42.github.com.metaprov.modelaapi.services.tenant.v1.GetTenantRequest\x1a\x43.github.com.metaprov.modelaapi.services.tenant.v1.GetTenantResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/tenants/{namespace}/{name}\x12\xe8\x01\n\x0cUpdateTenant\x12\x45.github.com.metaprov.modelaapi.services.tenant.v1.UpdateTenantRequest\x1a\x46.github.com.metaprov.modelaapi.services.tenant.v1.UpdateTenantResponse\"I\x82\xd3\xe4\x93\x02\x43\x1a>/v1/tenants/{tenant.metadata.namespace}/{tenant.metadata.name}:\x01*\x12\x9f\x01\n\x0c\x44\x65leteTenant\x12\x45.github.com.metaprov.modelaapi.services.tenant.v1.DeleteTenantRequest\x1a\x46.github.com.metaprov.modelaapi.services.tenant.v1.DeleteTenantResponse\"\x00\x42\x32Z0github.com/metaprov/modelaapi/services/tenant/v1b\x06proto3')



_LISTTENANTALERTSREQUEST = DESCRIPTOR.message_types_by_name['ListTenantAlertsRequest']
_LISTTENANTALERTSREQUEST_LABELSENTRY = _LISTTENANTALERTSREQUEST.nested_types_by_name['LabelsEntry']
_LISTTENANTALERTSRESPONSE = DESCRIPTOR.message_types_by_name['ListTenantAlertsResponse']
_LISTTENANTSREQUEST = DESCRIPTOR.message_types_by_name['ListTenantsRequest']
_LISTTENANTSREQUEST_LABELSENTRY = _LISTTENANTSREQUEST.nested_types_by_name['LabelsEntry']
_LISTTENANTSRESPONSE = DESCRIPTOR.message_types_by_name['ListTenantsResponse']
_CREATETENANTREQUEST = DESCRIPTOR.message_types_by_name['CreateTenantRequest']
_CREATETENANTRESPONSE = DESCRIPTOR.message_types_by_name['CreateTenantResponse']
_UPDATETENANTREQUEST = DESCRIPTOR.message_types_by_name['UpdateTenantRequest']
_UPDATETENANTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateTenantResponse']
_GETTENANTREQUEST = DESCRIPTOR.message_types_by_name['GetTenantRequest']
_GETTENANTRESPONSE = DESCRIPTOR.message_types_by_name['GetTenantResponse']
_DELETETENANTREQUEST = DESCRIPTOR.message_types_by_name['DeleteTenantRequest']
_DELETETENANTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteTenantResponse']
ListTenantAlertsRequest = _reflection.GeneratedProtocolMessageType('ListTenantAlertsRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTTENANTALERTSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.ListTenantAlertsRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTTENANTALERTSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.ListTenantAlertsRequest)
  })
_sym_db.RegisterMessage(ListTenantAlertsRequest)
_sym_db.RegisterMessage(ListTenantAlertsRequest.LabelsEntry)

ListTenantAlertsResponse = _reflection.GeneratedProtocolMessageType('ListTenantAlertsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTENANTALERTSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.ListTenantAlertsResponse)
  })
_sym_db.RegisterMessage(ListTenantAlertsResponse)

ListTenantsRequest = _reflection.GeneratedProtocolMessageType('ListTenantsRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTTENANTSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.ListTenantsRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTTENANTSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.ListTenantsRequest)
  })
_sym_db.RegisterMessage(ListTenantsRequest)
_sym_db.RegisterMessage(ListTenantsRequest.LabelsEntry)

ListTenantsResponse = _reflection.GeneratedProtocolMessageType('ListTenantsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTENANTSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.ListTenantsResponse)
  })
_sym_db.RegisterMessage(ListTenantsResponse)

CreateTenantRequest = _reflection.GeneratedProtocolMessageType('CreateTenantRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETENANTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.CreateTenantRequest)
  })
_sym_db.RegisterMessage(CreateTenantRequest)

CreateTenantResponse = _reflection.GeneratedProtocolMessageType('CreateTenantResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATETENANTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.CreateTenantResponse)
  })
_sym_db.RegisterMessage(CreateTenantResponse)

UpdateTenantRequest = _reflection.GeneratedProtocolMessageType('UpdateTenantRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETENANTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.UpdateTenantRequest)
  })
_sym_db.RegisterMessage(UpdateTenantRequest)

UpdateTenantResponse = _reflection.GeneratedProtocolMessageType('UpdateTenantResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETENANTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.UpdateTenantResponse)
  })
_sym_db.RegisterMessage(UpdateTenantResponse)

GetTenantRequest = _reflection.GeneratedProtocolMessageType('GetTenantRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTENANTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.GetTenantRequest)
  })
_sym_db.RegisterMessage(GetTenantRequest)

GetTenantResponse = _reflection.GeneratedProtocolMessageType('GetTenantResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTENANTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.GetTenantResponse)
  })
_sym_db.RegisterMessage(GetTenantResponse)

DeleteTenantRequest = _reflection.GeneratedProtocolMessageType('DeleteTenantRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETENANTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.DeleteTenantRequest)
  })
_sym_db.RegisterMessage(DeleteTenantRequest)

DeleteTenantResponse = _reflection.GeneratedProtocolMessageType('DeleteTenantResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETETENANTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.tenant.v1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.tenant.v1.DeleteTenantResponse)
  })
_sym_db.RegisterMessage(DeleteTenantResponse)

_TENANTSERVICE = DESCRIPTOR.services_by_name['TenantService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/metaprov/modelaapi/services/tenant/v1'
  _LISTTENANTALERTSREQUEST_LABELSENTRY._options = None
  _LISTTENANTALERTSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _LISTTENANTSREQUEST_LABELSENTRY._options = None
  _LISTTENANTSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _TENANTSERVICE.methods_by_name['ListTenantAlerts']._options = None
  _TENANTSERVICE.methods_by_name['ListTenantAlerts']._serialized_options = b'\202\323\344\223\002 \022\036/v1/tenants/{namespace}:alerts'
  _TENANTSERVICE.methods_by_name['ListTenants']._options = None
  _TENANTSERVICE.methods_by_name['ListTenants']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/tenants/{namespace}'
  _TENANTSERVICE.methods_by_name['CreateTenant']._options = None
  _TENANTSERVICE.methods_by_name['CreateTenant']._serialized_options = b'\202\323\344\223\002\020\"\013/v1/tenants:\001*'
  _TENANTSERVICE.methods_by_name['GetTenant']._options = None
  _TENANTSERVICE.methods_by_name['GetTenant']._serialized_options = b'\202\323\344\223\002 \022\036/v1/tenants/{namespace}/{name}'
  _TENANTSERVICE.methods_by_name['UpdateTenant']._options = None
  _TENANTSERVICE.methods_by_name['UpdateTenant']._serialized_options = b'\202\323\344\223\002C\032>/v1/tenants/{tenant.metadata.namespace}/{tenant.metadata.name}:\001*'
  _LISTTENANTALERTSREQUEST._serialized_start=470
  _LISTTENANTALERTSREQUEST._serialized_end=721
  _LISTTENANTALERTSREQUEST_LABELSENTRY._serialized_start=676
  _LISTTENANTALERTSREQUEST_LABELSENTRY._serialized_end=721
  _LISTTENANTALERTSRESPONSE._serialized_start=724
  _LISTTENANTALERTSRESPONSE._serialized_end=857
  _LISTTENANTSREQUEST._serialized_start=860
  _LISTTENANTSREQUEST._serialized_end=1044
  _LISTTENANTSREQUEST_LABELSENTRY._serialized_start=676
  _LISTTENANTSREQUEST_LABELSENTRY._serialized_end=721
  _LISTTENANTSRESPONSE._serialized_start=1047
  _LISTTENANTSRESPONSE._serialized_end=1177
  _CREATETENANTREQUEST._serialized_start=1179
  _CREATETENANTREQUEST._serialized_end=1279
  _CREATETENANTRESPONSE._serialized_start=1281
  _CREATETENANTRESPONSE._serialized_end=1303
  _UPDATETENANTREQUEST._serialized_start=1306
  _UPDATETENANTREQUEST._serialized_end=1454
  _UPDATETENANTRESPONSE._serialized_start=1456
  _UPDATETENANTRESPONSE._serialized_end=1478
  _GETTENANTREQUEST._serialized_start=1480
  _GETTENANTREQUEST._serialized_end=1531
  _GETTENANTRESPONSE._serialized_start=1534
  _GETTENANTRESPONSE._serialized_end=2058
  _DELETETENANTREQUEST._serialized_start=2060
  _DELETETENANTREQUEST._serialized_end=2114
  _DELETETENANTRESPONSE._serialized_start=2116
  _DELETETENANTRESPONSE._serialized_end=2138
  _TENANTSERVICE._serialized_start=2141
  _TENANTSERVICE._serialized_end=3330
# @@protoc_insertion_point(module_scope)
