from django.db import models
# Create your models here.

class UnidadesProduccion(models.Model):

    id = models.IntegerField(primary_key=True)
    zona_nombre = models.CharField(max_length=255)
    community_name = models.CharField(max_length=255)
    sector_name = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "vw_unidades_produccion"