from django.db import models
from django.utils.translation import gettext_lazy as _


class Applicant(models.Model):

    class IdentificationType(models.TextChoices):
        ID = 'C', _('CEDULA')
        PASSPORT = 'E', _('PASAPORTE')
    
    first_name = models.CharField(max_length=100, db_column='nombre')
    last_name = models.CharField(max_length=100, db_column='apellido')
    id_number = models.CharField(max_length=11, db_column='numero_identificacion')
    id_type = models.CharField(max_length=1, choices=IdentificationType.choices, default=IdentificationType.ID, db_column='tipo_identificacion')
    nationality = models.CharField(max_length=60, db_column='nacionalidad')
    birth_date = models.DateField(db_column='fecha_nacimiento')
    tel = models.CharField(max_length=10, db_column='telefono')
    celphone = models.CharField(max_length=10, db_column='celular')
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=False)

    class Meta:
        db_table = 'solicitante'
    

class Address(models.Model):
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE, related_name='address', db_column='solicitante_id')
    street = models.CharField(max_length=260, db_column='calle')
    number = models.IntegerField(db_column='numero')
    building = models.CharField(max_length=100, null=True, db_column='edificio')
    apartment = models.CharField(max_length=10, null=True, db_column='apartamento')
    town = models.CharField(max_length=60, db_column='sector')
    city = models.CharField(max_length=60, db_column='ciudad')
    state = models.CharField(max_length=100, db_column='provincia')

    class Meta:
        db_table = 'direccion'


class EmploymentData(models.Model):

    class EmploymentType(models.TextChoices):
        PRIVATE = 'PR', _('privado')
        PUBLIC = 'PU', _('publico')
        SELF_EMPLOYED = "SE", _('auto empleado')

    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE, related_name='employment_data', db_column='solicitante_id')
    employment_type = models.CharField(max_length=2,choices=EmploymentType.choices, default=EmploymentType.PRIVATE, db_column='estado_laboral')
    company_name = models.CharField(max_length=100, db_column='nombre_empresa')
    tel = models.CharField(max_length=10, db_column='telefono')
    tel_ext = models.CharField(max_length=4, db_column='extension_tel')
    current_role = models.CharField(max_length=260, db_column='cargo_puesto')
    start_date = models.DateField(db_column='fecha_ingreso')
    monthly_salary = models.DecimalField(decimal_places=2, max_digits=14, db_column='ingresos_mensuales')
    street = models.CharField(max_length=260, db_column='calle')
    number = models.IntegerField(db_column='numero')
    building = models.CharField(max_length=100, db_column='edificio')
    town = models.CharField(max_length=60, db_column='sector')
    city = models.CharField(max_length=60, db_column='ciudad')
    state = models.CharField(max_length=100, db_column='provincia')

    class Meta:
        db_table = 'datos_laborales'


class LoanRequest(models.Model):

    class LoanType(models.TextChoices):
        BUSINESS = 'B', _('comercial')
        VEHICLE = 'V', _('vehiculos')
        PERSONAL = 'P', _('personal')

    class RequestStatus(models.TextChoices):
        VALIDATING = 'VALIDANDO', _('validando')
        COMPLETED = 'COMPLETADO', _('completado')
        DENIED = 'CANCELADO', _('cancelado')
        APPROVED = 'APROVADO', _('aprovado')

    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE, related_name='loan_requests' , db_column='solicitante_id')
    loan_type = models.CharField(max_length=2, choices=LoanType.choices, default=LoanType.PERSONAL, db_column='tipo_prestamo')
    amount_requested = models.DecimalField(max_digits=14, decimal_places=2, db_column='monto_solicitado')
    amount_approved = models.DecimalField(max_digits=14, decimal_places=2, db_column='monto_aprovado')
    term = models.IntegerField(db_column='plazo')
    referer = models.CharField(max_length=260)
    status = models.CharField(max_length=10, choices=RequestStatus.choices, default=RequestStatus.VALIDATING, db_column='estatus_solicitud')

    class Meta:
        db_table = 'solicitud_prestamo'
   