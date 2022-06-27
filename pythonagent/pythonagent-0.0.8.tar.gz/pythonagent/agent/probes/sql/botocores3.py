
"""Interceptor for httplib/http.client.

"""

from __future__ import unicode_literals
from ..base import ExitCallInterceptor
import time
from pythonagent.utils import get_current_timestamp_in_ms
#from functools import wraps
# from agent.internal.proxy import *




# import agent
class BotocoreS3Interceptor(ExitCallInterceptor):
    #print('inside botocore client interceptor class inside botos3')

    def _cav_s3_make_request(self, make_request, Endpoint, operation_model, request_dict):#, _agent):
        #agent = _agent
        self.agent.logger.info('operation model inside s3 make request {}'.format(operation_model))
        self.agent.logger.info('operation model with extracted operation name {}'.format(operation_model.name))
        method_name = 'botocore.endpoint' + str(operation_model)
        query_string = operation_model.name
        #start_time = time.time_ns() // 1000000
        start_time = get_current_timestamp_in_ms()
        url = request_dict["url"]
        self.agent.method_entry_http_callout(0, method_name, query_string, url)
        endpiont_method = make_request(Endpoint, operation_model, request_dict)


        try:
            #end_time = time.time_ns() // 1000000
            end_time = get_current_timestamp_in_ms()
            duration = end_time - start_time
            self.agent.method_exit_http_callout(0, method_name, "s3", 200, duration)

        except Exception as e:
            self.agent.logger.error("Some error occurred inside wrapper in method exit call {}".format(e))

        self.agent.logger.info('request_dict inside s3 make request {}'.format(request_dict))
        return endpiont_method

def intercept_s3(agent, mod):
    #print("DIR for mod DIR", mod)
    #interceptor = BotocoreClientInterceptor(agent, mod.ClientCreator)
    interceptor = BotocoreS3Interceptor(agent, mod.Endpoint)
    interceptor.attach('make_request', patched_method_name='_cav_s3_make_request')