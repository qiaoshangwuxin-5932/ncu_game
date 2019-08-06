from django.http import  JsonResponse
import json as simplejson
from Gamer.views import User,Questions
import random
 # 检测

def check(request,username):
    check_score = User.objects.filter(username=username).values('score')
    for a in check_score:
        check_score = a['score']
        if check_score > 100:
            score = random.randint(50,100)
            User.objects.filter(username=username).update(score=score)


