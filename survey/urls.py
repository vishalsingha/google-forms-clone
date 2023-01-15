from django.urls import path
from django.views.decorators.csrf import csrf_exempt


from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('survey', views.survey, name = 'survey'),
    path('save_survey', views.save_survey, name = 'save_survey'),
    path('show_form/<int:key>', views.show_form, name = 'show_form'),
    path('save_response/<int:key>', views.save_response, name = 'save_response'),
    path('download_excel/<int:key>', views.download_excel, name = 'download_excel'),

    

]