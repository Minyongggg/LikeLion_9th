from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, related

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person")
    nickname = models.CharField(max_length=20, default=None)
    profile_img = models.ImageField(upload_to="profile_img", default='media/profile_img/codecademy1.jpg')
    # lecture = models.ManyToManyField(Lecture, through='Membership')
 


class Chatroom(models.Model):
    chatter1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatter1')
    chatter2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatter2')


class Chat(models.Model):
    From = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send_chats')
    To = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receive_chats')
    content = models.TextField()
    time = models.DateTimeField()
    read = models.BooleanField(default=False)
    room = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name='chats')
