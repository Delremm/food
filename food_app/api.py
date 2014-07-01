import builtins
import json
import datetime

from rest_framework import views
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.conf import settings

from food_app.models import Menu
from food_app.serializers import MenuSerializer


def validate_item_to_add(item_to_add):
    ret = False
    if ('id' in item_to_add) and ('cals' in item_to_add):
        if type(item_to_add['id']) == builtins.int:
            if (type(item_to_add['cals']) == builtins.int) and (
                    settings.MIN_CALS_DELIVERY <= item_to_add[
                        'cals'] <= settings.MAX_CALS_DELIVERY):
                ret = True
    return ret


class AddToCartView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        if 'item_to_add' in request.GET:
            try:
                item_to_add = json.loads(request.GET['item_to_add'])
            except:
                return Response('', status=status.HTTP_400_BAD_REQUEST)
            if not validate_item_to_add(item_to_add):
                return Response('', status=status.HTTP_400_BAD_REQUEST)
            product_qs = Menu.objects.filter(id=item_to_add['id'])
            if product_qs:
                request.cart.add(
                    product_qs[0], data={'cals': item_to_add['cals']}, replace=False)
            return Response('')
        else:
            return Response('', status=status.HTTP_400_BAD_REQUEST)


class MenusByTypeView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        if 'date' in request.GET:
            date = request.GET['date']
        else:
            date = datetime.date.today() + datetime.timedelta(days=1)
        menus = [
            [
                MenuSerializer(Menu.objects.filter(
                    date=date,
                    menu_type=menu_type[0]), many=True).data,
                menu_type[1]] for menu_type in Menu.MENU_TYPE]
        return Response(menus)


class MenusView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        if 'date' in request.GET:
            date = request.GET['date']
        else:
            date = datetime.date.today() + datetime.timedelta(days=1)
        menus = MenuSerializer(Menu.objects.filter(
            date=date), many=True).data
        return Response(menus)


class OrderOptionsView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        order_options = {
            'order_cals_min': settings.MIN_CALS_DELIVERY,
            'order_cals_max': settings.MAX_CALS_DELIVERY,
        }
        return Response(order_options)


class CartView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        cart = request.cart
        ret = [{
            'price': round(cart_line.product.price.net*cart_line.data['cals']),
            'menu': MenuSerializer(cart_line.product).data,
            'quantity': cart_line.quantity,
            'cals': cart_line.data['cals']} for cart_line in cart]
        return Response(ret)


class ClearCartView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        cart = request.cart
        cart.clear()
        request.cart = cart
        return Response('')
