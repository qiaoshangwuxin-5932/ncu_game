from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import View
from django.db.models import F
from django.utils.decorators import method_decorator
import os,json
from django.core.serializers import serialize
from .models import User,Questions
import json as simplejson






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




@csrf_exempt
def index(request):
    req = simplejson.loads(request.body)
    username = req['username']
    question = req['question']
    answer = req['answer']
    groups = req['groups']
    score = User.objects.filter(username=username).values('score')
    complete = Questions.objects.filter(groups=groups, question=question).values('scorelevel__f(answer)') #% (answer)  # 或者'{0}{1}' .format(xx,cat)
    for a in complete:
        print(a)
        a = a['scorelevel__A']
        print(a)
        for score in score:
            score = score['score']
            if complete:
                a = str(a)
                User.objects.update(username=username,score=F('score')+a)
                M = User.objects.filter(username=username).values('score')
                print(M)
                return HttpResponse('dwad')
    # for i in range(5):
    #     oneQ = question[i]
    #     score = 0
    #     complete = Questions.objects.filter(groups=groups, question=oneQ).values('level__%s') % (answer)  # 或者'{0}{1}' .format(xx,cat)
    #     for a in complete:
    #         a = score + a
    #         return a
    # score = a
    # User.objects.create_or_update(username=username, score=score)
    # score = User.objects.filter(username=username, ).values('score')
    # for a in score:
    #     print(f"{a}")
    #     return a
    # pass
#题目
def Choise(request):
    if request.method == "POST":
        if 1>0:
            req = simplejson.loads(request.body)
            groups = req['groups']
            question = Questions.objects.filter(groups=groups).values('id', 'question', 'option1', 'option2', 'option3')
            if question:
                list = [0, 1, 2, 3, 4]
                d = dict()
                for i in list:
                    oneQ = question[i]
                    d[i] = {
                        'status': 1,
                        'question': i+1,
                        'data':{
                                'id': oneQ['id'],
                                'data': {
                                    'question': oneQ['question'],
                                    'A': oneQ['option1'],
                                    'B': oneQ['option2'],
                                    'C': oneQ['option3'],
                                }
                        }
                    }
            return JsonResponse(d)



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
    list = [50,65,70,85,100]
    list1 = [0,1,2,3,4]
    for i in list1:
        score =obj.filter(username=username,score__gte=list[i],score__lt=list[i+1]).values('score')
        if score is not None:
            print(i)
            print(score)
            return i
        image = os.path.join(d,"photo/%s-$s") %(list[i],list[i+1])
        data = open(image,'rb').read()
        return HttpResponse(data,content_type='image/png')
        # score = obj.filter(username=username,score__gte=85,score__lte=100).values('score')



#九宫格
@csrf_exempt
def nine(request):

    if request.method == 'POST':
        d = os.path.dirname(__file__)
        nineAnswer = [1,2,3,4,5,6,7,8,9]
        # list = request.POST.getlist('list[]') # 数组名字
        list = simplejson.loads(request.body)
        print(list)
        if list == nineAnswer:
            image = os.path.join(d, "photo/myheart.jpg")
            data = open(image, 'rb').read()  # 读取图片
            return HttpResponse(data, content_type='image/png')
        else:
            return JsonResponse(
                {
                    'status':0,
                    'success':False,
                    'message':'你的拼图有错误哦'
                },
                json_dumps_params={'ensure_ascii': False}
            )

