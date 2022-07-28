from rest_framework import viewsets, permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from loanrequest.serializers import LoanRequestSerializer
from loanrequest.models import LoanRequest
from rest_framework.pagination import PageNumberPagination


class LoanRequestViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = [permissions.AllowAny]



class CustomResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
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
    template_name = 'loan_request_list.html'
    pagination_class = CustomResultsSetPagination
    

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data={'loan_request': serializer.data}, 
                        template_name='single_request.html')