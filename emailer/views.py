from emailer.api import SubscriberSerializer
from emailer.models import Subscriber

from rest_framework import views
from rest_framework import permissions, authentication
from rest_framework.response import Response

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class CreateSubscriberApi(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        email = request.GET.get('email', None)
        subscriber = Subscriber.objects.filter(email=email).exists()
        if not subscriber:
            try:
                validate_email(email)
            except ValidationError as e:
                return Response({'success': False, 'message': 'Ошибка в email'})
            else:
                Subscriber.objects.create(email=email)
                return Response({
                    'success': True,
                    'message': 'Мы рады, что вы следите за нами. Мы постараемся сообщить вам на %s самое интересное.' % email})
        else:
            return Response({'success': True, 'message': 'Спасибо, вы уже подписаны.'})
