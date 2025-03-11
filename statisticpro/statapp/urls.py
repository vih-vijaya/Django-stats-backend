from django.urls import path
from .views import UploadBusinessExcel, ExcelDataView, UpdateDeleteCompany, BusinessStatistics, USAnames, Profit,TotalProfitView, HighRevenueCompanies, AddCompany, TopRevenueCompany,HighestProfitByCountry

urlpatterns = [
    path('upload/', UploadBusinessExcel.as_view(), name='upload_business_excel'),
    path('business/stats/', BusinessStatistics.as_view(), name='business_stats'),
    path('business/USA/', USAnames.as_view(), name='USA_names'),
    path('business/profit/', Profit.as_view(), name='profit'),
    path('business/total_profit/', TotalProfitView.as_view(), name='total_profit'),
    path('business/high_revenue/', HighRevenueCompanies.as_view(), name='high_revenue_companies'),
    path('business/AddCompany/', AddCompany.as_view(), name='Add_company'),
    path('business/TopRevenueCompany/', TopRevenueCompany.as_view(), name='Top_revenue_company'),
    path('business/HighestProfitByCountry/', HighestProfitByCountry.as_view(), name='Highest_profit_by_country'),
    path('business/data/', ExcelDataView.as_view(), name='excel_data'),
    path('business/update_delete_company/<int:id>/', UpdateDeleteCompany.as_view(), name='update_delete_company'),
         
]