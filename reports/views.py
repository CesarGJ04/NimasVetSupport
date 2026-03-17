from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from .models import UnidadesProduccion
# Create your views here.

def home(request):
    return HttpResponse("<h1>Django funcionando correctamente</h1>")

def reports_home(request):
    return render(request, "reports/home.html")

def exportar_excel(request):

    resultados = UnidadesProduccion.objects.raw("""
        SELECT *
        FROM vw_unidades_produccion
        ORDER BY responsable
    """)

    data = [
        {
            "Zona": r.zona_nombre,
            "Comunidad": r.community_name,
            "Sector": r.sector_name,
            "Responsable": r.responsable,
            "DNI": r.dni
        }
        for r in resultados
    ]

    df = pd.DataFrame(data)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = "attachment; filename=responsables.xlsx"

    df.to_excel(response, index=False)

    return response