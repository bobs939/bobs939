from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse,JsonResponse

# Create your views here.
def tableview(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM devices")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return JsonResponse({'data': data})

# appname/views.py
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.db import connection

# from .serializer import DeviceSerializer

# @api_view(['GET'])
# def devices_list(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM devices")
#         data = [dict(zip(cursor.description, row)) for row in cursor.fetchall()]
#     serializer = DeviceSerializer(data, many=True)
#     return Response({'data': serializer.data})
