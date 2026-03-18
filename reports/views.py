from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import pandas as pd
from .models import UnidadesProduccion
# Create your views here.

def home(request):
    return HttpResponse("<h1>Django funcionando correctamente</h1>")

def reports_home(request):
    return render(request, "reports/home.html")

REPORTES = {
    "unidades": {
        "query": """
            SELECT *
            FROM vw_unidades_produccion
            ORDER BY responsable
        """,
        "columns": {
            "Zona_nombre": "Zona",
            "Comunity_name": "Comunidad",
            "secto_name": "Sector", 
            "responsable":"Responsable",
            "dni": "DNI"
        },
        "filename": "unidades_produccion.xlsx"
    }
}

def reports_home(request):
    return render(request, "reports/home.html")

def exportar_reporte(request, nombre_reporte):

    if nombre_reporte not in REPORTES:
        return HttpResponse("Reporte no encontrado", status=404)
    
    config = REPORTES[nombre_reporte]

    with connection.cursor() as cursor:
        cursor.execute(config["query"])
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=columns)
    df = df.rename(columns=config["columns"])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = f'attachment; filename={config["filename"]}'
    
    df.to_excel(response, index=False, engine="openpyxl")

    return response