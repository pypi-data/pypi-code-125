"""Base interceptor for distributed caches (typically, key-value stores).

"""

from __future__ import unicode_literals

#from appdynamics.agent.models.exitcalls import EXIT_CACHE, EXIT_SUBTYPE_CACHE
from ..base import ExitCallInterceptor

EXIT_CACHE= 1
EXIT_SUBTYPE_CACHE ='CACHE'
class CacheInterceptor(ExitCallInterceptor):
    """Base class for cache interceptors.

    Extra Parameters
    -----------------
    vendor : string
        The vendor name of this cache backend e.g. MEMCACHED.

    """

    backend_name_format_string = '{SERVER POOL} - {VENDOR}'

    def __init__(self, agent, cls, vendor):
        self.vendor = vendor
        super(CacheInterceptor, self).__init__(agent, cls)

    def get_backend(self, server_pool):
        """

        Parameters
        ----------
        server_pool : list of str

        """
        self.agent.logger.info('Modulenam CacheInterceptor class inside get_backend') 
        backend_properties = {
            'VENDOR': self.vendor,
            'SERVER POOL': '\n'.join(server_pool),
        }
        self.agent.logger.info("Modulenam CacheInterceptor class inside get_backend backend_properties is {0}".format(backend_properties))
        return self.agent.backend_registry.get_backend(EXIT_CACHE, EXIT_SUBTYPE_CACHE, backend_properties,self.backend_name_format_string)
        # return None


from .redis import intercept_redis


__all__ = ['intercept_redis']

