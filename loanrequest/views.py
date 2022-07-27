from django.shortcuts import render
from rest_framework import viewsets, permissions, views, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from loanrequest.serializers import ApplicantSerializer, LoanRequestSerializer, AddressSerializer, EmploymentDataSerializer
from loanrequest.models import Applicant, LoanRequest, Address, EmploymentData
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
# from rest_framework.decorators import api_view, action


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


def adminViewSet(request):
    return render(request, 'loan_request_list.html')


class CustomResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        dd = self.page.has_other_pages()
        dst = self.page.paginator.num_pages
        return Response({'loan_requests': {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        }})


class TestViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'test_template.html'
    pagination_class = CustomResultsSetPagination
    

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data={'loan_request': serializer.data}, 
                        template_name='single_request.html')