from django.urls import path
from .views import (
    CheckoutView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_product_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)

app_name = 'cart'


urlpatterns = [
    #path('' , cartView.as_view() , name='cart') ,
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-product-from-cart/<slug>/', remove_single_product_from_cart,
         name='remove-single-product-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
  
]

