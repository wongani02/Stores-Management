from django.shortcuts import render
from rest_framework import generics

from procurement.models import *
from .serializer import *

from rest_framework import generics
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView


class CreateRFQAPIView(generics.CreateAPIView):
    queryset = RFQ.objects.all()
    serializer_class = RFQSerializer


class OpenRFQsAPIView(generics.ListAPIView):
    queryset = RFQ.objects.filter(closing_date__gte=timezone.now()) | RFQ.objects.filter(closing_date__isnull=True)
    serializer_class = RFQSerializer


class ApplyToRFQAPIView(generics.CreateAPIView):
    queryset = RFQbid.objects.all()
    serializer_class = RFQbidSerializer



class ProcurementChoiceView(generics.ListAPIView):
    queryset = ProcurementChoice.objects.all()
    serializer_class = ProcurementChoiceSerializer


class TenderNoticeView(generics.ListAPIView):
    queryset = TenderNotice.objects.all()
    serializer_class = TenderNoticeSerializer


class BidView(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class ContractView(generics.ListAPIView):
    queryset = ProcurementChoice.objects.all()
    serializer_class = ContractSerializer


class ProcurementProcessView(generics.ListAPIView):
    queryset = ProcurementProcess.objects.all()
    serializer_class = ProcurementProcessSerializer


class PublicProcurementActView(generics.ListAPIView):
    queryset = PublicProcurementAct.objects.all()
    serializer_class = PublicProcurementActSerializer




class InventoryMetricsView(APIView):
    def post(self, request, *args, **kwargs):
        inventory_metrics_data = request.data.get('inventory_metrics')

        if inventory_metrics_data:
            # Perform actions with the inventory metrics data
            # For example, you can save it to a database
            # Replace this part with your actual processing logic

            return Response({'message': 'Inventory metrics data received and processed successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid or missing inventory metrics data in the request.'}, status=status.HTTP_400_BAD_REQUEST)
        


class ProductSkuDictView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch data to populate the product_sku_dict
        # Replace this part with your actual logic to fetch and format data

        fetched_data = {
            '1': ['772559868266', 'Medicine'],
            '2': ['566540807600', 'Fertilizer'],
            '3': ['357685595552', 'Maize'],
            # Add more data as needed
        }

        return Response({'product_sku_dict': fetched_data}, status=status.HTTP_200_OK)