from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
#the following view consists of views of ViewSet
# router.register(r'stock-viewset', views.StockListViewset, basename='stockitem')
#the following view consists of views of ModelViewSet
# router.register(r'stock-modelviewset', views.StockModelView, basename='stockitem-model')

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

urlpatterns = [
    path('api/stockitems/', views.StockList.as_view(), name='stockitem-list-create'),
    path('api/stockitems/<int:pk>/', views.StockDetail.as_view(), name='stockitem-list-create'),
    path('stock-item-check/', views.StockItemCheckView.as_view(), name='stock_check'),
    
    path('stock_items/', views.StockItemListView.as_view(), name="stock_items"),
    # Add more paths for other views if needed
    path('' ,include(router.urls)),
]
