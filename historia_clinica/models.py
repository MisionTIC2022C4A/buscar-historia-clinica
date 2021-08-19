from django.db import models


class Professional(models.Model):
	nombreCompleto = models.CharField(max_length=255)
	tipoIdentificacion = models.CharField(max_length=255)
	numeroIdentificacion = models.CharField(max_length=255)
	telefono = models.CharField(max_length=255, blank=True, null=True)
	email = models.CharField(max_length=255, blank=True, null=True)
	profesion = models.CharField(max_length=255, blank=True, null=True)
	especialidad = models.CharField(max_length=255, blank=True, null=True)
	registroMedico = models.CharField(max_length=255, blank=True, null=True)
	fechaCreacion = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = (('numeroIdentificacion', 'tipoIdentificacion'),)

	def __str__(self):
		return self.nombreCompleto


class Service(models.Model):
	codServicio = models.CharField(max_length=8, primary_key=True)
	nombreServicio = models.CharField(max_length=255)
	tipo = models.CharField(max_length=20)
	fechaCreacion = models.DateTimeField(auto_now_add=True)
    
	def __str__(self):
		return self.nombreServicio


class Attentions(models.Model):
	pacTipoId = models.CharField(max_length=3)
	pacNumId = models.CharField(max_length=20)
	pacNombre = models.CharField(max_length=255)
	servicio = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
	profesional = models.ForeignKey(Professional, on_delete=models.DO_NOTHING)
	fechaCreacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.idAtencion)




"""
class Patient(models.Model):
    idPersona = models.AutoField(primary_key=True)
    numero_identificacion = models.CharField(max_length=255)
    tipo_identificacion = models.CharField(max_length=255)
    aseguradora = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    estado_civil = models.CharField(max_length=255, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nombre_acompanante = models.CharField(max_length=255, blank=True, null=True)
    nombre_completo = models.CharField(max_length=255, blank=True, null=True)
    ocupacion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    vinculacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'patient'
        unique_together = (('numero_identificacion', 'tipo_identificacion'),)
        verbose_name_plural = 'Pacientes'
        verbose_name = 'Paciente'     
    
    def __str__(self):
        return self.nombre_completo
"""  
