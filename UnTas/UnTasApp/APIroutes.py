from django.conf.urls import url
from django.contrib import admin
from UnTasApp.controllers import controller, address, discount, item, itemCategory, order, sales


urlpatterns = [
#ROOT-----------------------------------------------------------------------------------------
	url(r'^$', controller.api_root),
#ADDRESS--------------------------------------------------------------------------------------
	url(r'^address$',address.addressRequest, name="address"),
#DISCOUNT-------------------------------------------------------------------------------------
	url(r'^discounts$', discount.discountRequest, name="discount"),
#ITEM-----------------------------------------------------------------------------------------
	url(r'^items$', item.itemRequest, name="item"),   
#CATEGORY-------------------------------------------------------------------------------------
	url(r'^itemCategory$',itemCategory.itemCategoryRequest, name='category'),   
#ORDER----------------------------------------------------------------------------------------   
	url(r'^order$', order.orderRequest, name='order'),
#SALES----------------------------------------------------------------------------------------
	url(r'sales$', sales.salesRequest, name='sales'),
   ]