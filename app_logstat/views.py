from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import pclog
from .serializers import pclogserializers

class pclogListApiView(APIView):
    # # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]


    # def get(self, request, *args, **kwargs):
    #     pclogs = pclog.objects.all()
    #     serializer = pclogserializers(pclogs, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        data = {
            'date': request.data.get('date'),
            'pc': request.data.get('pc'),
            'ip': request.data.get('ip'),
            'user': request.data.get('user'),
            'app_name': request.data.get('app_name'),
            'app_title': request.data.get('app_title'),
            'open_time': request.data.get('open_time'),
        }

        serializer = pclogserializers(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)