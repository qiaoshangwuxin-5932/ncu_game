from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from .models import User,Questions
import json as simplejson
from Gamer.check.checkscore import check
#题目
@csrf_exempt
def Choise(request):
    if request.method == "POST":
        req = simplejson.loads(request.body.decode('utf-8'))
        username=req['usrname']
        groups = req['groups']
        User.objects.filter(username=username).update(groups=groups)
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
@csrf_exempt
def ReturnImage(request):
    if request.method == 'POST':
        obj = User.objects
        d = os.path.dirname(__file__)
        req = simplejson.loads(request.body.decode('utf-8'))
        username = req['username']
        check(request,username)
        score = obj.filter(username=username,score__gte=85,score__lte=100).values('score')
        if not score:
            score = obj.filter(username=username,score__gte=70,score__lt=85).values('score')
            if not score:
                score = obj.filter(username=username, score__gte=65, score__lt=70).values('score')
                if not score:
                    '''只剩50~65了'''
                    image =os.path.join(d,"photo/50-65.jpg")
                    data = open(image, 'rb').read()
                    return HttpResponse(data,content_type='image/png')
                else:
                    image = os.path.join(d,"photo/65-70.jpg")
                    data = open(image, 'rb').read()
                    return HttpResponse(data, content_type='image/png')
            else:
                image = os.path.join(d,"photo/70-85.jpg")
                data = open(image, 'rb').read()
                return HttpResponse(data,content_type='image/png')
        else:
            image = os.path.join(d,"photo/50-65.jpg")
            data = open(image, 'rb').read()
            return HttpResponse(data, content_type='image/png')
'''
    d = os.path.dirname(__file__)
    image = os.path.join(d,"photo/image/Paper_Architecture_by_Dmitri_Popov.jpg")
    data = open(image,'rb').read()     # 读取图片
    return HttpResponse(data,content_type='image/png')
'''
@csrf_exempt
def ReturnImage2(request):
    if request.method == 'POST':
        obj = User.objects
        d = os.path.dirname(__file__)
        req = simplejson.loads(request.body)
        username = req['username']
        # username = request.GET.get('username')
        list = [50,65,70,85,100]
        list1 = [0,1,2,3,4]
        M = dict()
        lst = []
        for i in list1:
            if i == 100:
                i=i - 1
                score =obj.filter(username=username,score__gte=list[i],score__lt=list[i+1]).values('score')
                if score:
                    a = list[i]
                    b = list[i+1]
                    print(a,b)
            image = os.path.join(d,"photo/%s-%s.png"%(a,b))
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
        list = simplejson.loads(request.body.decode('utf-8'))
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

