from django.contrib import admin
from .models import Chat, Chatroom, Person

# Register your models here.
admin.site.register(Chat)
admin.site.register(Chatroom)
admin.site.register(Person)