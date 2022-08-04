from django.urls import path, include
from ClubApp import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('event_api', views.EventModelViewsetAPI, basename='event')

urlpatterns = [
    path('', views.home, name='home_link'),
    path('MyEvents', views.my_events, name='my_events_link'),
    path('AddEvent', views.add_event, name='add_event_link'),
    path('EventDetails/<event_id>', views.event_details, name='event_details_link'),
    path('Search', views.search, name='search_events_link'),
    path('UpdateEvent/<event_id>', views.update_event, name='update_event_link'),
    path('DeleteEvent/<event_id>', views.delete_event, name='delete_event_link'),
    path('EventsTxtFile', views.gen_events_txt, name='gen_events_txt_link'),
    path('EventsCSVFile', views.gen_events_csv, name='gen_events_csv_link'),
    path('EventsPDFFile', views.gen_events_pdf, name='gen_events_pdf_link'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)