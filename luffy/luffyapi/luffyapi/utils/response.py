from  rest_framework.response import Response

# 自定义response
class APIResponse(Response):
    def __init__(self,code=1,msg='成功',data=None,
                 status=None,headers=None,content_type=None,
                 **kwargs):
        dic={'code':code,'msg':msg}
        if data:
            dic['data']=data
        dic.update(kwargs)
        super().__init__(data=dic,status=status,headers=headers,content_type=content_type)