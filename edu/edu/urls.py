"""edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('ind/', views.ind,name='ind'),
    path('abc/', views.abc,name='abc'),
    path('show/', views.show,name='show'),
    path('veh/' ,views.veh ,name='veh'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('dele/<int:id>',views.dele,name='dele'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('djangoform/',views.djangoform,name='djangoform'),
    path('sport/',views.sport,name='sport'),
    path('move/<int:id>',views.move,name='move'),
    path('change/<int:id>',views.change,name='change'),


    





]
