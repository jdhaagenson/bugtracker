"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from customuser.views import login_view, user_details, logout_user
from bugtrack.views import main, complete, invalidate, assign, edit_ticket, create_ticket, ticket_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_user, name='logout_user'),
    path('new/', create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/edit/', edit_ticket, name='edit_ticket'),
    path('ticket/<int:ticket_id>/invalidate/', invalidate, name='invalidate'),
    path('ticket/<int:ticket_id>/complete/', complete, name='complete'),
    path('ticket/<int:ticket_id>/assign/', assign, name='assign'),
    path('ticket/<int:ticket_id>', ticket_details, name='ticket_details'),
    path('user/<int:userid>', user_details, name='user_details'),
