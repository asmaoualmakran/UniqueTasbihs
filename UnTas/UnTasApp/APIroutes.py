from django.conf.urls import url
from django.contrib import admin
from UnTasApp.controllers import controller
from UnTasApp.controllers import address


urlpatterns = [
#ROOT-----------------------------------------------------------------------------------------
	url(r'^$', controller.api_root),
#ADDRESS--------------------------------------------------------------------------------------
    url(r'^address$',address.addressRequest, name="address"),

   ]