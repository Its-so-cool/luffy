# 短信应用 SDK AppID
appid = 1400401608  # SDK AppID 以1400开头
# 短信应用 SDK AppKey
appkey = "c92d2705700fe5026c0c4f2b5b058329"
# 需要发送短信的手机号码
phone_numbers = ["13162888238"]
# 短信模板ID，需要在短信控制台中申请
template_id = 670796  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
sms_sign = "我们的目标是星辰大海啊"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
ssender = SmsSingleSender(appid, appkey)
params = ["5678"]  # 当模板没有参数时，`params = []`
try:
  result = ssender.send_with_param(86, phone_numbers[0],
      template_id, params, sign=sms_sign, extend="", ext="")
  print(result)
except HTTPError as e:
  print(e)
except Exception as e:
  print(e)
