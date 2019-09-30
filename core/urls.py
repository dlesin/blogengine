from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home_view_url'),
    path('category/<slug>/', CategoryDetailView.as_view(), name='category_detail_url'),
    path('post/<slug>/', PostDetailView.as_view(), name='post_detail_url'),
    path('contacts/', ContactView.as_view(), name='contacts_view_url'),
]









    # path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart_url'),
    # path('remove_from_cart/', RemoveFromCartView.as_view(), name='remove_from_cart_url'),
    # path('change_item_qty/', ChangeItemQtyView.as_view(), name='change_item_qty_url'),
    # path('order/', OrderView.as_view(), name='order_view_url'),
    # path('thanks/', ThanksView.as_view(), name='thanks_view_url'),
    # #path('checkout/', checkout_view, name='checkout_view_url'),
    # #path('make_order/', make_order_view, name='make_order_view_url'),

