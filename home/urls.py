from django.urls import path
from .views import indexView, aboutView, serviceView, contactView, elementView, newsView, footerView
import home.views

urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('sendmail/', home.views.sendmail, name='sendmail'),
    path('appoint_ment/', home.views.appoint_ment, name='appoint_ment'),
    path('contactmessage/', home.views.contactmessage, name='contactmessage'),
    path('about/', aboutView.as_view(), name='about'),
    path('services/', serviceView.as_view(), name='services'),
    path('contact/', contactView.as_view(), name='contact'),
    path('elements/', elementView.as_view(), name='elements'),
    path('news/', newsView.as_view(), name='news'),
    path('base/', footerView.as_view(), name='base')



]