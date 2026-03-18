from django.urls import path
from . import views

urlpatterns = [
      path("", views.home),
      path("reports/", views.reports_home),
      path("exportar/<str:nombre_reporte>/", views.exportar_reporte, name="export_report"),
]