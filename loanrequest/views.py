from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from loanrequest.models import LoanRequest
from loanrequest.serializers import LoanRequestSerializer


class LoanRequestViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = [permissions.AllowAny]



class HtmlTemplateResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({'loan_requests': {
            'current': self.page.number,
            'pages': self.page.paginator.get_elided_page_range(
                number=self.page.number, on_each_side=2, on_ends=3),

            'results': data
        }})


class TestViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'loan_request_list.html'
    pagination_class = HtmlTemplateResultsSetPagination
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data={'loan_request': serializer.data}, 
                        template_name='single_request.html')