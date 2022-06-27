"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,spar,vault,pub,quant,fi,axp,afi,npo,bpm,fpo,others],v1:[fiab]
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from fds.analyticsapi.engines.api_client import ApiClient, Endpoint as _Endpoint
from fds.analyticsapi.engines.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from fds.analyticsapi.engines.model.calculation_status_root import CalculationStatusRoot
from fds.analyticsapi.engines.model.calculations_summary_root import CalculationsSummaryRoot
from fds.analyticsapi.engines.model.client_error_response import ClientErrorResponse
from fds.analyticsapi.engines.model.pub_calculation_parameters_root import PubCalculationParametersRoot


class PubCalculationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __cancel_calculation_by_id(
            self,
            id,
            **kwargs
        ):
            """Cancel Pub calculation by id  # noqa: E501

            This is the endpoint to cancel a previously submitted calculation.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.cancel_calculation_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Create and Run Pub calculation endpoint

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.cancel_calculation_by_id = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pub/v3/calculations/{id}',
                'operation_id': 'cancel_calculation_by_id',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__cancel_calculation_by_id
        )

        def __get_all_calculations(
            self,
            page_number=1,
            **kwargs
        ):
            """Get all calculations  # noqa: E501

            This endpoints returns all active calculation requests.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_all_calculations(page_number=1, async_req=True)
            >>> result = thread.get()

            Args:
                page_number (int): defaults to 1, must be one of [1]

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CalculationsSummaryRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['page_number'] = \
                page_number
            return self.call_with_http_info(**kwargs)

        self.get_all_calculations = _Endpoint(
            settings={
                'response_type': dict({ 200:(CalculationsSummaryRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pub/v3/calculations',
                'operation_id': 'get_all_calculations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page_number',
                ],
                'required': [
                    'page_number',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page_number':
                        (int,),
                },
                'attribute_map': {
                    'page_number': 'pageNumber',
                },
                'location_map': {
                    'page_number': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_all_calculations
        )

        def __get_calculation_parameters(
            self,
            id,
            **kwargs
        ):
            """Get Pub calculation parameters by id  # noqa: E501

            This is the endpoint that returns the calculation parameters passed for a calculation.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_calculation_parameters(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Create and Run Pub calculation endpoint

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PubCalculationParametersRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_calculation_parameters = _Endpoint(
            settings={
                'response_type': dict({ 200:(PubCalculationParametersRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pub/v3/calculations/{id}',
                'operation_id': 'get_calculation_parameters',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_calculation_parameters
        )

        def __get_calculation_status_by_id(
            self,
            id,
            **kwargs
        ):
            """Get Pub calculation status by id  # noqa: E501

            This is the endpoint to check on the progress of a previously requested calculation.  If the calculation has finished computing, the location header will point to the result url.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_calculation_status_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Create and Run Pub calculation endpoint

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CalculationStatusRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_calculation_status_by_id = _Endpoint(
            settings={
                'response_type': dict({ 200:(CalculationStatusRoot,), 202:(CalculationStatusRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pub/v3/calculations/{id}/status',
                'operation_id': 'get_calculation_status_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_calculation_status_by_id
        )

        def __get_calculation_unit_result_by_id(
            self,
            id,
            unit_id,
            **kwargs
        ):
            """Get Pub calculation result by id  # noqa: E501

            This is the endpoint to get the result of a previously requested calculation.  If the calculation has finished computing, the body of the response will contain the requested document in the specified format.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_calculation_unit_result_by_id(id, unit_id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Get Pub calculation status by id endpoint
                unit_id (str): from url, provided from the location header in the Get Pub calculation status by id endpoint

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                file_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            kwargs['unit_id'] = \
                unit_id
            return self.call_with_http_info(**kwargs)

        self.get_calculation_unit_result_by_id = _Endpoint(
            settings={
                'response_type': dict({ 200:(file_type,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pub/v3/calculations/{id}/units/{unitId}/result',
                'operation_id': 'get_calculation_unit_result_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'unit_id',
                ],
                'required': [
                    'id',
                    'unit_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'unit_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'unit_id': 'unitId',
                },
                'location_map': {
                    'id': 'path',
                    'unit_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/x-protobuf',
                    'application/pdf'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_calculation_unit_result_by_id
        )

        def __post_and_calculate(
            self,
            **kwargs
        ):
            """Create and Run Pub calculation  # noqa: E501

            This endpoint runs the Pub calculation specified in the POST body parameters.  It can take one or more units as input.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_and_calculate(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_fact_set_api_long_running_deadline (int): Long running deadline in seconds when only one unit is passed in the POST body.. [optional]
                cache_control (str): Standard HTTP header.  Accepts max-stale.. [optional]
                pub_calculation_parameters_root (PubCalculationParametersRoot): Calculation Parameters. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                (For 202 status - CalculationStatusRoot)(For 200 status - CalculationStatusRoot)(For 201 status - File)
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.post_and_calculate = _Endpoint(
            settings={
                'response_type': dict({ 202:(CalculationStatusRoot,), 200:(CalculationStatusRoot,), 201:(file_type,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pub/v3/calculations',
                'operation_id': 'post_and_calculate',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_fact_set_api_long_running_deadline',
                    'cache_control',
                    'pub_calculation_parameters_root',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_fact_set_api_long_running_deadline':
                        (int,),
                    'cache_control':
                        (str,),
                    'pub_calculation_parameters_root':
                        (PubCalculationParametersRoot,),
                },
                'attribute_map': {
                    'x_fact_set_api_long_running_deadline': 'X-FactSet-Api-Long-Running-Deadline',
                    'cache_control': 'Cache-Control',
                },
                'location_map': {
                    'x_fact_set_api_long_running_deadline': 'header',
                    'cache_control': 'header',
                    'pub_calculation_parameters_root': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/pdf',
                    'application/vnd.openxmlformats-officedocument.presentationml.presentation'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__post_and_calculate
        )

        def __put_and_calculate(
            self,
            id,
            **kwargs
        ):
            """Create or Update Pub calculation and run it.  # noqa: E501

            This endpoint updates and run the Pub calculation specified in the PUT body parameters. This also allows creating new Pub calculations with custom ids.  It can take one or more units as input.    Remarks:    *   Start and and end date must be within the configuration's min and max date range  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.put_and_calculate(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): from url, provided from the location header in the Create and Run Pub calculation endpoint

            Keyword Args:
                x_fact_set_api_long_running_deadline (int): Long running deadline in seconds when only one unit is passed in the PUT body.. [optional]
                cache_control (str): Standard HTTP header.  Accepts max-stale.. [optional]
                pub_calculation_parameters_root (PubCalculationParametersRoot): Calculation Parameters. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                (For 202 status - CalculationStatusRoot)(For 200 status - CalculationStatusRoot)(For 201 status - File)
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.put_and_calculate = _Endpoint(
            settings={
                'response_type': dict({ 202:(CalculationStatusRoot,), 200:(CalculationStatusRoot,), 201:(file_type,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pub/v3/calculations/{id}',
                'operation_id': 'put_and_calculate',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'x_fact_set_api_long_running_deadline',
                    'cache_control',
                    'pub_calculation_parameters_root',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'x_fact_set_api_long_running_deadline':
                        (int,),
                    'cache_control':
                        (str,),
                    'pub_calculation_parameters_root':
                        (PubCalculationParametersRoot,),
                },
                'attribute_map': {
                    'id': 'id',
                    'x_fact_set_api_long_running_deadline': 'X-FactSet-Api-Long-Running-Deadline',
                    'cache_control': 'Cache-Control',
                },
                'location_map': {
                    'id': 'path',
                    'x_fact_set_api_long_running_deadline': 'header',
                    'cache_control': 'header',
                    'pub_calculation_parameters_root': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/pdf'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__put_and_calculate
        )
