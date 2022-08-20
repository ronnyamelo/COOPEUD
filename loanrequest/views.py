from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from loanrequest.models import LoanRequest
from loanrequest.serializers import LoanRequestSerializer
from loanrequest.filters import LoanRequestFilter


class HtmlTemplateResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({'loan_requests': {
            'page_size': self.page.paginator.per_page,
            'count': self.page.paginator.count,
            'current': self.page.number,
            'pages': self.page.paginator.get_elided_page_range(number=self.page.number, on_each_side=2, on_ends=3),
            'results': data
        }})


class TestViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'loan_request_list.html'
    pagination_class = HtmlTemplateResultsSetPagination
    filterset_class = LoanRequestFilter
    ordering_fields = ['status', 'request_date', 'amount_requested']

    """
    here the ordering for status works as I want it (validating requests first) only because
    grammatically, words begining with the letter 'V' on a rerverse ordering would be the first to appear
    but had I wanted the ordering to be different then this solution will not work
    """
    ordering = ['-status', 'request_date']
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data={'loan_request': serializer.data}, 
                        template_name='single_request.html')


class LoanRequestViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = LoanRequestFilter
    ordering_fields = ['status', 'request_date', 'amount_requested', 'amount_approved', 'term', 'loan_type']

