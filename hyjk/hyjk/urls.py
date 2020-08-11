"""hyjk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from api import user as UserApi
from api import RtspDevice as RtspDevice

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/login', UserApi.userLogin, name="userLogin"),
    path("api/user/logout", UserApi.userLogout, name="userLogout"),
    path("api/user/add", UserApi.userInfoAdd, name="userInfoAdd"),
    path("api/user/modify", UserApi.userInfoModify, name="userInfoModify"),
    path("api/user/query", UserApi.userInfoQuery, name="userInfoQuery"),
    path("api/user/delete", UserApi.userInfoDelete, name="userInfoDelete"),

    path("api/rtsp/device/add", RtspDevice.rtspDeviceInfoAdd, name="rtspDeviceInfoAdd"),
    path("api/rtsp/device/batch/add", RtspDevice.rtspDeviceInfoBatchAdd, name="rtspDeviceInfoBatchAdd"),
    path("api/rtsp/device/modify", RtspDevice.rtspDeviceInfoModify, name="rtspDeviceInfoModify"),
    path("api/rtsp/device/query", RtspDevice.rtspDeviceInfoQueryAll, name="rtspDeviceInfoQuery"),
    path("api/rtsp/device/delete", RtspDevice.rtspDeviceInfoDelete, name="rtspDeviceInfoDelete"),

]
