"""Base class for HTTP connection interceptors.

"""

from __future__ import unicode_literals

from ..base import ExitCallInterceptor
from pythonagent.lang import str, urlparse


EXIT_HTTP =0
EXIT_SUBTYPE_HTTP = 'HTTP'

class HTTPConnectionInterceptor(ExitCallInterceptor):
    # If the library you are intercepting has an HTTPSConnection class which
    # does not subclass httplib.HTTPSConnection, add it to this set.
    https_connection_classes = set()
    backend_name_format_string = '%s://{HOST}:{PORT}{URL}?{QUERY STRING}'

    @classmethod
    def _request_is_https(cls, connection):
        #print("INSIDE IS REQUEST HTTPS")
        if connection.port == 443:
            return True
        return isinstance(connection, tuple(cls.https_connection_classes))

    def get_backend(self, host, port, scheme, url):
        #self.agent.logger.info('Modulename: HTTPConnectionInterceptor class get_backend function')
        parsed_url = urlparse(url)
        backend_properties = {
            'HOST': host,
            'PORT': str(port),
            'URL': parsed_url.path,
            'QUERY STRING': parsed_url.query,
        }
        return self.agent.backend_registry.get_backend(EXIT_HTTP, EXIT_SUBTYPE_HTTP, backend_properties,
                                                       self.backend_name_format_string % scheme)


from .httplib import intercept_httplib
from .urllib3 import intercept_urllib3
from .requests import intercept_requests
from .tornado_httpclient import intercept_tornado_httpclient
from .boto import intercept_boto

__all__ = ['intercept_httplib', 'intercept_urllib3', 'intercept_requests', 'intercept_tornado_httpclient', 'intercept_boto']

