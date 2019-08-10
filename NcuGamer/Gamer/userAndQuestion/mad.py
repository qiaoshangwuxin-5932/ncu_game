from Gamer.models import User
from django.http import JsonResponse


#  恶心的简单判断
def mad(b,username,answer,groups):
    if b == 'one':
        User.objects.filter(username=username).update(one=answer, groups=groups)
    elif b == 'two':
        User.objects.filter(username=username).update(two=answer, groups=groups)
    elif b == 'three':
        User.objects.filter(username=username).update(three=answer, groups=groups)
    elif b == 'four':
        User.objects.filter(username=username).update(four=answer, groups=groups)
    elif b == 'five':
        User.objects.filter(username=username).update(four=answer, groups=groups)