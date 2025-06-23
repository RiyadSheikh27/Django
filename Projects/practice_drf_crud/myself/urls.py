from django.urls import path
from .views import myselfViewset

urlpatterns = [
    path('', myselfViewset.as_view(), name='myself'),
    path('myself/', myselfViewset.as_view(), name='myself_list_api'),
    path('myself/<int:id>/', myselfViewset.as_view(), name='myself_detail_api'),
]