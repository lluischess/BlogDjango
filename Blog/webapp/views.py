from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from webapp.form import BlogForm, BlogForm2
from webapp.models import Article, Profile


def home(request):
    context = {'articles': Article.objects.all()}
    return render(request, 'home.html', context)


def article_detail(request, slug):
    context = {}
    try:
        article_object = Article.objects.filter(slug=slug).first()
        context['article_object'] = article_object
    except Exception as Error:
        print(Error)

    return render(request, 'post-details.html', context)


def articlep_detail(request):
    context = {}
    try:
        articlep_object = Article.objects.filter(user=request.user)
        context['articlep_object'] = articlep_object
    except Exception as Error:
        print(Error)
    print(context)
    return render(request, 'detail.html', context)


def article_delete(request, id):
    try:
        article_object = Article.objects.get(id=id)

        if article_object.user == request.user:
            article_object.delete()

    except Exception as Error:
        print(Error)
    return redirect('/detail/')


def post_update(request, id):
    context = {}

    try:
        article_object = Article.objects.get(id=id)

        if article_object.user != request.user:
            return redirect('/')

        initial_dic = {'content': article_object.content, 'title': article_object.title,
                       'image': article_object.image}
        form = BlogForm2(initial=initial_dic)

        if request.method == 'POST':
            form = BlogForm2(request.POST, instance=article_object)

            if form.is_valid():
                form.save()

        context['form'] = form

    except Exception as Error:
        print(Error)
    return render(request, 'post-update.html', context)


def login_view(request):
    return render(request, 'login.html')


def V_logout(request):
    logout(request)
    return redirect('/')


def addpost(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            blog_object = Article.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(blog_object)
            return redirect('/addpost/')

    except Exception as error:
        print(error)

    return render(request, 'addpost.html', context)


def register(request):
    return render(request, 'register.html')


class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user is None:
                response['message'] = 'invalid username , user not found'
                raise Exception('invalid username not found')

            user_obj = authenticate(username=data.get('username'), password=data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password')


        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()


class RegisterView(APIView):

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

            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user:
                response['message'] = 'Username already taken'
                raise Exception('Username already taken')

            user_obj = User.objects.create(username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()

            response['status'] = 200
            response['message'] = 'User created'

        except Exception as error:
            print(error)
        return Response(response)


RegisterView = RegisterView.as_view()
