from django.urls import path
from . import views

urlpatterns = [
      path("", views.home),
      path("reports/", views.reports_home),
      path("exportar-unidades-produccion/", views.exportar_excel, name="export_excel"),
]