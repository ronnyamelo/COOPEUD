from django.shortcuts import render
from rest_framework import viewsets, permissions
from loanrequest.serializers import ApplicantSerializer, LoanRequestSerializer, AddressSerializer, EmploymentDataSerializer
from loanrequest.models import Applicant, LoanRequest, Address, EmploymentData
from rest_framework.decorators import api_view, action


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = [permissions.AllowAny]


class LoanRequestViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = [permissions.AllowAny]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.AllowAny]


class EmploymentDataViewSet(viewsets.ModelViewSet):
    queryset = EmploymentData.objects.all()
    serializer_class = EmploymentDataSerializer
    permission_classes = [permissions.AllowAny]


# @api_view(['GET', 'POST'])
# class ApplicantDtoViewSet(viewsets.ModelViewSet):
#     # queryset = Applicant.objects.all()
#     # serializer_class = ApplicantDtoSerializer
#     # permission_classes = [permissions.AllowAny]


