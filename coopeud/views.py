import json
import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import renderer_classes, api_view, permission_classes
from django.http import  HttpResponseNotFound
from coopeud.authorization import ClientCredentialsAuthorization
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
import os


def index(request):
    return  render(request, 'inicio.html', {'title': 'Inicio'})

def contact(request):
    return  render(request, 'contacto.html', {'title': 'Contacto'})

def location(request):
    return  render(request, 'ubicacion.html', {'title': 'Ubicacion'})

def formulario(request):
    return render(request, 'formulario_solicitud.html', {'title': 'Solicitud de prestamo'})

def history(request):
    return render(request, 'nosotros.html', {'title': 'Nosotros'})


authorization = ClientCredentialsAuthorization()

@csrf_exempt
@permission_classes([AllowAny])
@api_view(['POST', 'GET'])
@renderer_classes([JSONRenderer])
def handle_loan_request(request):
    
    if request.method == 'GET':
        return HttpResponseNotFound();

    url = os.environ.get('API_SOLICITUDES_ENDPOINT')
    payload = json.dumps(request.data)
    response = post_loan_request(url, payload, authorization.token)

    if response.status_code == 401 or response.status_code == 403:
        response = post_loan_request(url, payload, authorization.get_new_token())

    return Response(data=json.loads(response.content), status=response.status_code)


def post_loan_request(url, payload, token):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer' + ' ' + token
    }

    return requests.post(url=url, data=payload, headers=headers);