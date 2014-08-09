from django.shortcuts import render
from django.http import HttpResponse
import json

from schoolbus.models import Teacher, Group, User, Profile

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the SchoolBus index.")

def profile(request, profile_id):
    p = Profile.objects.get(id=profile_id)
    return HttpResponse("You're looking at profile '%s'." % p.name)

def profiles(request, group_uuid):
    profiles = Profile.objects.filter(group__uuid=group_uuid)
    output = ''
    for p in profiles:
        output += "Name: '%s' (%d %d), " % (p.name, p.level_min, p.level_max)

    return HttpResponse(output)

def getProfileByLogin(request, teacher_uuid, login):
    user = User.objects.get(group__teacher__uuid=teacher_uuid, login=login)
    p = user.group.profile
    output = '{"name": "%s", "level_min":%d, "level_max":%d}' % (p.name, p.level_min, p.level_max)
    return HttpResponse(output)
