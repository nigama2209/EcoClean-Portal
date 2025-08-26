from django.urls import path # type: ignore
from . import views # type: ignore

urlpatterns = [
    path('',views.customer,name='customer'),
    path('profile/<str:un>',views.cprofile,name='profile'),
    path('servicelist/<str:un>',views.csl,name='servicelist'),
    path('details/<int:un>',views.cdetails,name='details'),
    path('orderlist/<str:un>',views.col,name='orderlist'),
    path('cart/<str:un>',views.cart,name='cart'),
 path('cart/<str:un>/delete/<str:bookingid>/', views.delete_cart_item, name='delete_cart_item'),
path('order-confirmation/<str:un>/', views.order_confirmation, name='order_confirmation'),

    path('booking/<str:un>',views.booking,name='booking'),
    path('history/<str:un>',views.chistory,name='history'),
    path('feedback/<str:un>',views.cfeedback,name="feedback"),
    path('feedbacklist/<str:un>',views.fblist,name='feedbacklist'),
    path("customlogout",views.customlogout,name="logout")
]