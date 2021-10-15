"""message URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ##registration##
    path('registration/signup', views.signup, name="signup"),
    path('registration/login', views.login, name="login"),
    path('registration/logout', views.logout, name="logout"),


    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('chatlist', views.chatlist, name="chatlist"),
    path('makeroom/<int:friend_pk>', views.makeroom, name="makeroom"),
    path('chatroom/<int:room_pk>/<int:friend_pk>', views.chatroom, name="chatroom"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
