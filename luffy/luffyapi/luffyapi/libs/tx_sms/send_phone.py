from qcloudsms_py import SmsSingleSender
from luffyapi.utils.logger import log
from . import settings


def get_code():
    import random
    code = ''
    for i in range(4):
        code+=str(random.randint(0,9))
    return code

def send(phone,code):
    ssender = SmsSingleSender(settings.appid, settings.appkey)
    params = [code,5]  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86, phone,settings.template_id, params, sign=settings.sms_sign, extend="", ext="")
        if result.get('result')==0:
            return True
        else:
            return False
    except Exception as e:
        log.error(f'手机号{phone},短信发送失败{str(e)}')
