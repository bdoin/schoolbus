from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid

class Teacher(models.Model):
    uuid = models.CharField(max_length=32, blank=True, unique=True)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

@receiver(pre_save, sender=Teacher)
def teacher_pre_save(sender, **kwargs):
    if(not kwargs['instance'].pk):
        kwargs['instance'].uuid = uuid.uuid4().hex

class Profile(models.Model):
    name = models.CharField(max_length=60)
    level_min = models.IntegerField(default=1)
    level_max = models.IntegerField(default=6)

    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=60)
    parent = models.ForeignKey('self', null=True, blank=True)
    teacher = models.ForeignKey(Teacher)
    profile = models.ForeignKey(Profile)

    def __unicode__(self):
        return self.name

    def get_all_children(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Group.objects.filter(parent=self):
            r.append(c.get_all_children(include_self=False))
        return r

    def get_top_level_group(self):
        if self.parent:
            return self.parent.get_top_level_group()
        else:
            return self


class User(models.Model):
    name = models.CharField(max_length=100, blank=True)
    login = models.CharField(max_length=100, unique=True)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.login

    def get_top_level_group(self):
        return self.group.get_top_level_group()

