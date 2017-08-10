from django.shortcuts import get_object_or_404
from  rest_framework.views import APIView
from  rest_framework.response import Response
from  rest_framework import status
from  .models import Stock
from .serializers import StockSerializer

# list of all stocks or create a new one
# stocks/AMZ/

class StockList(APIView):


    def get(self,request):
        stocks= Stock.objects.All()
        serializer= StockSerializer(stocks,many=True)
        return Response(serializer.data)

    def post(self):
        pass

