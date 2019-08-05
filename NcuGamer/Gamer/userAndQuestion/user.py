# 用户
from Gamer.models import User
import json as simplejson
from django.views.generic import View
from django.http import JsonResponse

class Username(View):
    # username
    def post(self,request,*args,**kwargs):
        # username = request.POST.get('username')
        req = simplejson.loads(request.body)
        username = req['username']
        complete = User.objects.filter(username=username)
        if not complete:
            User.objects.create(username=username)
            a = {'success': True,"status":1}
            return JsonResponse(a)
        else:
            msg = "用户已重复,请更换注册名字"
            return JsonResponse(
                {
                    "status":0,
                    "success":False,
                    "message":msg,
                },
                json_dumps_params={'ensure_ascii': False}
            )