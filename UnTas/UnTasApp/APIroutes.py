from django.conf.urls import url
from django.contrib import admin
from UnTasApp.controllers import controller, address, discount, item, itemCategory,\
								 order, sales, stock, customer 


urlpatterns = [
#ROOT-----------------------------------------------------------------------------------------------------
	url(r'^$', controller.api_root),
#ADDRESS--------------------------------------------------------------------------------------------------
	url(r'^address$',address.addressRequest, name="address"),
	url(r'^address/(?P<pk>[0-9]+)$', address.singleAddressRequest, name="address-detail"),
#DISCOUNT-------------------------------------------------------------------------------------------------
	url(r'^discount$', discount.discountRequest, name="discount"),
	url(r'^discount/(?P<pk>[0-9]+)$', discount.singleDiscountRequest, name="discount-detail"),
#ITEM-----------------------------------------------------------------------------------------------------
	url(r'^item$', item.itemRequest, name="item"),   
	url(r'^item/(?P<pk>[0-9]+)$', item.singleItemRequest, name="item-detail"),
#CATEGORY-------------------------------------------------------------------------------------------------
	url(r'^itemCategory$',itemCategory.itemCategoryRequest, name='category'),   
	url(r'^itemCategory/(?P<pk>[0-9]+)$', itemCategory.singleItemCategoryRequest, name="category-detail"),
#ORDER----------------------------------------------------------------------------------------------------   
	url(r'^order$', order.orderRequest, name="order"),
	url(r'^order/(?P<pk>[0-9]+)$', order.singleOrderRequest, name="order-detail"),
#SALES----------------------------------------------------------------------------------------------------
	url(r'sales$', sales.salesRequest, name="sales"),
	url(r'^sales/(?P<pk>[0-9]+)$', sales.singleSaleRequest, name="sales-detail"),
#STOCK----------------------------------------------------------------------------------------------------
	url(r'stock$', stock.stockRequest, name="stock"),
	url(r'stock/(?P<pk>[0-9]+)$', stock.singleStockRequest, name="stock-detail"),
#CUSTOMER-------------------------------------------------------------------------------------------------
	url(r'customer$', customer.customerRequest, name="customer"),
	url(r'customer/(?P<pk>[0-9]+)$', customer.singleCustomerRequest, name="customer-detail"),
   ]