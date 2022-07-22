from rest_framework import serializers
from loanrequest.models import LoanRequest, Applicant, Address, EmploymentData


class LoanRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoanRequest
        fields = [
            'loan_type',
            'amount_requested',
            'amount_approved',
            'term',
            'referer',
            'status',
        ]


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
            'state'
        ]


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


class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
    loan_request = LoanRequestSerializer()
    address = AddressSerializer()
    employment_data = EmploymentDataSerializer()

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
            'loan_request',
            'address',
            'employment_data'
        ]



