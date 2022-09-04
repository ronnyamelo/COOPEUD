from rest_framework import viewsets, permissions, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from loanrequest.models import LoanRequest
from loanrequest.serializers import LoanRequestSerializer
from loanrequest.filters import LoanRequestFilter
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from django.views.decorators.csrf import csrf_exempt


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

class LoanRequestCreateViewSet(generics.CreateAPIView):
    authentication_classes = [OAuth2Authentication]
    serializer_class = LoanRequestSerializer
    permission_classes = [TokenHasScope]
    required_scopes = ['write']


class LoanRequestViewSet(viewsets.mixins.ListModelMixin, 
                         viewsets.mixins.RetrieveModelMixin,
                         viewsets.mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
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


def loginView(request):

    if (request.method == "GET"):
        return render(request, 'login.html')

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/solicitudes/')
    return redirect('/admin/solicitudes/')

def logoutView(request):
    logout(request)
    return redirect('/login/')

import requests


def test(request):
    url = "http://localhost:8000/o/token/"

    payload='grant_type=client_credentials'
    headers = {
    'Authorization': 'Basic Y2xpZW50OmNsaWVudF8x',
    'Content-Type': 'application/x-www-form-urlencoded',
    #   'Cookie': 'csrftoken=1ZTc9QX1wnPal93pwJ31wfZpFtG5okbkOwb7TSzkETqkdAITd9Eif3zupUXwMiXi'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
