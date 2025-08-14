from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductEntry
from .serializers import ProductEntrySerializer
from django.db.models import Sum

class ProductEntryAPIView(APIView):
    def post(self, request):
        serializer = ProductEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Get product-wise summary
        product_summary = ProductEntry.objects.values('product').annotate(
            product_total=Sum('amount')
        ).order_by('product')

        # Calculate grand total
        grand_total = ProductEntry.objects.aggregate(
            grand_total=Sum('amount')
        )['grand_total'] or 0

        response_data = {
            'product_wise_summary': list(product_summary),
            'grand_total': grand_total
        }

        return Response(response_data)

