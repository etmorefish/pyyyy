# -*- coding: utf-8 -*-
# @Time    : 20-5-25 下午9:42
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : order.py
# @Software: PyCharm

from django.db import models


class Order(models.Model):
    """
    订单id自增 名称字符串 状态布尔 价钱浮点 数量整数 描述大文本  发布时间时间日期
    """
    order_id = models.AutoField(primary_key=True, help_text='id')
    order_name = models.CharField(max_length=150, help_text='订单名称')
    order_status = models.BooleanField(help_text='订单状态')
    order_price = models.FloatField(default=0.0, help_text='价钱')
    order_amount = models.IntegerField(max_length=10000000, help_text='订单数量')
    order_dec = models.TextField(help_text='订单描述')
    order_pubtime = models.DateField(help_text='发布时间')

    def __str__(self):
        return self.order_name


from django.views import View

class OrderView(View):
    def search_o(self):
        res = Order.objects.all()
        res = Order.objects.fillter(order_id = 4)
        return res
    def add_o(self):
        data = Order.objects.create(order_name='wahaha', order_status=True, order_price=300.0, order_amount=50, order_des='wahaha dec')
        return data
    def delete_o(self):
        res =  Order.objects.get(order_name='wahaha').delete()
        return res
    def update_o(self):
        res = Order.objects.get(order_name='wahaha').update(order_name='hongniu', order_price=900.0, order_amount=60)
        return res