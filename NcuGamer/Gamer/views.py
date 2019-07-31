from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
import os
from django.core.serializers import serialize
from .models import User,Questions
import json as simplejson
import json


class Username(View):
    # username
    def post(self,request,*args,**kwargs):
        received_data = json.load(request.body.decode('utf-8'))
        username = received_data['username']
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
                }
            )




def Choise(self,request,*args,**kwargs):
    pass
    Post = request.POST
    if request.method == 'POST':
        username = Post.get('username')
        getGroup = Post.get('group')
        value = getGroup.group
        question = Questions.objects.filter(group=value).values('id','question','option1','option2','option3')
        list = [0,1,2,3,4]
        for i in list:
            oneQ = question[i]
                # request_news = [a for a in question]
                # print(request_news)
            return JsonResponse(
                {
                    'status':1,
                    'question':i,
                    'data':{
                        'id':oneQ.id,
                        'question':oneQ.question,
                        'option1':oneQ.option1,
                        'option2':oneQ.option2,
                        'option3':oneQ.option3,
                    }
                }
            )
        for i in list:
            oneQ = question[i]
            req = simplejson.loads(request.raw_post_data)
            score = 0
            responce = []
            data = req['data']
            answer = data[i]['answer']
            complete = Questions.objects.filter(group=value,question=oneQ).values('level__%s').format(answer)
            for a in complete:
                a = score+a
                return a
        score = a
        User.objects.create_or_update(username=username,score=score)
        score =User.objects.filter(username=username,).values('score')
        for a in score:
            print(f"{a}")
            return a


'''

'''
#  返回图片
def ReturnImage(request):
    obj = User.objects
    d = os.path.dirname(__file__)
    username = request.GET.get('username')
    score = obj.filter(username=username,score__gte=85,score__lte=100).values('score')
    if not score:
        score = obj.filter(username=username,score__gte=70,score__lt=85).values('score')
        if not score:
            score = obj.filter(username=username, score__gte=65, score__lt=70).values('score')
            if not score:
                '''只剩50~65了'''
                image =os.path.join(d,"photo/50-65.png")
                data = open(image, 'rb').read()
                return HttpResponse(data,content_type='image/png')
            else:
                image = os.path.join(d,"photo/65-70.png")
                data = open(image, 'rb').read()
                return HttpResponse(data, content_type='image/png')
        else:
            image = os.path.join(d,"photo/70-85.png")
            data = open(image, 'rb').read()
            return HttpResponse(data,content_type='image/png')
    else:
        image = os.path.join(d,"photo/85-100.png")
        data = open(image, 'rb').read()
        return HttpResponse(data, content_type='image/png')
'''
    d = os.path.dirname(__file__)
    image = os.path.join(d,"photo/image/Paper_Architecture_by_Dmitri_Popov.jpg")
    data = open(image,'rb').read()     # 读取图片
    return HttpResponse(data,content_type='image/png')
'''
def ReturnImage2(request):
    obj = User.objects
    d = os.path.dirname(__file__)
    username = request.GET.get('username')

    score = obj.filter(username=username,score__gte=85,score__lte=100).values('score')




@csrf_exempt
def nine(request):
    pass

    if request.method == 'POST':
        d = os.path.dirname(__file__)
        nineAnswer = [1,2,3,4,5,6,7,8,9]
        list = request.POST.getlist('list[]') # 数组名字
        if list == nineAnswer:
            image = os.path.join(d, "photo/myheart.jpg")
            data = open(image, 'rb').read()  # 读取图片
            return HttpResponse(data, content_type='image/png')



