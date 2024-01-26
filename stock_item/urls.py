from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'stockitems', views.StockList, basename='stockitem')

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

urlpatterns = [
    path('api/stockitems/', views.StockList.as_view(), name='stockitem-list-create'),
    path('api/stockitems/<int:pk>/', views.StockDetail.as_view(), name='stockitem-list-create'),
    # Add more paths for other views if needed
]
