from django.http import request
from rest_framework import serializers
from loanrequest.models import LoanRequest, Applicant, Address, EmploymentData


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
            'other_income',
            'street', 
            'number', 
            'building', 
            'town', 
            'city', 
            'state'
        ]


class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
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
            'address',
            'employment_data'
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
            'request_date',
            'cancelation_date',
            'approved_date',
            'denied_date',
            'completed_date',
            'denied_motive',
            'canceled_motive',
            'notes',
            'applicant',
        ]

    def validate_status(self, value):
        if self.context['request']._request.method == 'POST' and value != LoanRequest.RequestStatus.VALIDATING:
            raise serializers.ValidationError('status should be VALIDANDO', code='invalid')

        return value

    def create(self, validated_data):
        requester = validated_data.pop('applicant')
        address = requester.pop('address')
        employment_data = requester.pop('employment_data')
        
        applicant = Applicant.objects.create(**requester)
        Address.objects.create(applicant=applicant, **address)
        EmploymentData.objects.create(applicant=applicant, **employment_data)
        request = LoanRequest.objects.create(applicant=applicant, **validated_data)

        return request

    def update(self, instance, validated_data):
        applicant_serializer = self.fields['applicant']
        address_serializer = applicant_serializer.fields['address']
        employment_data_serializer = applicant_serializer.fields['employment_data']

        if 'applicant' in validated_data: 
            applicant = validated_data.pop('applicant')

            if 'employment_data' in applicant:
                employment_data = applicant.pop('employment_data')
                employment_data_serializer.update(instance.applicant.employment_data, employment_data)

            if 'address' in applicant:
                address = applicant.pop('address')
                address_serializer.update(instance.applicant.address, address)

            applicant_serializer.update(instance.applicant, applicant)

        return super().update(instance, validated_data)
