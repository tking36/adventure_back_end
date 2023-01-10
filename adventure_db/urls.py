from django.urls import path
from . import views

urlpatterns = [
    path('api/adventure', views.AdventureList.as_view(), name='adventure_list'), # api/adventure will be routed to the ContactList view for handling
    path('api/adventure/<int:pk>', views.AdventureDetail.as_view(), name='adventure_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
