"""Cyber_Hacking_Breaches URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from Cyber_Admins import views as admin_view
from Cyber_Users import views as user_view

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$',user_view.user_login, name='user_login'),
    url(r'^user_register/$',user_view.user_register,name='user_register'),
    url(r'^user_adddata/$',user_view.user_adddata,name='user_adddata'),
    url(r'^user_page/$',user_view.user_page,name='user_page'),
    url(r'^malware/$',user_view.malware,name='malware'),
    url(r'^unmalware/$',user_view.unmalware,name='unmalware'),
    url(r'^breaches_analysis/$',user_view.breaches_analysis,name='breaches_analysis'),
    url(r'chart_page/(?P<chart_type>\w+)', user_view.chart_page, name="chart_page"),


    url(r'^admin_login/$',admin_view.admin_login, name='admin_login'),
    url(r'^user_details/$',admin_view.user_details, name='user_details'),
    url(r'^admin_analysis/$',admin_view.admin_analysis, name='admin_analysis'),
    url(r'^achart_page/(?P<achart_type>\w+)', admin_view.achart_page, name="achart_page"),




]
