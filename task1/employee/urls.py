from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('empregister_view/',views.empregister_view,name='empregister'),
    path('emplogin_view/',views.emplogin_view,name='emplogin'),
    path('displayuser_view/',views.displayuser_view,name='displayuser'),
    path('displayadmin_view/',views.displayadmin_view,name='displayadmin'),


    path('empleave_view/',views.empleave_view,name='empleave'),



    path('approve_view/<int:id>',views.approve_view,name='approve'),
    path('reject_view/<int:id>',views.reject_view,name='reject'),
    


    

    path('home_view/',views.home_view,name='home')
    

    
    # path('displaydata/',views.disp_userdata,name='dispuserdata'),
]
