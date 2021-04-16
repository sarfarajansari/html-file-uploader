from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("project/<str:project>/<str:filename>/",views.project,name="project"),
    path("submit/",views.submit,name="submit")
]
