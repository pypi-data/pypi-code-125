# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/dataproduct/v1/dataproduct.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgithub.com/metaprov/modelaapi/services/dataproduct/v1/dataproduct.proto\x12\x35github.com.metaprov.modelaapi.services.dataproduct.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x45github.com/metaprov/modelaapi/pkg/apis/infra/v1alpha1/generated.proto\x1a\x44github.com/metaprov/modelaapi/pkg/apis/data/v1alpha1/generated.proto\x1aHgithub.com/metaprov/modelaapi/pkg/apis/training/v1alpha1/generated.proto\x1aIgithub.com/metaprov/modelaapi/pkg/apis/inference/v1alpha1/generated.proto\"\x80\x02\n\x17ListDataProductsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12j\n\x06labels\x18\x02 \x03(\x0b\x32Z.github.com.metaprov.modelaapi.services.dataproduct.v1.ListDataProductsRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x90\x01\n\x18ListDataProductsResponse\x12[\n\x0c\x64\x61taproducts\x18\x01 \x01(\x0b\x32\x45.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataProductList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"r\n\x18\x43reateDataProductRequest\x12V\n\x0b\x64\x61taproduct\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataProduct\"\x1b\n\x19\x43reateDataProductResponse\"\xa2\x01\n\x18UpdateDataProductRequest\x12V\n\x0b\x64\x61taproduct\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataProduct\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x1b\n\x19UpdateDataProductResponse\"8\n\x15GetDataProductRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x9a\x04\n\x16GetDataProductResponse\x12V\n\x0b\x64\x61taproduct\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataProduct\x12L\n\x06\x61lerts\x18\x02 \x03(\x0b\x32<.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Alert\x12O\n\x08\x64\x61tasets\x18\x03 \x03(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Dataset\x12P\n\x07studies\x18\x04 \x03(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.Study\x12O\n\x06models\x18\x05 \x03(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.Model\x12X\n\npredictors\x18\x06 \x03(\x0b\x32\x44.github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1.Predictor\x12\x0c\n\x04yaml\x18\x07 \x01(\t\";\n\x18\x44\x65leteDataProductRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1b\n\x19\x44\x65leteDataProductResponse2\x9c\t\n\x12\x44\x61taProductService\x12\xd9\x01\n\x10ListDataProducts\x12N.github.com.metaprov.modelaapi.services.dataproduct.v1.ListDataProductsRequest\x1aO.github.com.metaprov.modelaapi.services.dataproduct.v1.ListDataProductsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/dataproducts/{namespace}\x12\xd3\x01\n\x11\x43reateDataProduct\x12O.github.com.metaprov.modelaapi.services.dataproduct.v1.CreateDataProductRequest\x1aP.github.com.metaprov.modelaapi.services.dataproduct.v1.CreateDataProductResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/dataproducts:\x01*\x12\xda\x01\n\x0eGetDataProduct\x12L.github.com.metaprov.modelaapi.services.dataproduct.v1.GetDataProductRequest\x1aM.github.com.metaprov.modelaapi.services.dataproduct.v1.GetDataProductResponse\"+\x82\xd3\xe4\x93\x02%\x12#/v1/dataproducts/{namespace}/{name}\x12\x90\x02\n\x11UpdateDataProduct\x12O.github.com.metaprov.modelaapi.services.dataproduct.v1.UpdateDataProductRequest\x1aP.github.com.metaprov.modelaapi.services.dataproduct.v1.UpdateDataProductResponse\"X\x82\xd3\xe4\x93\x02R\x1aM/v1/dataproducts/{dataproduct.metadata.namespace}/{dataproduct.metadata.name}:\x01*\x12\xe3\x01\n\x11\x44\x65leteDataProduct\x12O.github.com.metaprov.modelaapi.services.dataproduct.v1.DeleteDataProductRequest\x1aP.github.com.metaprov.modelaapi.services.dataproduct.v1.DeleteDataProductResponse\"+\x82\xd3\xe4\x93\x02%*#/v1/dataproducts/{namespace}/{name}B7Z5github.com/metaprov/modelaapi/services/dataproduct/v1b\x06proto3')



_LISTDATAPRODUCTSREQUEST = DESCRIPTOR.message_types_by_name['ListDataProductsRequest']
_LISTDATAPRODUCTSREQUEST_LABELSENTRY = _LISTDATAPRODUCTSREQUEST.nested_types_by_name['LabelsEntry']
_LISTDATAPRODUCTSRESPONSE = DESCRIPTOR.message_types_by_name['ListDataProductsResponse']
_CREATEDATAPRODUCTREQUEST = DESCRIPTOR.message_types_by_name['CreateDataProductRequest']
_CREATEDATAPRODUCTRESPONSE = DESCRIPTOR.message_types_by_name['CreateDataProductResponse']
_UPDATEDATAPRODUCTREQUEST = DESCRIPTOR.message_types_by_name['UpdateDataProductRequest']
_UPDATEDATAPRODUCTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateDataProductResponse']
_GETDATAPRODUCTREQUEST = DESCRIPTOR.message_types_by_name['GetDataProductRequest']
_GETDATAPRODUCTRESPONSE = DESCRIPTOR.message_types_by_name['GetDataProductResponse']
_DELETEDATAPRODUCTREQUEST = DESCRIPTOR.message_types_by_name['DeleteDataProductRequest']
_DELETEDATAPRODUCTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteDataProductResponse']
ListDataProductsRequest = _reflection.GeneratedProtocolMessageType('ListDataProductsRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTDATAPRODUCTSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.ListDataProductsRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTDATAPRODUCTSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.ListDataProductsRequest)
  })
_sym_db.RegisterMessage(ListDataProductsRequest)
_sym_db.RegisterMessage(ListDataProductsRequest.LabelsEntry)

ListDataProductsResponse = _reflection.GeneratedProtocolMessageType('ListDataProductsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATAPRODUCTSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.ListDataProductsResponse)
  })
_sym_db.RegisterMessage(ListDataProductsResponse)

CreateDataProductRequest = _reflection.GeneratedProtocolMessageType('CreateDataProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATAPRODUCTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.CreateDataProductRequest)
  })
_sym_db.RegisterMessage(CreateDataProductRequest)

CreateDataProductResponse = _reflection.GeneratedProtocolMessageType('CreateDataProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATAPRODUCTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.CreateDataProductResponse)
  })
_sym_db.RegisterMessage(CreateDataProductResponse)

UpdateDataProductRequest = _reflection.GeneratedProtocolMessageType('UpdateDataProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATAPRODUCTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.UpdateDataProductRequest)
  })
_sym_db.RegisterMessage(UpdateDataProductRequest)

UpdateDataProductResponse = _reflection.GeneratedProtocolMessageType('UpdateDataProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATAPRODUCTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.UpdateDataProductResponse)
  })
_sym_db.RegisterMessage(UpdateDataProductResponse)

GetDataProductRequest = _reflection.GeneratedProtocolMessageType('GetDataProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATAPRODUCTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.GetDataProductRequest)
  })
_sym_db.RegisterMessage(GetDataProductRequest)

GetDataProductResponse = _reflection.GeneratedProtocolMessageType('GetDataProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATAPRODUCTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.GetDataProductResponse)
  })
_sym_db.RegisterMessage(GetDataProductResponse)

DeleteDataProductRequest = _reflection.GeneratedProtocolMessageType('DeleteDataProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATAPRODUCTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.DeleteDataProductRequest)
  })
_sym_db.RegisterMessage(DeleteDataProductRequest)

DeleteDataProductResponse = _reflection.GeneratedProtocolMessageType('DeleteDataProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATAPRODUCTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataproduct.v1.dataproduct_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataproduct.v1.DeleteDataProductResponse)
  })
_sym_db.RegisterMessage(DeleteDataProductResponse)

_DATAPRODUCTSERVICE = DESCRIPTOR.services_by_name['DataProductService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/metaprov/modelaapi/services/dataproduct/v1'
  _LISTDATAPRODUCTSREQUEST_LABELSENTRY._options = None
  _LISTDATAPRODUCTSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _DATAPRODUCTSERVICE.methods_by_name['ListDataProducts']._options = None
  _DATAPRODUCTSERVICE.methods_by_name['ListDataProducts']._serialized_options = b'\202\323\344\223\002\036\022\034/v1/dataproducts/{namespace}'
  _DATAPRODUCTSERVICE.methods_by_name['CreateDataProduct']._options = None
  _DATAPRODUCTSERVICE.methods_by_name['CreateDataProduct']._serialized_options = b'\202\323\344\223\002\025\"\020/v1/dataproducts:\001*'
  _DATAPRODUCTSERVICE.methods_by_name['GetDataProduct']._options = None
  _DATAPRODUCTSERVICE.methods_by_name['GetDataProduct']._serialized_options = b'\202\323\344\223\002%\022#/v1/dataproducts/{namespace}/{name}'
  _DATAPRODUCTSERVICE.methods_by_name['UpdateDataProduct']._options = None
  _DATAPRODUCTSERVICE.methods_by_name['UpdateDataProduct']._serialized_options = b'\202\323\344\223\002R\032M/v1/dataproducts/{dataproduct.metadata.namespace}/{dataproduct.metadata.name}:\001*'
  _DATAPRODUCTSERVICE.methods_by_name['DeleteDataProduct']._options = None
  _DATAPRODUCTSERVICE.methods_by_name['DeleteDataProduct']._serialized_options = b'\202\323\344\223\002%*#/v1/dataproducts/{namespace}/{name}'
  _LISTDATAPRODUCTSREQUEST._serialized_start=485
  _LISTDATAPRODUCTSREQUEST._serialized_end=741
  _LISTDATAPRODUCTSREQUEST_LABELSENTRY._serialized_start=696
  _LISTDATAPRODUCTSREQUEST_LABELSENTRY._serialized_end=741
  _LISTDATAPRODUCTSRESPONSE._serialized_start=744
  _LISTDATAPRODUCTSRESPONSE._serialized_end=888
  _CREATEDATAPRODUCTREQUEST._serialized_start=890
  _CREATEDATAPRODUCTREQUEST._serialized_end=1004
  _CREATEDATAPRODUCTRESPONSE._serialized_start=1006
  _CREATEDATAPRODUCTRESPONSE._serialized_end=1033
  _UPDATEDATAPRODUCTREQUEST._serialized_start=1036
  _UPDATEDATAPRODUCTREQUEST._serialized_end=1198
  _UPDATEDATAPRODUCTRESPONSE._serialized_start=1200
  _UPDATEDATAPRODUCTRESPONSE._serialized_end=1227
  _GETDATAPRODUCTREQUEST._serialized_start=1229
  _GETDATAPRODUCTREQUEST._serialized_end=1285
  _GETDATAPRODUCTRESPONSE._serialized_start=1288
  _GETDATAPRODUCTRESPONSE._serialized_end=1826
  _DELETEDATAPRODUCTREQUEST._serialized_start=1828
  _DELETEDATAPRODUCTREQUEST._serialized_end=1887
  _DELETEDATAPRODUCTRESPONSE._serialized_start=1889
  _DELETEDATAPRODUCTRESPONSE._serialized_end=1916
  _DATAPRODUCTSERVICE._serialized_start=1919
  _DATAPRODUCTSERVICE._serialized_end=3099
# @@protoc_insertion_point(module_scope)
