from django.http import request
from rest_framework import serializers
from loanrequest.models import LoanRequest, Applicant, Address, EmploymentData
from django.db import models
from django.utils.translation import gettext_lazy as _



class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            'street', 
            'number', 
            'building', 
            'apartment', 
            'town', 
            'city', 
            'state',
        ]


class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
    
    address = AddressSerializer(read_only=True, many=True)
    # employment_data = EmploymentDataSerializer()

    class Meta:
        model = Applicant
        fields = [
            'first_name',
            'last_name',
            'id_number',
            'id_type',
            'nationality',
            'birth_date',
            'tel',
            'celphone',
            'facebook',
            'twitter',
            'instagram',
            'email',
            'address'
            # 'employment_data'
        ]


class LoanRequestSerializer(serializers.HyperlinkedModelSerializer):
    applicant = ApplicantSerializer()

    class Meta:
        model = LoanRequest
        fields = [
            'url',
            'loan_type',
            'amount_requested',
            'amount_approved',
            'term',
            'referer',
            'status',
            'applicant'
        ]

        # exclude = ['applicant.loan_requests']


    def create(self, validated_data):
        applicant_data = validated_data.pop('applicant')
        customer = Applicant.objects.create(**applicant_data)
        request = LoanRequest.objects.create(applicant=customer, **validated_data)

        return request



class EmploymentDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmploymentData
        fields = [
            'employment_type', 
            'company_name', 
            'tel', 
            'tel_ext', 
            'current_role', 
            'start_date', 
            'monthly_salary', 
            'street', 
            'number', 
            'building', 
            'town', 
            'city', 
            'state'
        ]




# class ApplicantDtoSerializer(serializers.HyperlinkedModelSerializer):
#     loan_request = LoanRequestSerializer()
#     # address = AddressSerializer()
#     # employment_data = EmploymentDataSerializer()

#     class Meta:
#         model = Applicant
#         fields = [
#             'first_name',
#             'last_name',
#             'id_number',
#             'id_type',
#             'nationality',
#             'birth_date',
#             'tel',
#             'celphone',
#             'facebook',
#             'twitter',
#             'instagram',
#             'email',
#             'loan_request',
#             # 'address',
#             # 'employment_data'
#         ]




# class ApplicantDto(models.Model):
#     # loan_request = None
#     # address = None
#     # employment_data = None

#     class IdentificationType(models.TextChoices):
#         ID = 'C', _('CEDULA')
#         PASSPORT = 'E', _('PASAPORTE')

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     id_number = models.CharField(max_length=11)
#     id_type = models.CharField(max_length=1, choices=IdentificationType.choices, default=IdentificationType.ID)
#     nationality = models.CharField(max_length=60)
#     birth_date = models.DateField()
#     tel = models.CharField(max_length=10)
#     celphone = models.CharField(max_length=10)
#     facebook = models.CharField(max_length=50)
#     twitter = models.CharField(max_length=50)
#     instagram = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254, blank=False)

#     class Meta:
#         managed = False
