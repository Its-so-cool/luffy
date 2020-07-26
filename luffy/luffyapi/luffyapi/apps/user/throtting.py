
from rest_framework.throttling import SimpleRateThrottle
class SMSThrotting(SimpleRateThrottle):
    scope = 'sms'
    def get_cache_key(self, request, view):
        phone = request.data.get('phone')
        #'throttle_%(scope)s_%(ident)s'
        return self.cache_format%{'scope':self.scope,'ident':phone}