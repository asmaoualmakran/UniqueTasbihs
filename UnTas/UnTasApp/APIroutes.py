from django.conf.urls import url
from django.contrib import admin
from UnTasApp.controllers import controller, address, discount, item, itemCategory,\
								 order, sales, stock, customer 


urlpatterns = [
#ROOT-----------------------------------------------------------------------------------------
	url(r'^$', controller.api_root),
#ADDRESS--------------------------------------------------------------------------------------
	url(r'^address$',address.addressRequest, name="address"),
	url(r'^address/(?P<pk>[0-9]+)$', address.singleAddressRequest, name="address-detail"),
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
#STOCK
	url(r'stock$', stock.stockRequest, name='stock'),
#CUSTOMER
	url(r'customer$', customer.customerRequest, name='customer'),
   ]