from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from.models import Business
from.serializers import BusinessSerializer
from django.db.models import Sum, Max
import pandas as pd
import numpy as np

# Create your views here.

class UploadBusinessExcel(APIView):
    def post(self, request):
        excel_file = request.FILES['office_file']
        df=pd.read_excel(excel_file)

        for _, row in df.iterrows():
            Business.objects.create(
                name=row['name'],
                revenue=row['revenue'],
                profit=row['profit'],
                employees=row['employees'],
                country=row['country'],
            )

        return Response({'message': 'Office file uploaded successfully'})
    
class ExcelDataView(APIView):    
    def get(self, request):
        businesses = Business.objects.all().values("id", "name", "revenue", "profit", "employees", "country")
        return Response(list(businesses))
    
class UpdateDeleteCompany(APIView):
    def get(self, request):
        businesses = Business.objects.all().values("id", "name", "revenue", "profit", "employees", "country")
        return Response(list(businesses))
    def put(self, request, id):
        """
        Update company details
        """
        company = get_object_or_404(Business, id=id)
        serializer = BusinessSerializer(company, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Delete a company
        """
        company = get_object_or_404(Business, id=id)
        company.delete()
        return Response({"message": "Company deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class BusinessStatistics(APIView):
    def get(self, request):
        business_data = Business.objects.values_list('name', 'revenue', 'profit', 'employees','country')
        np_data=np.array(list(business_data))

        #Convert numeric columns to float (skip first and last columns)
        np_data_numeric = np_data[:, 1:-1].astype(float)

        status={
            'mean' : np.mean(np_data_numeric, axis=1).tolist(),
            'std_deviation' : np.std(np_data_numeric, axis=1).tolist(),
            'median' : np.median(np_data_numeric, axis=1).tolist(),
        }
        return Response(status)
    
#All the companies in USA 
class USAnames(APIView):
    def get(self, request):
        usa_companies = Business.objects.filter(country='USA').values_list('name', flat=True)
        return Response({"companies": list(usa_companies)})
    
#profit > 20000
class Profit(APIView):
    def get(self, request):
       high_profit_companies = Business.objects.filter(profit__gt=20000).values_list('name', flat=True)
       return Response({"companies": list(high_profit_companies)})

#Total revenue for all companies
class TotalProfitView(APIView):
    def get(self, request):
         total_profit = Business.objects.aggregate(total=Sum('profit'))
         return Response({"total_profit": total_profit['total']})

    
class HighRevenueCompanies(APIView):
    def get(self, request):
        companies = Business.objects.filter(revenue__gt=50000).values_list('name', flat=True)
        return Response({"companies": list(companies)})
    
# Add a new company
class AddCompany(APIView):
    def post(self, request):
        serializer = BusinessSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Fetch the company with the highest revenue
class TopRevenueCompany(APIView):
    def get(self, request):
        company = Business.objects.order_by("revenue").first()
        return Response({"company": company.name, "revenue": company.revenue}) if company else Response({"message": "No data available"})    


class HighestProfitByCountry(APIView):
    def get(self, request):
        country_profits = (Business.objects.values("country").annotate(max_profit=Max("profit")).order_by("-max_profit"))
        return Response({"data": list(country_profits)})
