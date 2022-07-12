from django.db import models
import enum

# Create your models here.

class IdentityDocument(enum.Enum):
    Identification = 1
    Passport = 2

    def __init__(self) -> None:
        pass

IDENTIFICATION_TYPE = [
    (IdentityDocument.Identification, 'cedula')
    (IdentityDocument.Passport, 'pasaporte')
]


class Country(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)


class Applicant(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False, db_column='nombre')
    last_name = models.CharField(max_length=100, blank=False, null=False, db_column='apellido')
    id_number = models.CharField(max_length=11, null=False, blank=False, db_column='numero_identificacion')
    id_type = models.IntegerField(choices=IDENTIFICATION_TYPE, default=IdentityDocument.Identification, db_column='tipo_identificacion')
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank=False, db_column='pais_nacionalidad')
    birth_date = models.DateField(null=False, db_column='fecha_nacimiento')
    tel = models.CharField(max_length=10, null=False, db_column='telefono')
    celphone = models.CharField(max_length=10, db_column='celular')
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=False, blank=False)

    class Meta:
        db_table = 'solicitante'
    

class Address(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE, null=False, blank=False, db_column='solicitante_id')
    street = models.CharField(max_length=260, blank=False, null=False, db_column='calle')
    number = models.IntegerField(max_length=7, blank=False, null=False, db_column='numero')
    building = models.CharField(max_length=100, blank=False, null=False, db_column='edificio')
    apartment = models.CharField(max_length=10, blank=False, null=False, db_column='apartamento')
    town = models.CharField(max_length=60, blank=False, null=False, db_column='sector')
    city = models.CharField(max_length=60, blank=False, null=False, db_column='ciudad')
    state = models.CharField(max_length=100, blank=False, null=False, db_column='provincia')

    class Meta:
        db_table = 'direccion'


class EmploymentType(enum.Enum):
    Private = 1
    Public = 2
    Entrepreneur = 3

EMPLOYMENT_TYPE = [
    (EmploymentType.Private, 'privado')
    (EmploymentType.Public, 'publico')
    (EmploymentType.Entrepreneur, 'auto empleado')
]

class EmploymentData(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE, null=False, blank=False, db_column='solicitante_id')
    employment_type = models.IntegerField(choices=EMPLOYMENT_TYPE, default=EmploymentType.Private, db_column='estado_laboral')
    company_name = models.CharField(max_length=100, blank=False, null=False, db_column='nombre_empresa')
    tel = models.CharField(max_length=10, null=False, db_column='telefono')
    tel_ext = models.CharField(max_length=4, null=False, db_column='extension_tel')
    current_role = models.CharField(max_length=260, blank=False, null=False, db_column='cargo_puesto')
    start_date = models.DateField(blank=False, null=False, db_column='fecha_ingreso')
    monthly_salary = models.DecimalField(null=False, blank=False, db_column='ingresos_mensuales')
    street = models.CharField(max_length=260, blank=False, null=False, db_column='calle')
    number = models.IntegerField(max_length=7, blank=False, null=False, db_column='numero')
    building = models.CharField(max_length=100, blank=False, null=False, db_column='edificio')
    town = models.CharField(max_length=60, blank=False, null=False, db_column='sector')
    city = models.CharField(max_length=60, blank=False, null=False, db_column='ciudad')
    state = models.CharField(max_length=100, blank=False, null=False, db_column='provincia')


    class Meta:
        db_table = 'datos_laborales'


class LoanRequest(models.Model):
    fecha_solicitud = ""


    class Meta:
        db_table = 'solicitud_prestamo'
    

    