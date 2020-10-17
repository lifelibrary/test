from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Item
import requests
class ItemView(ListView):
    # def as_view()
    model = Item
    template_name = 'home.html'

def pay_with_kakao(request):
    '''
    POST /v1/payment/ready HTTP/1.1,
    Host: kapi.kakao.com,
    Authorization: KakaoAK {APP_ADMIN_KEY},
    Content-type: application/x-www-form-urlencoded;charset=utf-8
    '''
    headers = { 'Authorization': 'KakaoAK efcfe9ef3d158b23e63a1d391560fb58',
                'Accept': 'application/json;charset=UTF-8',
                'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    url = 'https://kapi.kakao.com/v1/payment/ready'
    params = {
        'cid':'TC0ONETIME',
        'partner_order_id':'1',
        'partner_user_id':"2",
        'item_name':'wow',
        'quantity': 3,
        'total_amount': 10,
        'tax_free_amount':1,
        'approval_url':'http://localhost:8000/admin', #결제 완료시 여기에 pgtoken보내줌
        'cancel_url':'http://localhost:8000',
        'fail_url':'http://localhost:8000',

        
        }
    res = requests.post(url, headers=headers, data=params)
    res_json = res.json()
    pc_url = res_json['next_redirect_pc_url']

    return redirect(pc_url)

    pay_url = 'https://kapi.kakao.com/v1/payment/approve'
    pay_params = {
        'cid':'TC0ONETIME',
        'tid': res_json['tid'],
        'partner_order_id':'1',
        'partner_user_id':"2",
        'pg_token': "a"


    }