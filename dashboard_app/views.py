from django.http import JsonResponse
from django.shortcuts import render
from .models import YourModel
from .serializers import DataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


def get():
    queryset = YourModel.objects.all()
    serializer = DataSerializer(queryset, many=True)
    return Response(serializer.data)


class DataAPIView(APIView):
    pass


def dashboard_view(request):
    return render(request, 'dashboard_app/home.html')


def my_view(request):
    return render(request, 'dashboard_app/template2.html')


def api_data_view():
    # Fetch data from the database
    data = YourModel.objects.values()

    # Convert the QuerySet to a list
    data_list = list(data)

    # Return JSON response
    return JsonResponse(data=data_list, safe=False)


def item_detail_view():
    return None


def form_submit_view():
    return None


def login_view():
    return None


def logout_view():
    return None


def register_view():
    return None
