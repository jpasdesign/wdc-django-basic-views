"""django_basic_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django_basic_views import views

urlpatterns = [
    path('admin/', admin.site.urls),

    ##################
    # Your URLs here #
    ##################

    path('hello-world/', views.hello_world, name='hello-world'),
    path('date/', views.current_date, name='current_date'),
    path('my-age/<int:year>/<int:month>/<int:day>', views.my_age, name='my-age'),
    path('next-birthday/<birthday>/', views.next_birthday, name='next_birthday'),
    path('profile/', views.profile, name='profile'),
]
