from rest_framework import views
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.conf import settings

import json


class AddToCartView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        if 'item_to_add' in request.GET:
            try:
                item_to_add = json.loads(request.GET['item_to_add'])
                print(item_to_add)
            except:
                return Response('', status=status.HTTP_400_BAD_REQUEST)
            if 'cart' in request.session:
                request.session['cart'].append(item_to_add)
            else:
                request.session['cart'] = [item_to_add, ]
            print('item added')
            return Response('')
        else:
            return Response('', status=status.HTTP_406_NOT_ACCEPTABLE)
