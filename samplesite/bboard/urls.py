from django.urls import path
from .views import index, rubric_bbs,BbUpdateView,BbDeleteView,ajax_add,async_ping

urlpatterns = [
    path('ajax/add/', ajax_add, name='ajax_add'),
    path('<int:rubric_id>/', rubric_bbs, name='rubric_bbs'),
    path('', index, name='index'),
    path('<int:pk>/edit/', BbUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', BbDeleteView.as_view(), name='delete'),
    path('async/ping/', async_ping, name='async_ping'),

]