from django.urls import path
from .views import ItemView, pay_with_kakao

urlpatterns = [path('', ItemView.as_view(), name='items'),
                path('kakaopay', pay_with_kakao, name='kakaopay')]