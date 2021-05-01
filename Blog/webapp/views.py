from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


class LoginView(APIView):

    def post(self, request):
        response = {'status': 500, 'message': 'Something is wrong'}
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Username not found'
                raise Exception('Username not found')
            if data.get('password') is None:
                response['message'] = 'Password not found'
                raise Exception('Password not found')

        except Exception as error:
            print(error)
        return Response(response)
