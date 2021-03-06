from rest_framework.views import exception_handler
from .response import APIResponse
from .logger import log

def common_exception_handler(exc, context):
    log.error('views:%s 错误是%s' %(context['view'].__class__.__name__,str(exc)))
    ret = exception_handler(exc, context)
    if not ret:
        # 判断错误类型 报对应的错
        return APIResponse(code=0, msg='error', data=str(exc))
    else:
        return APIResponse(code=0, msg='error', data=ret.data)
