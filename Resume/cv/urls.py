from django.urls import path
from cv import views

urlpatterns = [
    #------define urls for Course app views functtion======


path('aboutme/',views.aboutme),
path('contact/',views.contact),
path('education/',views.education),
path('footer/',views.footer),
path('portfolio/',views.portfolio),
path('skill/',views.skill),
path('workexp/',views.workexp),
    

]