from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import pandas as pd
from .models import UnidadesProduccion
# Create your views here.

def home(request):
    return HttpResponse("<h1>Django funcionando correctamente</h1>")

def reports_home(request):
    return render(request, "reports/home.html", {
        "reportes": REPORTES
    })


REPORTES = {
    "unidades": {
        "query": """
            SELECT *
            FROM vw_unidades_produccion
            ORDER BY responsable
        """,
        "columns": {
            "zona_nombre": "Zona",
            "comunity_name": "Comunidad",
            "secto_name": "Sector", 
            "responsable":"Responsable",
            "dni": "DNI"
        },
        "filename": "unidades_produccion.xlsx"
    },
    "alpacas": {
        "query": """
            SELECT *
            FROM vw_ReporteAlpacas
            ORDER BY visited_at DESC
        """,
        "columns": {
            "visited_at": "Fecha Visita",
            "zona": "Zona",
            "comunity_name": "Comunidad",
            "sector_name": "Sector",
            "up_responsable": "Responsable UP",
            "personal_especialista": "Especialista",
            "persona_responsable": "Responsable",
            "actividad": "Actividad",
            "hato_number": "Total Hato",
            "hato_babies_number": "Crías",
            "hato_mothers_number": "Madres",
            "hato_males_number": "Machos",
            "female_alpaca_earring_number": "Arete",
            "female_alpaca_race": "Raza",
            "female_alpaca_color": "Color",
            "female_alpaca_age": "Edad",
            "female_alpaca_category": "Categoría",
            "female_alpaca_total_score": "Puntaje",
            "empadre_date": "Fecha Empadre",
            "alpacas_empadradas": "Empadradas",
            "alpacas_empadradas_number": "N° Empadradas",
            "male_empadre_number": "Machos Empadre",
            "pregnant": "Preñadas",
            "empty": "Vacías"
        },
        "filename": "reporte_alpacas.xlsx"
    },
    "ovinos": {
        "query": """
            SELECT *
            FROM vw_ReporteOvinos
            ORDER BY visited_at DESC
        """,
        "columns": {
            "visited_at": "Fecha Visita",
            "zona": "Zona",
            "comunidad": "Comunidad",
            "sector": "Sector",
            "up_responsable": "Responsable UP",
            "personal_especialista": "Especialista",
            "persona_responsable": "Responsable",
            "actividad": "Actividad",
            "selected_ovines": "Ovinos Seleccionados",
            "synchronized_ovines": "Ovinos Sincronizados",
            "inseminated_sheeps_corriedale": "Inseminados Corriedale",
            "inseminated_sheeps_criollas": "Inseminados Criollos",
            "pregnant": "Preñadas",
            "empty": "Vacías",
            "not_evaluated": "No Evaluadas",
            "baby_males": "Crías Machos",
            "baby_females": "Crías Hembras",
            "baby_deaths": "Muertes Crías",
            "course_female_attendance": "Asistencia Mujeres",
            "course_male_attendance": "Asistencia Hombres",
            "technical_assistance_attendance": "Asistencia Técnica",
            "ovinos_number": "Total Ovinos"
        },
        "filename": "reporte_ovinos.xlsx"
    },
    "vacunos": {
        "query": """
            SELECT *
            FROM vw_reportevacunos
            ORDER BY visited_at DESC
        """,
        "columns": {
            "visited_at": "Fecha Visita",
            "zona": "Zona",
            "comunidad": "Comunidad",
            "sector": "Sector",
            "up_responsable": "Responsable UP",
            "personal_especialista": "Especialista",
            "persona_responsable": "Responsable",
            "actividad": "Actividad",
            "bull_name": "Nombre Toro",
            "bull_race": "Raza Toro",
            "pajilla_type": "Tipo Pajilla",
            "pajilla_origin": "Origen Pajilla",
            "pajillas_number": "N° Pajillas",
            "cow_name": "Nombre Vaca",
            "cow_race": "Raza Vaca",
            "service_number": "N° Servicios",
            "pregnant": "Preñadas",
            "empty": "Vacías",
            "birthday": "Fecha Nacimiento",
            "earring_number": "N° Arete",
            "baby_name": "Nombre Cría",
            "male": "Machos",
            "female": "Hembras",
            "death": "Muertes",
            "baby_bull_name": "Padre Cría",
            "baby_cow_name": "Madre Cría",
            "female_attendance": "Asistencia Mujeres",
            "male_attendance": "Asistencia Hombres",
            "technical_assistance_attendance": "Asistencia Técnica",
            "vacunos_number": "Total Vacunos"
        },
        "filename": "reporte_vacunos.xlsx"
    },
    "desparasitacion": {
        "query": """
            SELECT *
            FROM vw_ReporteDesparacitacion
            ORDER BY visited_at DESC
        """,
        "columns": {
            "visited_at": "Fecha Visita",
            "zona": "Zona",
            "comunidad": "Comunidad",
            "sector": "Sector",
            "up_responsable": "Responsable UP",
            "personal_especialista": "Especialista",
            "persona_responsable": "Responsable",
            "actividad": "Actividad",
            "v_race": "Raza Vacunos",
            "v_dewormed": "Vacunos Desparasitados",
            "v_no_dewormed": "Vacunos No Desparasitados",
            "v_total": "Total Vacunos",
            "o_race": "Raza Ovinos",
            "o_dewormed": "Ovinos Desparasitados",
            "o_no_dewormed": "Ovinos No Desparasitados",
            "o_total": "Total Ovinos",
            "a_race": "Raza Alpacas",
            "a_dewormed": "Alpacas Desparasitadas",
            "a_no_dewormed": "Alpacas No Desparasitadas",
            "a_total": "Total Alpacas",
            "l_race": "Raza Llamas",
            "l_dewormed": "Llamas Desparasitadas",
            "l_no_dewormed": "Llamas No Desparasitadas",
            "l_total": "Total Llamas",
            "c_total": "Total Camélidos",
            "total": "Total General"
        },
        "filename": "reporte_desparasitacion.xlsx"
    }
}


def exportar_reporte(request, nombre_reporte):

    if nombre_reporte not in REPORTES:
        return HttpResponse("Reporte no encontrado", status=404)
    
    config = REPORTES[nombre_reporte]

    df = pd.read_sql(config["query"], connection)

    print(df.columns)

    df = df.rename(columns=config["columns"])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = f'attachment; filename={config["filename"]}'
    
    df.to_excel(response, index=False, engine="openpyxl")

    return response