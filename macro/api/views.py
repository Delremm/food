from rest_framework import views
from rest_framework.response import Response
from rest_framework import permissions
from django.conf import settings


class MacroDataView(views.APIView):

    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        macro_data = settings.FORMEAL_CONF['MACRO']
        return Response(macro_data)
