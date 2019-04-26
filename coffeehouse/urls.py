"""coffeehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
#
# from django.conf.urls import url
# from django.contrib import admin
#
# from css import views
# from css.views import hello
# from css.views import current_datetime
# from css.views import home_page
# from css.views import about_info
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^hello/$', hello),
#     url(r'^thetime/$', current_datetime),
#     url(r'^$', home_page),
#     url(r'^aboutinfo/$', about_info),
#     url(r'^teachers', views.teachers, name='teachers'),
# ]

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('about.urls')),
]