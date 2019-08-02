
'''
from django.shortcuts import render, HttpResponse, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
import os
from ..models import User,Questions,ScoreLevel

def level(request):
# 1 研发
    A = 20;B = 15;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=1)
    # 2
    A = 10;B = 20;C = 15
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=2)
    # 3
    A = 20;B = 15;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=3)
    # 4
    A = 15;B = 10;C = 20
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=4)
    # 5
    A = 10;B = 15;C = 20
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=5)
    # 6  产品
    A = 15;B = 20;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=6)
    # 7
    A = 15;B = 10;C = 20
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=7)
    # 8
    A = 15;B = 20;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=8)
    # 9
    A = 10;B = 15;C = 20
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=9)
    # 10
    A = 15;B = 10;C = 20
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=10)
    # 11  设计
    A = 20;B = 15;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=11)
    # 12
    A = 20;B = 15;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=12)
    # 13
    A = 15;B = 10;C = 20
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=13)
    # 14
    A = 20;B = 15;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=14)
    # 15
    A = 20;B = 15;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=15)
    # 16 运营
    A = 20;B = 15;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=16)
    # 17
    A = 20;B = 10;C = 15
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=17)
    # 18
    A = 20;B = 10;C = 15
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=18)
    # 19
    A = 20;B = 15;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=19)
    # 20
    A = 15;B = 10;C = 20
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=20)
    # 21
    A = 10;B = 15;C = 20
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=21)
    # 22
    A = 10;B = 15;C = 20
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=22)
    # 23
    A = 10;B = 20;C = 15
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=23)
    # 24
    A = 10;B = 20;C = 15
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=24)
    # 25
    A = 20;B = 15;C = 10
    ScoreLevel.objects.create(A=A,B=B,C=C,answer_id=25)
    return HttpResponse('WWW')
    '''