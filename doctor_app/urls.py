from django.urls import path
from . import views
urlpatterns = [

    path("",views.createDoctor),
    path("doctorlist",views.listdoctor),
    path("detailsview/<int:doctor_id>", views.detailsview),
    path("updateview/<int:doctor_id>", views.updateview)

]
